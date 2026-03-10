# File-Based Storage for Crawled Data

This document describes the interim file-based storage solution for processing crawled data while the ingestion worker is being developed.

## Overview

Instead of sending crawled data to RabbitMQ for processing by an incomplete ingestion worker, this solution saves crawled data directly to disk in JSON format. This allows you to:

1. **Start crawling immediately** without waiting for the ingestion worker
2. **Preserve all crawled data** for later processing
3. **Process data offline** using the batch processor
4. **Export data** to various formats (JSONL, CSV)
5. **Resume crawls** with automatic deduplication

## Quick Start

### 1. Configure for File Storage

Edit `src/config.py` or set environment variables:

```python
CRAWLER_STORAGE_MODE="file"  # Use file storage instead of RabbitMQ
CRAWLER_STORAGE_PATH="./crawled_data"  # Where to save data
CRAWLER_BATCH_SIZE=10  # Articles per batch file
```

### 2. Start a Crawl

Using the crawl manager CLI:

```bash
# Basic crawl
python src/crawl_manager.py crawl https://example.com --max-pages 100

# With specific domains
python src/crawl_manager.py crawl https://example.com --domains example.com www.example.com --max-pages 500
```

Or programmatically:

```python
python src/crawler.py  # Uses configuration from config.py
```

### 3. Monitor Progress

Data is saved to timestamped session directories:

```
crawled_data/
├── 20241211_143022/          # Session directory (timestamp)
│   ├── example_com/           # Domain subdirectory
│   │   ├── a3f2b1c4_20241211_143025.json  # Individual articles
│   │   └── b5d8e2a1_20241211_143028.json
│   ├── index.jsonl            # Index of all saved files
│   └── statistics.json        # Session statistics
```

### 4. Process the Data

List available sessions:

```bash
python src/crawl_manager.py list
```

Process and export data:

```bash
# Export to JSONL (for further processing)
python src/batch_processor.py --storage ./crawled_data --export jsonl --output processed_data.jsonl

# Export to CSV (for analysis)
python src/batch_processor.py --storage ./crawled_data --export csv --output processed_data.csv

# Process specific session
python src/batch_processor.py --storage ./crawled_data --session 20241211_143022 --export jsonl --output output.jsonl
```

## Components

### FileStoragePublisher

Saves crawled articles to disk in JSON format:

- **Organized structure**: Sessions → Domains → Articles
- **Deduplication**: Tracks processed URLs to avoid duplicates
- **Batching**: Configurable batch size for efficiency
- **Metadata tracking**: Index file and statistics

### BatchProcessor

Processes stored data offline:

- **Chunking**: Splits documents into chunks for semantic search
- **Embedding generation**: Placeholder for embedding models
- **Export formats**: JSONL, CSV
- **Progress tracking**: Resume from where you left off

### CrawlManager

CLI tool for managing crawl operations:

- **Start crawls**: Simple command to begin crawling
- **List sessions**: View all crawl sessions
- **Process data**: Export and transform crawled data
- **Estimate scope**: Predict crawl time and page count

## Usage Examples

### Example 1: Crawl a Large Site

```bash
# First, estimate the scope
python src/crawl_estimator.py https://large-site.com

# Start the crawl with appropriate limits
python src/crawl_manager.py crawl https://large-site.com --max-pages 5000

# Monitor progress (in another terminal)
watch -n 5 "ls -lh crawled_data/*/statistics.json | tail -1"

# Process when done
python src/batch_processor.py --export jsonl --output large_site_chunks.jsonl
```

### Example 2: Test Small Crawl

```bash
# Quick test with example.com
python src/test_file_crawl.py

# View results
cat test_crawl_data/*/statistics.json | jq .
```

### Example 3: Resume Interrupted Crawl

The FileStoragePublisher automatically tracks processed URLs, so you can simply restart the crawl:

```bash
# Start crawl (may be interrupted)
python src/crawl_manager.py crawl https://site.com --max-pages 10000

# If interrupted, just run again - it will skip already processed URLs
python src/crawl_manager.py crawl https://site.com --max-pages 10000
```

## Data Format

### Saved Article (JSON)

```json
{
  "source_document_id": "https://example.com/page",
  "content": "Full markdown content...",
  "source": {
    "uri": "https://example.com/page",
    "module": "Intranet Connector",
    "retrieved_at": "2024-12-11T14:30:00Z"
  },
  "author": {
    "name": "John Doe"
  },
  "tags": [],
  "permissions": [],
  "metadata": {
    "title": "Page Title",
    "status_code": 200,
    "tables": []
  }
}
```

### Processed Chunk (JSONL Export)

```json
{
  "chunk_id": "page_0",
  "source_document_id": "https://example.com/page",
  "chunk_index": 0,
  "content": "Chunk text...",
  "url": "https://example.com/page",
  "metadata": {...},
  "permissions": [],
  "processed_at": "2024-12-11T15:00:00Z"
}
```

## Migration to Production

When the ingestion worker is ready, you can:

1. **Switch storage mode**: Change `STORAGE_MODE` from "file" to "rabbitmq"
2. **Replay stored data**: Use the batch processor to send stored data to RabbitMQ
3. **Keep as backup**: Continue using file storage as a backup/archive system

## Advantages of This Approach

1. **No dependencies**: Works without RabbitMQ or ingestion worker
2. **Data preservation**: All crawled data is saved and can be reprocessed
3. **Flexibility**: Process data when and how you need
4. **Debugging**: Easy to inspect crawled data (just JSON files)
5. **Resume capability**: Automatic deduplication prevents re-crawling
6. **Batch processing**: Efficient offline processing of large datasets

## Performance Considerations

- **Disk space**: Each page typically uses 5-50 KB (depending on content)
- **I/O performance**: Use SSD for better performance with large crawls
- **Batch size**: Larger batches (50-100) are more efficient for large crawls
- **Parallel processing**: The batch processor can be run in parallel on different sessions

## Troubleshooting

### Out of disk space

```bash
# Check disk usage
du -sh crawled_data/*

# Remove old sessions
rm -rf crawled_data/20241201_*  # Remove December 1st sessions
```

### Slow processing

- Increase batch size in configuration
- Use Parquet storage mode for better compression
- Process on a machine with more RAM/CPU

### Duplicate prevention not working

- Check that the storage path is consistent
- Ensure the index.jsonl files are not corrupted
- Clear processed_urls by starting a new session

## Next Steps

1. Implement real embedding generation in BatchProcessor
2. Add database export option
3. Create web UI for monitoring crawls
4. Add support for incremental/scheduled crawls
5. Integrate with vector databases for semantic search