"""Configuration settings for the Atrius Docs MCP Server."""

import os
from typing import Optional

from pydantic import BaseSettings


class Settings(BaseSettings):
    """Application settings."""

    # Pinecone configuration
    pinecone_api_key: str
    pinecone_index_name: str = "atrius-docs"
    pinecone_namespace: str = "docs"

    # MCP Server configuration
    server_host: str = "0.0.0.0"
    server_port: int = 3001

    # Search configuration
    default_top_k: int = 5
    max_top_k: int = 20
    enable_reranking: bool = True

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = False


def get_settings() -> Settings:
    """Get application settings."""
    return Settings()
