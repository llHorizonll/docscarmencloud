"""
ChromaDB Embedding Script for Carmen Documentation RAG

This script:
1. Loads processed chunks from preprocessing step
2. Generates embeddings using multilingual models
3. Stores embeddings in ChromaDB
4. Provides query interface for testing
"""

import os
import json
from pathlib import Path
from typing import List, Dict, Any, Optional, Tuple
import chromadb
from chromadb.config import Settings


class CarmenChromaDB:
    """ChromaDB manager for Carmen documentation RAG."""

    def __init__(self,
                 persist_directory: str = "./carmen_chroma_db",
                 collection_name: str = "carmen_docs_2"):
        """
        Initialize ChromaDB client.

        Args:
            persist_directory: Directory to persist the database
            collection_name: Name of the collection
        """
        self.persist_directory = Path(persist_directory)
        self.persist_directory.mkdir(exist_ok=True)

        # Initialize ChromaDB client with persistence
        self.client = chromadb.PersistentClient(
            path=str(self.persist_directory),
            settings=Settings(
                anonymized_telemetry=False,
                allow_reset=True
            )
        )

        self.collection_name = collection_name
        self.collection = None

    @staticmethod
    def generate_url(file_path: str) -> str:
        """Convert file path to VitePress URL."""
        if not file_path:
            return ""
        # VitePress uses direct file-to-URL mapping
        # docs/carmen_cloud/ap/AP-invoice.md -> /carmen_cloud/ap/AP-invoice.md
        return "/" + file_path

    def create_collection(self, reset: bool = False):
        """Create or recreate the collection."""
        if reset:
            try:
                self.client.delete_collection(self.collection_name)
                print(f"Deleted existing collection: {self.collection_name}")
            except Exception:
                pass

        # Create collection with metadata configuration
        self.collection = self.client.get_or_create_collection(
            name=self.collection_name,
            metadata={"description": "Carmen Cloud Documentation RAG"}
        )

        print(f"Collection '{self.collection_name}' ready")

    def load_chunks(self, chunks_file: str) -> List[Dict[str, Any]]:
        """Load processed chunks from JSON file."""
        chunks_path = Path(chunks_file)
        if not chunks_path.exists():
            raise FileNotFoundError(f"Chunks file not found: {chunks_file}")

        with open(chunks_path, 'r', encoding='utf-8') as f:
            chunks = json.load(f)

        print(f"Loaded {len(chunks)} chunks from {chunks_file}")
        return chunks

    def prepare_embeddings(self, chunks: List[Dict[str, Any]]) -> Tuple[List[str], List[Dict], List[Dict]]:
        """
        Prepare data for ChromaDB insertion.

        Returns:
            Tuple of (ids, documents, metadatas)
        """
        ids = []
        documents = []
        metadatas = []

        for i, chunk in enumerate(chunks):
            # Create unique ID
            chunk_id = chunk.get("chunk_id", f"chunk_{i}")

            # Prepare document content
            content = chunk.get("content", "")

            # Add bilingual context for better search
            metadata = chunk.get("metadata", {})
            title_en = metadata.get("title_en", "")
            if title_en:
                # Prepend English title for better cross-language search
                content = f"[EN: {title_en}]\n\n{content}"

            # Prepare metadata (ChromaDB requires flat metadata)
            flat_metadata = {
                "file_path": chunk.get("file_path", ""),  # Store file path for URL generation
                "module": metadata.get("module", ""),
                "submodule": metadata.get("submodule", ""),
                "doc_type": metadata.get("doc_type", ""),
                "country": metadata.get("country_specific", ""),
                "chunk_type": chunk.get("chunk_type", ""),
                "sequence": chunk.get("sequence", 0),
                "total_chunks": chunk.get("total_chunks", 1),
                "lang": metadata.get("lang", "th-TH")
            }

            # Add tags as comma-separated string
            tags = metadata.get("tags", [])
            if tags:
                flat_metadata["tags"] = ",".join(tags)

            ids.append(chunk_id)
            documents.append(content)
            metadatas.append(flat_metadata)

        return ids, documents, metadatas

    def add_chunks(self, chunks: List[Dict[str, Any]], batch_size: int = 100):
        """
        Add chunks to the collection.

        Args:
            chunks: List of chunk dictionaries
            batch_size: Number of chunks to add per batch
        """
        if not self.collection:
            raise RuntimeError("Collection not initialized. Call create_collection() first.")

        # Prepare data
        ids, documents, metadatas = self.prepare_embeddings(chunks)

        # Add in batches
        total = len(ids)
        for i in range(0, total, batch_size):
            batch_end = min(i + batch_size, total)
            batch_ids = ids[i:batch_end]
            batch_docs = documents[i:batch_end]
            batch_metas = metadatas[i:batch_end]

            self.collection.add(
                ids=batch_ids,
                documents=batch_docs,
                metadatas=batch_metas
            )

            print(f"Added batch {i//batch_size + 1}/{(total + batch_size - 1)//batch_size} "
                  f"({batch_end - i} chunks, {batch_end}/{total} total)")

        print(f"Successfully added {total} chunks to collection")

    def query(self,
              query_text: str,
              n_results: int = 5,
              filter_metadata: Optional[Dict[str, Any]] = None) -> List[Dict[str, Any]]:
        """
        Query the collection.

        Args:
            query_text: The query string
            n_results: Number of results to return
            filter_metadata: Optional metadata filter

        Returns:
            List of results with content and metadata
        """
        if not self.collection:
            raise RuntimeError("Collection not initialized. Call create_collection() first.")

        results = self.collection.query(
            query_texts=[query_text],
            n_results=n_results,
            where=filter_metadata
        )

        # Format results
        formatted = []
        if results['documents'] and results['documents'][0]:
            for i, doc in enumerate(results['documents'][0]):
                formatted.append({
                    "content": doc,
                    "metadata": results['metadatas'][0][i] if results['metadatas'] else {},
                    "distance": results['distances'][0][i] if results['distances'] else None,
                    "chunk_id": results['ids'][0][i] if results['ids'] else None
                })

        return formatted

    def query_by_module(self,
                       query_text: str,
                       module: str,
                       n_results: int = 5) -> List[Dict[str, Any]]:
        """Query within a specific module."""
        return self.query(query_text, n_results, filter_metadata={"module": module})

    def query_by_country(self,
                        query_text: str,
                        country: str,
                        n_results: int = 5) -> List[Dict[str, Any]]:
        """Query within a specific country context."""
        return self.query(query_text, n_results, filter_metadata={"country": country})

    def get_collection_info(self) -> Dict[str, Any]:
        """Get information about the collection."""
        if not self.collection:
            return {"error": "Collection not initialized"}

        count = self.collection.count()

        # Get sample of metadata to analyze
        # Note: ChromaDB doesn't have a direct way to get all metadata
        # We'd need to query with a limit

        return {
            "name": self.collection_name,
            "count": count,
            "persist_directory": str(self.persist_directory)
        }


