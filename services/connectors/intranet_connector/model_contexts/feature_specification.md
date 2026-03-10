# Intranet Connector Feature Specification

This document details the planned behavior and features of the Intranet Connector service, aligning with the overall project goals for the Knowledge Management System (KMS) as outlined in `GEMINI.md`.

## 1. Overview

The Intranet Connector is a critical component responsible for integrating internal company intranet content into the tierzero KMS. It will listen for crawl requests, fetch content and associated permissions from a specified intranet API, and publish this raw data to a message bus for further ingestion and processing.

## 2. Core Features & Behavior

### 2.1. Job Listening and Processing

*   **Subscription:** The connector will subscribe to the `crawl.requested` topic on the RabbitMQ message bus.
*   **Filtering:** It will specifically process messages where the `source_type` field is `INTRANET`.
*   **Message Acknowledgment:** Upon successful receipt and parsing of a job message, the message will be acknowledged.
*   **Job Parsing:** The service will extract the Intranet API base URL and any necessary authentication credentials from the received job message.

### 2.2. Content Crawling and Extraction ✅ **IMPLEMENTED**

*   **Crawling Mechanism:** The connector leverages `Crawl4AI` with advanced configuration for efficient web crawling.
*   **Crawling Strategies:** Supports multiple strategies:
    *   **BFS (Breadth-First Search)** - Default strategy
    *   **DFS (Depth-First Search)** - For deep content exploration
    *   **Best-First** - Keyword relevance-based prioritization
*   **Content Discovery:** `Crawl4AI` handles the discovery of linked pages with configurable depth and page limits.
*   **Advanced Content Processing:**
    *   **Markdown Generation:** Uses `DefaultMarkdownGenerator` for clean content extraction
    *   **Content Filtering:** Automatically excludes unwanted elements:
        *   Forms, headers, footers, navigation elements
        *   External links (configurable)
        *   Social media links (configurable)
    *   **Domain Filtering:** Restricts crawling to specified domains
*   **Data Extraction:** For each discovered page, the connector extracts:
    *   Clean markdown content (filtered and processed)
    *   Page title from metadata
    *   Original URL
    *   HTTP status codes and redirect information
    *   Available metadata (author, last updated date)
*   **Configuration-Driven:** All crawling behavior is controlled via `CrawlerSettings` configuration.

### 2.3. Permissions Fetching ⚠️ **PLACEHOLDER IMPLEMENTATION**

*   **Current Status:** Basic permission structure is implemented but returns empty arrays.
*   **Future Implementation:** Will involve direct API calls to the Intranet's authentication/authorization system.
*   **Data Structure:** Permissions are included in the `RawArticle` structure as a list of permission strings.
*   **Next Steps:** Implement actual permission fetching logic based on specific intranet requirements.

### 2.4. Data Publishing ✅ **IMPLEMENTED**

*   **Current Status:** The crawler generates validated `RawArticle` objects using Pydantic models.
*   **Future Integration:** Will publish to the `content.raw.received` topic once message queue integration is added.
*   **Message Structure:**
    ```json
    {
      "source_document_id": "https://intranet.example.com/docs/page-123",
      "content": "The full text of the page...",
      "source": {
        "uri": "https://intranet.example.com/docs/page-123",
        "module": "Intranet Connector",
        "retrieved_at": "2025-07-22T10:00:00Z"
      },
      "author": {
        "name": "hr@example.com"
      },
      "tags": ["onboarding", "guide"],
      "permissions": ["group:all-employees", "user:john.doe"],
      "metadata": {
        "title": "Onboarding Guide",
        "last_updated": "YYYY-MM-DDTHH:MM:SSZ"
      }
    }
    ```
    *   The structure is defined by the `RawArticle` Pydantic model.

### 2.5. Error Handling and Resilience

