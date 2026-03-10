#!/usr/bin/env python3
"""
FastAPI wrapper for the HPC Deep Research (DR) Pipeline
Exposes the DR functionality via HTTP REST API
"""

import sys
import os
from fastapi import FastAPI, HTTPException, BackgroundTasks
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse
from pydantic import BaseModel, Field
from typing import Optional, List, Dict, Any
import asyncio
import json
import time

# Add ticketknowledgedb to path so we can import DR_Pipeline
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "ticketknowledgedb"))

from DR_Pipeline.dr_workflow import DRWorkflow
from DR_Pipeline.dr_config import config
from DR_Pipeline.search_service import search_service
from DR_Pipeline.dr_models import HPCSearchRequest

# Initialize FastAPI app
app = FastAPI(
    title="HPC Deep Research API",
    description="Multi-agent deep research system for HPC support questions",
    version="1.0.0",
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize DR workflow
dr_workflow = DRWorkflow()


# ============================================================================
# Request/Response Models
# ============================================================================


class QueryRequest(BaseModel):
    """Request model for DR query"""

    query: str = Field(..., description="HPC support question to research")
    max_iterations: Optional[int] = Field(None, description="Override max iterations")
    brief: Optional[bool] = Field(False, description="Return only concise answer")


class QueryResponse(BaseModel):
    """Response model for DR query"""

    query: str
    concise_answer: str
    confidence_score: float
    total_iterations: int
    processing_time: float
    final_report: Optional[str] = None
    iterations: Optional[List[Dict[str, Any]]] = None


class HealthResponse(BaseModel):
    """Health check response"""

    status: str
    elasticsearch_connected: bool
    llm_configured: bool
    config: Dict[str, Any]


class SearchRequest(BaseModel):
    """Request model for direct search"""

    query: str
    index: str = Field(
        "docs", description="Index to search: docs, tickets, or knowledgebase"
    )
    max_results: int = Field(10, description="Maximum results to return")


# ============================================================================
# API Endpoints
# ============================================================================


@app.get("/")
async def root():
    """Root endpoint"""
    return {
        "service": "HPC Deep Research API",
        "version": "1.0.0",
        "endpoints": {
            "health": "/health",
            "query": "/query",
            "query_stream": "/query/stream",
            "search": "/search",
        },
    }


@app.get("/health", response_model=HealthResponse)
async def health_check():
    """
    Health check endpoint
    Tests Elasticsearch connection and LLM configuration
    """
    # Test Elasticsearch connection
    es_connected = False
    try:
        es_connected = search_service.test_connection()
    except Exception as e:
        print(f"Elasticsearch connection failed: {e}")

    # Check LLM configuration
    llm_configured = bool(config.llm_base_url and config.llm_model)

    return HealthResponse(
        status="healthy" if (es_connected and llm_configured) else "degraded",
        elasticsearch_connected=es_connected,
        llm_configured=llm_configured,
        config={
            "llm_model": config.llm_model,
            "llm_base_url": config.llm_base_url,
            "elastic_url": config.elastic_url,
            "max_iterations": config.max_iterations,
            "indices": {
                "docs": config.docs_index,
                "tickets": config.tickets_index,
            },
        },
    )


@app.post("/query", response_model=QueryResponse)
async def process_query(request: QueryRequest):
    """
    Process an HPC support query through the DR pipeline
    Returns comprehensive research results
    """
    try:
        # Override config if requested
        if request.max_iterations:
            config.max_iterations = request.max_iterations

        # Process query
        result = await dr_workflow.process_query(request.query)

        # Serialize iterations to dict
        iterations_dict = None
        if not request.brief:
            iterations_dict = [
                {
                    "iteration_number": it.iteration_number,
                    "research_answers": [
                        {
                            "research_type": ans.research_type.value,
                            "answer": ans.answer,
                            "confidence": ans.confidence,
                            "sources": ans.sources[:5],  # Limit sources
                        }
                        for ans in it.research_answers
                    ],
                    "assumptions": [
                        {
                            "assumption": assump.assumption,
                            "is_valid": assump.is_valid,
                            "evidence": assump.evidence,
                            "confidence": assump.confidence,
                        }
                        for assump in it.user_assumptions
                    ],
                }
                for it in result.iterations
            ]

        return QueryResponse(
            query=result.user_query,
            concise_answer=result.concise_answer,
            confidence_score=result.confidence_score,
            total_iterations=result.total_iterations,
            processing_time=result.processing_time,
            final_report=result.final_report if not request.brief else None,
            iterations=iterations_dict,
        )

    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Query processing failed: {str(e)}"
        )


