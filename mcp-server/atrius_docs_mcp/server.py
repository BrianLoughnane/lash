"""Main MCP server implementation for Atrius documentation search."""

import logging
from typing import Any, Dict, List, Optional

from fastmcp import FastMCP
from pydantic import BaseModel, Field

from .config import get_settings
from .pinecone_client import AtriusPineconeClient, SearchResult

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize settings and clients
settings = get_settings()
pinecone_client = AtriusPineconeClient(settings)

# Create FastMCP server
server = FastMCP("Atrius Documentation Search")


class SearchDocsParams(BaseModel):
    """Parameters for searching documentation."""

    query: str = Field(..., description="Search query in natural language")
    top_k: int = Field(5, description="Number of results to return (max 20)", ge=1, le=20)
    collection: Optional[str] = Field(None, description="Filter by collection (optional)")


class GetDocumentParams(BaseModel):
    """Parameters for getting a specific document."""

    doc_id: str = Field(..., description="Document ID to retrieve")


class SearchByCollectionParams(BaseModel):
    """Parameters for searching within a specific collection."""

    collection: str = Field(..., description="Collection name to search in")
    query: str = Field(..., description="Search query in natural language")
    top_k: int = Field(5, description="Number of results to return (max 20)", ge=1, le=20)


@server.tool()
def search_docs(params: SearchDocsParams) -> Dict[str, Any]:
    """
    Search the Atrius documentation using semantic similarity.

    This tool performs semantic search across all vectorized Atrius documentation
    to find relevant articles, guides, and technical information. Use natural
    language queries to find information about Atrius features, configuration,
    troubleshooting, and best practices.

    Example queries:
    - "How do I add a new building?"
    - "What are degree days and how are they calculated?"
    - "Setting up alerts for energy consumption"
    - "Building tenant management"
    """
    try:
        logger.info(
            f"Searching docs: '{params.query}' (top_k={params.top_k}, collection={params.collection})"
        )

        results = pinecone_client.search_documents(
            query=params.query, top_k=params.top_k, collection_filter=params.collection
        )

        # Format results for LLM consumption
        formatted_results = []
        for result in results:
            formatted_results.append(
                {
                    "id": result.id,
                    "title": result.title,
                    "collection": result.collection,
                    "relevance_score": round(result.score, 3),
                    "content_preview": result.content[:500] + "..."
                    if len(result.content) > 500
                    else result.content,
                    "topics": result.topics,
                    "file_path": result.file_path,
                    "last_updated": result.updated,
                }
            )

        return {
            "query": params.query,
            "total_results": len(formatted_results),
            "results": formatted_results,
            "collection_filter": params.collection,
            "message": f"Found {len(formatted_results)} relevant documents",
        }

    except Exception as e:
        logger.error(f"Search failed: {e}")
        return {"error": str(e), "message": "Search failed due to an internal error"}


@server.tool()
def get_document(params: GetDocumentParams) -> Dict[str, Any]:
    """
    Retrieve a specific document by its ID.

    Use this tool when you need the full content of a specific document
    that was found in search results. The document ID can be obtained
    from search_docs results.
    """
    try:
        logger.info(f"Fetching document: {params.doc_id}")

        result = pinecone_client.get_document_by_id(params.doc_id)

        if result:
            return {
                "id": result.id,
                "title": result.title,
                "collection": result.collection,
                "full_content": result.content,
                "topics": result.topics,
                "file_path": result.file_path,
                "last_updated": result.updated,
                "message": "Document retrieved successfully",
            }
        else:
            return {
                "error": "Document not found",
                "doc_id": params.doc_id,
                "message": f"No document found with ID: {params.doc_id}",
            }

    except Exception as e:
        logger.error(f"Failed to fetch document {params.doc_id}: {e}")
        return {
            "error": str(e),
            "doc_id": params.doc_id,
            "message": "Failed to retrieve document due to an internal error",
        }