*   **Network Errors:** The service will be resilient to network issues and API rate limits from the Intranet.
*   **Retry Mechanism:** An exponential backoff retry mechanism will be implemented for failed HTTP requests.
*   **Dead-Letter Queue:** If a message cannot be processed after a configured number of retries (a "poison pill"), it will be moved to a dead-letter queue for manual inspection and debugging.

### 2.6. Health Monitoring

*   **Health Endpoint:** The service will expose a `/health` endpoint (via FastAPI) for external monitoring systems to check its operational status.

## 3. Technology Stack

*   **Language:** Python
*   **Web Framework:** FastAPI (for health checks and potential administrative endpoints)
*   **Messaging:** `pika` library for RabbitMQ communication
*   **Crawling:** `Crawl4AI` for efficient web crawling and content extraction
*   **HTTP Client:** `httpx` (for direct API calls if `Crawl4AI` cannot handle specific content or permissions fetching)
*   **Configuration:** `pydantic` for environment variable management and settings validation

## 4. Configuration ✅ **IMPLEMENTED**

The connector uses `CrawlerSettings` (Pydantic-based configuration) with the following options:

### 4.1. Crawler Behavior
*   `CRAWLER_STRATEGY`: Crawling strategy (`"bfs"`, `"dfs"`, `"best_first"`) - Default: `"bfs"`
*   `CRAWLER_MAX_DEPTH`: Maximum crawl depth - Default: `4`
*   `CRAWLER_MAX_PAGES`: Maximum pages to crawl - Default: `100`
*   `CRAWLER_USE_PLAYWRIGHT`: Enable browser-based crawling - Default: `False`

### 4.2. Content Filtering
*   `CRAWLER_EXCLUDED_TAGS`: HTML tags to exclude - Default: `['form', 'header', 'footer', 'nav']`
*   `CRAWLER_EXCLUDE_EXTERNAL_LINKS`: Filter external links - Default: `True`
*   `CRAWLER_EXCLUDE_SOCIAL_MEDIA_LINKS`: Filter social media links - Default: `True`

### 4.3. Authentication
*   `CRAWLER_AUTH_TOKEN`: Optional authentication token for protected content

### 4.4. Future Message Queue Configuration
*   `RABBITMQ_HOST`: Hostname or IP address of the RabbitMQ server
*   `RABBITMQ_USER`: Username for RabbitMQ authentication
*   `RABBITMQ_PASS`: Password for RabbitMQ authentication
*   `LOG_LEVEL`: Logging level (e.g., `INFO`, `DEBUG`, `WARNING`, `ERROR`)

## 5. Current Implementation Status

### 5.1. Completed Features ✅
*   **Advanced Content Crawling**: Multi-strategy crawling with content filtering
*   **Markdown Generation**: Clean content extraction with unwanted element removal
*   **Structured Data Models**: Pydantic-based `RawArticle` validation
*   **Configurable Behavior**: Comprehensive settings via `CrawlerSettings`
*   **Domain Filtering**: Restrict crawling to specified domains
*   **Link Filtering**: Exclude external and social media links

### 5.2. In Progress ⚠️
*   **Permissions Integration**: Basic structure implemented, actual fetching pending
*   **Message Queue Integration**: Data models ready, queue publishing pending

### 5.3. Not Yet Implemented ❌
*   **Job Listening**: Subscription to `crawl.requested` topic
*   **Health Monitoring**: `/health` endpoint via FastAPI
*   **Error Handling**: Retry mechanisms and dead-letter queue handling

---

## 6. Future Considerations (Beyond Current Implementation)

*   **Incremental Crawling:** Implement logic for detecting changes in intranet content and only re-crawling/re-ingesting updated pages.
*   **Full API Integration:** Develop more robust integration with complex intranet APIs that do not expose content via standard web pages.
*   **Advanced Permission Mapping:** Map intranet-specific permission schemes to a standardized tierzero permission model.
*   **Scalability:** Consider distributed crawling strategies for very large intranets.
