# Confluence Data Scraper

A comprehensive Python tool for extracting all data from a Confluence instance using the REST API v2.

## Features

- **Complete Data Extraction**: Pages, blog posts, attachments, comments, labels, and permissions
- **Incremental Scraping**: Resume capability with checkpoint system
- **Rate Limiting**: Automatic handling of API rate limits with exponential backoff
- **Concurrent Processing**: Multi-threaded extraction for improved performance
- **Progress Tracking**: Real-time progress updates and ETA calculations
- **Error Recovery**: Automatic retry mechanism and detailed error logging
- **Flexible Storage**: JSON and HTML export formats with organized directory structure

## Installation

```bash
pip install -r requirements.txt
```

## Quick Start

### Basic Usage

```bash
python main.py --base-url https://company.atlassian.net/wiki --token YOUR_BEARER_TOKEN
```

### With Custom Options

```bash
python main.py \
  --base-url https://company.atlassian.net/wiki \
  --token YOUR_BEARER_TOKEN \
  --output-dir my_export \
  --max-workers 10 \
  --page-size 100
```

## Command Line Options

| Option | Description | Default |
|--------|-------------|---------|
| `--base-url` | Confluence instance URL (required) | - |
| `--token` | Bearer token for authentication (required) | - |
| `--output-dir` | Output directory for exported data | confluence_export |
| `--max-workers` | Number of concurrent workers | 5 |
| `--page-size` | Items per API request (max 250) | 50 |
| `--no-attachments` | Skip downloading attachments | False |
| `--no-resume` | Start fresh, ignore checkpoint | False |
| `--config-file` | Load configuration from JSON file | - |
| `--save-config` | Save configuration to JSON file | - |
| `--test-connection` | Test API connection and exit | False |

## Configuration File

Create a configuration file for reusable settings:

```json
{
  "base_url": "https://company.atlassian.net/wiki",
  "bearer_token": "YOUR_BEARER_TOKEN",
  "output_dir": "confluence_export",
  "max_workers": 5,
  "page_size": 50,
  "download_attachments": true
}
```

Use with: `python main.py --config-file config.json`

## Output Structure

```
confluence_export/
├── metadata.json           # Export metadata and configuration
├── export_report.json      # Summary statistics and failed items
├── checkpoint.json         # Resume checkpoint data
├── spaces/
│   ├── SPACE_KEY/
│   │   ├── space_info.json
│   │   ├── permissions.json
│   │   ├── pages/
│   │   │   ├── {page_id}.json
│   │   │   └── {page_id}.html
│   │   ├── blogs/
│   │   │   ├── {blog_id}.json
│   │   │   └── {blog_id}.html
│   │   ├── attachments/
│   │   │   └── page/{page_id}/
│   │   │       ├── {files}
│   │   │       └── metadata.json
│   │   ├── comments/
│   │   │   └── page/{page_id}_comments.json
│   │   └── labels/
│   │       └── page_{page_id}_labels.json
└── logs/
    └── scraper_{timestamp}.log
```

## Python API Usage

```python
from confluence_scraper import ConfluenceScraper, ScraperConfig

# Create configuration
config = ScraperConfig(
    base_url="https://company.atlassian.net/wiki",
    bearer_token="YOUR_BEARER_TOKEN",
    output_dir="my_export",
    max_workers=10,
    download_attachments=True
)

# Initialize scraper
scraper = ConfluenceScraper(config)

# Test connection
if scraper.test_connection():
    # Start scraping
    scraper.scrape_all(resume=True)
```

## Resume Capability

The scraper automatically saves progress to a checkpoint file. If interrupted:

1. **Resume**: Simply run the same command again (default behavior)
2. **Start Fresh**: Add `--no-resume` flag to ignore checkpoint

## Rate Limiting

The scraper handles Confluence API rate limits automatically:

- Exponential backoff on 429 responses
- Random jitter between requests
- Respects Retry-After headers
- Configurable retry attempts

## Performance Tips

1. **Adjust Workers**: Increase `--max-workers` for faster extraction (be mindful of rate limits)
2. **Optimize Page Size**: Use larger `--page-size` (up to 250) for fewer API calls
3. **Skip Attachments**: Use `--no-attachments` if file downloads aren't needed
4. **Monitor Progress**: Check logs for real-time progress and ETA

## Troubleshooting

### Authentication Issues
- Ensure bearer token is valid and has necessary permissions
- Test connection with `--test-connection` flag

### Rate Limiting
- Reduce `--max-workers` if hitting rate limits frequently
- The scraper will automatically retry with backoff

### Memory Usage
- For large instances, monitor memory usage
- Consider processing spaces individually if needed

### Resume Issues
- Delete `checkpoint.json` to force a fresh start
- Check `export_report.json` for failed items

## Export Report

After completion, check `export_report.json` for:

- Total spaces, pages, blogs processed
- Number of attachments and comments extracted
- Failed items with error details
- Total API requests made
- Processing timestamps

## Security Notes

- Never commit configuration files with tokens
- Store bearer tokens securely
- Use environment variables for sensitive data in production
- Review exported data for sensitive information before sharing

## Requirements

- Python 3.7+
- Confluence REST API v2 access
- Valid bearer token with read permissions

## License

This tool is provided as-is for data extraction purposes. Ensure compliance with your organization's data governance policies when using this tool.