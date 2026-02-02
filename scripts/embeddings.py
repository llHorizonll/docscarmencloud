"""
Custom Embedding Functions for Carmen RAG

Supports multiple embedding models optimized for Thai-English content.
"""

import os
from typing import List
from chromadb.api.types import EmbeddingFunction


class MultilingualE5Embedding(EmbeddingFunction):
    """
    Custom embedding function using multilingual-e5 model.
    This model is optimized for Thai-English bilingual content.
    Uses e5-base by default (smaller, ~400MB vs 2.2GB for e5-large)
    """

    def __init__(self, model_name: str = "intfloat/multilingual-e5-base"):
        """Initialize the embedding model."""
        self.model_name = model_name
        self._model = None
        self._device = None

    def _load_model(self):
        """Lazy load the model."""
        if self._model is None:
            try:
                from sentence_transformers import SentenceTransformer
                import torch

                # Check if CUDA is available
                self._device = "cuda" if torch.cuda.is_available() else "cpu"
                print(f"[*] Loading embedding model: {self.model_name}")
                print(f"    Device: {self._device}")

                self._model = SentenceTransformer(self.model_name, device=self._device)
                print("[*] Model loaded successfully")

            except ImportError:
                raise ImportError(
                    "sentence_transformers is required. Install with: "
                    "pip install sentence-transformers"
                )

    def __call__(self, texts: List[str]) -> List[List[float]]:
        """
        Generate embeddings for a list of texts.

        Args:
            texts: List of text strings to embed

        Returns:
            List of embedding vectors
        """
        self._load_model()

        # E5 models require "query:" prefix for queries
        # For documents, we use "passage:" prefix
        processed_texts = []
        for text in texts:
            # Check if this looks like a query (short, question-like)
            is_query = (
                "?" in text or
                any(text.startswith(p) for p in ["วิธี", "How", "What", "Where", "When", "Why"]) or
                "วิธี" in text or "how" in text.lower()
            )
            if len(text) < 200 and is_query:
                processed_texts.append(f"query: {text}")
            else:
                processed_texts.append(f"passage: {text}")

        # Generate embeddings
        embeddings = self._model.encode(
            processed_texts,
            convert_to_numpy=True,
            normalize_embeddings=True  # Important for cosine similarity
        )

        return embeddings.tolist()


class ThaiEmbedding(EmbeddingFunction):
    """
    Fallback embedding using paraphrase-multilingual-mpnet-base-v2.
    Good alternative if E5 is not available. (~270MB)
    """

    def __init__(self, model_name: str = "paraphrase-multilingual-mpnet-base-v2"):
        """Initialize the embedding model."""
        self.model_name = model_name
        self._model = None
        self._device = None

    def _load_model(self):
        """Lazy load the model."""
        if self._model is None:
            try:
                from sentence_transformers import SentenceTransformer
                import torch

                self._device = "cuda" if torch.cuda.is_available() else "cpu"
                print(f"[*] Loading embedding model: {self.model_name}")
                print(f"    Device: {self._device}")

                self._model = SentenceTransformer(self.model_name, device=self._device)
                print("[*] Model loaded successfully")

            except ImportError:
                raise ImportError(
                    "sentence_transformers is required. Install with: "
                    "pip install sentence-transformers"
                )

    def __call__(self, texts: List[str]) -> List[List[float]]:
        """Generate embeddings for texts."""
        self._load_model()

        embeddings = self._model.encode(
            texts,
            convert_to_numpy=True,
            normalize_embeddings=True
        )

        return embeddings.tolist()


# Recommended embedding functions
EMBEDDING_MODELS = {
    "mpnet": lambda: ThaiEmbedding("paraphrase-multilingual-mpnet-base-v2"),
    "e5-base": lambda: MultilingualE5Embedding("intfloat/multilingual-e5-base"),
    "e5-large": lambda: MultilingualE5Embedding("intfloat/multilingual-e5-large"),
    "default": lambda: ThaiEmbedding("paraphrase-multilingual-mpnet-base-v2"),
}


def get_embedding_function(model_name: str = "mpnet") -> EmbeddingFunction:
    """
    Get an embedding function by name.

    Args:
        model_name: Name of the model ('e5-large', 'e5-base', 'mpnet', 'default')

    Returns:
        Embedding function instance
    """
    if model_name not in EMBEDDING_MODELS:
        raise ValueError(
            f"Unknown model: {model_name}. Available: {list(EMBEDDING_MODELS.keys())}"
        )

    return EMBEDDING_MODELS[model_name]()


if __name__ == "__main__":
    # Test the embedding function
    print("[*] Testing embedding function...")

    embed_fn = get_embedding_function("mpnet")

    test_texts = [
        "วิธีสร้างใบแจ้งหนี้ AP",
        "How to create AP invoice",
        "Account Payable module for managing vendor invoices",
    ]

    print("\n[*] Generating embeddings for test texts...")
    embeddings = embed_fn(test_texts)

    print(f"\n[OK] Generated {len(embeddings)} embeddings")
    print(f"    Embedding dimension: {len(embeddings[0])}")

    # Test similarity (dot product since embeddings are normalized)
    import numpy as np

    e1 = np.array(embeddings[0])
    e2 = np.array(embeddings[1])
    e3 = np.array(embeddings[2])

    sim_thai_en = np.dot(e1, e2)
    sim_thai_doc = np.dot(e1, e3)
    sim_en_doc = np.dot(e2, e3)

    print(f"\n[INFO] Similarity scores:")
    print(f"    Thai-English (same meaning): {sim_thai_en:.4f}")
    print(f"    Thai-Document: {sim_thai_doc:.4f}")
    print(f"    English-Document: {sim_en_doc:.4f}")
