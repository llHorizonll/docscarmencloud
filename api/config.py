"""
Configuration for Carmen RAG API.
"""

from pathlib import Path
from typing import List, Optional
from pydantic_settings import BaseSettings


# Get project root (api directory is inside the project)
PROJECT_ROOT = Path(__file__).parent.parent
DEFAULT_CHROMA_DB_PATH = PROJECT_ROOT / "carmen_chroma_db_v2"


class Settings(BaseSettings):
    """Application settings."""

    # Database
    CHROMA_DB_PATH: Path = DEFAULT_CHROMA_DB_PATH
    COLLECTION_NAME: str = "carmen_docs_2"

    # API
    API_HOST: str = "127.0.0.1"
    API_PORT: int = 8001
    ALLOWED_ORIGINS: List[str] = [
        "http://localhost:5173",
        "http://localhost:4173",
        "http://127.0.0.1:5173",
        "http://127.0.0.1:4173",
    ]

    # RAG
    DEFAULT_N_RESULTS: int = 5
    MAX_N_RESULTS: int = 50

    # LLM Settings (OpenRouter)
    OPENROUTER_API_KEY: Optional[str] = None
    LLM_MODEL: str = "nvidia/llama-3.1-nemotron-70b-instruct"  # Nemotron 3 Nano model
    LLM_BASE_URL: str = "https://openrouter.ai/api/v1"
    LLM_TEMPERATURE: float = 0.1  # Lower for more deterministic extraction
    LLM_MAX_TOKENS: int = 2000  # Higher to include full solution content

    # CORS
    ALLOW_CREDENTIALS: bool = True
    ALLOW_METHODS: List[str] = ["*"]
    ALLOW_HEADERS: List[str] = ["*"]

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        extra = "ignore"


settings = Settings()