class ThaiEnglishQueryProcessor:
    """Process queries for Thai-English bilingual search."""

    @staticmethod
    def translate_keywords(query: str) -> str:
        """
        Translate common accounting keywords between Thai and English.

        This is a simple translation table. For production, use a proper
        translation API like Google Translate or a local model.
        """
        translations = {
            # Thai to English
            "ใบแจ้งหนี้": "invoice",
            "บันทึกบัญชี": "post",
            "เจ้าหนี้": "payable",
            "ลูกหนี้": "receivable",
            "ภาษี": "tax",
            "วาท": "vat",
            "หัก ณ ที่จ่าย": "withholding",
            "ค่าเสื่อม": "depreciation",
            "สินทรัพย์": "asset",
            "สมุดบัญชีรายวัน": "journal voucher",
            "โพสต์": "post",
            "ลบ": "delete",
            "แก้ไข": "edit",
            "เปลี่ยน": "change",
            "สร้าง": "create",
            "บันทึก": "save",
            "กด": "press",
            "ไม่ได้": "cannot",
            "ไม่สามารถ": "cannot",

            # English to Thai
            "invoice": "ใบแจ้งหนี้",
            "payable": "เจ้าหนี้",
            "receivable": "ลูกหนี้",
            "tax": "ภาษี",
            "vat": "วาท",
            "withholding": "หัก ณ ที่จ่าย",
            "depreciation": "ค่าเสื่อม",
            "asset": "สินทรัพย์",
            "journal": "สมุดบัญชีรายวัน",
            "post": "โพสต์",
            "delete": "ลบ",
            "edit": "แก้ไข",
            "change": "เปลี่ยน",
            "create": "สร้าง",
            "save": "บันทึก",
            "press": "กด",
            "cannot": "ไม่ได้",
        }

        augmented_query = query

        for thai, english in translations.items():
            if thai in query:
                augmented_query += f" {english}"
            elif english in query.lower():
                augmented_query += f" {thai}"

        return augmented_query

    @staticmethod
    def augment_query(query: str) -> str:
        """Augment query with related terms for better retrieval."""
        # Add keyword translations
        query = ThaiEnglishQueryProcessor.translate_keywords(query)

        # Add module hints
        module_hints = {
            "ap": ["account payable", "เจ้าหนี้", "vendor", "purchase", "ap invoice", "ap payment"],
            "ar": ["account receivable", "ลูกหนี้", "customer", "sales", "ar invoice", "receipt"],
            "gl": ["general ledger", "บัญชีแยกประเภท", "journal", "voucher", "jv", "posting"],
            "asset": ["สินทรัพย์", "depreciation", "ค่าเสื่อม", "register", "disposal"],
            "configuration": ["account code", "user permission", "department", "payment type", "currency", "setup"],
            "workbook": ["refresh", "add-in", "excel", "upload", "workbook", "template"],
        }

        query_lower = query.lower()
        for module, hints in module_hints.items():
            if any(hint in query_lower for hint in hints):
                query += f" module:{module}"

                # For troubleshooting, add extra context
                if any(kw in query_lower for kw in ["ไม่ได้", "ไม่สามารถ", "cannot", "error", "ปัญหา", "ไม่"]):
                    if module == "configuration":
                        query += " configuration troubleshooting delete edit"
                    elif module == "gl":
                        query += " gl troubleshooting posted jv"
                    elif module == "asset":
                        query += " asset troubleshooting depreciation"
                break

        # If query is about deleting/changing configuration items
        if any(kw in query_lower for kw in ["ลบ", "แก้ไข", "เปลี่ยน", "delete", "edit", "change"]):
            if "account code" in query_lower:
                # Account Code deletion queries
                query += ' configuration troubleshooting "วิธีแก้ไขที่ถูกต้อง" inactive status'
            elif "account nature" in query_lower:
                # Account Nature change queries - don't add inactive status
                query += ' configuration troubleshooting "วิธีแก้ไขที่ถูกต้อง"'
            if "jv" in query_lower or "journal" in query_lower or "posted" in query_lower:
                query += ' gl troubleshooting "วิธีแก้ไขที่ถูกต้อง" reversal'
            if "invoice" in query_lower and "ap" in query_lower:
                query += " ap troubleshooting"

        return query


