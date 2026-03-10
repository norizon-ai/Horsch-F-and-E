# HPC Knowledge Base Elasticsearch Setup

This repository contains scripts to set up and search a comprehensive HPC knowledge base using Elasticsearch. The system indexes both documentation from the NHR@FAU website and historical support tickets.

## Overview

The knowledge base consists of two main indices:
- **`docs`**: Documentation from https://doc.nhr.fau.de (scraped using the web scraper)
- **`tickets`**: Historical support tickets from the knowledgebase directory

## Prerequisites

1. **Elasticsearch**: Running instance (default: http://localhost:9200)
2. **Python packages**: `requests` (already included in most Python installations)
3. **Data files**:
   - `/Users/sebastian/Downloads/ticketknowledgedb/docsmd/docs_data.jsonl` (from web scraper)
   - Markdown files in `/Users/sebastian/Downloads/ticketknowledgedb/knowledgebase/`

## Setup Process

### Step 1: Convert Knowledgebase to JSONL

First, convert the markdown ticket files to JSONL format:

```bash
python convert_knowledgebase_to_jsonl.py
```

This will:
- Parse all `.md` files in the knowledgebase directory
- Extract structured information (keywords, summary, problem description, solution, etc.)
- Create `knowledgebase_data.jsonl`

**Options:**
```bash
python convert_knowledgebase_to_jsonl.py --knowledgebase-dir /path/to/knowledgebase --output /path/to/output.jsonl
```

### Step 2: Insert Documentation Data

Insert the documentation data into Elasticsearch:

```bash
python insert_docs_data.py
```

This will:
- Create the `docs` index with appropriate mappings
- Insert all documentation pages from `docs_data.jsonl`
- Index fields: id, url, title, titles, text, filename

**Options:**
```bash
python insert_docs_data.py /path/to/docs_data.jsonl --index-name docs --recreate
```

### Step 3: Insert Ticket Data

Insert the ticket knowledgebase data into Elasticsearch:

```bash
python insert_knowledgebase_data.py
```

This will:
- Create the `tickets` index with appropriate mappings
- Insert all ticket data from `knowledgebase_data.jsonl`
- Index fields: ticket_id, keywords, summary, problem_description, root_cause, solution, actions_taken, general_learnings

**Options:**
```bash
python insert_knowledgebase_data.py /path/to/knowledgebase_data.jsonl --index-name tickets --recreate
```

## Searching the Knowledge Base

### Basic Search

Search across both documentation and tickets:

```bash
python search_knowledge.py "jupyter notebook"
```

### Search Specific Index

Search only documentation:
```bash
python search_knowledge.py "slurm batch jobs" --docs-only
```

Search only tickets:
```bash
python search_knowledge.py "quota exceeded" --tickets-only
```

### Advanced Options

```bash
python search_knowledge.py "python environment" --size 10 --info
```

**Options:**
- `--size N`: Number of results per index (default: 5)
- `--docs-only`: Search only documentation
- `--tickets-only`: Search only tickets
- `--info`: Show index information (document counts)
- `--elastic-url URL`: Custom Elasticsearch URL

## Index Structure

### Documentation Index (`docs`)

```json
{
  "id": "unique_hash",
  "url": "https://doc.nhr.fau.de/...",
  "title": "Page Title",
  "titles": ["Heading 1", "Heading 2"],
  "text": "Full markdown content",
  "filename": "page_filename.md",
  "indexed_at": "2024-01-01T00:00:00",
  "text_length": 1234,
  "source": "documentation"
}
```

### Tickets Index (`tickets`)

```json
{
  "id": "unique_hash",
  "ticket_id": "42015918",
  "filename": "42015918_mercurial.md",
  "title": "Ticket 42015918",
  "keywords": ["Mercurial", "Cluster", "Installation"],
  "summary": "Brief summary of the ticket",
  "problem_description": "Detailed problem description",
  "root_cause": "Root cause analysis",
  "solution": "Solution provided",
  "actions_taken": "Actions taken by support",
  "general_learnings": "General learnings from the ticket",
  "text": "Full markdown content",
  "indexed_at": "2024-01-01T00:00:00",
  "text_length": 1234,
  "source": "knowledgebase"
}
```

## Search Features

### Multi-field Search
The search automatically searches across relevant fields with different weights:

**Documentation:**
- `title^2` (highest weight)
- `text`
- `titles`

**Tickets:**
- `title^2` (highest weight)
- `summary^1.5`
- `keywords^1.5`
- `text`
- `problem_description`
- `solution`
- `actions_taken`

### Highlighting
Search results include highlighted fragments showing where matches were found.

### Fuzzy Matching
Automatic fuzzy matching handles typos and similar terms.

## Example Usage

### 1. Setup Everything
```bash
# Convert tickets to JSONL
python convert_knowledgebase_to_jsonl.py

# Insert documentation
python insert_docs_data.py --recreate

# Insert tickets
python insert_knowledgebase_data.py --recreate
```

### 2. Search Examples
```bash
# General search
python search_knowledge.py "GPU allocation"

# Find SLURM documentation
python search_knowledge.py "sbatch srun" --docs-only

# Find quota-related tickets
python search_knowledge.py "disk quota" --tickets-only

# Get more results
python search_knowledge.py "python modules" --size 10
```

### 3. Check Status
```bash
python search_knowledge.py "test" --info
```

## Troubleshooting

### Elasticsearch Connection Issues
- Ensure Elasticsearch is running on http://localhost:9200
- Use `--elastic-url` to specify a different URL
- Check firewall settings

### No Search Results
- Verify indices exist: `python search_knowledge.py "test" --info`
- Try simpler search terms
- Check for typos (fuzzy matching helps but has limits)

### Data Issues
- Ensure JSONL files are properly formatted
- Check file paths in the scripts
- Use `--recreate` flag to rebuild indices

## File Structure

```
ticketknowledgedb/
├── convert_knowledgebase_to_jsonl.py    # Convert MD files to JSONL
├── insert_docs_data.py                  # Insert documentation
├── insert_knowledgebase_data.py         # Insert tickets
├── search_knowledge.py                  # Search interface
├── knowledgebase_data.jsonl            # Generated ticket data
├── docsmd/
│   └── docs_data.jsonl                 # Documentation data
└── knowledgebase/
    ├── 42015918_mercurial.md           # Ticket files
    └── ...
```

## Environment Variables

- `ELASTIC_URL`: Elasticsearch URL (default: http://localhost:9200)

## Performance Notes

- Batch size: 1000 documents per bulk operation (configurable)
- Automatic retries on failures
- Progress reporting for large datasets
- Memory-efficient streaming processing

This setup provides a powerful search interface for both official HPC documentation and historical support tickets, enabling quick resolution of user issues and comprehensive knowledge discovery.
