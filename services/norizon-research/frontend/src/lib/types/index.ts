// ============================================================================
// Core Types
// ============================================================================

export interface Message {
	id: string;
	role: 'user' | 'assistant' | 'system';
	content: string;
	timestamp: number;
	sources?: Source[];
	isStreaming?: boolean;
	// New: Progress tracking during search
	progress?: SearchProgress;
	// New: Active agent for dynamic badge
	activeAgent?: string;
	// New: Confidence score from backend
	confidence?: number;
	// New: Job ID for reference
	jobId?: string;
	// New: Persisted agent iterations for reference after completion
	agentIterations?: AgentIteration[];
}

export interface Source {
	id: string;
	title: string;
	url: string;
	snippet: string;
	relevance?: number;
	// New: Source type for icons
	sourceType?: 'sharepoint' | 'confluence' | 'wiki' | 'web' | 'elasticsearch' | 'unknown';
	// New: Last updated date
	lastUpdated?: string;
	// New: Status for UI feedback
	status?: 'checking' | 'checked' | 'indexed';
}

// ============================================================================
// Chat Context Types (for workflow → chat handoff)
// ============================================================================

export type ChatContextType = 'meeting-protocol' | 'document' | null;

export type ChatContextAction = 'email' | 'status' | 'chat' | 'meeting';

export interface ChatContext {
	type: ChatContextType;
	jobId: string;
	action: ChatContextAction;
	protocol?: Protocol;
	loadedAt: number;
}

export interface ChatSession {
	id: string;
	title: string;
	messages: Message[];
	createdAt: number;
	updatedAt: number;
	context?: ChatContext;
	workflowType?: string;
}

// ============================================================================
// Search Progress Types
// ============================================================================

export interface AgentIteration {
	iterationNumber: number;
	agentName: string;
	searchQuery?: string;
	status: 'searching' | 'done' | 'thinking';
	resultsCount?: number;
	displayName?: string;
	iconUrl?: string;
	// For thinking steps
	thinkingMessage?: string;
	// Configurable labels from agents.yaml
	searchingLabel?: string;
	itemLabel?: string;
}

export interface SearchProgress {
	phase: string;
	message: string;
	currentIteration?: number;
	totalIterations?: number;
	toolsCalled?: string[];
	activeAgent?: string;
	// Per-agent iteration tracking
	agentIterations?: AgentIteration[];
	isComplete?: boolean;
	// True when supervisor is thinking (analyzing or generating report)
	isThinking?: boolean;
}

export interface AvailableSource {
	id: string;
	name: string;
	source_type: 'sharepoint' | 'confluence' | 'wiki' | 'jira' | 'web' | 'unknown';
	enabled: boolean;
}

// ============================================================================
// Citation Types (New for inline citations)
// ============================================================================

export interface Citation {
	index: number;
	sourceId: string;
	source: Source;
	excerpt?: string;
}

// ============================================================================
// API Types (Updated for new backend)
// ============================================================================

export interface ResearchQuery {
	query: string;
	sessionId?: string;
	maxIterations?: number;
	executionStrategy?: 'iterative' | 'parallel';
}

export interface ResearchResponse {
	jobId: string;
	answer: string;
	report?: string;
	sources: Source[];
	confidence: number;
	iterations: number;
	processingTimeMs: number;
	timestamp: number;
}

// ============================================================================
// Stream Event Types (New for SSE)
// ============================================================================

export type StreamEventType = 'progress' | 'iteration' | 'complete' | 'error' | 'keepalive';

export interface StreamChunk {
	type: StreamEventType;
	data: unknown;
}

export interface ProgressEvent {
	type: 'progress';
	phase: string;
	message: string;
}

export interface IterationEvent {
	type: 'iteration';
	iterationNumber: number;
	toolsCalled: string[];
	decision?: 'CONTINUE' | 'COMPLETE';
}

export interface CompleteEvent {
	type: 'complete';
	result: ResearchResponse;
}

export interface ErrorEvent {
	type: 'error';
	error: string;
	detail?: string;
}

// ============================================================================
// UI State Types (New)
// ============================================================================

export interface DateGroup {
	label: string;
	sessions: ChatSession[];
}

export interface MessageAction {
	id: string;
	icon: string;
	label: string;
	action: () => void;
}

