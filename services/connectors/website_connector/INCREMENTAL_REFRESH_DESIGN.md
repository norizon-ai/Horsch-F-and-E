# Incremental Website Refresh Design

## Overview

This document outlines the design for daily incremental website refresh, including change detection, deletion handling, and integration with the message queue pipeline.

## Architecture Decision: Where to Process HTML → Markdown

### Chosen Approach: Convert in Website Connector ✅

**Flow:**
```
HTML Download → Clean & Convert to Markdown → Send to Queue → Embeddings → Elasticsearch
```

**Rationale:**
- ✅ **Separation of concerns** - Website connector handles web-specific tasks (HTML parsing, cleaning)
- ✅ **Reusable ingestion worker** - Worker can accept markdown from ANY source (PDFs, docs, etc.)
- ✅ **Better for debugging** - Can inspect markdown files before sending to queue
- ✅ **Smaller queue messages** - Markdown is cleaner/smaller than HTML
- ✅ **Worker stays simple** - Only handles embedding + storage, not HTML parsing

**Architecture:**
```
┌─────────────────────┐
│ Website Connector   │
│ - Download HTML     │
│ - Clean HTML        │
│ - Convert to MD     │ ← Domain-specific processing
└──────────┬──────────┘
           │ (clean markdown)
           ↓
┌─────────────────────┐
│   Message Queue     │
└──────────┬──────────┘
           │
           ↓
┌─────────────────────┐
│  Ingestion Worker   │
│ - Calculate embed.  │
│ - Store in ES       │ ← Generic processing
└─────────────────────┘
```

This architecture allows easy addition of other connectors (PDF, Word, etc.) that all feed markdown to the same generic ingestion worker.

---

## Daily Refresh Strategy

### Scheduling Options

#### Option 1: Cron Job (Linux/Standard)
```bash
# Edit crontab
crontab -e

# Add daily job at 2 AM
0 2 * * * cd /path/to/rag-server && ./services/connectors/website_connector/scrape_all.sh >> /var/log/fau_scrape.log 2>&1
```

**Pros:**
- ✅ Built into Linux/macOS
- ✅ Simple and reliable
- ✅ Survives reboots

**Cons:**
- ❌ Mac must be on at scheduled time
- ❌ Doesn't run if computer is asleep

#### Option 2: macOS launchd (Recommended for Mac)

Create `~/Library/LaunchAgents/com.fau.scraper.plist`:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>com.fau.scraper</string>
    <key>ProgramArguments</key>
    <array>
        <string>/bin/bash</string>
        <string>/Users/lisaschmidt/Documents/GitHub/rag-server/services/connectors/website_connector/scrape_all.sh</string>
    </array>
    <key>StartCalendarInterval</key>
    <dict>
        <key>Hour</key>
        <integer>2</integer>
        <key>Minute</key>
        <integer>0</integer>
    </dict>
    <key>StandardOutPath</key>
    <string>/tmp/fau_scraper.log</string>
    <key>StandardErrorPath</key>
    <string>/tmp/fau_scraper_error.log</string>
</dict>
</plist>
```

Load with:
```bash
launchctl load ~/Library/LaunchAgents/com.fau.scraper.plist
```

**Pros:**
- ✅ macOS native
- ✅ Can catch up after sleep/shutdown
- ✅ Better logging

#### Option 3: Python Scheduler (Portable)

```python
# scheduled_scraper.py
import schedule
import time
import subprocess

def run_scraper():
    print("Starting daily scrape...")
    subprocess.run([
        "./services/connectors/website_connector/scrape_all.sh"
    ])
    print("Scrape completed")

# Schedule daily at 2 AM
schedule.every().day.at("02:00").do(run_scraper)

while True:
    schedule.run_pending()
    time.sleep(60)
```

**Pros:**
- ✅ Cross-platform
- ✅ Easy to add complex logic
- ✅ Can integrate with Python codebase

**Cons:**
- ❌ Process must keep running

### Incremental vs Full Refresh Strategy

**Recommended Approach:**

```bash
# Daily: Incremental refresh (fast - only new/changed)
0 2 * * * cd /path && ./incremental_scrape.sh

