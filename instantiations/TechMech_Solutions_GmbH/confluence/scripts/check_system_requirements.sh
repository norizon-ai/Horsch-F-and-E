#!/bin/bash

# ====================================================
# DEMO CONFLUENCE ASSISTANT - SETUP SCRIPT
# ====================================================
# Prepares the environment for the TechMech Solutions demo

set -e  # Exit on error

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Script directory
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_DIR="$(dirname "$SCRIPT_DIR")"

echo -e "${BLUE}========================================${NC}"
echo -e "${BLUE}Demo Confluence Assistant - Setup${NC}"
echo -e "${BLUE}TechMech Solutions Synthetic Data${NC}"
echo -e "${BLUE}========================================${NC}"
echo ""

# ----------------------------------------------------
# Check Prerequisites
# ----------------------------------------------------
echo -e "${YELLOW}Checking prerequisites...${NC}"

# Check Docker
if ! command -v docker &> /dev/null; then
    echo -e "${RED}Error: Docker is not installed${NC}"
    echo "Please install Docker Desktop from: https://www.docker.com/products/docker-desktop"
    exit 1
fi
echo -e "${GREEN}✓ Docker found${NC}"

# Check Docker Compose
if ! docker compose version &> /dev/null; then
    echo -e "${RED}Error: Docker Compose is not available${NC}"
    echo "Please install Docker Compose or update Docker Desktop"
    exit 1
fi
echo -e "${GREEN}✓ Docker Compose found${NC}"

# Check Docker is running
if ! docker info &> /dev/null; then
    echo -e "${RED}Error: Docker daemon is not running${NC}"
    echo "Please start Docker Desktop"
    exit 1
fi
echo -e "${GREEN}✓ Docker daemon is running${NC}"

# Check Python 3
if ! command -v python3 &> /dev/null; then
    echo -e "${RED}Error: Python 3 is not installed${NC}"
    echo "Python 3 is required for indexing the demo data"
    exit 1
fi
echo -e "${GREEN}✓ Python 3 found${NC}"

echo ""

# ----------------------------------------------------
# Check Generated Data
# ----------------------------------------------------
echo -e "${YELLOW}Checking demo data...${NC}"

DATA_DIR="$PROJECT_DIR/generated_confluence"
if [ ! -d "$DATA_DIR" ]; then
    echo -e "${RED}Error: Generated confluence data not found${NC}"
    echo "Expected directory: $DATA_DIR"
    echo ""
    echo "Please generate the demo data first:"
    echo "  cd $PROJECT_DIR"
    echo "  python3 generate_confluence.py --api-key YOUR_KEY"
    exit 1
fi

# Count markdown files
MD_COUNT=$(find "$DATA_DIR" -name "*.md" | wc -l | tr -d ' ')
if [ "$MD_COUNT" -eq 0 ]; then
    echo -e "${RED}Error: No markdown files found in $DATA_DIR${NC}"
    echo "Please generate the demo data first"
    exit 1
fi

echo -e "${GREEN}✓ Found $MD_COUNT markdown pages${NC}"
echo ""

# ----------------------------------------------------
# Create .env file if it doesn't exist
# ----------------------------------------------------
ENV_FILE="$PROJECT_DIR/.env"
ENV_EXAMPLE="$PROJECT_DIR/.env.example"

if [ ! -f "$ENV_FILE" ]; then
    echo -e "${YELLOW}Creating .env file from template...${NC}"
    cp "$ENV_EXAMPLE" "$ENV_FILE"
    echo -e "${GREEN}✓ Created .env file${NC}"
    echo ""
    echo -e "${YELLOW}IMPORTANT: Please edit $ENV_FILE and add your API keys${NC}"
    echo -e "${YELLOW}At minimum, you need to set:${NC}"
    echo "  - OPENAI_API_KEY (or another model backend)"
    echo ""

    # Ask if user wants to edit now
    read -p "Would you like to edit the .env file now? (y/n) " -n 1 -r
    echo
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        ${EDITOR:-nano} "$ENV_FILE"
    else
        echo -e "${YELLOW}Remember to edit $ENV_FILE before running the demo!${NC}"
    fi
else
    echo -e "${GREEN}✓ .env file already exists${NC}"
fi

echo ""

# ----------------------------------------------------
# Verify Configuration
# ----------------------------------------------------
echo -e "${YELLOW}Verifying configuration...${NC}"