// ============================================================================
// Export Types (New for client-side export)
// ============================================================================

export interface ExportOptions {
	format: 'pdf' | 'docx';
	includeMetadata?: boolean;
	includeSources?: boolean;
}

// ============================================================================
// Workflow Types (Meeting Documentation)
// ============================================================================

export type WorkflowStep = 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9;

export type WorkflowStatus = 'pending' | 'processing' | 'completed' | 'failed';

export interface WorkflowJob {
	id: string;
	type: 'meeting';
	status: WorkflowStatus;
	currentStep: WorkflowStep;
	createdAt: number;
	updatedAt: number;
}

export interface WorkflowFile {
	name: string;
	size: number;
	type: string;
	duration?: number;
	url?: string;
	lastModified?: number;
}

export interface ProcessingStage {
	id: string;
	label: string;
	status: 'pending' | 'processing' | 'completed' | 'failed';
}

export interface ProcessingInsight {
	timestamp: string; // "[00:42]"
	message: string; // "3 unique voice profiles detected"
}

export interface WorkflowProcessingProgress {
	stage: string;
	percent: number;
	message: string;
	stages?: ProcessingStage[];
	insights?: ProcessingInsight[]; // Live insight feed entries
	detectedKeywords?: string[]; // Keywords detected during processing
}

export interface Speaker {
	id: string;
	detectedName: string;
	confirmedName: string;
	sampleAudioUrl?: string;
	speakingTime?: number;
	// Enterprise features
	transcriptSnippet?: string; // First ~10 words of speaker's speech
	confidence?: number; // AI confidence in speaker identification (0-100)
	isExternal?: boolean; // Mark as external partner/guest
	waveformData?: number[]; // Normalized audio waveform for visualization
	hint?: string; // Contextual role label from inference (e.g. "host", "audience (Nottingham)")
}

export interface ActionItem {
	id: string;
	text: string;
	assignee?: string;
	dueDate?: string;
	completed: boolean;
}

// Meeting Templates
export interface MeetingTemplate {
	id: string;
	name: string;
	description: string;
	icon: string;
	category: 'internal' | 'external' | 'project';
	// Structure modifications this template applies
	structure: {
		suggestedTitle?: string;
		customSections?: TemplateSection[];
		actionItemDefaults?: Partial<ActionItem>[];
	};
}

export interface TemplateSection {
	id: string;
	label: string;
	type: 'textarea' | 'list' | 'text';
	placeholder?: string;
	defaultValue?: string;
}

export interface TemplateSuggestion {
	templateId: string;
	confidence: number;
	reason: string;
}

export interface UserSuggestion {
	id: string;
	name: string;
	email: string;
	department?: string;
}

export interface TranscriptSegment {
	id: string;
	speakerId: string;      // Links to Speaker.id
	speakerName: string;    // Display name (can be edited)
	startTime: number;      // Seconds
	endTime: number;        // Seconds
	text: string;           // The spoken content
}

export interface CustomSection {
	id: string;
	label: string;
	type: 'text' | 'list';
	content: string | string[];  // string for text type, string[] for list type
}

export interface Protocol {
	title: string;
	date: string;
	attendees: string[];
	executiveSummary: string;
	actionItems: ActionItem[];
	fullTranscript: string;  // Keep for backwards compat
	transcriptSegments?: TranscriptSegment[];  // New structured format
	decisions?: string[];
	nextSteps?: string[];
	templateId?: string;  // Selected template ID
	customSections?: CustomSection[];  // Template-specific sections
}

export type PostAction = 'email' | 'meeting' | 'status' | 'chat';

export interface WorkflowState {
	jobId: string;
	currentStep: WorkflowStep;
	file: WorkflowFile | null;
	processingProgress: WorkflowProcessingProgress | null;
	speakers: Speaker[];
	protocol: Protocol | null;
	selectedPostAction: PostAction | null;
	confluenceUrl?: string;
	// Protocol editing state
	isProtocolSaved?: boolean;  // True after user clicks "Save & Continue"
	historyId?: string;  // Database history record ID (for updates instead of duplicates)
	suggestedTemplateId?: string;  // AI-suggested template based on transcript
	// Destination selection (moved to Step 1)
	destinationSpaceId?: string;
	destinationParentPageId?: string;
	// Processing completion state (for back navigation)
	processingComplete?: boolean;
}
