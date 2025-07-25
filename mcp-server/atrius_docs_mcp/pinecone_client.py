"""Pinecone client wrapper for Atrius documentation search."""

import logging
from typing import Any, Dict, List, Optional

from pinecone import Pinecone, ServerlessSpec
from pydantic import BaseModel

from .config import Settings

logger = logging.getLogger(__name__)


class SearchResult(BaseModel):
    """Search result model."""

    id: str
    score: float
    title: str
    content: str
    collection: str
    file_path: str
    topics: List[str]
    updated: Optional[str] = None


class DocumentMetadata(BaseModel):
    """Document metadata model."""

    id: str
    title: str
    collection: str
    file_path: str
    topics: List[str]
    updated: Optional[str] = None


class AtriusPineconeClient:
    """Pinecone client for Atrius documentation search."""

    def __init__(self, settings: Settings):
        """Initialize the Pinecone client."""
        self.settings = settings
        self.pc = Pinecone(api_key=settings.pinecone_api_key)
        self.index = None
        self._connect_to_index()

    def _connect_to_index(self) -> None:
        """Connect to the Pinecone index."""
        try:
            # Get index description to get the host
            index_desc = self.pc.describe_index(self.settings.pinecone_index_name)
            self.index = self.pc.Index(host=index_desc.host)
            logger.info(f"Connected to Pinecone index: {self.settings.pinecone_index_name}")
        except Exception as e:
            logger.error(f"Failed to connect to Pinecone index: {e}")
            raise

    def search_documents(
        self,
        query: str,
        top_k: int = 5,
        collection_filter: Optional[str] = None,
        include_metadata: bool = True,
    ) -> List[SearchResult]:
        """
        Search documents using semantic similarity.

        Args:
            query: Search query text
            top_k: Number of results to return
            collection_filter: Optional collection to filter by
            include_metadata: Whether to include metadata in results

        Returns:
            List of search results
        """
        try:
            # Build filter if collection specified
            filter_dict = {}
            if collection_filter:
                filter_dict["collection"] = {"$eq": collection_filter}

            # Perform search using integrated inference
            response = self.index.search_records(
                namespace=self.settings.pinecone_namespace,
                query={
                    "inputs": {"text": query},
                    "top_k": min(top_k, self.settings.max_top_k),
                    "filter": filter_dict if filter_dict else None,
                },
            )

            # Convert to SearchResult objects
            results = []
            for match in response.get("matches", []):
                try:
                    metadata = match.get("metadata", {})
                    result = SearchResult(
                        id=match["id"],
                        score=match["score"],
                        title=metadata.get("title", "Untitled"),
                        content=metadata.get("content", ""),
                        collection=metadata.get("collection", "unknown"),
                        file_path=metadata.get("file_path", ""),
                        topics=metadata.get("topics", []),
                        updated=metadata.get("updated"),
                    )
                    results.append(result)
                except Exception as e:
                    logger.warning(f"Failed to parse search result: {e}")
                    continue

            logger.info(f"Search completed: {len(results)} results for query '{query}'")
            return results

        except Exception as e:
            logger.error(f"Search failed: {e}")
            raise

    def get_document_by_id(self, doc_id: str) -> Optional[SearchResult]:
        """
        Get a specific document by its ID.

        Args:
            doc_id: Document ID to retrieve

        Returns:
            SearchResult if found, None otherwise
        """
        try:
            response = self.index.fetch(ids=[doc_id], namespace=self.settings.pinecone_namespace)

            if doc_id in response.get("vectors", {}):
                vector_data = response["vectors"][doc_id]
                metadata = vector_data.get("metadata", {})

                return SearchResult(
                    id=doc_id,
                    score=1.0,  # Perfect match for direct fetch
                    title=metadata.get("title", "Untitled"),
                    content=metadata.get("content", ""),
                    collection=metadata.get("collection", "unknown"),
                    file_path=metadata.get("file_path", ""),
                    topics=metadata.get("topics", []),
                    updated=metadata.get("updated"),
                )

            return None

        except Exception as e:
            logger.error(f"Failed to fetch document {doc_id}: {e}")
            return None

    def list_collections(self) -> List[str]:
        """
        Get list of available collections.

        Returns:
            List of collection names
        """
        try:
            # Get index stats to understand the namespace
            stats = self.index.describe_index_stats()

            # Since we don't have a direct way to list all unique collections,
            # we'll return the known collections from the documentation
            known_collections = [
                "welcome",
                "buildings",
                "advanced",
                "points-and-bills",
                "apps",
                "dashboards",
                "settings",
                "integrations",
            ]

            return known_collections

        except Exception as e:
            logger.error(f"Failed to list collections: {e}")
            return []

    def get_index_stats(self) -> Dict[str, Any]:
        """
        Get index statistics.

        Returns:
            Dictionary with index stats
        """
        try:
            return self.index.describe_index_stats()
        except Exception as e:
            logger.error(f"Failed to get index stats: {e}")
            return {}
