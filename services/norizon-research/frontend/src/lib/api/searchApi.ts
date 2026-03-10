/**
 * Search API Client for custom-deepresearch backend
 * Implements two-phase flow: start job → stream events
 */

// ============================================================================
// Type Definitions
// ============================================================================

/**
 * A message in the conversation history for context.
 * Used to enable follow-up questions that reference previous messages.
 */
export interface ConversationMessage {
  role: 'user' | 'assistant';
  content: string;
  sources?: string[];  // Source titles for assistant messages
}

export interface SearchRequest {
  query: string;
  conversation_history?: ConversationMessage[];
  document_context?: string;  // Additional context (e.g., meeting protocol) to include in search
  max_iterations?: number;
  execution_strategy?: 'iterative' | 'parallel';
}

export interface JobResponse {
  job_id: string;
  status: 'pending' | 'running' | 'completed' | 'failed';
  created_at: string;
}

export interface SourceReference {
  id: string;
  title: string;
  url: string | null;
  score: number;
  source_type?: string | null;
  snippet?: string | null;
}

export interface FindingSummary {
  source_type: string;
  source_name: string;
  confidence: number;
  sources_count: number;
  success: boolean;
}

export interface IterationSummary {
  iteration_number: number;
  tools_called: string[];
  findings_count: number;
  findings: FindingSummary[];
  decision: string | null;
}

export interface SearchResult {
  job_id: string;
  status: string;
  query: string;
  final_report: string;
  concise_answer: string;
  confidence_score: number;
  total_iterations: number;
  processing_time_ms: number;
  sources: SourceReference[];
  iterations: IterationSummary[];
  created_at: string;
  completed_at: string | null;
}

export interface ToolInfo {
  name: string;
  type: string;
  description: string;
  enabled: boolean;
}

export interface HealthResponse {
  status: string;
  llm: { status: string; provider: string; model: string };
  tools: number;
  supervisor: string;
}

// Source search status types for per-source progress tracking
export interface SourceSearchStatusBackend {
  id: string;
  name: string;
  status: 'waiting' | 'searching' | 'done';
  count: number;
  source_type: string;
}

export interface AvailableSourceBackend {
  id: string;
  name: string;
  source_type: string;
  enabled: boolean;
}

export interface SourcesResponse {
  sources: AvailableSourceBackend[];
}

// SSE Event types emitted during streaming
export type StreamEvent =
  | { type: 'progress'; phase: string; message: string; sourcesStatus?: SourceSearchStatusBackend[]; extra?: Record<string, unknown> }
  | { type: 'iteration'; iteration_number: number; tools_called: string[]; decision?: string }
  | { type: 'agent_status'; iteration_number: number; agent_name: string; status: 'searching' | 'done'; search_query?: string; results_count?: number; display_name?: string; icon_url?: string; searching_label?: string; item_label?: string }
  | { type: 'report_chunk'; content: string }
  | { type: 'complete'; result: SearchResult }
  | { type: 'error'; error: string; detail?: string }
  | { type: 'keepalive' };

// ============================================================================
// API Client
// ============================================================================

/**
 * Get the appropriate API base URL based on the runtime environment.
 * - Browser (client-side): Uses VITE_API_BASE_URL (typically http://localhost:8000/api/v1)
 * - SSR (server-side in container): Uses VITE_SSR_API_BASE_URL (typically http://deepsearch:8000/api/v1)
 */
function getBaseUrl(): string {
  const isBrowser = typeof window !== 'undefined';

  if (isBrowser) {
    // Client-side: use the browser-accessible URL
    return import.meta.env.VITE_API_BASE_URL || 'http://localhost:8000/api/v1';
  } else {
    // Server-side (SSR): use the internal Docker network URL
    return import.meta.env.VITE_SSR_API_BASE_URL || import.meta.env.VITE_API_BASE_URL || 'http://deepsearch:8000/api/v1';
  }
}

export class SearchAPI {
  private static get baseUrl(): string {
    return getBaseUrl();
  }

  /**
   * Start a search job
   * @param request - Search parameters
   * @returns Job info with job_id
   */
  static async startSearch(request: SearchRequest): Promise<JobResponse> {
    const response = await fetch(`${this.baseUrl}/search`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(request),
    });

