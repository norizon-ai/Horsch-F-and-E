/**
 * History API Client
 *
 * Provides access to workflow history and session data.
 */

import { authStore } from '$lib/stores/authStore';

const WORKFLOW_API_URL = import.meta.env.VITE_WORKFLOW_API_URL || 'http://localhost:8001';

/**
 * Get authorization headers with Bearer token
 */
async function getAuthHeaders(): Promise<HeadersInit> {
	const token = await authStore.getAccessToken();

	if (!token) {
		console.warn('⚠️  No auth token available');
		throw new Error('Authentication required');
	}

	return {
		'Authorization': `Bearer ${token}`,
		'Content-Type': 'application/json'
	};
}

/**
 * Get workflow history item by ID
 */
export async function getHistoryById(historyId: string) {
	try {
		const headers = await getAuthHeaders();

		const response = await fetch(`${WORKFLOW_API_URL}/history/${historyId}`, {
			method: 'GET',
			headers
		});

		if (response.status === 404) {
			console.log(`ℹ️ History record ${historyId} not found (expected for new sessions)`);
			return null;
		}

		if (!response.ok) {
			throw new Error(`Failed to fetch history: ${response.status} ${response.statusText}`);
		}

		return await response.json();
	} catch (error) {
		console.error('❌ Error fetching history:', error);
		throw error;
	}
}

/**
 * Get all workflow history for current user
 */
export async function getAllHistory() {
	try {
		const headers = await getAuthHeaders();

		const response = await fetch(`${WORKFLOW_API_URL}/history`, {
			method: 'GET',
			headers
		});

		if (!response.ok) {
			throw new Error(`Failed to fetch history: ${response.status} ${response.statusText}`);
		}

		return await response.json();
	} catch (error) {
		console.error('❌ Error fetching history:', error);
		throw error;
	}
}

/**
 * Create new workflow history record
 */
export async function createHistory(workflowName: string, title: string, payload: any = {}) {
	try {
		const headers = await getAuthHeaders();

		const response = await fetch(`${WORKFLOW_API_URL}/history`, {
			method: 'POST',
			headers,
			body: JSON.stringify({
				workflow_name: workflowName,
				title,
				payload
			})
		});

		if (!response.ok) {
			throw new Error(`Failed to create history: ${response.status} ${response.statusText}`);
		}

		return await response.json();
	} catch (error) {
		console.error('❌ Error creating history:', error);
		throw error;
	}
}

/**
 * Soft delete workflow history
 */
export async function deleteHistory(historyId: string) {
	try {
		const headers = await getAuthHeaders();

		const response = await fetch(`${WORKFLOW_API_URL}/history/${historyId}`, {
			method: 'DELETE',
			headers
		});

		if (!response.ok) {
			throw new Error(`Failed to delete history: ${response.status} ${response.statusText}`);
		}

		return true;
	} catch (error) {
		console.error('❌ Error deleting history:', error);
		throw error;
	}
}

/**
 * Update workflow history title
 */
export async function updateHistoryTitle(historyId: string, title: string) {
	try {
		const headers = await getAuthHeaders();

		const response = await fetch(`${WORKFLOW_API_URL}/history/${historyId}/title`, {
			method: 'PATCH',
			headers,
			body: JSON.stringify({ title })
		});

		if (!response.ok) {
			throw new Error(`Failed to update title: ${response.status} ${response.statusText}`);
		}

		return await response.json();
	} catch (error) {
		console.error('❌ Error updating title:', error);
		throw error;
	}
}

/**
 * Update workflow history payload
 */
export async function updateHistoryPayload(historyId: string, payload: any) {
	try {
		const headers = await getAuthHeaders();

		const response = await fetch(`${WORKFLOW_API_URL}/history/${historyId}/payload`, {
			method: 'PATCH',
			headers,
			body: JSON.stringify({ payload })
		});

		if (!response.ok) {
			throw new Error(`Failed to update payload: ${response.status} ${response.statusText}`);
		}

		return await response.json();
	} catch (error) {
		console.error('❌ Error updating payload:', error);
		throw error;
	}
}