# Weekly: Full refresh (slow - everything)
0 2 * * 0 cd /path && ./full_scrape.sh
```

**Daily Incremental:**
1. `wget --timestamping` (only downloads if server file is newer)
2. Process changed HTML → markdown
3. Send only changed docs to queue
4. Update embeddings for changed docs only

**Weekly Full:**
1. Full scrape (catch missed pages, disconnected branches)
2. Full reindex
3. Verify data integrity

---

## Change Detection

### Approach: Hybrid Timestamp + Content Hash (Recommended)

Combines speed of timestamp checks with accuracy of content hashing.

#### Implementation

```python
import hashlib
import json
from pathlib import Path
from datetime import datetime

class HybridChangeDetector:
    def __init__(self):
        self.last_run_file = Path(".last_run_timestamp")
        self.hash_db_file = Path(".content_hashes.json")
        self.last_run_time = self.get_last_run_time()
        self.hashes = self.load_hashes()

    def get_last_run_time(self):
        """Get timestamp of last processing run"""
        if self.last_run_file.exists():
            timestamp = float(self.last_run_file.read_text())
            return datetime.fromtimestamp(timestamp)
        return datetime.min  # Process everything if first run

    def load_hashes(self):
        """Load previous content hashes from disk"""
        if self.hash_db_file.exists():
            return json.loads(self.hash_db_file.read_text())
        return {}

    def is_changed(self, file_path):
        """Two-phase check: timestamp first (fast), then hash (accurate)"""

        # Phase 1: Quick timestamp check
        file_mtime = datetime.fromtimestamp(file_path.stat().st_mtime)
        if file_mtime <= self.last_run_time:
            # File not modified since last run - skip
            return False

        # Phase 2: File was touched - verify with content hash
        current_hash = self.get_content_hash(file_path)
        file_key = str(file_path)

        if file_key not in self.hashes or self.hashes[file_key] != current_hash:
            # Actually changed
            self.hashes[file_key] = current_hash
            return True

        # Timestamp changed but content same (false positive from wget)
        return False

    def get_content_hash(self, file_path):
        """Calculate MD5 hash of file content"""
        with open(file_path, 'rb') as f:
            return hashlib.md5(f.read()).hexdigest()

    def save_state(self):
        """Save timestamps and hashes after processing"""
        self.last_run_file.write_text(str(datetime.now().timestamp()))
        self.hash_db_file.write_text(json.dumps(self.hashes, indent=2))

# Usage
detector = HybridChangeDetector()
changed_count = 0

for html_file in Path("fau_temp_html").rglob("*.html"):
    if detector.is_changed(html_file):
        print(f"✓ Changed: {html_file}")
        markdown = convert_to_markdown(html_file)
        send_to_queue(markdown)
        changed_count += 1

print(f"\nProcessed {changed_count} changed files")
detector.save_state()
```

#### Why Hybrid Approach?

**Pros:**
- ✅ **Fast** - Timestamp check filters out most unchanged files (O(1) stat call)
- ✅ **Accurate** - Content hash catches actual changes, ignores false positives
- ✅ **Handles edge cases** - wget `--timestamping` may touch files without changing content
- ✅ **No external dependencies** - Just file system + JSON

**Comparison with alternatives:**

| Approach | Speed | Accuracy | Use Case |
|----------|-------|----------|----------|
| Timestamp only | Fast ⚡ | Medium ⚠️ | Quick checks, can have false positives |
| Content hash only | Slow 🐌 | High ✅ | Small datasets, need perfect accuracy |
| **Hybrid** | **Fast ⚡** | **High ✅** | **Production - best of both** |

#### State Files

The detector maintains two state files:

1. **`.last_run_timestamp`** - Single timestamp of last successful run
   ```
   1728934567.123456
   ```

2. **`.content_hashes.json`** - Hash database
   ```json
   {
     "fau_temp_html/www.fau.de/index.html": "a3b5c7d9e1f2g4h6",
     "fau_temp_html/research.fau.de/index.html": "b4c6d8e0f2g4h6i8"
   }
   ```

**Location:** Store in the `fau_temp_html/` directory or connector root.

---

## Deletion Handling

### Problem

When a page is removed from the website, we need to:
1. Detect that it no longer exists
2. Remove it from Elasticsearch
3. Clean up any associated metadata

### Approach: URL Registry Comparison (Recommended)

Track all known URLs and compare with current scrape to find deletions.

#### Implementation

```python
class DeletionTracker:
    def __init__(self, registry_file=".url_registry.json"):
        self.registry_file = Path(registry_file)
        self.known_urls = self.load_registry()
        self.current_run_urls = set()

    def load_registry(self):
        """Load all previously scraped URLs"""
        if self.registry_file.exists():
            return set(json.loads(self.registry_file.read_text()))
        return set()

    def mark_as_seen(self, url):
        """Track that this URL exists in current scrape"""
        self.current_run_urls.add(url)

    def get_deleted_urls(self):
        """Find URLs that existed before but not in current run"""
        deleted = self.known_urls - self.current_run_urls
        return list(deleted)

    def update_registry(self):
        """Save current URLs as the new registry"""
        self.registry_file.write_text(
            json.dumps(list(self.current_run_urls), indent=2)
        )

