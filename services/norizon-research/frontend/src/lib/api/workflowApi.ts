/**
 * Workflow API Client for Meeting Documentation workflow
 * Connects to the workflow-service backend
 */

import type {
	WorkflowJob,
	Speaker,
	Protocol,
	ActionItem,
	WorkflowProcessingProgress,
	MeetingTemplate,
	TemplateSuggestion,
	UserSuggestion
} from '$lib/types';

// ============================================================================
// Type Definitions
// ============================================================================

export interface CreateJobResponse {
	job_id: string;
	status: 'pending';
	created_at: string;
}

export interface UploadResponse {
	success: boolean;
	file_id: string;
	duration_seconds: number;
}

export interface TranscriptionEvent {
	type: 'progress' | 'complete' | 'error';
	stage?: string;
	percent?: number;
	message?: string;
	speakers?: Speaker[];
	transcript?: string;
	error?: string;
}

export interface SpeakersResponse {
	speakers: Speaker[];
}

export interface ProtocolResponse {
	protocol: Protocol;
}

export interface PublishResponse {
	success: boolean;
	confluence_url: string;
	page_id: string;
}

export interface TemplatesResponse {
	templates: MeetingTemplate[];
	suggestion?: TemplateSuggestion;
}

export interface UsersSearchResponse {
	users: UserSuggestion[];
}

export interface ConfluenceSpace {
	id: string;
	key: string;
	name: string;
	icon: string;
	type: string;
}

export interface ConfluencePage {
	id: string;
	title: string;
	parentId?: string;
	hasChildren: boolean;
}

export interface ConfluenceSpacesResponse {
	spaces: ConfluenceSpace[];
}

// Microsoft Teams Integration
export interface TeamsMeeting {
	id: string;
	subject: string;
	startDateTime: string;
	endDateTime: string;
	attendeeCount: number;
	hasRecording: boolean;
	recordingId?: string;
	organizerName?: string;
}

export interface TeamsMeetingsResponse {
	meetings: TeamsMeeting[];
	connected: boolean;
}

export interface TeamsAuthStatusResponse {
	connected: boolean;
	configured?: boolean;
	userName?: string;
	expiresAt?: string;
}

export interface TeamsImportResponse {
	success: boolean;
	file_id: string;
	duration_seconds: number;
}

export interface ConfluencePagesResponse {
	pages: ConfluencePage[];
}

// ============================================================================
// API Client
// ============================================================================

/**
 * Get the appropriate API base URL based on the runtime environment.
 */
function getBaseUrl(): string {
	return import.meta.env.VITE_WORKFLOW_API_URL || 'http://localhost:8001';
}

export class WorkflowAPI {
	/**
	 * Create a new workflow job
	 */
	static async createJob(): Promise<CreateJobResponse> {
		const response = await fetch(`${getBaseUrl()}/jobs`, {
			method: 'POST',
			headers: { 'Content-Type': 'application/json' }
		});

		if (!response.ok) {
			throw new Error(`Failed to create job: ${response.status}`);
		}

		return response.json();
	}

	/**
	 * Upload a file for transcription
	 */
	static async uploadFile(jobId: string, file: File): Promise<UploadResponse> {
		const formData = new FormData();
		formData.append('file', file);

		// Get current UI language from localStorage (de/en)
		const language = (typeof window !== 'undefined' && localStorage.getItem('locale')) || 'de';

		const response = await fetch(`${getBaseUrl()}/jobs/${jobId}/upload`, {
			method: 'POST',
			headers: {
				'X-Language': language
			},
			body: formData
		});

		if (!response.ok) {
			throw new Error(`Failed to upload file: ${response.status}`);
		}

		return response.json();
	}

