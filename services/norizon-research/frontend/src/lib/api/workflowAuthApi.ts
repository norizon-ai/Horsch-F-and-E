/**
 * Authenticated Workflow API Client
 *
 * Wraps WorkflowAPI calls with Azure AD bearer token authentication.
 */

import { authStore } from '$lib/stores/authStore';

const WORKFLOW_API_URL = import.meta.env.VITE_WORKFLOW_API_URL || 'http://localhost:8001';

/**
 * Get authorization headers with Bearer token
 */
async function getAuthHeaders(): Promise<HeadersInit> {
	const token = await authStore.getAccessToken();

	if (!token) {
		throw new Error('No authentication token available');
	}

	return {
		'Authorization': `Bearer ${token}`,
		'Content-Type': 'application/json'
	};
}

/**
 * Authenticated API wrapper
 */
export const AuthenticatedAPI = {
	/**
	 * Test authentication with backend
	 */
	async testAuth() {
		const headers = await getAuthHeaders();

		const response = await fetch(`${WORKFLOW_API_URL}/api/auth/test`, {
			method: 'GET',
			headers
		});

		if (!response.ok) {
			throw new Error(`Auth test failed: ${response.statusText}`);
		}

		return response.json();
	},

	/**
	 * Get current user info from backend
	 */
	async getCurrentUser() {
		const headers = await getAuthHeaders();

		const response = await fetch(`${WORKFLOW_API_URL}/api/users/me`, {
			method: 'GET',
			headers
		});

		if (!response.ok) {
			throw new Error(`Failed to get user: ${response.statusText}`);
		}

		return response.json();
	},

	/**
	 * Get workflow history for current user
	 */
	async getHistory() {
		const headers = await getAuthHeaders();

		const response = await fetch(`${WORKFLOW_API_URL}/api/history`, {
			method: 'GET',
			headers
		});

		if (!response.ok) {
			throw new Error(`Failed to get history: ${response.statusText}`);
		}

		return response.json();
	},

	/**
	 * Get specific history item by ID
	 */
	async getHistoryById(id: string) {
		const headers = await getAuthHeaders();

		const response = await fetch(`${WORKFLOW_API_URL}/api/history/${id}`, {
			method: 'GET',
			headers
		});

		if (!response.ok) {
			throw new Error(`Failed to get history item: ${response.statusText}`);
		}

		return response.json();
	},

	/**
	 * Create workflow job with authentication
	 */
	async createJob(type: string, payload: any) {
		const headers = await getAuthHeaders();

		const response = await fetch(`${WORKFLOW_API_URL}/api/workflow/jobs`, {
			method: 'POST',
			headers,
			body: JSON.stringify({ type, payload })
		});

		if (!response.ok) {
			throw new Error(`Failed to create job: ${response.statusText}`);
		}

		return response.json();
	}
};
