/**
 * History Store
 *
 * Manages workflow history state and database synchronization.
 */

import { writable, derived } from 'svelte/store';
import { getAllHistory, deleteHistory, updateHistoryTitle } from '$lib/api/historyApi';
import type { ChatSession } from '$lib/types';

interface HistoryItem {
	id: string;
	workflow_id: string;
	workflow_name: string;
	title: string;
	created_at: string;
	updated_at: string | null;
}

interface HistoryState {
	items: HistoryItem[];
	isLoading: boolean;
	error: string | null;
}

const initialState: HistoryState = {
	items: [],
	isLoading: false,
	error: null
};

function createHistoryStore() {
	const { subscribe, set, update } = writable<HistoryState>(initialState);

	return {
		subscribe,

		/**
		 * Load all history from the database
		 */
		async loadHistory() {
			update(state => ({ ...state, isLoading: true, error: null }));

			try {
				const items = await getAllHistory();
				update(state => ({
					...state,
					items,
					isLoading: false
				}));
			} catch (error) {
				console.error('❌ Failed to load history:', error);
				update(state => ({
					...state,
					error: error instanceof Error ? error.message : 'Failed to load history',
					isLoading: false
				}));
			}
		},

		/**
		 * Delete history item (soft delete)
		 */
		async deleteItem(id: string) {
			try {
				await deleteHistory(id);

				// Remove from local state
				update(state => ({
					...state,
					items: state.items.filter(item => item.id !== id)
				}));

				return true;
			} catch (error) {
				console.error('❌ Failed to delete history:', error);
				return false;
			}
		},

		/**
		 * Update history item title
		 */
		async updateTitle(id: string, newTitle: string) {
			try {
				const updated = await updateHistoryTitle(id, newTitle);

				// Update local state
				update(state => ({
					...state,
					items: state.items.map(item =>
						item.id === id ? { ...item, title: updated.title, updated_at: updated.updated_at } : item
					)
				}));

				return true;
			} catch (error) {
				console.error('❌ Failed to update title:', error);
				return false;
			}
		},

		/**
		 * Add new history item to local state
		 */
		addItem(item: HistoryItem) {
			update(state => ({
				...state,
				items: [item, ...state.items]
			}));
		},

		/**
		 * Clear all history (local state only)
		 */
		clear() {
			set(initialState);
		}
	};
}

export const historyStore = createHistoryStore();

// Derived store for sessions compatible with ChatSession type
export const historySessions = derived(historyStore, ($history) => {
	return $history.items.map((item): ChatSession => ({
		id: item.id,
		title: item.title,
		messages: [],
		createdAt: new Date(item.created_at).getTime(),
		updatedAt: item.updated_at ? new Date(item.updated_at).getTime() : new Date(item.created_at).getTime(),
		workflowType: item.workflow_name
	}));
});
