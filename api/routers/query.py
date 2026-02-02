"""
Query router for documentation search.
"""

import json
from fastapi import APIRouter, HTTPException
from fastapi.responses import StreamingResponse
from services import get_rag_service
from models.schemas import QueryRequest, QueryResponse

router = APIRouter()


@router.post("/query", response_model=QueryResponse, tags=["query"])
async def query_documentation(request: QueryRequest):
    """
    Query Carmen documentation using RAG.

    - **query**: User's question (Thai or English)
    - **language**: Response language (th or en, default: th)
    - **n_results**: Number of results to retrieve (1-50, default: 5)
    - **module_filter**: Optional filter by module (ap, ar, gl, asset, etc.)

    Returns formatted answer with can/cannot indication and sources.
    """
    try:
        rag_service = get_rag_service()

        result = rag_service.query(
            query_text=request.query,
            n_results=request.n_results,
            module_filter=request.module_filter,
            language=request.language.value
        )

        return QueryResponse(**result)

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Query failed: {str(e)}"
        )


@router.post("/query/stream", tags=["query"])
async def query_stream(request: QueryRequest):
    """
    Stream query response using Server-Sent Events (SSE).

    Useful for real-time streaming of responses.
    """
    async def generate():
        try:
            rag_service = get_rag_service()

            result = rag_service.query(
                query_text=request.query,
                n_results=request.n_results,
                module_filter=request.module_filter,
                language=request.language.value
            )

            # Send as SSE
            yield f"data: {json.dumps(result)}\n\n"
            yield "data: [DONE]\n\n"

        except Exception as e:
            error_data = {"error": str(e)}
            yield f"data: {json.dumps(error_data)}\n\n"
            yield "data: [DONE]\n\n"

    return StreamingResponse(
        generate(),
        media_type="text/event-stream",
        headers={
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
        }
    )
