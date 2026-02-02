"""
Pydantic models for request/response validation.
"""

from pydantic import BaseModel, Field
from typing import List, Optional
from enum import Enum


class Language(str, Enum):
    """Supported languages."""
    THAI = "th"
    ENGLISH = "en"


class CanCannotStatus(str, Enum):
    """Can/Cannot status indicators."""
    CAN = "can"
    CANNOT = "cannot"
    CANNOT_WITH_WORKAROUND = "cannot_with_workaround"
    UNKNOWN = "unknown"


class SourceMetadata(BaseModel):
    """Source metadata for a result."""
    module: str
    submodule: str
    doc_type: str
    url: str  # Clickable URL to source documentation
    distance: float


class QueryRequest(BaseModel):
    """Request model for querying documentation."""
    query: str = Field(..., min_length=1, max_length=500, description="User query")
    language: Language = Field(default=Language.THAI, description="Response language")
    n_results: int = Field(default=5, ge=1, le=50, description="Number of results")
    module_filter: Optional[str] = Field(default=None, description="Filter by module")


class QueryResponse(BaseModel):
    """Response model for documentation query."""
    query: str
    answer: str
    can_cannot: CanCannotStatus
    sources: List[SourceMetadata]
    language: str
    processing_time_ms: int


class DatabaseInfo(BaseModel):
    """Database information."""
    collection: str
    count: int
    persist_directory: str


class HealthResponse(BaseModel):
    """Health check response."""
    status: str
    database: DatabaseInfo
    llm_loaded: bool
