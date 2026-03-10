#!/bin/bash
# Efficiently scrape all valid subdomains

# =============================================================================
# LOAD CONFIGURATION
# =============================================================================

# Try to load config from multiple locations
CONFIG_LOADED=false

for config_path in "./config.env" "$HOME/.website-connector/config.env" "/app/config.env"; do
    if [ -f "$config_path" ]; then
        echo "Loading configuration from: $config_path"
        source "$config_path"
        CONFIG_LOADED=true
        break
    fi
done

if [ "$CONFIG_LOADED" = false ]; then
    echo "Warning: No config.env found. Using default values."
    echo "Copy config.env.example to config.env to customize settings."
fi

# =============================================================================
# SET DEFAULTS (fallback if not in config)
# =============================================================================

WEBSITES_FILE="${WEBSITES_FILE:-valid_websites.txt}"
OUTPUT_DIR="${OUTPUT_DIR:-fau_temp_html_eu_de}"
PARALLEL_JOBS="${PARALLEL_JOBS:-50}"
DOMAINS="${DOMAINS:-fau.de,fau.eu}"
WAIT_TIME="${WAIT_TIME:-0.5}"
RANDOM_WAIT="${RANDOM_WAIT:-true}"
TIMEOUT="${TIMEOUT:-30}"
MAX_RETRIES="${MAX_RETRIES:-3}"
QUOTA_PER_SITE="${QUOTA_PER_SITE:-500m}"
MAX_REDIRECTS="${MAX_REDIRECTS:-5}"
REJECT_EXTENSIONS="${REJECT_EXTENSIONS:-*.pdf,*.zip,*.tar.gz,*.exe,*.dmg,*.jpg,*.jpeg,*.png,*.gif,*.svg,*.ico,*.webp,*.bmp,*.tiff,*.css,*.js}"
REJECT_URL_PATTERN="${REJECT_URL_PATTERN:-.*(\?|&)(session|sid|token|ref|utm_|PHPSESSID)=.*}"

# Check if file exists
if [ ! -f "$WEBSITES_FILE" ]; then
    echo "Error: $WEBSITES_FILE not found!"
    echo "Run filter_subdomains.py first"
    exit 1
fi

# =============================================================================
# DISPLAY CONFIGURATION
# =============================================================================

TOTAL_SITES=$(wc -l < "$WEBSITES_FILE")
echo ""
echo "=========================================="
echo "Website Connector - Scraping Configuration"
echo "=========================================="
echo "Websites file:     $WEBSITES_FILE"
echo "Total sites:       $TOTAL_SITES"
echo "Output directory:  $OUTPUT_DIR"
echo "Parallel jobs:     $PARALLEL_JOBS"
echo "Domains:           $DOMAINS"
echo "Timeout:           ${TIMEOUT}s"
echo "Max retries:       $MAX_RETRIES"
echo "Quota per site:    $QUOTA_PER_SITE"
echo "=========================================="
echo ""

# =============================================================================
# SCRAPING FUNCTION
# =============================================================================

scrape_site() {
    local url="$1"
    echo "[$(date '+%H:%M:%S')] Starting: $url"

    # Build wget command with configuration variables
    local wget_cmd=(
        wget
        --recursive
        --no-clobber
        --continue
        --html-extension
        --restrict-file-names=windows
        --domains="$DOMAINS"
        --no-parent
        --reject="$REJECT_EXTENSIONS"
        --reject-regex="$REJECT_URL_PATTERN"
        --max-redirect="$MAX_REDIRECTS"
        --directory-prefix="$OUTPUT_DIR"
        --wait="$WAIT_TIME"
        --timeout="$TIMEOUT"
        --tries="$MAX_RETRIES"
        --quota="$QUOTA_PER_SITE"
        --quiet
    )

    # Add --random-wait if enabled
    if [ "$RANDOM_WAIT" = "true" ]; then
        wget_cmd+=(--random-wait)
    fi

    # Add URL
    wget_cmd+=("$url")

    # Execute wget command
    "${wget_cmd[@]}" 2>&1 | grep -v "^--" || true

    echo "[$(date '+%H:%M:%S')] Completed: $url"
}

# Export function and variables for GNU parallel
export -f scrape_site
export OUTPUT_DIR DOMAINS REJECT_EXTENSIONS REJECT_URL_PATTERN MAX_REDIRECTS WAIT_TIME TIMEOUT MAX_RETRIES QUOTA_PER_SITE RANDOM_WAIT

# =============================================================================
# PARALLEL EXECUTION
# =============================================================================

# Check if GNU parallel is installed
if command -v parallel &> /dev/null; then
    echo "Using GNU Parallel for optimal performance..."
    cat "$WEBSITES_FILE" | parallel -j "$PARALLEL_JOBS" --bar scrape_site {}
else
    echo "GNU Parallel not found. Using sequential processing..."
    echo "Tip: Install with 'brew install parallel' for faster downloads"

    COUNT=0
    while IFS= read -r url; do
        COUNT=$((COUNT + 1))
        echo "[$COUNT/$TOTAL_SITES] Scraping: $url"
        scrape_site "$url"
    done < "$WEBSITES_FILE"
fi

echo ""
echo "=========================================="
echo "All scraping completed!"
echo "Output directory: $OUTPUT_DIR"
echo "=========================================="

# Count downloaded files
HTML_COUNT=$(find "$OUTPUT_DIR" -name "*.html" 2>/dev/null | wc -l)
echo "Total HTML files downloaded: $HTML_COUNT"
