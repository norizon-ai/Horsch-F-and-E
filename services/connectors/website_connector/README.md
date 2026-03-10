# Service Instructions: Website Connector

The website connector is a microservice allowing to use data from one or more websites for downstream applications, such as storing it in a database.

## Usage Options
1. docker container, configuration and data loading via config file
2. docker container prebuilt with data, configuration limited to interfaces
3. locally + give config file (debuggable, best for defining config)

## Prerequisites to use locally
Note: For docker deployment you only require Docker.

- **subfinder** - Fast subdomain discovery tool (install: `brew install subfinder` or [download](https://github.com/projectdiscovery/subfinder))
- **wget** - Website downloader with connection reuse (install: `brew install wget`)
- **GNU Parallel** (optional) - For parallel scraping (install: `brew install parallel`)
- **Python 3.8+** - For filtering and HTML-to-markdown conversion
- **Python packages** - `pip install requests beautifulsoup4 lxml html2text tqdm pyyaml`

## Config Guide for Docker, local and production usage

The website connector is configured using environment variables via `config.env`. This allows the service to work **consistently across local development, Docker containers, and production deployments**.

### Quick Start

1. **Copy the example config:**
   ```bash
   cp config.env.example config.env
   ```

2. **Edit `config.env`** to match your use case:
   ```bash
   # Example: Scrape example.com with conservative settings
   DOMAINS="fau.de"
   PARALLEL_JOBS=10
   OUTPUT_DIR="example_html"
   ```

The config is automatically loaded when you run scripts.


### Configuration Options

See `config.env.example` for all available options with detailed comments. Key settings:

| Variable | Description | Example |
|----------|-------------|---------|
| `DOMAINS` | Comma-separated domains to crawl | `"fau.de,fau.eu"` |
| `PARALLEL_JOBS` | Number of concurrent wget processes | `50` (adjust by bandwidth) |
| `OUTPUT_DIR` | Where to store downloaded HTML | `"temp_html"` |
| `TIMEOUT` | Request timeout in seconds | `30` |
| `REJECT_EXTENSIONS` | File types to skip | `"*.pdf,*.jpg,*.png"` |


**Parallel jobs guideline**:

| Connection Speed | Recommended PARALLEL_JOBS | Rationale |
|-----------------|---------------------------|-----------|
| < 10 Mbps | 3-5 | Bandwidth limited |
| 10-50 Mbps | 8-15 | Mixed constraint |
| 50-100 Mbps | 15-25 | Latency limited |
| 100+ Mbps | 20-35 | Pure latency |
| Gigabit+ | 30-50 | Limited by CPU/RAM |

### Local vs Docker Configuration

**Local development:**
- Config is loaded from `./config.env` in the project directory
- Override variables: `PARALLEL_JOBS=10 ./scrape_all.sh`

**Docker deployment:**
```yaml
# docker-compose.yml
services:
  website-connector:
    env_file: config.env  # Loads all variables
    # Or use environment section:
    environment:
      - PARALLEL_JOBS=50
      - DOMAINS=fau.de,fau.eu
```

### Configuration Priority

Variables are resolved in this order (highest to lowest priority):
1. Command-line: `PARALLEL_JOBS=10 ./scrape_all.sh`
2. Environment: `export PARALLEL_JOBS=10`
3. Config file: `config.env`
4. Built-in defaults: Fallback values in scripts

## Local Setup

### Step 1: Configure Your Environment

Copy and edit the configuration file:
```bash
cp config.env.example config.env
# Edit config.env with your domains and settings
```

### Step 2: Discover Subdomains

Find subdomains using [subfinder](https://github.com/projectdiscovery/subfinder) (see also [docs](https://projectdiscovery.io/blog/do-you-really-know-subfinder-an-in-depth-guide-to-all-features-of-subfinder-beginner-to-advanced)). Subfinder is fast because it's a passive subdomain discovery tool written in golang.

**Single domain:**
```bash
subfinder -d example.com -o subdomains.txt
```

**Multiple top-level domains** (e.g., `.fau.de` and `.fau.eu`):
```bash
# Discover .de subdomains
subfinder -d fau.de -o subdomains_de.txt

# Discover .eu subdomains
subfinder -d fau.eu -o subdomains_eu.txt

# Combine both
cat subdomains_de.txt subdomains_eu.txt > subdomains.txt
```

### Step 3: Filter Subdomains

Clean the list by removing infrastructure servers and checking which domains serve HTML:

```bash
python filter_subdomains.py subdomains.txt
```

This creates `valid_websites.txt` with only accessible HTML-serving domains. The filter automatically:
- Removes infrastructure patterns (mail servers, databases, CI/CD, etc.)
- Normalizes www/non-www duplicates
- Tests each domain for HTML content
- Shows progress with a progress bar

### Step 4: Scrape All Websites

Download all pages with wget. Wget is fast because it re-uses HTTP connections; the downside is it doesn't render JavaScript content.

**Run the scraper:**
```bash
./scrape_all.sh # automatically loads the config from the config file
```

The script uses GNU Parallel to spawn multiple wget processes for fast parallel downloads. Configuration is automatically loaded from `config.env`.

**Resume after interruption:**
```bash
./scrape_all.sh  # Automatically resumes with --no-clobber and --continue
```

**Override config temporarily:**
```bash
PARALLEL_JOBS=10 OUTPUT_DIR=/tmp/test ./scrape_all.sh
```

### Step 5: Convert HTML to Markdown

Transform downloaded HTML pages into clean Markdown format. This is done in the website connector (not the ingestion worker) since it's a website-specific task.

**Prerequisites:**
```bash
# Install pandoc (required for conversion)
brew install pandoc  # macOS
# OR
sudo apt install pandoc  # Linux
```

**Run the converter:**
```bash
python html_to_markdown.py
```

**What it does:**
- Removes navigation, headers, footers, and other non-content elements (configurable in `config.env`)
- Converts clean HTML to Markdown using pandoc
- Processes files in parallel for speed
- Generates JSONL file with metadata for downstream processing
- Shows progress with a progress bar

**Configuration in `config.env`:**
```bash
# Input/Output
HTML_INPUT_DIR="fau_temp_html_eu_de"  # Should match scraping OUTPUT_DIR
MARKDOWN_OUTPUT_DIR="fau_docsmd"

# Content cleaning (customize based on website structure)
REMOVE_ELEMENTS="nav,footer,header,script,style,aside"
REMOVE_SELECTORS=".navigation,#sidebar,.breadcrumb"

# Performance
PARALLEL_WORKERS=""  # Auto-detect, or set manually (e.g., "4")

# Cleanup
CLEANUP_HTML=false  # Set to true to delete HTML after conversion
```

**Output:**
- `fau_docsmd/*.md` - Individual markdown files
- `fau_docsmd/docs_data.jsonl` - Structured data with metadata (url, title, headings, content)

## (not yet implemented) Scheduled Re-Scraping / Updating the db

We have several options to refresh the connector content (launchd, python scheduler are also available but omitted here because they do not fit the system setup well). 

Docker + Cron:

```Dockerfile
  # In your Dockerfile
  RUN apt-get install -y cron

  # Add cron job
  COPY scraper_cron /etc/cron.d/scraper_cron
  RUN chmod 0644 /etc/cron.d/scraper_cron
  RUN crontab /etc/cron.d/scraper_cron
```

Cloud Scheduler
 - AWS: EventBridge + Lambda
 - GCP: Cloud Scheduler + Cloud Run
 - Azure: Logic Apps

## Diff / Minimal updates to the db

Timestamping: 
  - Only downloads if server file is newer
  - Much faster than full re-download
  - Perfect for daily updates
  - Comparing html_file.stat().st_mtime
  - Simple and fast
  - Works with wget's --timestamping
  - No database needed

  Cons:
  - Relies on file system timestamps
  - Can miss changes if file dates are wrong

Content Hashing:
Store hash of content, compare on each run
  - ✅ Detects actual content changes
  - ✅ Ignores timestamp issues
  - ✅ Very reliable

  Cons:
  - ❌ Slower (must read every file to hash)
  - ❌ Stores hash database
  Possible to combine with timestamps

Database Tracking:
- stores metadata in the elastic db or in a separate db
- compare each hash based on the url 

How do we delete a file from the db if the url is no longer on the server? Four options:
1. Track during scraping (store a registry of all known URLs) -> send deletion request to the message queue url
2. Scrape and detect 404 messages
3. compare disk vs. database
Is it okay if the website service communicates directly with the elasticsearch db?

Full Refresh + comparison:

How do we track delete
