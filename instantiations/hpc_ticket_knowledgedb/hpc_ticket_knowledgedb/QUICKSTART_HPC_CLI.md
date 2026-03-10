# HPC CLI - Quick Start Guide

## Installation (Already Done!)

The HPC CLI has been installed in editable mode. You can now use the `hpc` command.

## Verify Installation

```bash
# Check version
hpc version

# Check system health
hpc doctor

# View configuration
hpc config show
```

## Basic Usage

### 1. Start Interactive Chat (Main Feature!)

```bash
# Launch the Claude Code-like chat interface
hpc

# Or explicitly
hpc chat
```

**Keyboard Shortcuts:**
- `Ctrl+Enter` - Send message
- `Shift+Enter` - New line
- `Ctrl+Q` - Quit
- `Ctrl+L` - Clear chat
- `Ctrl+B` - Toggle brief mode

**Slash Commands:**
- `/help` - Show commands
- `/clear` - Clear history
- `/gpu` - GPU status (coming soon)
- `/dr <query>` - Deep research (coming soon)

### 2. Configuration

```bash
# Initialize config file (already done)
hpc config init

# View current configuration
hpc config show

# Set LLM endpoint (if different)
hpc config set llm.url "http://your-llm:port/v1"

# Set ClusterCockpit JWT
hpc config set clustercockpit.jwt "YOUR_JWT_TOKEN"
```

### 3. Available Commands

```bash
# Chat mode (default)
hpc chat
hpc chat "How do I submit a SLURM job?"

# Deep research (coming soon)
hpc research "GPU performance optimization"
hpc research "MPI best practices" --detailed

# Cluster monitoring (coming soon)
hpc cluster gpu-usage --days 7
hpc cluster worst-users --days 30

# Configuration
hpc config show
hpc config set <key> <value>
hpc config path

# System
hpc version
hpc doctor
```

## Current Status

### ✅ Implemented (MVP Phase 1)
- **Interactive Chat UI** - Full Claude Code-like interface with Textual
- **Message Bubbles** - User and assistant messages with timestamps
- **Streaming Responses** - Real-time typewriter effect
- **Multi-line Input** - Ctrl+Enter to send, Shift+Enter for new lines
- **Markdown Rendering** - Rich text formatting with code highlighting
- **Session Management** - Save/load conversations with `/save` and `/load`
- **Configuration System** - TOML config + environment variables + keyring
- **LLM Client** - OpenAI-compatible streaming client
- **CLI Framework** - Click-based with subcommands
- **Health Checks** - `hpc doctor` to verify system status

### ⚠️ Coming Soon (Phases 2-3)
- **Deep Research Integration** - Multi-agent research with Elasticsearch
- **Cluster Monitoring** - GPU utilization tracking
- **Tool Calling Framework** - LLM can invoke DR and cluster tools
- **Advanced Features** - Tool visualization, progress indicators

## Testing the Chat UI

### Option 1: Test with a Real LLM

If you have access to the GPT-OSS endpoint:

```bash
# It's already configured! Just run:
hpc chat
```

Then type any HPC question and see the response stream in real-time.

### Option 2: Configure a Different LLM

If you want to use Ollama or another endpoint:

```bash
# Set your endpoint
hpc config set llm.url "http://localhost:11434/v1"
hpc config set llm.model "llama3"

# Start chat
hpc chat
```

## Example Session

```bash
$ hpc chat

╭─────────────────────────────────────────────────────────────╮
│ HPC Assistant                         v0.1.0  [Ctrl+Q] Quit │
├─────────────────────────────────────────────────────────────┤
│                           🤖 HPC Assistant                   │
│                                                              │
│                  Welcome! I can help you with:               │
│                  • SLURM job submission                      │
│                  • GPU cluster monitoring                    │
│                  • Deep research on HPC topics               │
│                                                              │
│                  Type your question below!                   │
├─────────────────────────────────────────────────────────────┤
│ ▶ Type your message... (Ctrl+Enter to send)                 │
│ [Send] Ctrl+Enter  [Brief: OFF]              Session: 0 msgs│
└─────────────────────────────────────────────────────────────┘

> How do I submit a GPU job with 4 GPUs?

[Assistant streams response with code examples...]
```

## File Structure

Key files created:

```
hpc_cli/
├── __init__.py               ✅ Package initialization
├── version.py                ✅ Version info
├── cli.py                    ✅ Main CLI with Click
├── config.py                 ✅ Configuration management
│
├── ui/                       ✅ Textual chat interface
│   ├── app.py                ✅ Main Textual application
│   ├── widgets/
│   │   ├── message_bubble.py ✅ User/Assistant messages
│   │   ├── chat_container.py ✅ Scrollable chat area
│   │   ├── input_area.py     ✅ Multi-line input
│   │   ├── status_bar.py     ✅ Status indicators
│   │   └── welcome_screen.py ✅ Initial screen
│   └── styles/
│       └── chat.tcss         ✅ Textual CSS styling
│
├── agents/                   ✅ LLM integration
│   ├── llm_client.py         ✅ Streaming LLM client
│   └── chat_agent.py         ✅ Chat orchestration
│
├── dr/                       ⚠️  Stubs (to be implemented)
│   └── integration.py        ⚠️  DR integration
│
└── cluster/                  ⚠️  Stubs (to be implemented)
    └── commands.py           ⚠️  Cluster monitoring

pyproject.toml                ✅ Package config
README_HPC_CLI.md             ✅ Full documentation
QUICKSTART_HPC_CLI.md         ✅ This file
```

## Next Steps

### For Development

1. **Test the Chat UI** - Try it with the LLM endpoint
2. **Integrate DR Pipeline** - Connect existing deep research code
3. **Add Cluster Tools** - Integrate ClusterCockpit monitoring
4. **Implement Tool Calling** - Let LLM invoke tools automatically

### For Production Use

1. **Configure Your Environment**
   ```bash
   hpc config set llm.url "YOUR_LLM_URL"
   hpc config set elasticsearch.url "YOUR_ES_URL"
   hpc config set clustercockpit.jwt "YOUR_JWT"
   ```

2. **Test Connections**
   ```bash
   hpc doctor
   ```

3. **Start Using**
   ```bash
   hpc chat
   ```

## Troubleshooting

### Chat UI won't start

```bash
# Check if Textual is installed
python -c "import textual; print('Textual OK')"

# Re-install if needed
pip install -e .
```

### LLM connection errors

```bash
# Test endpoint manually
curl http://lme49.cs.fau.de:30000/v1/models

# Check config
hpc config show

# Verify system health
hpc doctor
```

### Import errors

```bash
# Make sure you're in the right directory
cd /Users/lisaschmidt/Documents/GitHub/rag-server/products/hpc_ticket_knowledgedb

# Reinstall
pip install -e .
```

## Support

For questions or issues:
- Check `README_HPC_CLI.md` for full documentation
- Run `hpc --help` for command reference
- Use `hpc doctor` to diagnose issues
- Contact the HPC support team

## What's Working Right Now

1. ✅ **Beautiful Chat UI** - Full Claude Code-like interface
2. ✅ **Streaming Responses** - Real-time typewriter effect
3. ✅ **Keyboard Shortcuts** - Ctrl+Enter, Ctrl+Q, etc.
4. ✅ **Configuration** - Easy config management
5. ✅ **Session Save/Load** - Export/import conversations
6. ✅ **Health Checks** - Verify all connections
7. ✅ **Markdown Rendering** - Code blocks, formatting

Try it now: `hpc chat`
