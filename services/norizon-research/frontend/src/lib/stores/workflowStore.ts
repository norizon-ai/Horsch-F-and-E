import { writable, derived, get } from 'svelte/store';
import type {
	WorkflowState,
	WorkflowStep,
	WorkflowFile,
	WorkflowProcessingProgress,
	Speaker,
	Protocol,
	PostAction
} from '$lib/types';

// Store for all workflow jobs
const workflows = writable<Map<string, WorkflowState>>(new Map());

// Store for current active workflow job ID
export const currentWorkflowId = writable<string | null>(null);

// Derived store for current workflow state
export const currentWorkflow = derived(
	[workflows, currentWorkflowId],
	([$workflows, $currentWorkflowId]) => {
		if (!$currentWorkflowId) return null;
		return $workflows.get($currentWorkflowId) || null;
	}
);

// Helper to get localStorage key for a job
function getStorageKey(jobId: string): string {
	return `norizon-workflow-meeting-${jobId}`;
}

// Helper functions
export const workflowStore = {
	// Initialize a new workflow job
	initJob: (jobId: string): WorkflowState => {
		const newState: WorkflowState = {
			jobId,
			currentStep: 1,
			file: null,
			processingProgress: null,
			speakers: [],
			protocol: null,
			selectedPostAction: null
		};

		workflows.update($workflows => {
			$workflows.set(jobId, newState);
			return new Map($workflows);
		});

		currentWorkflowId.set(jobId);
		saveToLocalStorage(jobId);

		return newState;
	},

	// Load workflow from localStorage if exists
	loadJob: (jobId: string): WorkflowState | null => {
		if (typeof window === 'undefined') return null;

		try {
			const stored = localStorage.getItem(getStorageKey(jobId));
			if (stored) {
				const state = JSON.parse(stored) as WorkflowState;
				workflows.update($workflows => {
					$workflows.set(jobId, state);
					return new Map($workflows);
				});
				currentWorkflowId.set(jobId);
				return state;
			}
		} catch (error) {
			console.error('Failed to load workflow:', error);
		}
		return null;
	},

	// Set current step
	setStep: (step: WorkflowStep) => {
		const jobId = get(currentWorkflowId);
		if (!jobId) return;

		workflows.update($workflows => {
			const state = $workflows.get(jobId);
			if (state) {
				state.currentStep = step;
				return new Map($workflows);
			}
			return $workflows;
		});
		saveToLocalStorage(jobId);
	},

	// Go to next step
	nextStep: () => {
		const state = get(currentWorkflow);
		if (state && state.currentStep < 9) {
			workflowStore.setStep((state.currentStep + 1) as WorkflowStep);
		}
	},

	// Go to previous step
	prevStep: () => {
		const state = get(currentWorkflow);
		if (state && state.currentStep > 1) {
			workflowStore.setStep((state.currentStep - 1) as WorkflowStep);
		}
	},

	// Set file info
	setFile: (file: WorkflowFile) => {
		const jobId = get(currentWorkflowId);
		if (!jobId) return;

		workflows.update($workflows => {
			const state = $workflows.get(jobId);
			if (state) {
				state.file = file;
				return new Map($workflows);
			}
			return $workflows;
		});
		saveToLocalStorage(jobId);
	},

	// Clear file
	clearFile: () => {
		const jobId = get(currentWorkflowId);
		if (!jobId) return;

		workflows.update($workflows => {
			const state = $workflows.get(jobId);
			if (state) {
				state.file = null;
				return new Map($workflows);
			}
			return $workflows;
		});
		saveToLocalStorage(jobId);
	},

	// Update processing progress
	setProgress: (progress: WorkflowProcessingProgress | null) => {
		const jobId = get(currentWorkflowId);
		if (!jobId) return;

		workflows.update($workflows => {
			const state = $workflows.get(jobId);
			if (state) {
				// Create a new state object to ensure Svelte detects the change
				const newState = { ...state, processingProgress: progress };
				const newMap = new Map($workflows);
				newMap.set(jobId, newState);
				return newMap;
			}
			return $workflows;
		});
		// Don't save progress to localStorage on every update for performance
	},

	// Set speakers
	setSpeakers: (speakers: Speaker[]) => {
		const jobId = get(currentWorkflowId);
		if (!jobId) return;

		workflows.update($workflows => {
			const state = $workflows.get(jobId);
			if (state) {
				state.speakers = speakers;
				return new Map($workflows);
			}
			return $workflows;
		});
		saveToLocalStorage(jobId);
	},

	// Update a single speaker's confirmed name
	updateSpeakerName: (speakerId: string, confirmedName: string) => {
		const jobId = get(currentWorkflowId);
		if (!jobId) return;

		workflows.update($workflows => {
			const state = $workflows.get(jobId);
			if (state) {
				state.speakers = state.speakers.map(s =>
					s.id === speakerId ? { ...s, confirmedName } : s
				);
				return new Map($workflows);
			}
			return $workflows;
		});
		saveToLocalStorage(jobId);
	},

	// Toggle a speaker's external status
	toggleSpeakerExternal: (speakerId: string) => {
		const jobId = get(currentWorkflowId);
		if (!jobId) return;

		workflows.update($workflows => {
			const state = $workflows.get(jobId);
			if (state) {
				state.speakers = state.speakers.map(s =>
					s.id === speakerId ? { ...s, isExternal: !s.isExternal } : s
				);
				return new Map($workflows);
			}
			return $workflows;
		});
		saveToLocalStorage(jobId);
	},

	// Set protocol
	setProtocol: (protocol: Protocol) => {
		const jobId = get(currentWorkflowId);
		if (!jobId) return;

		workflows.update($workflows => {
			const state = $workflows.get(jobId);
			if (state) {
				state.protocol = protocol;
				return new Map($workflows);
			}
			return $workflows;
		});
		saveToLocalStorage(jobId);
	},

	// Update protocol field
	updateProtocol: (updates: Partial<Protocol>) => {
		const jobId = get(currentWorkflowId);
		if (!jobId) return;

		workflows.update($workflows => {
			const state = $workflows.get(jobId);
			if (state && state.protocol) {
				state.protocol = { ...state.protocol, ...updates };
				return new Map($workflows);
			}
			return $workflows;
		});
		saveToLocalStorage(jobId);
	},

	// Update protocol summary (for sidebar editor)
	updateProtocolSummary: (summary: string) => {
		const jobId = get(currentWorkflowId);
		if (!jobId) return;

		workflows.update($workflows => {
			const state = $workflows.get(jobId);
			if (state && state.protocol) {
				state.protocol = { ...state.protocol, executiveSummary: summary };
				return new Map($workflows);
			}
			return $workflows;
		});
		saveToLocalStorage(jobId);
	},

	// Set selected post action
	setPostAction: (action: PostAction | null) => {
		const jobId = get(currentWorkflowId);
		if (!jobId) return;

		workflows.update($workflows => {
			const state = $workflows.get(jobId);
			if (state) {
				state.selectedPostAction = action;
				return new Map($workflows);
			}
			return $workflows;
		});
		saveToLocalStorage(jobId);
	},

	// Set Confluence URL after publishing
	setConfluenceUrl: (url: string) => {
		const jobId = get(currentWorkflowId);
		if (!jobId) return;

		workflows.update($workflows => {
			const state = $workflows.get(jobId);
			if (state) {
				state.confluenceUrl = url;
				return new Map($workflows);
			}
			return $workflows;
		});
		saveToLocalStorage(jobId);
	},

	// Generic update method for any workflow field
	updateWorkflow: (updates: Partial<WorkflowState>) => {
		const jobId = get(currentWorkflowId);
		if (!jobId) return;

		workflows.update($workflows => {
			const state = $workflows.get(jobId);
			if (state) {
				const newState = { ...state, ...updates };
				const newMap = new Map($workflows);
				newMap.set(jobId, newState);
				return newMap;
			}
			return $workflows;
		});
		saveToLocalStorage(jobId);
	},

	// Set protocol saved state (after user clicks "Save & Continue")
	setProtocolSaved: (saved: boolean) => {
		const jobId = get(currentWorkflowId);
		if (!jobId) return;

		workflows.update($workflows => {
			const state = $workflows.get(jobId);
			if (state) {
				state.isProtocolSaved = saved;
				return new Map($workflows);
			}
			return $workflows;
		});
		saveToLocalStorage(jobId);
	},

	// Set suggested template ID (from AI analysis)
	setSuggestedTemplate: (templateId: string) => {
		const jobId = get(currentWorkflowId);
		if (!jobId) return;

		workflows.update($workflows => {
			const state = $workflows.get(jobId);
			if (state) {
				state.suggestedTemplateId = templateId;
				return new Map($workflows);
			}
			return $workflows;
		});
		saveToLocalStorage(jobId);
	},

	// Set destination (Confluence space and parent page)
	setDestination: (spaceId: string, parentPageId: string) => {
		const jobId = get(currentWorkflowId);
		if (!jobId) return;

		workflows.update($workflows => {
			const state = $workflows.get(jobId);
			if (state) {
				state.destinationSpaceId = spaceId;
				state.destinationParentPageId = parentPageId;
				return new Map($workflows);
			}
			return $workflows;
		});
		saveToLocalStorage(jobId);
	},

	// Set processing complete state (for back navigation)
	setProcessingComplete: (complete: boolean) => {
		const jobId = get(currentWorkflowId);
		if (!jobId) return;

		workflows.update($workflows => {
			const state = $workflows.get(jobId);
			if (state) {
				state.processingComplete = complete;
				return new Map($workflows);
			}
			return $workflows;
		});
		saveToLocalStorage(jobId);
	},

	// Delete a workflow job
	deleteJob: (jobId: string) => {
		workflows.update($workflows => {
			$workflows.delete(jobId);
			return new Map($workflows);
		});
		if (typeof window !== 'undefined') {
			localStorage.removeItem(getStorageKey(jobId));
		}
		const current = get(currentWorkflowId);
		if (current === jobId) {
			currentWorkflowId.set(null);
		}
	},

	// Clear current workflow
	clearCurrent: () => {
		currentWorkflowId.set(null);
	}
};

// Save workflow state to localStorage
function saveToLocalStorage(jobId: string) {
	if (typeof window === 'undefined') return;

	const $workflows = get(workflows);
	const state = $workflows.get(jobId);

	if (state) {
		try {
			localStorage.setItem(getStorageKey(jobId), JSON.stringify(state));
		} catch (error) {
			console.error('Failed to save workflow to localStorage:', error);
		}
	}
}