@app.post("/query/stream")
async def process_query_stream(request: QueryRequest):
    """
    Process query with streaming response
    Returns incremental updates as the research progresses
    """

    async def event_generator():
        """Generate SSE events for query processing"""
        try:
            # Send initial event
            yield f"data: {json.dumps({'type': 'started', 'query': request.query})}\n\n"

            # Process query
            result = await dr_workflow.process_query(request.query)

            # Send intermediate updates (if we had them)
            for i, iteration in enumerate(result.iterations, 1):
                yield f"data: {json.dumps({'type': 'iteration', 'number': i, 'total': len(result.iterations)})}\n\n"
                await asyncio.sleep(0.1)  # Small delay for streaming effect

            # Send final result
            final_data = {
                "type": "completed",
                "answer": result.concise_answer,
                "confidence": result.confidence_score,
                "iterations": result.total_iterations,
                "processing_time": result.processing_time,
            }
            yield f"data: {json.dumps(final_data)}\n\n"

        except Exception as e:
            error_data = {"type": "error", "message": str(e)}
            yield f"data: {json.dumps(error_data)}\n\n"

    return StreamingResponse(
        event_generator(),
        media_type="text/event-stream",
        headers={"Cache-Control": "no-cache", "X-Accel-Buffering": "no"},
    )


@app.post("/search")
async def search(request: SearchRequest):
    """
    Direct search endpoint
    Searches Elasticsearch indices without DR processing
    """
    try:
        # Map index name to search_type
        search_type_map = {
            "docs": "docs",
            "tickets": "tickets",
            "knowledgebase": "tickets",  # Map knowledgebase to tickets for now
        }
        search_type = search_type_map.get(request.index, "docs")

        # Create HPCSearchRequest
        hpc_search_request = HPCSearchRequest(
            query=request.query,
            search_type=search_type,
            max_results=request.max_results
        )

        # Perform search
        search_response = await search_service.search(hpc_search_request)

        # Check for errors
        if search_response.error:
            raise HTTPException(
                status_code=500,
                detail=f"Search failed: {search_response.error}"
            )

        return {
            "query": search_response.query,
            "index": request.index,
            "results": [
                {
                    "title": r.title,
                    "content": r.content[:500],  # Truncate content
                    "score": r.score,
                    "source": r.source_type,  # Fixed: source_type, not source
                }
                for r in search_response.results
            ],
            "total": search_response.total_found,
            "search_time": search_response.search_time
        }

    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Search failed: {str(e)}")


@app.on_event("startup")
async def startup_event():
    """Initialize services on startup"""
    print("Starting HPC DR API...")
    print(f"   LLM Model: {config.llm_model}")
    print(f"   LLM URL: {config.llm_base_url}")
    print(f"   Elasticsearch: {config.elastic_url}")

    # Test Elasticsearch connection
    try:
        if search_service.test_connection():
            print("Elasticsearch connection verified")
        else:
            print("[!] Warning: Elasticsearch connection test failed")
            print("   API will start but searches may fail")
    except Exception as e:
        print(f"[!] Warning: Elasticsearch connection error: {e}")
        print("   API will start but searches may fail")


@app.on_event("shutdown")
async def shutdown_event():
    """Cleanup on shutdown"""
    print("Shutting down HPC DR API...")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