# Usage
tracker = DeletionTracker()

# Process all current HTML files
for html_file in Path("fau_temp_html").rglob("*.html"):
    url = convert_file_path_to_url(html_file)
    tracker.mark_as_seen(url)

    if change_detector.is_changed(html_file):
        process_and_send_to_queue(html_file)

# Find deleted pages
deleted_urls = tracker.get_deleted_urls()
print(f"Found {len(deleted_urls)} deleted pages")

# Send deletion messages to queue
for url in deleted_urls:
    send_deletion_to_queue(url)

tracker.update_registry()
```

#### File Path to URL Conversion

```python
def convert_file_to_url(file_path):
    """Convert local file path back to original URL"""
    # Example: fau_temp_html/www.fau.de/about/index.html
    #       -> https://www.fau.de/about/

    path_str = str(file_path)

    # Remove base directory
    path_str = path_str.replace("fau_temp_html/", "")

    # Handle index.html
    path_str = path_str.replace("/index.html", "/")

    # Handle .html extension
    path_str = path_str.replace(".html", "")

    # Add protocol
    return f"https://{path_str}"
```

### Message Queue Integration

Send both **upsert** and **delete** actions through the queue:

```python
class WebsiteConnector:
    def __init__(self, message_queue):
        self.queue = message_queue
        self.change_detector = HybridChangeDetector()
        self.deletion_tracker = DeletionTracker()

    def process_scrape_results(self, html_dir):
        """Process scraping results and handle deletions"""

        stats = {
            'new': 0,
            'updated': 0,
            'unchanged': 0,
            'deleted': 0
        }

        # 1. Process existing files (upserts)
        for html_file in Path(html_dir).rglob("*.html"):
            url = self.file_to_url(html_file)
            self.deletion_tracker.mark_as_seen(url)

            if self.change_detector.is_changed(html_file):
                markdown = self.convert_to_markdown(html_file)

                self.queue.send({
                    "action": "upsert",
                    "url": url,
                    "content": markdown,
                    "metadata": self.extract_metadata(html_file)
                })

                stats['updated'] += 1
            else:
                stats['unchanged'] += 1

        # 2. Handle deletions
        deleted_urls = self.deletion_tracker.get_deleted_urls()

        for url in deleted_urls:
            self.queue.send({
                "action": "delete",
                "url": url
            })
            stats['deleted'] += 1

        # 3. Save state
        self.change_detector.save_state()
        self.deletion_tracker.update_registry()

        logger.info(f"Processing complete: {stats}")
        return stats
```

### Ingestion Worker Updates

The worker must handle both upsert and delete actions:

```python
def process_message(msg):
    """Process messages from queue"""

    if msg['action'] == 'upsert':
        # Normal processing: calculate embeddings and store
        embeddings = calculate_embeddings(msg['content'])
        store_in_elasticsearch(msg, embeddings)
        logger.info(f"Upserted: {msg['url']}")

    elif msg['action'] == 'delete':
        # Delete from Elasticsearch by URL
        delete_from_elasticsearch(msg['url'])
        logger.info(f"Deleted: {msg['url']}")

    else:
        logger.error(f"Unknown action: {msg.get('action')}")
```

### Elasticsearch Deletion

```python
def delete_from_elasticsearch(url, es_client, index_name):
    """Delete document from Elasticsearch by URL"""

    try:
        # Delete by query (URL field)
        query = {
            "query": {
                "term": {
                    "url.keyword": url
                }
            }
        }

        result = es_client.delete_by_query(
            index=index_name,
            body=query
        )

        deleted_count = result.get('deleted', 0)
        logger.info(f"Deleted {deleted_count} documents for URL: {url}")

        return deleted_count

    except Exception as e:
        logger.error(f"Failed to delete {url}: {e}")
        return 0
```

---

## Complete Daily Refresh Flow

### End-to-End Process

```
1. Cron/launchd triggers scrape at 2 AM
   ↓
2. scrape_all.sh runs wget --timestamping
   - Downloads only changed files from server (fast)
   - Maintains directory structure in fau_temp_html/
   ↓
