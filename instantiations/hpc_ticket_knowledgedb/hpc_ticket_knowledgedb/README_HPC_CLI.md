# HPC CLI - AI-Powered HPC Support Tool

A unified command-line interface for HPC support featuring:
- 🤖 **Interactive Chat UI** - Claude Code-like terminal interface
- 🔬 **Deep Research** - Multi-agent research system for complex HPC questions
- 📊 **Cluster Monitoring** - GPU utilization tracking via ClusterCockpit

## Features

### Interactive Chat Interface
Beautiful Textual-based chat UI that looks and feels like Claude Code:
- Scrollable conversation history with message bubbles
- Streaming responses with typewriter effect
- Multi-line input (Ctrl+Enter to send)
- Markdown rendering with syntax-highlighted code blocks
- Session save/load functionality
- Tool execution visualization

### Deep Research Mode
Multi-iteration research pipeline that:
- Queries Elasticsearch knowledge bases (docs + tickets)
- Uses multiple research agents for comprehensive analysis
- Validates assumptions and assesses answer quality
- Iterates up to 3 times until confidence thresholds are met

### Cluster Monitoring
Direct access to ClusterCockpit data:
- Find underutilized GPU jobs
- Rank users by GPU waste
- Job statistics and analytics

## Installation

### Prerequisites
- Python 3.10 or higher
- Access to LLM endpoint (e.g., GPT-OSS, Ollama, OpenAI)
- Optional: Elasticsearch instance (for Deep Research)
- Optional: ClusterCockpit JWT token (for monitoring)

### Install from Source

```bash
# Clone repository
cd /path/to/hpc_ticket_knowledgedb

# Install in editable mode
pip install -e .

# Initialize configuration
hpc config init
```

### Configure

```bash
# Set LLM endpoint
hpc config set llm.url "http://your-llm-endpoint:port/v1"
hpc config set llm.model "openai/gpt-oss-120b"

# Set Elasticsearch (for Deep Research)
hpc config set elasticsearch.url "http://localhost:9200"

# Set ClusterCockpit JWT (for monitoring)
hpc config set clustercockpit.jwt "YOUR_JWT_TOKEN"
```

### Verify Installation

```bash
# Check system health
hpc doctor

# Show configuration
hpc config show
```

## Usage

### Interactive Chat (Default)

```bash
# Start chat UI
hpc

# Or explicitly
hpc chat

# Start with initial query
hpc chat "How do I submit a SLURM job?"
```

### Chat Interface

```
╭─────────────────────────────────────────────────────────────╮
│ HPC Assistant                         v0.1.0  [Ctrl+Q] Quit │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│ ┌─ You ──────────────────────────────── 14:32:15 ─────────┐ │
│ │ How do I submit a GPU job?                              │ │
│ └─────────────────────────────────────────────────────────┘ │
│                                                              │
│ ┌─ Assistant ────────────────────────── 14:32:18 ─────────┐ │
│ │ To submit a GPU job, use sbatch with --gres=gpu:4       │ │
│ │                                                          │ │
│ │ ┌─ SLURM Script ──────────────────────────────────────┐ │ │
│ │ │ #!/bin/bash                                         │ │ │
│ │ │ #SBATCH --gres=gpu:4                                │ │ │
│ │ │ python train.py                                     │ │ │
│ │ └─────────────────────────────────────────────────────┘ │ │
│ └─────────────────────────────────────────────────────────┘ │
│                                                          ↓ 2/2│
├─────────────────────────────────────────────────────────────┤
│ ▶ Type your message... (Ctrl+Enter to send)                 │
│ [Send] Ctrl+Enter  [Brief: OFF]              Session: 2 msgs│
└─────────────────────────────────────────────────────────────┘
```

### Keyboard Shortcuts

| Shortcut | Action |
|----------|--------|
| `Ctrl+Enter` | Send message |
| `Shift+Enter` | New line in message |
| `Ctrl+Q` | Quit |
| `Ctrl+L` | Clear chat |
| `Ctrl+B` | Toggle brief mode |
| `Ctrl+S` | Save session |
| `Escape` | Cancel generation |

### Slash Commands

| Command | Description |
|---------|-------------|
| `/help` | Show available commands |
| `/clear` | Clear chat history |
| `/gpu` | Check GPU cluster status |
| `/dr <query>` | Deep research mode |
| `/save <file>` | Save conversation |
| `/load <file>` | Load conversation |

### Deep Research

```bash
# Research a complex HPC question
hpc research "Why is my GPU training slow?"

# Show detailed iterations and sources
hpc research "MPI+GPU best practices" --detailed

# Brief mode (concise answer only)
hpc research "SLURM job priorities" --brief
```

### Cluster Monitoring

```bash
# Find underutilized GPU jobs
hpc cluster gpu-usage --days 7 --max-util 70

# Export to JSON
hpc cluster gpu-usage --days 3 --output json --save report.json

# Rank users by GPU waste
hpc cluster worst-users --days 30 --top 20

# Export ranking
hpc cluster worst-users --output json --save waste-ranking.json
```

## Configuration

Configuration file location: `~/.config/hpc-cli/config.toml`