def main():
    """Main entry point for testing."""
    import sys

    # Configuration
    chunks_file = Path(__file__).parent.parent / "processed" / "chunks.json"
    persist_dir = Path(__file__).parent.parent / "carmen_chroma_db"

    # Initialize
    print("Initializing Carmen ChromaDB...")
    db = CarmenChromaDB(str(persist_dir))

    # Create collection
    db.create_collection(reset=False)

    # Load and add chunks (if collection is empty)
    if db.collection.count() == 0:
        print("Loading chunks...")
        chunks = db.load_chunks(str(chunks_file))
        print("Adding chunks to collection...")
        db.add_chunks(chunks)
    else:
        print(f"Collection already has {db.collection.count()} chunks")

    # Interactive query mode
    print("\n" + "="*50)
    print("Carmen Documentation RAG - Query Mode")
    print("="*50)
    print("Enter queries in Thai or English.")
    print("Commands: 'quit', 'info', 'stats'")
    print("-"*50)

    query_processor = ThaiEnglishQueryProcessor()

    while True:
        try:
            user_input = input("\nQuery: ").strip()

            if not user_input:
                continue

            if user_input.lower() in ['quit', 'exit', 'q']:
                print("Goodbye!")
                break

            if user_input.lower() == 'info':
                info = db.get_collection_info()
                print(json.dumps(info, indent=2))
                continue

            if user_input.lower() == 'stats':
                count = db.collection.count()
                print(f"Total chunks in database: {count}")
                continue

            # Augment query for better retrieval
            augmented_query = query_processor.augment_query(user_input)

            # Execute query
            results = db.query(augmented_query, n_results=5)

            # Display results
            print(f"\n--- Results for: '{user_input}' ---")
            for i, result in enumerate(results, 1):
                print(f"\n{i}. [{result['metadata'].get('module', 'N/A')}/{result['metadata'].get('submodule', 'N/A')}] "
                      f"(Distance: {result.get('distance', 'N/A'):.3f})")
                print(f"   Type: {result['metadata'].get('doc_type', 'N/A')}")
                content = result['content'][:300] + "..." if len(result['content']) > 300 else result['content']
                print(f"   Content: {content}")

        except KeyboardInterrupt:
            print("\nGoodbye!")
            break
        except Exception as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()