    if (!response.ok) {
      const error = await response.json().catch(() => ({ detail: response.statusText }));
      throw new Error(error.detail || `Failed to start search: ${response.status}`);
    }

    return response.json();
  }

  /**
   * Stream search progress via SSE
   * @param jobId - The job ID to stream
   * @yields StreamEvent objects as they arrive
   */
  static async *streamSearch(jobId: string): AsyncGenerator<StreamEvent> {
    const response = await fetch(`${this.baseUrl}/search/${jobId}/stream`, {
      headers: {
        'Accept': 'text/event-stream',
      },
    });

    if (!response.ok) {
      throw new Error(`Failed to connect to stream: ${response.status}`);
    }

    if (!response.body) {
      throw new Error('Response body is null');
    }

    const reader = response.body.getReader();
    const decoder = new TextDecoder();
    let buffer = '';
    let currentEvent = '';
    let currentData = '';

    try {
      while (true) {
        const { done, value } = await reader.read();
        if (done) break;

        buffer += decoder.decode(value, { stream: true });
        const lines = buffer.split('\n');
        buffer = lines.pop() || '';

        for (const line of lines) {
          if (line.startsWith('id: ')) {
            // Event ID - we can ignore this for now
            continue;
          } else if (line.startsWith('event: ')) {
            currentEvent = line.slice(7).trim();
          } else if (line.startsWith('data: ')) {
            currentData = line.slice(6);
          } else if (line === '' && currentEvent && currentData) {
            // End of SSE message - emit the event
            const event = this.parseEvent(currentEvent, currentData);
            yield event;

            // Reset for next event
            currentEvent = '';
            currentData = '';

            // Stop streaming after complete or error
            if (event.type === 'complete' || event.type === 'error') {
              return;
            }
          }
        }
      }
    } finally {
      reader.releaseLock();
    }
  }

  /**
   * Parse SSE event into typed StreamEvent
   */
  private static parseEvent(eventType: string, data: string): StreamEvent {
    try {
      const parsed = JSON.parse(data);

      switch (eventType) {
        case 'progress':
          return {
            type: 'progress',
            phase: parsed.phase || 'unknown',
            message: parsed.message || '',
            sourcesStatus: parsed.sources_status,
            extra: parsed,
          };

        case 'iteration':
          return {
            type: 'iteration',
            iteration_number: parsed.iteration_number,
            tools_called: parsed.tools_called || [],
            decision: parsed.decision,
          };

        case 'agent_status':
          return {
            type: 'agent_status',
            iteration_number: parsed.iteration_number,
            agent_name: parsed.agent_name,
            status: parsed.status,
            search_query: parsed.search_query,
            results_count: parsed.results_count,
            display_name: parsed.display_name,
            icon_url: parsed.icon_url,
            searching_label: parsed.searching_label,
            item_label: parsed.item_label,
          };

        case 'report_chunk':
          return {
            type: 'report_chunk',
            content: parsed.content || '',
          };

        case 'complete':
          return {
            type: 'complete',
            result: parsed,
          };

        case 'error':
          return {
            type: 'error',
            error: parsed.error || 'Unknown error',
            detail: parsed.detail,
          };

        case 'keepalive':
          return { type: 'keepalive' };

        default:
          console.warn(`Unknown SSE event type: ${eventType}`);
          return { type: 'keepalive' };
      }
    } catch (e) {
      console.error('Failed to parse SSE event:', e, { eventType, data });
      return {
        type: 'error',
        error: 'Failed to parse server response',
        detail: String(e),
      };
    }
  }

  /**
   * Get job status
   * @param jobId - The job ID to check
   */
  static async getStatus(jobId: string): Promise<{
    job_id: string;
    status: string;
    progress?: string;
    current_iteration?: number;
    created_at: string;
    updated_at?: string;
  }> {
    const response = await fetch(`${this.baseUrl}/search/${jobId}`);

    if (!response.ok) {
      throw new Error(`Failed to get status: ${response.status}`);
    }

    return response.json();
  }

  /**
   * Get final result (fallback if streaming fails)
   * @param jobId - The job ID to get result for
   */
  static async getResult(jobId: string): Promise<SearchResult> {
    const response = await fetch(`${this.baseUrl}/search/${jobId}/result`);

    if (!response.ok) {
      const error = await response.json().catch(() => ({ detail: response.statusText }));
      throw new Error(error.detail || `Failed to get result: ${response.status}`);
    }

    return response.json();
  }

  /**
   * Synchronous search (blocking)
   * Use this for simpler use cases where streaming isn't needed
   */
  static async searchSync(request: SearchRequest): Promise<SearchResult> {
    const response = await fetch(`${this.baseUrl}/search/sync`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(request),
    });

    if (!response.ok) {
      const error = await response.json().catch(() => ({ detail: response.statusText }));
      throw new Error(error.detail || `Search failed: ${response.status}`);
    }

    return response.json();
  }

  /**
   * Health check
   */
  static async healthCheck(): Promise<HealthResponse> {
    const response = await fetch(`${this.baseUrl}/health`);

    if (!response.ok) {
      throw new Error(`Health check failed: ${response.status}`);
    }

    return response.json();
  }

  /**
   * Check if backend is reachable
   */
  static async isHealthy(): Promise<boolean> {
    try {
      const health = await this.healthCheck();
      return health.status === 'healthy';
    } catch {
      return false;
    }
  }

  /**
   * Get available tools/agents
   */
  static async getTools(): Promise<ToolInfo[]> {
    const response = await fetch(`${this.baseUrl}/tools`);

    if (!response.ok) {
      throw new Error(`Failed to get tools: ${response.status}`);
    }

    const data = await response.json();
    return data.tools || [];
  }

  /**
   * Get available data sources for search
   * @returns List of available sources with their types and enabled status
   */
  static async getSources(): Promise<AvailableSourceBackend[]> {
    const response = await fetch(`${this.baseUrl}/sources`);

    if (!response.ok) {
      // Return empty array if endpoint not available yet (fallback)
      console.warn('Sources endpoint not available, using fallback');
      return [];
    }

    const data: SourcesResponse = await response.json();
    return data.sources || [];
  }
}

