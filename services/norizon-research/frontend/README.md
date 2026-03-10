# Nora Frontend

Modern SvelteKit-based frontend for Nora - the DeepSearch-powered knowledge assistant.

## Tech Stack

- **SvelteKit 2.0** - Full-stack framework
- **TypeScript** - Type-safe development
- **Tailwind CSS** - Utility-first styling
- **Marked** - Markdown rendering
- **Vite** - Build tool

## Project Structure

```
frontend/
├── src/
│   ├── lib/
│   │   ├── components/         # Svelte components (14 total)
│   │   │   ├── NoraLayout.svelte       # Main app layout wrapper
│   │   │   ├── Sidebar.svelte          # Session history sidebar
│   │   │   ├── ChatHeader.svelte       # Chat header with actions
│   │   │   ├── ChatMessage.svelte      # Message display with markdown
│   │   │   ├── ChatInput.svelte        # Message input with auto-resize
│   │   │   ├── SearchProgress.svelte   # Real-time agent progress tracking
│   │   │   ├── SourcesSummary.svelte   # Sources panel header
│   │   │   ├── SourceCard.svelte       # Source citation card
│   │   │   ├── SourceFlipCard.svelte   # Animated source card variant
│   │   │   ├── InlineCitation.svelte   # Numbered inline citations
│   │   │   ├── MessageActions.svelte   # Copy/export message actions
│   │   │   ├── TwoPanelLayout.svelte   # Two-column responsive layout
│   │   │   ├── ThreeColumnLayout.svelte # Three-column layout variant
│   │   │   └── SkeletonLoading.svelte  # Loading placeholders
│   │   ├── stores/
│   │   │   ├── chatStore.ts    # Session & message state
│   │   │   └── configStore.ts  # App configuration
│   │   ├── api/
│   │   │   └── searchApi.ts    # DeepSearch API client
│   │   ├── types/
│   │   │   └── index.ts        # TypeScript interfaces
│   │   ├── i18n/
│   │   │   └── index.ts        # Internationalization
│   │   └── utils/
│   │       └── index.ts        # Utility functions
│   ├── routes/
│   │   ├── +layout.svelte
│   │   ├── +page.svelte
│   │   └── chat/[sessionId]/
│   │       └── +page.svelte
│   └── app.css
├── static/
├── Dockerfile
├── Dockerfile.dev
└── package.json
```

## Development

```bash
# Install dependencies
npm install

# Configure environment
cp .env.example .env

# Start dev server (http://localhost:5173)
npm run dev
```

### Scripts

| Command | Description |
|---------|-------------|
| `npm run dev` | Development server |
| `npm run build` | Production build |
| `npm run preview` | Preview production build |
| `npm run check` | TypeScript checking |
| `npm run lint` | Lint code |
| `npm run format` | Format with Prettier |

## Configuration

### Environment Variables

```env
# API endpoints
VITE_API_BASE_URL=http://localhost:8000/api/v1
VITE_SSR_API_BASE_URL=http://deepsearch:8000/api/v1

# App settings
VITE_APP_TITLE=Nora
VITE_APP_DESCRIPTION=Knowledge Search Assistant

# Feature flags
VITE_ENABLE_SHARE=true
VITE_ENABLE_EXPORT=true
```

### API Integration

The frontend connects to DeepSearch on port **8000**:
- **Browser requests**: `VITE_API_BASE_URL`
- **SSR requests** (Docker): `VITE_SSR_API_BASE_URL` using service name

## Key Components

### SearchProgress
Real-time visualization of agent iterations during search. Shows:
- Current search phase with icons
- Agent names and status (waiting/searching/done)
- Iteration count and progress

### Sidebar
Session history management:
- List of past sessions with timestamps
- New session creation
- Session deletion
- localStorage persistence

### InlineCitation
Numbered reference markers `[1]` that link to sources. Hover for preview.

### ChatMessage
Message display with:
- Markdown rendering via Marked
- Inline source citations
- Streaming indicator
- User/assistant avatars

See `src/lib/components/` for full implementation details.

## Features

### SSE Streaming
Real-time updates via Server-Sent Events. Event types:
- `progress` - Search phase updates
- `iteration` - Agent iteration tracking
- `agent_status` - Individual agent status
- `report_chunk` - Streaming response text
- `complete` - Final result with sources
- `error` - Error handling

See `src/lib/api/searchApi.ts` for streaming implementation.

### Session Management
- URL-based routing: `/chat/[sessionId]`
- localStorage persistence
- Conversation history sent with requests
- Smart truncation for context limits

### Export
Dispatches events for PDF/Word/SharePoint export integration.
See `MessageActions.svelte` for implementation.

## Type System

Key interfaces in `src/lib/types/index.ts`:

| Interface | Purpose |
|-----------|---------|
| `Message` | Chat message with role, content, sources |
| `ChatSession` | Session with messages and metadata |
| `Source` | Citation with title, url, snippet, score |
| `SearchProgress` | Real-time search status |
| `AgentIteration` | Agent execution tracking |
| `StreamEvent` | Union type for SSE events |

## Styling

### Norizon Colors
```css
--norizon-orange: #ff6b35;
--norizon-blue: #3b82f6;
```

Configured in `tailwind.config.js`. See root `CLAUDE.md` for full design system.

## Docker

```bash
# Production
docker build -t nora-frontend .
docker run -p 3000:3000 nora-frontend

# Development
docker build -f Dockerfile.dev -t nora-frontend-dev .
```

## Debugging

```bash
# Clear build cache
rm -rf .svelte-kit node_modules && npm install

# Type check
npm run check

# Check API connection
curl http://localhost:8000/api/v1/health
```

Enable verbose logging in browser console:
```javascript
localStorage.debug = '*'
```

## License

Proprietary - Norizon GbR