	/**
	 * Stream transcription progress via SSE
	 */
	static async *streamTranscription(jobId: string): AsyncGenerator<TranscriptionEvent> {
		const response = await fetch(`${getBaseUrl()}/transcribe/${jobId}/stream`, {
			headers: { 'Accept': 'text/event-stream' }
		});

		if (!response.ok) {
			throw new Error(`Failed to connect to transcription stream: ${response.status}`);
		}

		if (!response.body) {
			throw new Error('Response body is null');
		}

		const reader = response.body.getReader();
		const decoder = new TextDecoder();
		let buffer = '';

		try {
			while (true) {
				const { done, value } = await reader.read();
				if (done) break;

				buffer += decoder.decode(value, { stream: true });
				const lines = buffer.split('\n');
				buffer = lines.pop() || '';

				for (const line of lines) {
					if (line.startsWith('data: ')) {
						try {
							const data = JSON.parse(line.slice(6));
							yield data as TranscriptionEvent;
							if (data.type === 'complete' || data.type === 'error') {
								return;
							}
						} catch (e) {
							console.error('Failed to parse SSE event:', e);
						}
					}
				}
			}
		} finally {
			reader.releaseLock();
		}
	}

	/**
	 * Get detected speakers for a job
	 */
	static async getSpeakers(jobId: string): Promise<SpeakersResponse> {
		const response = await fetch(`${getBaseUrl()}/jobs/${jobId}/speakers`);

		if (!response.ok) {
			throw new Error(`Failed to get speakers: ${response.status}`);
		}

		return response.json();
	}

	/**
	 * Update speaker names
	 */
	static async updateSpeakers(jobId: string, speakers: Speaker[]): Promise<void> {
		const response = await fetch(`${getBaseUrl()}/jobs/${jobId}/speakers`, {
			method: 'PUT',
			headers: { 'Content-Type': 'application/json' },
			body: JSON.stringify({ speakers })
		});

		if (!response.ok) {
			throw new Error(`Failed to update speakers: ${response.status}`);
		}
	}

	/**
	 * Generate protocol from transcription
	 */
	static async generateProtocol(jobId: string, templateId?: string): Promise<ProtocolResponse> {
		const response = await fetch(`${getBaseUrl()}/jobs/${jobId}/protocol`, {
			method: 'POST',
			headers: { 'Content-Type': 'application/json' },
			body: JSON.stringify({ templateId })
		});

		if (!response.ok) {
			throw new Error(`Failed to generate protocol: ${response.status}`);
		}

		return response.json();
	}

	/**
	 * Publish protocol to Confluence
	 */
	static async publishToConfluence(
		protocol: Protocol,
		spaceKey?: string,
		jobId?: string
	): Promise<PublishResponse> {
		const endpoint = jobId
			? `${getBaseUrl()}/jobs/${jobId}/publish`
			: `${getBaseUrl()}/publish`;

		const response = await fetch(endpoint, {
			method: 'POST',
			headers: { 'Content-Type': 'application/json' },
			body: JSON.stringify({ protocol, space_key: spaceKey })
		});

		if (!response.ok) {
			throw new Error(`Failed to publish to Confluence: ${response.status}`);
		}

		return response.json();
	}