// ============================================================================
// Helper Functions
// ============================================================================

/**
 * Configuration for smart truncation of conversation history
 */
const HISTORY_CONFIG = {
  /** Number of recent message pairs to include in full */
  recentPairsInFull: 3,
  /** Max characters for user messages in older pairs */
  maxUserChars: 200,
  /** Max characters for assistant messages in older pairs */
  maxAssistantChars: 300,
  /** Approximate token budget for history (rough estimate: 4 chars per token) */
  tokenBudget: 4000,
};

/**
 * Build optimized conversation history from messages with smart truncation.
 * - Recent messages are included in full
 * - Older messages are truncated
 * - Only content and source titles are included (not full traces)
 *
 * @param messages - Array of messages from the session
 * @returns Array of ConversationMessage for the API
 */
export function buildConversationHistory(
  messages: Array<{ role: 'user' | 'assistant' | 'system'; content: string; sources?: Array<{ title: string }> }>
): ConversationMessage[] {
  // Filter to only user and assistant messages with content
  const relevantMessages = messages.filter(
    (m) => (m.role === 'user' || m.role === 'assistant') && m.content && m.content.trim()
  );

  if (relevantMessages.length === 0) {
    return [];
  }

  // Count message pairs (user + assistant = 1 pair)
  const pairCount = Math.ceil(relevantMessages.length / 2);
  const recentPairThreshold = Math.max(0, pairCount - HISTORY_CONFIG.recentPairsInFull);

  const history: ConversationMessage[] = [];
  let currentPair = 0;
  let totalChars = 0;

  for (let i = 0; i < relevantMessages.length; i++) {
    const msg = relevantMessages[i];

    // Track pairs (each user message starts a new pair)
    if (msg.role === 'user') {
      currentPair++;
    }

    const isRecent = currentPair > recentPairThreshold;
    let content = msg.content;

    // Apply truncation for older messages
    if (!isRecent) {
      const maxChars = msg.role === 'user'
        ? HISTORY_CONFIG.maxUserChars
        : HISTORY_CONFIG.maxAssistantChars;

      if (content.length > maxChars) {
        content = content.slice(0, maxChars) + '...';
      }
    }

    // Check token budget (rough estimate)
    const estimatedTokens = totalChars / 4;
    if (estimatedTokens > HISTORY_CONFIG.tokenBudget) {
      // Budget exceeded, stop adding older messages
      // But always include recent messages
      if (!isRecent) {
        continue;
      }
    }

    const historyItem: ConversationMessage = {
      role: msg.role as 'user' | 'assistant',
      content,
    };

    // Add source titles for assistant messages
    if (msg.role === 'assistant' && msg.sources && msg.sources.length > 0) {
      historyItem.sources = msg.sources.map((s) => s.title).slice(0, 10);
    }

    history.push(historyItem);
    totalChars += content.length;
  }

  return history;
}

