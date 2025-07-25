# Atrius Documentation MCP Server

A Model Context Protocol (MCP) server that provides semantic search capabilities over vectorized Atrius documentation using Pinecone. This server enables LLMs to intelligently search and retrieve information from the Atrius Learning & Support Hub.

## Overview

This MCP server connects to your existing Pinecone index containing vectorized Atrius documentation and provides search capabilities through the MCP protocol. It includes:

- **Semantic Search**: Natural language queries across all documentation
- **Collection Filtering**: Search within specific documentation collections  
- **Document Retrieval**: Get full content of specific documents
- **Metadata Support**: Rich metadata including topics, collections, and update dates
- **Docker Support**: Containerized for easy deployment

## Features

### Available MCP Tools

1. **`search_docs`** - Semantic search across all documentation
2. **`get_document`** - Retrieve specific document by ID
3. **`list_collections`** - Browse available documentation collections
4. **`search_by_collection`** - Search within specific collections
5. **`get_index_stats`** - Get Pinecone index statistics

### Documentation Collections

- **welcome** - Getting started guides and basic support
- **buildings** - Building management, spaces, and tenants
- **advanced** - Advanced features like baselines and forecasting
- **points-and-bills** - Data points and billing management
- **apps** - Application functionality and data management
- **dashboards** - Dashboard creation and customization
- **settings** - System settings and configuration
- **integrations** - Third-party integrations and APIs

## Quick Start

### Prerequisites

- Docker and Docker Compose
- Pinecone API key
- Access to the `atrius-docs` Pinecone index

### Option 1: Using Docker Compose (Recommended)

1. **Clone and navigate to the MCP server directory:**
   ```bash
   cd mcp-server
   ```

2. **Create environment file:**
   ```bash
   cp env.example .env
   # Edit .env with your Pinecone API key
   ```

3. **Build and run with Docker Compose:**
   ```bash
   docker-compose up --build
   ```

The server will be available at `http://localhost:3001`

### Option 2: Using Docker directly

1. **Build the Docker image:**
   ```bash
   docker build -t atrius-docs-mcp .
   ```

2. **Run the container:**
   ```bash
   docker run -p 3001:3001 \
     -e PINECONE_API_KEY=your_api_key_here \
     -e PINECONE_INDEX_NAME=atrius-docs \
     -e PINECONE_NAMESPACE=docs \
     atrius-docs-mcp
   ```

### Option 3: Local Development

1. **Install Poetry:**
   ```bash
   curl -sSL https://install.python-poetry.org | python3 -
   ```

2. **Install dependencies:**
   ```bash
   poetry install
   ```

3. **Set environment variables:**
   ```bash
   export PINECONE_API_KEY=your_api_key_here
   export PINECONE_INDEX_NAME=atrius-docs
   export PINECONE_NAMESPACE=docs
   ```

4. **Run the server:**
   ```bash
   poetry run python -m atrius_docs_mcp.server
   ```

## Configuration

### Environment Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `PINECONE_API_KEY` | *required* | Your Pinecone API key |
| `PINECONE_INDEX_NAME` | `atrius-docs` | Name of the Pinecone index |
| `PINECONE_NAMESPACE` | `docs` | Namespace within the index |
| `SERVER_HOST` | `0.0.0.0` | Server bind address |
| `SERVER_PORT` | `3001` | Server port |
| `DEFAULT_TOP_K` | `5` | Default number of search results |
| `MAX_TOP_K` | `20` | Maximum number of search results |
| `ENABLE_RERANKING` | `true` | Enable result reranking |

## Usage Examples

### Testing with MCP Inspector

The MCP Inspector is a great tool for testing the server:

```bash
# Test with Docker
npx @modelcontextprotocol/inspector -- docker run -i --rm \
  -e PINECONE_API_KEY=your_key_here \
  -e PINECONE_INDEX_NAME=atrius-docs \
  -e PINECONE_NAMESPACE=docs \
  atrius-docs-mcp

# Test locally
npx @modelcontextprotocol/inspector -- poetry run python -m atrius_docs_mcp.server
```

### Connecting to Claude Desktop

Add to your Claude Desktop MCP configuration:

```json
{
  "mcpServers": {
    "atrius-docs": {
      "command": "docker",
      "args": [
        "run", "-i", "--rm",
        "-e", "PINECONE_API_KEY",
        "-e", "PINECONE_INDEX_NAME", 
        "-e", "PINECONE_NAMESPACE",
        "atrius-docs-mcp"
      ],
      "env": {
        "PINECONE_API_KEY": "your_pinecone_api_key_here",
        "PINECONE_INDEX_NAME": "atrius-docs",
        "PINECONE_NAMESPACE": "docs"
      }
    }
  }
}
```