3. HTML Processor starts
   ├─ HybridChangeDetector: Find changed files on disk
   ├─ DeletionTracker: Track current URLs
   └─ For each HTML file:
      ├─ Mark as seen in DeletionTracker
      ├─ If changed:
      │  ├─ Clean HTML (remove nav, scripts, etc.)
      │  ├─ Convert to markdown
      │  └─ Send "upsert" to queue
      └─ If unchanged: skip
   ↓
4. Find deletions
   ├─ Compare current URLs vs previous run
   └─ Send "delete" messages to queue
   ↓
5. Save state
   ├─ Update .last_run_timestamp
   ├─ Update .content_hashes.json
   └─ Update .url_registry.json
   ↓
6. Message Queue
   ├─ Buffers upsert/delete messages
   └─ Delivers to ingestion worker
   ↓
7. Ingestion Worker
   ├─ Upserts: Calculate embeddings → Store in ES
   └─ Deletes: Remove from ES by URL
   ↓
8. Elasticsearch updated
   ├─ New/changed documents indexed
   └─ Deleted documents removed
```

### Performance Characteristics

**For 4000+ subdomains:**

**Initial Full Scrape:**
- Time: 6-12 hours (depends on site sizes)
- Files: 50k-200k HTML pages
- Disk: 10-50 GB

**Daily Incremental:**
- Typical changes: 1-5% of pages (50-1000 files)
- Time: 10-30 minutes
- Queue messages: 50-1000 upserts + 10-50 deletes

**Weekly Full Refresh:**
- Re-validates everything
- Catches disconnected pages
- Time: Similar to initial scrape

### Monitoring Metrics

Track these metrics for health monitoring:

```python
stats = {
    'scrape_start': datetime,
    'scrape_end': datetime,
    'scrape_duration_seconds': float,

    'html_files_total': int,
    'html_files_new': int,
    'html_files_changed': int,
    'html_files_unchanged': int,

    'urls_deleted': int,

    'queue_messages_sent': int,
    'queue_messages_upsert': int,
    'queue_messages_delete': int,

    'errors': int,
    'warnings': int
}
```

Log to file for historical tracking:
```python
# scrape_history.jsonl
{"date": "2025-10-15", "stats": {...}}
{"date": "2025-10-16", "stats": {...}}
```

---

## State Files Overview

The system maintains several state files in the connector directory:

| File | Purpose | Format | Size |
|------|---------|--------|------|
| `.last_run_timestamp` | Track last successful run | Single float timestamp | < 1 KB |
| `.content_hashes.json` | Hash of each file's content | JSON: {filepath: hash} | ~1-10 MB |
| `.url_registry.json` | All known URLs from previous run | JSON: [urls] | ~1-5 MB |
| `scrape_progress.log` | Execution logs | Text | ~1-10 MB |
| `wget.log` | wget output (optional) | Text | ~5-50 MB |

**Backup Strategy:**
- Commit state files to git (for small repos)
- Or backup to S3/cloud storage daily
- Allows recovery if state is corrupted

---

## Error Handling

### Partial Scrape Failures

If scraping fails partway through:

```python
try:
    # Process all files
    for html_file in files:
        process_file(html_file)

    # Only save state if ALL processing succeeded
    change_detector.save_state()
    deletion_tracker.update_registry()

except Exception as e:
    logger.error(f"Scraping failed: {e}")
    logger.info("State not saved - will retry next run")
    # State files remain unchanged, next run will reprocess
```

### wget Failures

Handle individual subdomain failures:

```bash
# In scrape_all.sh
scrape_site() {
    wget ... || {
        echo "Failed: $url" >> failed_sites.log
        return 1
    }
}
```

Track failed sites and retry:
```python
# Retry failed sites from previous run
if Path("failed_sites.log").exists():
    failed_sites = Path("failed_sites.log").read_text().splitlines()
    for site in failed_sites:
        retry_scrape(site)
```

### Queue Failures

Implement retry logic for message queue:

```python
def send_to_queue_with_retry(message, max_retries=3):
    for attempt in range(max_retries):
        try:
            queue.send(message)
            return True
        except Exception as e:
            logger.warning(f"Queue send failed (attempt {attempt+1}): {e}")
            time.sleep(2 ** attempt)  # Exponential backoff

    # If all retries failed, log to dead letter file
    with open("failed_queue_messages.jsonl", "a") as f:
        f.write(json.dumps(message) + "\n")

    return False