	/**
	 * Export protocol to PDF
	 * Downloads the PDF file directly to the user's device
	 */
	static async exportToPdf(protocol: Protocol, jobId?: string): Promise<void> {
		const endpoint = jobId
			? `${getBaseUrl()}/jobs/${jobId}/export/pdf`
			: `${getBaseUrl()}/export/pdf`;

		const response = await fetch(endpoint, {
			method: 'POST',
			headers: { 'Content-Type': 'application/json' },
			body: JSON.stringify({ protocol })
		});

		if (!response.ok) {
			throw new Error(`Failed to export PDF: ${response.status}`);
		}

		// Get the PDF blob
		const blob = await response.blob();

		// Extract filename from Content-Disposition header or use default
		const contentDisposition = response.headers.get('Content-Disposition');
		let filename = 'protocol.pdf';

		console.log('Content-Disposition header:', contentDisposition);

		if (contentDisposition) {
			// Try both quoted and unquoted filename formats
			const filenameMatch = contentDisposition.match(/filename[^;=\n]*=((['"]).*?\2|[^;\n]*)/);
			if (filenameMatch && filenameMatch[1]) {
				filename = filenameMatch[1].replace(/['"]/g, '');
				console.log('Extracted filename:', filename);
			}
		}

		console.log('Final filename:', filename);

		// Create a download link and trigger download
		const url = window.URL.createObjectURL(blob);
		const a = document.createElement('a');
		a.href = url;
		a.download = filename;
		document.body.appendChild(a);
		a.click();

		// Clean up
		window.URL.revokeObjectURL(url);
		document.body.removeChild(a);
	}

	/**
	 * Get available meeting templates with AI suggestion
	 * The suggestion is based on transcript analysis
	 */
	static async getTemplates(jobId: string): Promise<TemplatesResponse> {
		const response = await fetch(`${getBaseUrl()}/jobs/${jobId}/templates`);

		if (!response.ok) {
			throw new Error(`Failed to get templates: ${response.status}`);
		}

		return response.json();
	}

	/**
	 * Get a single template by ID
	 */
	static async getTemplate(templateId: string): Promise<MeetingTemplate | null> {
		const response = await fetch(`${getBaseUrl()}/templates/${templateId}`);

		if (!response.ok) {
			if (response.status === 404) return null;
			throw new Error(`Failed to get template: ${response.status}`);
		}

		return response.json();
	}

	/**
	 * Search users from AD/LDAP for autocomplete
	 */
	static async searchUsers(query: string): Promise<UsersSearchResponse> {
		const response = await fetch(`${getBaseUrl()}/users/search?q=${encodeURIComponent(query)}`);

		if (!response.ok) {
			throw new Error(`Failed to search users: ${response.status}`);
		}

		return response.json();
	}

	/**
	 * Get available Confluence spaces
	 */
	static async getConfluenceSpaces(): Promise<ConfluenceSpacesResponse> {
		const response = await fetch(`${getBaseUrl()}/confluence/spaces`);

		if (!response.ok) {
			throw new Error(`Failed to get Confluence spaces: ${response.status}`);
		}

		return response.json();
	}

	/**
	 * Get pages in a Confluence space
	 * @param spaceKey The space key (e.g., "MARKETING")
	 * @param parentId Optional parent page ID to get children
	 */
	// ----- Microsoft Teams Integration -----

	/**
	 * Check if the user has a valid Microsoft Teams session
	 */
	static async getTeamsAuthStatus(): Promise<TeamsAuthStatusResponse> {
		const response = await fetch(`${getBaseUrl()}/auth/microsoft/status`, {
			credentials: 'include'
		});

		if (!response.ok) {
			return { connected: false };
		}

		return response.json();
	}

	/**
	 * Get the Microsoft login URL to open in a popup
	 */
	static async getTeamsLoginUrl(): Promise<string> {
		const response = await fetch(`${getBaseUrl()}/auth/microsoft/login`);

		if (!response.ok) {
			throw new Error(`Failed to get login URL: ${response.status}`);
		}

		const data = await response.json();
		return data.auth_url;
	}

	/**
	 * List recent Teams meetings with recordings
	 */
	static async getTeamsMeetings(): Promise<TeamsMeetingsResponse> {
		const response = await fetch(`${getBaseUrl()}/teams/meetings`, {
			credentials: 'include'
		});

		if (!response.ok) {
			throw new Error(`Failed to get meetings: ${response.status}`);
		}

		return response.json();
	}

	/**
	 * Import a Teams recording into a workflow job
	 */
	static async importTeamsRecording(
		jobId: string,
		meetingId: string,
		recordingId: string,
		meetingSubject?: string,
		meetingStart?: string
	): Promise<TeamsImportResponse> {
		const response = await fetch(`${getBaseUrl()}/jobs/${jobId}/import-teams-recording`, {
			method: 'POST',
			headers: { 'Content-Type': 'application/json' },
			credentials: 'include',
			body: JSON.stringify({
				meeting_id: meetingId,
				recording_id: recordingId,
				meeting_subject: meetingSubject || '',
				meeting_start: meetingStart || ''
			})
		});

		if (!response.ok) {
			throw new Error(`Failed to import recording: ${response.status}`);
		}

		return response.json();
	}

	/**
	 * Disconnect Microsoft Teams session
	 */
	static async disconnectTeams(): Promise<void> {
		await fetch(`${getBaseUrl()}/auth/microsoft/logout`, {
			method: 'DELETE',
			credentials: 'include'
		});
	}

	/**
	 * Download the rendered protocol as a Markdown file.
	 */
	static async downloadMarkdown(jobId: string, filename?: string): Promise<void> {
		const response = await fetch(
			`${getBaseUrl()}/jobs/${jobId}/protocol/render?format=markdown`
		);

		if (!response.ok) {
			throw new Error(`Failed to render protocol: ${response.status}`);
		}

		const text = await response.text();
		const blob = new Blob([text], { type: 'text/markdown;charset=utf-8' });
		const url = window.URL.createObjectURL(blob);
		const a = document.createElement('a');
		a.href = url;
		a.download = filename || 'protocol.md';
		document.body.appendChild(a);
		a.click();
		window.URL.revokeObjectURL(url);
		document.body.removeChild(a);
	}

	static async getConfluencePages(spaceKey: string, parentId?: string): Promise<ConfluencePagesResponse> {
		let url = `${getBaseUrl()}/confluence/spaces/${spaceKey}/pages`;
		if (parentId) {
			url += `?parent_id=${encodeURIComponent(parentId)}`;
		}

		const response = await fetch(url);

		if (!response.ok) {
			throw new Error(`Failed to get Confluence pages: ${response.status}`);
		}

		return response.json();
	}
}

// ============================================================================
// Helper Functions
// ============================================================================

/**
 * Format duration in seconds to human-readable string
 */
export function formatDuration(seconds: number): string {
	const mins = Math.floor(seconds / 60);
	const secs = seconds % 60;
	if (mins === 0) {
		return `${secs}s`;
	}
	return secs > 0 ? `${mins}m ${secs}s` : `${mins}m`;
}

/**
 * Format file size to human-readable string
 */
export function formatFileSize(bytes: number): string {
	if (bytes < 1024) {
		return `${bytes} B`;
	} else if (bytes < 1024 * 1024) {
		return `${(bytes / 1024).toFixed(1)} KB`;
	} else if (bytes < 1024 * 1024 * 1024) {
		return `${(bytes / (1024 * 1024)).toFixed(1)} MB`;
	}
	return `${(bytes / (1024 * 1024 * 1024)).toFixed(2)} GB`;
}

/**
 * Validate file type for upload
 */
export function isValidAudioFile(file: File): boolean {
	const validTypes = [
		'audio/mpeg',
		'audio/mp3',
		'audio/mp4',
		'audio/m4a',
		'audio/x-m4a',
		'audio/wav',
		'audio/webm',
		'video/mp4',
		'video/webm'
	];

	const validExtensions = ['.mp3', '.mp4', '.m4a', '.wav', '.webm'];
	const extension = file.name.toLowerCase().slice(file.name.lastIndexOf('.'));

	return validTypes.includes(file.type) || validExtensions.includes(extension);
}

/**
 * Get file type label
 */
export function getFileTypeLabel(file: { name: string; type?: string }): string {
	const extension = file.name.toLowerCase().slice(file.name.lastIndexOf('.') + 1);
	const labels: Record<string, string> = {
		mp3: 'MP3 Audio',
		mp4: 'MP4 Video/Audio',
		m4a: 'M4A Audio',
		wav: 'WAV Audio',
		webm: 'WebM Audio/Video'
	};
	return labels[extension] || 'Audio-Datei';
}
