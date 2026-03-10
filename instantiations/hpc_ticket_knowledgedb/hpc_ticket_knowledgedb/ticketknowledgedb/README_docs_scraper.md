# Documentation Scraper for doc.nhr.fau.de

This script downloads all pages from https://doc.nhr.fau.de, converts them to markdown format, and saves them in two formats:

1. **Individual Markdown files** in the `docsmd/` directory
2. **JSONL file** with structured data including text, titles, and metadata

## Installation

First, install the required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

### Basic Usage

Run the scraper with default settings:

```bash
python download_docs.py
```

This will:
- Create a `docsmd/` directory in the current folder
- Download all pages from https://doc.nhr.fau.de
- Save each page as a `.md` file with URL-based naming
- Create a `docs_data.jsonl` file with structured data

### Output Format

#### Markdown Files
Each page is saved as a `.md` file with a filename based on the URL. For example:
- `https://doc.nhr.fau.de/access/ssh-how-it-works/index.html` → `https___doc.nhr.fau.de_access_ssh-how-it-works_index.html.md`

#### JSONL Format
Each line in `docs_data.jsonl` contains:
```json
{
  "id": "unique_md5_hash",
  "url": "https://doc.nhr.fau.de/page/url",
  "title": "Page Title",
  "titles": ["Heading 1", "Heading 2", "..."],
  "text": "Full markdown content",
  "filename": "corresponding_md_filename.md"
}
```

## Features

- **Respectful crawling**: Includes delays between requests and checks robots.txt
- **Content cleaning**: Removes navigation, footers, and other non-content elements
- **Duplicate detection**: Avoids downloading the same page multiple times
- **Error handling**: Continues crawling even if individual pages fail
- **Progress logging**: Shows real-time progress during crawling
- **URL normalization**: Handles relative links and removes fragments/query parameters

## Customization

You can modify the script to:
- Change the output directory by modifying the `output_dir` parameter
- Adjust the maximum number of pages with the `max_pages` parameter
- Modify the delay between requests by changing the `time.sleep()` value
- Customize HTML cleaning rules in the `clean_html_content()` method

## Example Output Structure

```
docsmd/
├── docs_data.jsonl
├── https___doc.nhr.fau.de.md
├── https___doc.nhr.fau.de_access_ssh-how-it-works_index.md
├── https___doc.nhr.fau.de_software_modules_index.md
└── ... (more .md files)
```

## Notes

- The scraper is designed to be respectful and includes a 1-second delay between requests
- It automatically handles relative URLs and stays within the doc.nhr.fau.de domain
- Large websites may take considerable time to crawl completely
- The script can be interrupted with Ctrl+C and will show progress up to that point