```

---

## Future Enhancements

### 1. Distributed Scraping
- Split subdomain list across multiple machines
- Parallel processing for faster full scrapes
- Central coordination via Redis or database

### 2. Smart Prioritization
- Prioritize frequently-updated pages (news, blogs)
- Deprioritize static pages (about, contact)
- Use historical change patterns

### 3. Change Notification
- Send email/Slack alerts when important pages change
- Track metrics on change frequency by domain
- Alert on large-scale deletions (possible scraping issue)

### 4. Incremental Embedding Updates
- Only recalculate embeddings for changed text chunks
- Store chunk-level hashes for fine-grained updates
- Significant performance improvement for large documents

### 5. A/B Version Comparison
- Store previous version of changed pages
- Generate diff reports
- Useful for content auditing and compliance

---

## Testing Strategy

### Unit Tests

Test individual components:

```python
def test_change_detector():
    detector = HybridChangeDetector()

    # Create test file
    test_file = Path("test.html")
    test_file.write_text("content v1")

    # First check - should be new
    assert detector.is_changed(test_file) == True

    # Second check - should be unchanged
    assert detector.is_changed(test_file) == False

    # Modify content
    test_file.write_text("content v2")
    assert detector.is_changed(test_file) == True
```

### Integration Tests

Test full pipeline:

```python
def test_incremental_pipeline():
    # 1. Initial scrape
    run_scrape()
    initial_count = count_es_documents()

    # 2. Add new page to HTML dir
    create_test_html("new_page.html")

    # 3. Run incremental
    run_scrape()
    new_count = count_es_documents()

    assert new_count == initial_count + 1

    # 4. Delete page
    delete_html("new_page.html")

    # 5. Run incremental
    run_scrape()
    final_count = count_es_documents()

    assert final_count == initial_count
```

### Manual Testing Checklist

- [ ] Initial full scrape completes successfully
- [ ] Incremental detects no changes on second run
- [ ] Incremental detects modified files
- [ ] Incremental detects new files
- [ ] Deletion tracking finds removed pages
- [ ] Queue receives both upsert and delete messages
- [ ] Elasticsearch properly stores and deletes documents
- [ ] State files are saved correctly
- [ ] Scrape survives interruption (state not saved)
- [ ] Recovery from partial failures works

---

## Configuration

### Environment Variables

```bash
# .env file
SCRAPE_OUTPUT_DIR="fau_temp_html"
SCRAPE_PARALLEL_JOBS=25
SCRAPE_WGET_TIMEOUT=30
SCRAPE_WAIT_TIME=0.5

MESSAGE_QUEUE_URL="amqp://localhost:5672"
MESSAGE_QUEUE_NAME="document_processing"

ES_HOST="localhost"
ES_PORT=9200
ES_INDEX="fau_documents"

LOG_LEVEL="INFO"
LOG_FILE="scrape_progress.log"
```

### Connector Configuration

```python
# config.py
from dataclasses import dataclass
from pathlib import Path

@dataclass
class ConnectorConfig:
    # Paths
    html_dir: Path = Path("fau_temp_html")
    state_dir: Path = Path(".")

    # Change detection
    enable_change_detection: bool = True
    enable_deletion_tracking: bool = True

    # Processing
    max_file_size_mb: int = 50
    skip_patterns: list = None

    # Message queue
    queue_batch_size: int = 100
    queue_retry_attempts: int = 3

    # Logging
    log_level: str = "INFO"
    log_file: Path = Path("scrape_progress.log")

config = ConnectorConfig()
```

---

## Deployment Checklist

Before deploying to production:

- [ ] Install dependencies (`wget`, `python`, `gnu-parallel`)
- [ ] Configure environment variables
- [ ] Set up cron/launchd schedule
- [ ] Configure message queue connection
- [ ] Configure Elasticsearch connection
- [ ] Test initial scrape on subset
- [ ] Verify queue integration
- [ ] Verify ES indexing
- [ ] Set up monitoring/alerting
- [ ] Document runbook for operators
- [ ] Test failure recovery scenarios
- [ ] Set up log rotation
- [ ] Configure backup for state files

---

## References

- `scrape_all.sh` - Parallel wget scraping script
- `filter_subdomains.py` - Subdomain filtering and validation
- `fast_download_docs.py` - HTML to markdown conversion (to be refactored)
- Message queue documentation: [link]
- Elasticsearch schema: [link]
- Ingestion worker code: [link]

## Change Log

- 2025-10-15: Initial design document created