### Example Queries

Once connected, you can ask questions like:

- "How do I add a new building to Atrius?"
- "What are degree days and how are they calculated?"
- "Show me documentation about setting up energy consumption alerts"
- "How do I manage building tenants?"
- "What integrations are available in Atrius?"

## API Reference

### search_docs

Search across all documentation using semantic similarity.

**Parameters:**
- `query` (string, required): Natural language search query
- `top_k` (integer, optional): Number of results (1-20, default: 5)
- `collection` (string, optional): Filter by collection name

**Returns:**
- `query`: Original search query
- `total_results`: Number of results found
- `results`: Array of matching documents with metadata
- `collection_filter`: Applied collection filter
- `message`: Status message

### get_document

Retrieve a specific document by its ID.

**Parameters:**
- `doc_id` (string, required): Document ID from search results

**Returns:**
- `id`: Document ID
- `title`: Document title
- `collection`: Collection name
- `full_content`: Complete document content
- `topics`: Related topics
- `file_path`: Original file path
- `last_updated`: Last update timestamp

### list_collections

Get all available documentation collections.

**Returns:**
- `total_collections`: Number of collections
- `collections`: Array of collection objects with names and descriptions

### search_by_collection

Search within a specific documentation collection.

**Parameters:**
- `collection` (string, required): Collection name to search in
- `query` (string, required): Natural language search query  
- `top_k` (integer, optional): Number of results (1-20, default: 5)

**Returns:**
Similar to `search_docs` but filtered to the specified collection.

### get_index_stats

Get statistics about the Pinecone index.

**Returns:**
- `index_name`: Name of the Pinecone index
- `namespace`: Namespace being used
- `stats`: Detailed index statistics from Pinecone

## Architecture

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│                 │    │                 │    │                 │
│   LLM Client    │───▶│  MCP Server     │───▶│   Pinecone      │
│  (Claude, etc.) │    │  (FastMCP)      │    │   Index         │
│                 │    │                 │    │ (atrius-docs)   │
└─────────────────┘    └─────────────────┘    └─────────────────┘
```

### Components

- **FastMCP**: Handles MCP protocol communication
- **Pinecone Client**: Manages vector database operations
- **Pydantic Models**: Data validation and serialization
- **Docker**: Containerization for deployment

## Development

### Project Structure

```
mcp-server/
├── atrius_docs_mcp/
│   ├── __init__.py
│   ├── config.py          # Configuration settings
│   ├── pinecone_client.py # Pinecone integration
│   └── server.py          # Main MCP server
├── Dockerfile
├── docker-compose.yml
├── pyproject.toml
├── env.example
└── README.md
```

### Running Tests

```bash
# Install test dependencies
poetry install --with dev

# Run tests (when implemented)
poetry run pytest

# Code formatting
poetry run black atrius_docs_mcp/
poetry run ruff check atrius_docs_mcp/
```

### Building for Production

```bash
# Build optimized Docker image
docker build -t atrius-docs-mcp:latest .

# Tag for registry
docker tag atrius-docs-mcp:latest your-registry/atrius-docs-mcp:latest

# Push to registry
docker push your-registry/atrius-docs-mcp:latest
```

## Troubleshooting

### Common Issues

1. **Connection Error to Pinecone**
   - Verify PINECONE_API_KEY is correct
   - Check index name and namespace
   - Ensure index exists and is active

2. **No Search Results**
   - Verify the index contains data in the specified namespace
   - Check if collection filters are too restrictive
   - Try broader search queries

3. **Docker Build Failures**
   - Ensure Docker has sufficient memory (>2GB recommended)
   - Check Poetry lock file is up to date
   - Verify network access for dependency downloads

4. **Performance Issues**
   - Consider reducing `top_k` values for faster responses
   - Check Pinecone index location vs server location
   - Monitor container resource usage

### Health Check

The server includes a health check endpoint:

```bash
curl http://localhost:3001/health
```

### Logs

View server logs:

```bash
# Docker Compose
docker-compose logs -f atrius-docs-mcp

# Docker
docker logs -f atrius-docs-mcp-server
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Update documentation
6. Submit a pull request

## License

[Add your license information here]

## Support

For issues related to:
- **MCP Server**: Check logs and environment configuration
- **Pinecone Integration**: Verify API key and index settings  
- **Docker Deployment**: Check container logs and resource limits
- **Atrius Documentation**: Refer to the source documentation

## Changelog

### v0.1.0 (Initial Release)
- FastMCP server implementation
- Pinecone integration for vector search
- Docker containerization
- Five core MCP tools for documentation search
- Support for all Atrius documentation collections 