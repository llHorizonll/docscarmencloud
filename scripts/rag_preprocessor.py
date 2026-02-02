"""
RAG Preprocessing Script for Carmen Documentation

This script processes markdown files for RAG implementation:
1. Standardizes frontmatter metadata
2. Extracts and processes image references
3. Extracts video metadata
4. Cleans HTML/CSS artifacts
5. Implements semantic chunking
"""

import os
import re
import hashlib
import json
from pathlib import Path
from typing import Dict, List, Tuple, Any
from dataclasses import dataclass, asdict
from datetime import datetime


@dataclass
class DocumentMetadata:
    """Standardized metadata structure for Carmen documentation."""
    title: str = ""
    title_en: str = ""
    lang: str = "th-TH"
    module: str = ""
    submodule: str = ""
    doc_type: str = "procedure"  # procedure, configuration, troubleshooting, reference, overview
    complexity: str = "intermediate"  # beginner, intermediate, advanced
    tags: List[str] = None
    last_updated: str = ""
    version: str = "1.0"
    country_specific: str = "generic"  # thailand, philippines, generic
    target_audience: str = "accountant"  # accountant, controller, system_admin
    media_type: List[str] = None  # screenshot, video_tutorial, step_by_step
    related_docs: List[str] = None
    chunk_count: int = 0

    def __post_init__(self):
        if self.tags is None:
            self.tags = []
        if self.media_type is None:
            self.media_type = []
        if self.related_docs is None:
            self.related_docs = []


@dataclass
class Chunk:
    """A content chunk for vector database embedding."""
    chunk_id: str
    doc_path: str
    file_path: str  # Original file path relative to docs/ for URL generation
    sequence: int
    total_chunks: int
    chunk_type: str  # procedure, reference, table, formula, video
    content: str
    metadata: Dict[str, Any]
    overlap: str = ""


