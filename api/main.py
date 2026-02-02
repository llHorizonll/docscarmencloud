"""
Carmen RAG API - Main FastAPI Application

FastAPI server that exposes the ChromaDB RAG functionality
for Carmen Cloud documentation search.
"""

import nest_asyncio  # Enable nested event loops for LLM calls

# Apply nest_asyncio to allow async LLM calls within sync context
nest_asyncio.apply()

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from config import settings
from routers import query, health

# Create FastAPI application
app = FastAPI(
    title="Carmen RAG API",
    description="RAG-based documentation search API for Carmen Cloud",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,
    allow_credentials=settings.ALLOW_CREDENTIALS,
    allow_methods=settings.ALLOW_METHODS,
    allow_headers=settings.ALLOW_HEADERS,
)

# Include routers
app.include_router(query.router, prefix="/api/v1")
app.include_router(health.router, prefix="/api/v1")


@app.get("/", tags=["root"])
async def root():
    """Root endpoint with API information."""
    return {
        "name": "Carmen RAG API",
        "version": "1.0.0",
        "description": "RAG-based documentation search API for Carmen Cloud",
        "endpoints": {
            "health": "/api/v1/health",
            "query": "/api/v1/query",
            "query_stream": "/api/v1/query/stream",
            "docs": "/docs"
        }
    }


@app.get("/health", tags=["root"])
async def health_redirect():
    """Redirect to health check endpoint."""
    from fastapi.responses import RedirectResponse
    return RedirectResponse(url="/api/v1/health")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "main:app",
        host=settings.API_HOST,
        port=settings.API_PORT,
        reload=True
    )
