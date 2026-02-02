"""
RAG Service - Wraps existing ChromaDB and response formatter.
With LLM generation via OpenRouter.
"""

import sys
import os
import time
import asyncio
from pathlib import Path
from typing import Optional, Dict, Any, List
import httpx

# Add scripts directory to path to import existing modules
_scripts_path = Path(__file__).parent.parent.parent / "scripts"
if str(_scripts_path) not in sys.path:
    sys.path.insert(0, str(_scripts_path))

from chroma_embedder import CarmenChromaDB, ThaiEnglishQueryProcessor
from response_formatter import CarmenResponseFormatter


class RAGService:
    """
    Service for RAG-based documentation queries with LLM generation.
    """

    _instance: Optional["RAGService"] = None

    def __new__(cls) -> "RAGService":
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._initialized = False
        return cls._instance

    def __init__(self):
        if self._initialized:
            return

        from config import settings

        # Initialize ChromaDB connection
        self.db = CarmenChromaDB(str(settings.CHROMA_DB_PATH))
        self.db.create_collection()

        # Initialize query processor and response formatter
        self.query_processor = ThaiEnglishQueryProcessor()
        self.formatter = CarmenResponseFormatter()

        # LLM Settings
        self.llm_api_key = settings.OPENROUTER_API_KEY or os.getenv("OPENROUTER_API_KEY")
        self.llm_model = settings.LLM_MODEL
        self.llm_base_url = settings.LLM_BASE_URL
        self.llm_temperature = settings.LLM_TEMPERATURE
        self.llm_max_tokens = settings.LLM_MAX_TOKENS
        self.llm_enabled = bool(self.llm_api_key)

        self._initialized = True

    async def _generate_with_llm(
        self,
        query: str,
        context_docs: List[Dict[str, Any]],
        language: str = "th"
    ) -> str:
        """
        Generate response using LLM via OpenRouter.
        LLM acts as EXTRACTOR - extracts and formats content from documents, NOT generates new content.

        Args:
            query: User's question
            context_docs: Retrieved context documents
            language: Response language

        Returns:
            Generated response
        """
        if not self.llm_enabled:
            return None

        # Build context from retrieved documents - focus on solution markers
        context_parts = []
        for i, doc in enumerate(context_docs[:10], 1):
            content = doc.get("document", "") or doc.get("content", "")
            metadata = doc.get("metadata", {})
            source = metadata.get("module", "") + "/" + metadata.get("submodule", "")
            context_parts.append(f"[เอกสารที่ {i} จาก {source}]\n{content}")

        context = "\n\n".join(context_parts)

        # System prompt - STRICT extraction mode
        if language == "th":
            system_prompt = f"""คุณคือ EXTRACTOR ดึงข้อมูลจากเอกสารเท่านั้น ห้ามคิดเอง

เอกสารที่มี:
{context}

คำถาม: {query}

กฎระเบียบ:
1. ดึงคำตอบจากเอกสารโดยตรง เหมือนคัดลอกมา
2. ถ้ามี "วิธีแก้ไขที่ถูกต้อง" ให้ใช้ขั้นตอนนั้นทั้งหมด
3. เริ่มตอบด้วย **ได้** หรือ **ไม่ได้** หรือ **ไม่ได้ (แต่มีวิธีแก้ไข)** ให้ถูกต้อง
4. อย่าเติมข้อมูลเอง อย่าแต่งประโยคเอง
5. อย่าอธิบายเพิ่ม อย่าสรุป ให้ข้อมูลเต็มๆ จากเอกสาร
6. ถ้ามี checklist ให้รวมด้วย

รูปแบบการตอบ:
**ได้** หรือ **ไม่ได้** หรือ **ไม่ได้ (แต่มีวิธีแก้ไข)**

[วิธีแก้ไข/ขั้นตอนจากเอกสาร]

**Checklist ตรวจสอบ:**
[checklist จากเอกสารถ้ามี]

ที่มา: [module/submodule]"""
        else:
            system_prompt = f"""You are an EXTRACTOR - extract content from documents only, do NOT generate.

Available documents:
{context}

Question: {query}

Rules:
1. Extract answer directly from documents
2. Use "Solutions:" or similar markers
3. Start with **Can** or **Cannot** or **Cannot (but has workaround)**
4. Do NOT add your own information
5. Do NOT explain or summarize, give full content from document
6. Include checklist if present

Response format:
**Can** or **Cannot** or **Cannot (but has workaround)**

[solution/steps from document]

**Checklist:**
[checklist if present]

Source: [module/submodule]"""

        try:
            async with httpx.AsyncClient(timeout=30.0) as client:
                response = await client.post(
                    f"{self.llm_base_url}/chat/completions",
                    headers={
                        "Authorization": f"Bearer {self.llm_api_key}",
                        "Content-Type": "application/json",
                        "HTTP-Referer": "https://carmen.blue",
                        "X-Title": "Carmen Cloud Documentation",
                    },
                    json={
                        "model": self.llm_model,
                        "messages": [
                            {"role": "system", "content": system_prompt},
                            {"role": "user", "content": query}
                        ],
                        "temperature": self.llm_temperature,
                        "max_tokens": self.llm_max_tokens,
                    }
                )
                response.raise_for_status()
                data = response.json()
                return data["choices"][0]["message"]["content"]
        except Exception as e:
            print(f"LLM generation error: {e}")
            return None

    def query(
        self,
        query_text: str,
        n_results: int = 5,
        module_filter: Optional[str] = None,
        language: str = "th",
        use_llm: Optional[bool] = None  # Default: True (use LLM)
    ) -> Dict[str, Any]:
        """
        Query the documentation using RAG with optional LLM generation.

        Args:
            query_text: User's query
            n_results: Number of results to retrieve
            module_filter: Optional filter by module
            language: Response language ("th" or "en")
            use_llm: Use LLM for response (default: True, set False for faster formatter)

        Returns:
            Dictionary with query results and metadata
        """
        start_time = time.time()

        # Augment query for better retrieval
        augmented_query = self.query_processor.augment_query(query_text)

        # Build metadata filter
        filter_metadata = {"module": module_filter} if module_filter else None

        # For troubleshooting queries, get more results
        is_troubleshooting = self._is_troubleshooting_query(query_text)
        actual_n_results = n_results if not is_troubleshooting else min(n_results * 10, 50)

        # Query database
        results = self.db.query(
            augmented_query,
            n_results=actual_n_results,
            filter_metadata=filter_metadata
        )

        # Determine if we should use LLM - default to True (use LLM for better answers)
        # Set use_llm=False to use faster formatter instead
        should_use_llm = use_llm if use_llm is not None else True

        if should_use_llm and self.llm_enabled:
            # Use async LLM generation
            try:
                llm_response = asyncio.run(self._generate_with_llm(query_text, results, language))
                if llm_response:
                    formatted_response = llm_response
                    can_cannot = self._extract_can_cannot_from_llm(llm_response, results)
                else:
                    # Fallback to formatter if LLM fails
                    formatted_response = self.formatter.format_response(
                        query_text, results, language=language
                    )
                    can_cannot = self._extract_can_cannot_status(formatted_response)
            except RuntimeError:
                # Event loop is already running, try creating new loop
                import nest_asyncio
                nest_asyncio.apply()
                try:
                    llm_response = asyncio.run(self._generate_with_llm(query_text, results, language))
                    if llm_response:
                        formatted_response = llm_response
                        can_cannot = self._extract_can_cannot_from_llm(llm_response, results)
                    else:
                        formatted_response = self.formatter.format_response(
                            query_text, results, language=language
                        )
                        can_cannot = self._extract_can_cannot_status(formatted_response)
                except:
                    # Final fallback
                    formatted_response = self.formatter.format_response(
                        query_text, results, language=language
                    )
                    can_cannot = self._extract_can_cannot_status(formatted_response)
        else:
            # Use existing formatter (no LLM)
            formatted_response = self.formatter.format_response(
                query_text, results, language=language
            )
            can_cannot = self._extract_can_cannot_status(formatted_response)

        # Extract source metadata with URLs
        sources = []
        for i, r in enumerate(results[:5]):  # Top 5 sources
            metadata = r.get("metadata", {})
            file_path = metadata.get("file_path", "")
            url = self.db.generate_url(file_path) if file_path else ""

            sources.append({
                "module": metadata.get("module", "unknown"),
                "submodule": metadata.get("submodule", "unknown"),
                "doc_type": metadata.get("doc_type", "unknown"),
                "url": url,  # Add clickable URL
                "distance": r.get("distance", 0)
            })

        processing_time = int((time.time() - start_time) * 1000)

        return {
            "query": query_text,
            "answer": formatted_response,
            "can_cannot": can_cannot,
            "sources": sources,
            "language": language,
            "processing_time_ms": processing_time
        }

    def _is_troubleshooting_query(self, query: str) -> bool:
        """Check if query is about a problem/troubleshooting."""
        keywords = [
            "ไม่ได้", "ไม่สามารถ", "error", "ผิดพลาด",
            "ปัญหา", "แก้ไข", "fix", "troubleshooting",
            "cannot", "can't", "not working",
            "ได้ไหม", "ไหม", "ทำได้ไหม", "ทำยังไง", "วิธี"
        ]
        return any(kw in query.lower() for kw in keywords)

    def _extract_can_cannot_status(self, response: str) -> str:
        """
        Extract can/cannot status from formatted response.

        Returns: One of "can", "cannot", "cannot_with_workaround", "unknown"
        """
        if "**ได้** (มีวิธีแก้ไข)" in response:
            return "cannot_with_workaround"
        elif "**ไม่ได้** (แต่มีวิธีแก้ไข)" in response:
            return "cannot_with_workaround"
        elif "**ไม่ได้**" in response:
            return "cannot"
        elif "**ได้**" in response:
            return "can"
        return "unknown"

    def _extract_can_cannot_from_llm(
        self,
        llm_response: str,
        results: List[Dict[str, Any]]
    ) -> str:
        """
        Extract can/cannot status from LLM response and retrieved docs.
        """
        response_lower = llm_response.lower()

        # Check for positive indicators (can do)
        positive_words = ["ได้", "สามารถ", "สำเร็จ", "ทำได้", "yes", "can", "possible"]
        # Check for negative indicators (cannot do)
        negative_words = ["ไม่ได้", "ไม่สามารถ", "ไม่", "no", "cannot", "not possible"]
        # Check for workaround indicators
        workaround_words = ["แต่", "อย่างไร", "วิธีแก้", "วิธีทำ", "fix", "แก้ไข", "solve", "however"]

        has_positive = any(word in llm_response for word in positive_words)
        has_negative = any(word in llm_response for word in negative_words)
        has_workaround = any(word in llm_response for word in workaround_words)

        # Check retrieved documents for can/cannot badges
        for r in results[:3]:
            content = r.get("document", "") or r.get("content", "")
            if "**ได้**" in content:
                has_positive = True
            if "**ไม่ได้**" in content:
                has_negative = True

        # Determine status
        if has_negative and has_workaround:
            return "cannot_with_workaround"
        elif has_negative:
            return "cannot"
        elif has_positive:
            return "can"
        return "unknown"

    def get_database_info(self) -> Dict[str, Any]:
        """Get database information."""
        info = self.db.get_collection_info()
        return {
            "collection": info["name"],
            "count": info["count"],
            "persist_directory": info["persist_directory"],
            "llm_enabled": self.llm_enabled,
            "llm_model": self.llm_model if self.llm_enabled else None
        }

    @property
    def is_initialized(self) -> bool:
        """Check if service is initialized."""
        return self._initialized


# Singleton instance
_rag_service_instance: Optional[RAGService] = None


def get_rag_service() -> RAGService:
    """Get or create the RAG service singleton instance."""
    global _rag_service_instance
    if _rag_service_instance is None:
        _rag_service_instance = RAGService()
    return _rag_service_instance