### Configuration Sections

**LLM:**
```toml
[llm]
url = "http://lme49.cs.fau.de:30000/v1"
model = "openai/gpt-oss-120b"
temperature = 0.2
max_tokens = 2000
api_key = "dummy"
```

**Elasticsearch:**
```toml
[elasticsearch]
url = "http://localhost:9200"
docs_index = "docs"
tickets_index = "tickets"
```

**Deep Research:**
```toml
[dr]
max_iterations = 3
confidence_threshold = 0.6
max_search_results = 10
```

**ClusterCockpit:**
```toml
[clustercockpit]
url = "https://monitoring.nhr.fau.de"
clusters = ["alex", "helma"]
```

### Environment Variables

Override config with environment variables:
```bash
export LLM_BASE_URL="http://localhost:11434/v1"
export LLM_MODEL="llama3"
export ELASTIC_URL="http://localhost:9200"
export CLUSTERCOCKPIT_JWT="your_jwt_token"
```

## Architecture

```
hpc-cli
├── Interactive Chat UI (Textual)
│   ├── Message bubbles (user/assistant)
│   ├── Streaming responses
│   └── Tool visualization
│
├── LLM Chat Agent
│   ├── Conversation management
│   ├── Tool calling framework
│   └── Streaming client
│
├── Deep Research Tool
│   ├── Multi-agent research
│   ├── Elasticsearch queries
│   └── Quality feedback loops
│
└── Cluster Monitoring Tools
    ├── ClusterCockpit API client
    ├── GPU utilization analysis
    └── User waste ranking
```

## Development

### Project Structure

```
hpc_cli/
├── __init__.py
├── version.py
├── cli.py                   # Click CLI commands
├── config.py                # Configuration management
│
├── ui/                      # Textual chat interface
│   ├── app.py               # Main Textual app
│   ├── widgets/             # UI components
│   ├── styles/              # Textual CSS
│   └── formatters/          # Markdown rendering
│
├── agents/                  # LLM chat agent
│   ├── llm_client.py        # Streaming LLM client
│   └── chat_agent.py        # Chat orchestration
│
├── tools/                   # Tool system
│   ├── base.py              # Tool framework
│   └── registry.py          # Tool discovery
│
├── dr/                      # Deep research
│   ├── workflow.py          # DR orchestration
│   └── integration.py       # CLI integration
│
└── cluster/                 # Cluster monitoring
    ├── client.py            # ClusterCockpit API
    └── commands.py          # CLI commands
```

### Running Tests

```bash
# Install dev dependencies
pip install -e ".[dev]"

# Run tests (when implemented)
pytest

# Type checking
mypy hpc_cli

# Code formatting
black hpc_cli
ruff check hpc_cli
```

## Troubleshooting

### LLM Connection Issues

```bash
# Check LLM endpoint
curl http://your-llm-endpoint:port/v1/models

# Verify configuration
hpc config show

# Test connection
hpc doctor
```

### Elasticsearch Not Reachable

```bash
# Check Elasticsearch
curl http://localhost:9200/_cluster/health

# Verify indices exist
curl http://localhost:9200/_cat/indices?v

# Update configuration
hpc config set elasticsearch.url "http://localhost:9200"
```

### ClusterCockpit Authentication

```bash
# Set JWT token (stored securely in keyring)
hpc config set clustercockpit.jwt "YOUR_JWT_TOKEN"

# Verify stored
hpc config show
```

## Known Limitations (MVP)

- ✅ Interactive chat UI with streaming - **IMPLEMENTED**
- ✅ LLM client with OpenAI-compatible API - **IMPLEMENTED**
- ✅ Configuration management - **IMPLEMENTED**
- ⚠️  Deep Research integration - **Coming soon**
- ⚠️  Cluster monitoring tools - **Coming soon**
- ⚠️  Tool calling framework - **Coming soon**
- ⚠️  Session persistence - **Basic implementation**

## Roadmap

### Phase 1: Foundation ✅
- [x] CLI framework with Click
- [x] Configuration system
- [x] Textual chat UI
- [x] LLM client integration
- [x] Basic streaming

### Phase 2: Deep Research (In Progress)
- [ ] Adapt DR_Pipeline code
- [ ] Fix global state issue
- [ ] Elasticsearch integration
- [ ] Progress streaming
- [ ] Quality indicators

### Phase 3: Cluster Monitoring (Planned)
- [ ] ClusterCockpit API client
- [ ] GPU utilization finder
- [ ] User waste ranking
- [ ] Output formatting (table/JSON/CSV)

### Phase 4: Tool Integration (Planned)
- [ ] Tool calling framework
- [ ] DR as LLM tool
- [ ] Cluster tools as LLM tools
- [ ] Natural language queries

## Contributing

This is an internal tool for the HPC support team. For questions or feature requests, contact the HPC team.

## License

MIT License - Copyright (c) 2024 HPC Team

## Acknowledgments

- Built with [Textual](https://github.com/Textualize/textual) for the beautiful terminal UI
- Inspired by [Claude Code](https://claude.ai/code) for the chat interface
- Integrates existing DR_Pipeline and ClusterCockpit monitoring systems
