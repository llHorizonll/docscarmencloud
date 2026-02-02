"""
Health check router.
"""

from fastapi import APIRouter
from services import get_rag_service
from models.schemas import HealthResponse

router = APIRouter()


@router.get("/health", response_model=HealthResponse, tags=["health"])
async def health_check():
    """
    Health check endpoint.

    Returns API status and database information.
    """
    rag_service = get_rag_service()

    db_info = rag_service.get_database_info()

    return HealthResponse(
        status="healthy",
        database={
            "collection": db_info["collection"],
            "count": db_info["count"],
            "persist_directory": db_info["persist_directory"]
        },
        llm_loaded=rag_service.is_initialized
    )