# Source the .env file to check variables
set -a
source "$ENV_FILE"
set +a

# Check if API key is set
if [ -z "$OPENAI_API_KEY" ] && [ -z "$GROQ_API_KEY" ] && [ -z "$OLLAMA_BASE_URL" ]; then
    echo -e "${RED}Warning: No model backend configured${NC}"
    echo "Please set one of: OPENAI_API_KEY, GROQ_API_KEY, or OLLAMA_BASE_URL"
    echo ""
fi

# Check if API key looks like placeholder
if [ "$OPENAI_API_KEY" = "your-openai-api-key-here" ]; then
    echo -e "${RED}Warning: OPENAI_API_KEY appears to be a placeholder${NC}"
    echo "Please update it with your actual API key"
    echo ""
fi

echo ""

# ----------------------------------------------------
# Check Available Resources
# ----------------------------------------------------
echo -e "${YELLOW}Checking system resources...${NC}"

# Get available memory (in GB)
if [[ "$OSTYPE" == "darwin"* ]]; then
    # macOS
    TOTAL_MEM=$(sysctl -n hw.memsize | awk '{print int($1/1024/1024/1024)}')
else
    # Linux
    TOTAL_MEM=$(free -g | awk '/^Mem:/{print $2}')
fi

echo "Total system memory: ${TOTAL_MEM}GB"

if [ "$TOTAL_MEM" -lt 8 ]; then
    echo -e "${YELLOW}Warning: System has less than 8GB RAM${NC}"
    echo "The pipeline requires at least 4GB for Elasticsearch and 2GB for DeepResearch"
    echo ""
fi

# Check disk space
AVAILABLE_DISK=$(df -h "$PROJECT_DIR" | awk 'NR==2 {print $4}')
echo "Available disk space: $AVAILABLE_DISK"

echo ""

# ----------------------------------------------------
# Pull Required Images
# ----------------------------------------------------
echo -e "${YELLOW}Pulling required Docker images...${NC}"
echo "This may take a few minutes on first run..."
echo ""

cd "$PROJECT_DIR"

if docker compose pull; then
    echo -e "${GREEN}✓ Successfully pulled all images${NC}"
else
    echo -e "${RED}Warning: Some images could not be pulled${NC}"
    echo "They will be built during the first startup"
fi

echo ""

# ----------------------------------------------------
# Check Python Dependencies
# ----------------------------------------------------
echo -e "${YELLOW}Checking Python dependencies for indexing...${NC}"

REQUIRED_PACKAGES="elasticsearch sentence-transformers"
MISSING_PACKAGES=""

for package in $REQUIRED_PACKAGES; do
    if ! python3 -c "import ${package//-/_}" &> /dev/null 2>&1; then
        MISSING_PACKAGES="$MISSING_PACKAGES $package"
    fi
done

if [ -n "$MISSING_PACKAGES" ]; then
    echo -e "${YELLOW}Missing Python packages:$MISSING_PACKAGES${NC}"
    echo ""
    echo "These are needed for indexing. You can install them with:"
    echo "  pip3 install$MISSING_PACKAGES"
    echo ""
else
    echo -e "${GREEN}✓ All required Python packages installed${NC}"
fi

echo ""

# ----------------------------------------------------
# Setup Complete
# ----------------------------------------------------
echo -e "${GREEN}========================================${NC}"
echo -e "${GREEN}Setup Complete!${NC}"
echo -e "${GREEN}========================================${NC}"
echo ""
echo -e "Next steps:"
echo ""
echo -e "1. ${BLUE}Review your configuration:${NC}"
echo "   cat .env"
echo ""
echo -e "2. ${BLUE}Run the full demo workflow:${NC}"
echo "   ./scripts/run_demo.sh"
echo ""
echo -e "   Or manually:"
echo ""
echo -e "3. ${BLUE}Start Elasticsearch:${NC}"
echo "   docker compose up -d elasticsearch"
echo ""
echo -e "4. ${BLUE}Index the demo data:${NC}"
echo "   ./scripts/index_confluence.sh"
echo ""
echo -e "5. ${BLUE}Start DeepResearch API:${NC}"
echo "   docker compose up -d deepresearch-api"
echo ""
echo -e "6. ${BLUE}Start LangGraph (optional):${NC}"
echo "   ./scripts/start_langgraph.sh"
echo ""
echo -e "For more information, see: ${BLUE}README.md${NC}"
echo ""
