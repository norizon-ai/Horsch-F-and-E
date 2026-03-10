# High-Level Data Flow

This document describes the data flow from content crawling to final storage in the RAG system.

## Overview

The data flow consists of four main stages that transform raw crawled content into searchable knowledge articles:

```
Intranet Connector → Message Queue → Ingestion Worker → Elasticsearch
```

---

## 1. Intranet Connector

**Purpose**: Content Discovery and Extraction

The `IntranetCrawler` performs the following operations:

- **Scans** intranet sources (web pages, documents)
- **Extracts** raw content using advanced markdown generation
- **Filters** unwanted elements (forms, headers, footers, navigation)
- **Structures** data into `RawArticle` objects with proper validation
- **Publishes** messages to the message queue

### Output: `RawArticle` Message

```json
{
  "source_document_id": "https://example.com/page",
  "content": "# Page Title\n\nClean markdown content...",
  "source": {
    "uri": "https://example.com/page",
    "module": "Intranet Connector",
    "retrieved_at": "2024-01-01T12:00:00Z"
  },
  "author": {
    "name": "John Doe"
  },
  "tags": ["tag1", "tag2"],
  "permissions": ["group:employees"],
  "metadata": {
    "title": "Page Title",
    "status_code": 200
  }
}
```

---

## 2. Message Queue

**Technology**: RabbitMQ or Kafka  
**Queue Name**: `articles.raw`

**Purpose**: Decoupling and Reliability

- **Receives** `RawArticle` messages from the Intranet Connector
- **Buffers** messages to handle processing speed differences
- **Ensures** message durability and delivery guarantees
- **Enables** horizontal scaling of workers

### Benefits

- ✅ **Resilience**: Crawler can continue if ingestion is slow
- ✅ **Scalability**: Multiple workers can process messages
- ✅ **Reliability**: Messages persist until successfully processed

---

## 3. Ingestion Worker

**Purpose**: Content Processing and Enrichment

The ingestion worker subscribes to the `articles.raw` queue and performs:

### 3.1. Data Transformation
- **Assigns** new unique `document_id` (UUID)
- **Validates** and cleans incoming data
- **Maps** author names to system user IDs (if available)

### 3.2. Vector Embedding Generation
- **Processes** the markdown content through embedding models
- **Generates** `content_vector` using sentence transformers
- **Optimizes** embeddings for semantic search

### 3.3. Access Control Processing
- **Applies** business logic for permission validation
- **Transforms** permission strings into system-compatible format
- **Ensures** proper access control metadata

### 3.4. Final Object Construction
- **Builds** the complete `KnowledgeArticle` object
- **Validates** all required fields
- **Prepares** for indexing

### Output: `KnowledgeArticle` Object

```json
{
  "document_id": "uuid-123-456",
  "source_document_id": "https://example.com/page",
  "content": "# Page Title\n\nClean markdown content...",
  "content_vector": [0.1, 0.2, 0.3, ...],
  "title": "Page Title",
  "author_id": "user-456",
  "permissions": ["group:employees"],
  "created_at": "2024-01-01T12:00:00Z",
  "metadata": {
    "source_uri": "https://example.com/page",
    "module": "Intranet Connector"
  }
}
```

---

## 4. Elasticsearch

**Index Name**: `knowledge_articles`

**Purpose**: Final Storage and Search

- **Indexes** the complete `KnowledgeArticle` document
- **Enables** full-text search capabilities
- **Supports** vector similarity search
- **Provides** fast retrieval for RAG queries

### Search Capabilities

- 🔍 **Full-text search** on content and metadata
- 🎯 **Semantic search** using vector embeddings  
- 🔒 **Permission-filtered** results
- ⚡ **Fast retrieval** for real-time applications

---

## Data Flow Summary

| Stage | Input | Processing | Output |
|-------|-------|------------|--------|
| **Intranet Connector** | Web pages | Content extraction & filtering | `RawArticle` |
| **Message Queue** | `RawArticle` | Buffering & routing | Queued messages |
| **Ingestion Worker** | `RawArticle` | Embedding generation & enrichment | `KnowledgeArticle` |
| **Elasticsearch** | `KnowledgeArticle` | Indexing & storage | Searchable documents |

---

## Error Handling

- **Queue acknowledgment**: Messages are only acknowledged after successful processing
- **Retry logic**: Failed messages are automatically requeued
- **Dead letter queues**: Permanently failed messages are moved for manual inspection
- **Monitoring**: Each stage includes logging and metrics for observability