/**
 * Convert SourceReference to the frontend Source type
 */
export function toFrontendSource(source: SourceReference): {
  id: string;
  title: string;
  url: string;
  snippet: string;
  relevance: number;
  sourceType?: 'sharepoint' | 'confluence' | 'wiki' | 'web' | 'elasticsearch' | 'unknown';
} {
  // Map backend source_type to frontend sourceType
  let sourceType: 'sharepoint' | 'confluence' | 'wiki' | 'web' | 'elasticsearch' | 'unknown' | undefined;
  if (source.source_type) {
    const st = source.source_type.toLowerCase();
    if (st === 'sharepoint') sourceType = 'sharepoint';
    else if (st === 'confluence') sourceType = 'confluence';
    else if (st === 'wiki') sourceType = 'wiki';
    else if (st === 'web' || st === 'websearch') sourceType = 'web';
    else if (st === 'elasticsearch' || st === 'docs' || st === 'tickets') sourceType = 'elasticsearch';
    else sourceType = 'unknown';
  }

  return {
    id: source.id,
    title: source.title,
    url: source.url || '',
    snippet: source.snippet || '',
    relevance: source.score,
    sourceType,
  };
}

/**
 * Extract active agent name from iteration data
 */
export function getActiveAgent(iteration: IterationSummary): string | null {
  if (iteration.findings.length > 0) {
    return iteration.findings[0].source_name;
  }
  if (iteration.tools_called.length > 0) {
    return iteration.tools_called[0];
  }
  return null;
}

/**
 * Convert backend source search status to frontend format
 */
export function toFrontendSourceStatus(
  source: SourceSearchStatusBackend
): {
  id: string;
  name: string;
  status: 'waiting' | 'searching' | 'done';
  count: number;
  sourceType: 'sharepoint' | 'confluence' | 'wiki' | 'jira' | 'web' | 'unknown';
} {
  let sourceType: 'sharepoint' | 'confluence' | 'wiki' | 'jira' | 'web' | 'unknown' = 'unknown';
  if (source.source_type) {
    const st = source.source_type.toLowerCase();
    if (st === 'sharepoint') sourceType = 'sharepoint';
    else if (st === 'confluence') sourceType = 'confluence';
    else if (st === 'wiki') sourceType = 'wiki';
    else if (st === 'jira') sourceType = 'jira';
    else if (st === 'web' || st === 'websearch') sourceType = 'web';
    else sourceType = 'unknown';
  }

  return {
    id: source.id,
    name: source.name,
    status: source.status,
    count: source.count,
    sourceType,
  };
}

/**
 * Convert available source to initial source status (waiting state)
 */
export function toInitialSourceStatus(
  source: AvailableSourceBackend
): {
  id: string;
  name: string;
  status: 'waiting';
  count: number;
  sourceType: 'sharepoint' | 'confluence' | 'wiki' | 'jira' | 'web' | 'unknown';
} {
  let sourceType: 'sharepoint' | 'confluence' | 'wiki' | 'jira' | 'web' | 'unknown' = 'unknown';
  if (source.source_type) {
    const st = source.source_type.toLowerCase();
    if (st === 'sharepoint') sourceType = 'sharepoint';
    else if (st === 'confluence') sourceType = 'confluence';
    else if (st === 'wiki') sourceType = 'wiki';
    else if (st === 'jira') sourceType = 'jira';
    else if (st === 'web' || st === 'websearch') sourceType = 'web';
    else sourceType = 'unknown';
  }

  return {
    id: source.id,
    name: source.name,
    status: 'waiting',
    count: 0,
    sourceType,
  };
}