class CarmenRAGPreprocessor:
    """Main preprocessor class for Carmen documentation."""

    def __init__(self, docs_dir: str, output_dir: str = None):
        self.docs_dir = Path(docs_dir)
        self.output_dir = Path(output_dir) if output_dir else self.docs_dir / "processed"
        self.output_dir.mkdir(exist_ok=True)

        # Module detection patterns
        self.module_patterns = {
            "ap": r"carmen_cloud/ap",
            "ar": r"carmen_cloud/ar",
            "gl": r"carmen_cloud/gl",
            "asset": r"carmen_cloud/asset",
            "configuration": r"carmen_cloud/configuration",
            "workbook": r"carmen_cloud/workbook",
            "material": r"Blueledgers/Material",
            "procurement": r"Blueledgers/Procurement",
            "portions": r"Blueledgers/Portions",
            "options": r"Blueledgers/Options",
        }

        # Tag detection patterns
        self.tax_tags = r"(ภ\.ง\.ด\.|vat|tax|wht|ภาษี|withholding|input tax|output tax)"
        self.invoice_tags = r"(invoice|ใบแจ้งหนี้|billing)"
        self.payment_tags = r"(payment|ชำระ|receipt|ใบเสร็จ)"
        self.reconciliation_tags = r"(reconciliation|ปรับสมดุล|match)"

    def detect_module(self, file_path: Path) -> Tuple[str, str]:
        """Detect module and submodule from file path."""
        path_str = str(file_path).replace("\\", "/")
        for module, pattern in self.module_patterns.items():
            if re.search(pattern, path_str, re.IGNORECASE):
                return module, module
        return "unknown", "unknown"

    def detect_doc_type(self, content: str, filename: str) -> str:
        """Detect document type from content and filename."""
        filename_lower = filename.lower()

        if "troubleshoot" in filename_lower or "error" in content.lower():
            return "troubleshooting"
        if "overview" in filename_lower or "index" in filename_lower:
            return "overview"
        if "config" in filename_lower or "setting" in filename_lower:
            return "configuration"
        if "glossary" in filename_lower or "reference" in filename_lower:
            return "reference"
        return "procedure"

    def detect_country(self, content: str, file_path: Path) -> str:
        """Detect country-specific content."""
        path_str = str(file_path).lower()

        if "philippines" in path_str or "bir" in content.lower():
            return "philippines"
        if any(term in content.lower() for term in ["ภ.ง.ด.", "rdprep", " revenue department"]):
            return "thailand"
        return "generic"

    def extract_title_en(self, content: str, title_th: str) -> str:
        """Extract English title from content."""
        # Check for English title in first paragraph
        lines = content.split('\n')
        for line in lines[:20]:
            line = line.strip()
            if line and not line.startswith('#') and not line.startswith('---'):
                # Check if line is mostly ASCII (English)
                if len(line) > 3 and sum(1 for c in line if ord(c) < 128) / len(line) > 0.7:
                    return line
        return ""

    def extract_frontmatter(self, content: str) -> Tuple[Dict[str, Any], str]:
        """Extract existing frontmatter from content."""
        frontmatter = {}
        body = content

        if content.startswith('---'):
            parts = content.split('---', 2)
            if len(parts) >= 3:
                fm_text = parts[1]
                body = parts[2]

                # Parse YAML-like frontmatter
                for line in fm_text.split('\n'):
                    if ':' in line:
                        key, value = line.split(':', 1)
                        frontmatter[key.strip()] = value.strip()

        return frontmatter, body

    def create_metadata(self, file_path: Path, content: str) -> DocumentMetadata:
        """Create standardized metadata for a document."""
        # Extract existing frontmatter
        existing_fm, body = self.extract_frontmatter(content)

        # Get title from existing frontmatter or extract from content
        title = existing_fm.get('title', '')
        if not title:
            # Find first heading
            match = re.search(r'^#\s+(.+)$', body, re.MULTILINE)
            title = match.group(1) if match else file_path.stem

        # Detect other attributes
        module, submodule = self.detect_module(file_path)
        doc_type = self.detect_doc_type(body, file_path.name)
        country = self.detect_country(body, file_path)
        title_en = existing_fm.get('title_en') or self.extract_title_en(body, title)

        # Generate tags
        tags = self._generate_tags(body, module, doc_type)

        # Detect media types
        media_types = []
        if '![' in body:
            media_types.append("screenshot")
        if "youtube" in body.lower() or "iframe" in body.lower():
            media_types.append("video_tutorial")
        if re.search(r'^\d+\.', body, re.MULTILINE):
            media_types.append("step_by_step")

        metadata = DocumentMetadata(
            title=title,
            title_en=title_en or existing_fm.get('title_en', ''),
            lang=existing_fm.get('lang', 'th-TH'),
            module=module,
            submodule=submodule,
            doc_type=existing_fm.get('doc_type', doc_type),
            complexity=existing_fm.get('complexity', 'intermediate'),
            tags=tags,
            last_updated=existing_fm.get('last_updated', datetime.fromtimestamp(
                file_path.stat().st_mtime).strftime('%Y-%m-%d')),
            version=existing_fm.get('version', '1.0'),
            country_specific=country,
            target_audience=existing_fm.get('target_audience', 'accountant'),
            media_type=media_types,
            related_docs=existing_fm.get('related_docs', '').split(',') if existing_fm.get('related_docs') else []
        )

        return metadata

    def _generate_tags(self, content: str, module: str, doc_type: str) -> List[str]:
        """Generate tags from content analysis."""
        tags = [module, doc_type]
        content_lower = content.lower()

        # Tax-related
        if re.search(self.tax_tags, content_lower):
            tags.extend(["tax", "compliance"])
            if "wht" in content_lower or "หัก ณ ที่จ่าย" in content:
                tags.append("withholding_tax")
            if "vat" in content_lower or "ภาษีมูลค่าเพิ่ม" in content:
                tags.append("vat")

        # Function-specific
        if re.search(self.invoice_tags, content_lower):
            tags.append("invoice")
        if re.search(self.payment_tags, content_lower):
            tags.append("payment")
        if re.search(self.reconciliation_tags, content_lower):
            tags.append("reconciliation")

        # Country-specific
        if "philippines" in content_lower or "bir" in content_lower:
            tags.append("philippines")
        if "ภ.ง.ด." in content or "rdprep" in content_lower:
            tags.append("thailand")

        return list(set(tags))  # Remove duplicates

    def clean_content(self, content: str) -> str:
        """Clean HTML/CSS artifacts and normalize formatting."""
        # Remove inline styles
        content = re.sub(r'\s*style="[^"]*"', '', content)

        # Remove span tags but keep content
        content = re.sub(r'<span\s+class="[^"]*"\s*>([^<]+)</span>', r'\1', content)

        # Remove self-closing img tags in text (keep markdown image references)
        content = re.sub(r'<img\s+src="[^"]*"\s*(?:style="[^"]*")?\s*/?>', '', content)

        # Convert iframes to video metadata markers
        content = re.sub(
            r'<iframe[^>]*youtube\.com/embed/([^"?]+)[^>]*></iframe>',
            r'[VIDEO:youtube:\1]',
            content
        )

        # Clean up excessive whitespace
        content = re.sub(r'\n{3,}', '\n\n', content)

        return content.strip()

    def extract_image_references(self, content: str) -> List[Dict[str, str]]:
        """Extract image references with contextual descriptions."""
        images = []

        # Pattern: ![alt text](image-XX.png)
        pattern = r'!\[(.*?)\]\((image-\d+\.\w+)\)'
        matches = re.finditer(pattern, content)

        for match in matches:
            alt_text = match.group(1).strip()
            filename = match.group(2)

            # Generate description from alt text or context
            description = alt_text if alt_text and alt_text != "alt text" else f"Screenshot: {filename}"

            images.append({
                "filename": filename,
                "description": description,
                "type": "screenshot"
            })

        return images

    def extract_video_metadata(self, content: str) -> List[Dict[str, str]]:
        """Extract YouTube video metadata."""
        videos = []

        # Find YouTube video IDs from iframes
        pattern = r'youtube\.com/embed/([a-zA-Z0-9_-]+)'
        matches = re.finditer(pattern, content)

        for match in matches:
            video_id = match.group(1)
            videos.append({
                "platform": "youtube",
                "video_id": video_id,
                "url": f"https://www.youtube.com/watch?v={video_id}",
                "thumbnail": f"https://img.youtube.com/vi/{video_id}/default.jpg"
            })

        return videos

    def semantic_chunk(self, content: str, metadata: DocumentMetadata,
                       max_tokens: int = 800, min_tokens: int = 200, file_id: str = None, file_path: str = "") -> List[Chunk]:
        """Split content into semantic chunks."""
        chunks = []

        # Split by headers first
        sections = re.split(r'^(#{1,3}\s+.+)$', content, flags=re.MULTILINE)
        sections = [s.strip() for s in sections if s.strip()]

        current_chunk = ""
        chunk_sequence = 0

        for i, section in enumerate(sections):
            # Check if section is a header
            if section.startswith('#'):
                if current_chunk:
                    chunks.append(self._create_chunk(
                        current_chunk, metadata, chunk_sequence, len(chunks) + 1, file_id, file_path
                    ))
                    chunk_sequence += 1
                current_chunk = section + "\n\n"
            else:
                # Estimate tokens (rough approximation: 1 token ≈ 3 characters for Thai)
                estimated_tokens = len(current_chunk) / 3

                if estimated_tokens > max_tokens:
                    # Need to split current chunk
                    sub_chunks = self._split_large_chunk(current_chunk, max_tokens)
                    for sub in sub_chunks:
                        chunks.append(self._create_chunk(
                            sub, metadata, chunk_sequence, len(chunks) + 1, file_id, file_path
                        ))
                        chunk_sequence += 1
                    current_chunk = section + "\n\n"
                elif estimated_tokens + len(section) / 3 > max_tokens:
                    # Save current chunk and start new one
                    chunks.append(self._create_chunk(
                        current_chunk, metadata, chunk_sequence, len(chunks) + 1, file_id, file_path
                    ))
                    chunk_sequence += 1
                    current_chunk = section + "\n\n"
                else:
                    current_chunk += section + "\n\n"

        # Add final chunk
        if current_chunk:
            chunks.append(self._create_chunk(
                current_chunk, metadata, chunk_sequence, len(chunks) + 1, file_id, file_path
            ))

        # Update metadata with chunk count
        metadata.chunk_count = len(chunks)

        return chunks

    def _split_large_chunk(self, text: str, max_tokens: int) -> List[str]:
        """Split a large chunk into smaller pieces."""
        # Try to split at paragraph breaks first
        paragraphs = text.split('\n\n')
        chunks = []
        current = ""

        for para in paragraphs:
            if (len(current) + len(para)) / 3 > max_tokens:
                if current:
                    chunks.append(current)
                # Split long paragraphs by sentences
                if len(para) / 3 > max_tokens:
                    sentences = re.split(r'[.!?。]+', para)
                    temp = ""
                    for sent in sentences:
                        if (len(temp) + len(sent)) / 3 > max_tokens:
                            if temp:
                                chunks.append(temp)
                            temp = sent
                        else:
                            temp += sent + ". "
                    current = temp
                else:
                    current = para
            else:
                current += "\n\n" + para if current else para

        if current:
            chunks.append(current)

        return chunks

    def _create_chunk(self, content: str, metadata: DocumentMetadata,
                      sequence: int, total: int, file_id: str = None, file_path: str = "") -> Chunk:
        """Create a chunk object."""
        # Determine chunk type
        chunk_type = "reference"
        if "## ขั้นตอน" in content or "## Step" in content or re.search(r'^\d+\.', content, re.MULTILINE):
            chunk_type = "procedure"
        elif "[VIDEO:" in content:
            chunk_type = "video"
        elif "|" in content and "---" in content:
            chunk_type = "table"

        # Create unique chunk_id including file identifier to prevent duplicates across files
        if file_id:
            chunk_id = f"{metadata.module}_{metadata.submodule}_{file_id}_{sequence}"
        else:
            chunk_id = f"{metadata.module}_{metadata.submodule}_{sequence}"

        chunk_metadata = {
            "title": metadata.title,
            "title_en": metadata.title_en,
            "lang": metadata.lang,
            "module": metadata.module,
            "submodule": metadata.submodule,
            "doc_type": metadata.doc_type,
            "tags": metadata.tags,
            "country_specific": metadata.country_specific,
            "target_audience": metadata.target_audience,
            "chunk_type": chunk_type
        }

        return Chunk(
            chunk_id=chunk_id,
            doc_path=str(metadata.module) + "/" + str(metadata.submodule),
            file_path=file_path,  # Store original file path for URL generation
            sequence=sequence,
            total_chunks=total,
            chunk_type=chunk_type,
            content=content.strip(),
            metadata=chunk_metadata
        )

    def process_file(self, file_path: Path) -> Dict[str, Any]:
        """Process a single markdown file."""
        try:
            # Read file
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()

            # Skip empty files
            if not content.strip():
                return {"status": "skipped", "reason": "empty"}

            # Create metadata
            metadata = self.create_metadata(file_path, content)

            # Clean content
            cleaned_content = self.clean_content(content)

            # Extract multimedia info
            images = self.extract_image_references(cleaned_content)
            videos = self.extract_video_metadata(cleaned_content)

            # Get relative file path from docs_dir for URL generation
            relative_path = file_path.relative_to(self.docs_dir)
            file_path_str = str(relative_path).replace("\\", "/")

            # Create unique file_id from filename and parent directory
            # This handles cases where multiple files have the same name (e.g., index.md)
            file_id = f"{file_path.parent.name}_{file_path.stem}"

            # Create chunks with file_id for unique chunk IDs and file_path for URLs
            chunks = self.semantic_chunk(cleaned_content, metadata, file_id=file_id, file_path=file_path_str)

            return {
                "status": "success",
                "file": str(file_path),
                "metadata": asdict(metadata),
                "images": images,
                "videos": videos,
                "chunks": [asdict(chunk) for chunk in chunks],
                "stats": {
                    "original_size": len(content),
                    "cleaned_size": len(cleaned_content),
                    "image_count": len(images),
                    "video_count": len(videos),
                    "chunk_count": len(chunks)
                }
            }

        except Exception as e:
            return {
                "status": "error",
                "file": str(file_path),
                "error": str(e)
            }

    def process_directory(self, pattern: str = "**/*.md") -> List[Dict[str, Any]]:
        """Process all markdown files in directory."""
        results = []

        # Find all markdown files
        markdown_files = list(self.docs_dir.glob(pattern))

        # Exclude certain directories
        exclude_dirs = {"node_modules", ".git", "dist", ".vitepress"}
        markdown_files = [
            f for f in markdown_files
            if not any(exclude in f.parts for exclude in exclude_dirs)
        ]

        print(f"Found {len(markdown_files)} markdown files to process")

        for file_path in markdown_files:
            result = self.process_file(file_path)
            results.append(result)
            print(f"Processed: {file_path.name} - {result['status']}")

        return results

    def save_processed_data(self, results: List[Dict[str, Any]]):
        """Save processed data to output directory."""
        # Save summary
        summary = {
            "total_files": len(results),
            "successful": sum(1 for r in results if r.get("status") == "success"),
            "skipped": sum(1 for r in results if r.get("status") == "skipped"),
            "errors": sum(1 for r in results if r.get("status") == "error"),
            "total_chunks": sum(r.get("stats", {}).get("chunk_count", 0) for r in results),
            "total_images": sum(r.get("stats", {}).get("image_count", 0) for r in results),
            "total_videos": sum(r.get("stats", {}).get("video_count", 0) for r in results),
        }

        with open(self.output_dir / "summary.json", 'w', encoding='utf-8') as f:
            json.dump(summary, f, indent=2, ensure_ascii=False)

        # Save all results
        with open(self.output_dir / "processed_documents.json", 'w', encoding='utf-8') as f:
            json.dump(results, f, indent=2, ensure_ascii=False)

        # Save chunks separately for embedding
        all_chunks = []
        for result in results:
            if result.get("status") == "success":
                for chunk in result.get("chunks", []):
                    all_chunks.append(chunk)

        with open(self.output_dir / "chunks.json", 'w', encoding='utf-8') as f:
            json.dump(all_chunks, f, indent=2, ensure_ascii=False)

        print(f"\n=== Summary ===")
        print(f"Total files: {summary['total_files']}")
        print(f"Successful: {summary['successful']}")
        print(f"Total chunks: {summary['total_chunks']}")
        print(f"Total images: {summary['total_images']}")
        print(f"Total videos: {summary['total_videos']}")
        print(f"Output saved to: {self.output_dir}")


def main():
    """Main entry point."""
    import sys

    # Default paths
    docs_dir = Path(__file__).parent.parent / "docs"
    output_dir = Path(__file__).parent.parent / "processed"

    # Parse arguments
    if len(sys.argv) > 1:
        docs_dir = Path(sys.argv[1])
    if len(sys.argv) > 2:
        output_dir = Path(sys.argv[2])

    print(f"Processing markdown files from: {docs_dir}")
    print(f"Output directory: {output_dir}")

    # Create preprocessor
    preprocessor = CarmenRAGPreprocessor(str(docs_dir), str(output_dir))

    # Process all files
    results = preprocessor.process_directory()

    # Save results
    preprocessor.save_processed_data(results)


if __name__ == "__main__":
    main()