@server.tool()
def list_collections() -> Dict[str, Any]:
    """
    List all available documentation collections.

    Returns the available collections in the Atrius documentation,
    which can be used to filter search results or browse by category.
    """
    try:
        logger.info("Listing available collections")

        collections = pinecone_client.list_collections()

        # Add descriptions for known collections
        collection_info = {
            "welcome": "Getting started guides and basic support information",
            "buildings": "Building management, spaces, tenants, and profiles",
            "advanced": "Advanced features like baselines, forecasts, and normalization",
            "points-and-bills": "Data points and billing management",
            "apps": "Application functionality and data management tools",
            "dashboards": "Dashboard creation and customization",
            "settings": "System settings and configuration options",
            "integrations": "Third-party integrations and API documentation",
        }

        detailed_collections = []
        for collection in collections:
            detailed_collections.append(
                {
                    "name": collection,
                    "description": collection_info.get(collection, "Documentation collection"),
                }
            )

        return {
            "total_collections": len(detailed_collections),
            "collections": detailed_collections,
            "message": f"Found {len(detailed_collections)} documentation collections",
        }

    except Exception as e:
        logger.error(f"Failed to list collections: {e}")
        return {"error": str(e), "message": "Failed to list collections due to an internal error"}


@server.tool()
def search_by_collection(params: SearchByCollectionParams) -> Dict[str, Any]:
    """
    Search within a specific documentation collection.

    Use this tool when you want to focus your search on a particular
    area of the documentation, such as only looking in "buildings"
    or "advanced" collections.
    """
    try:
        logger.info(f"Searching in collection '{params.collection}': '{params.query}'")

        results = pinecone_client.search_documents(
            query=params.query, top_k=params.top_k, collection_filter=params.collection
        )

        if not results:
            return {
                "query": params.query,
                "collection": params.collection,
                "total_results": 0,
                "results": [],
                "message": f"No results found in collection '{params.collection}' for query '{params.query}'",
            }

        # Format results
        formatted_results = []
        for result in results:
            formatted_results.append(
                {
                    "id": result.id,
                    "title": result.title,
                    "relevance_score": round(result.score, 3),
                    "content_preview": result.content[:500] + "..."
                    if len(result.content) > 500
                    else result.content,
                    "topics": result.topics,
                    "file_path": result.file_path,
                    "last_updated": result.updated,
                }
            )

        return {
            "query": params.query,
            "collection": params.collection,
            "total_results": len(formatted_results),
            "results": formatted_results,
            "message": f"Found {len(formatted_results)} relevant documents in '{params.collection}' collection",
        }

    except Exception as e:
        logger.error(f"Collection search failed: {e}")
        return {
            "error": str(e),
            "message": f"Search in collection '{params.collection}' failed due to an internal error",
        }


@server.tool()
def get_index_stats() -> Dict[str, Any]:
    """
    Get statistics about the documentation index.

    Returns information about the Pinecone index including total vectors,
    namespaces, and other metrics useful for understanding the scope
    of available documentation.
    """
    try:
        logger.info("Getting index statistics")

        stats = pinecone_client.get_index_stats()

        return {
            "index_name": settings.pinecone_index_name,
            "namespace": settings.pinecone_namespace,
            "stats": stats,
            "message": "Index statistics retrieved successfully",
        }

    except Exception as e:
        logger.error(f"Failed to get index stats: {e}")
        return {"error": str(e), "message": "Failed to retrieve index statistics"}


def main():
    """Run the MCP server."""
    import uvicorn

    logger.info("Starting Atrius Documentation MCP Server")
    logger.info(f"Server will run on {settings.server_host}:{settings.server_port}")
    logger.info(f"Connected to Pinecone index: {settings.pinecone_index_name}")

    # Run the server
    uvicorn.run(
        "atrius_docs_mcp.server:server.app",
        host=settings.server_host,
        port=settings.server_port,
        log_level="info",
    )


if __name__ == "__main__":
    main()
