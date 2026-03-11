import { writable, derived } from 'svelte/store';
import type { ChatSession, Message, ChatContext } from '$types';
import { createHistory, updateHistoryPayload, getHistoryById } from '$lib/api/historyApi';
import { historyStore } from '$lib/stores/historyStore';

// Store for all chat sessions
export const sessions = writable<Map<string, ChatSession>>(new Map());

// Store for current active session ID
export const currentSessionId = writable<string | null>(null);

// Derived store for current session
export const currentSession = derived(
	[sessions, currentSessionId],
	([$sessions, $currentSessionId]) => {
		if (!$currentSessionId) return null;
		return $sessions.get($currentSessionId) || null;
	}
);

// Store for sources panel visibility
export const showSources = writable<boolean>(true);

// Store for loading state
export const isLoading = writable<boolean>(false);

// Helper functions
export const chatStore = {
	// Create a new session
	createSession: (id?: string): string => {
		const sessionId = id || crypto.randomUUID();
		const newSession: ChatSession = {
			id: sessionId,
			title: 'New Research',
			messages: [],
			createdAt: Date.now(),
			updatedAt: Date.now()
		};

		sessions.update($sessions => {
			$sessions.set(sessionId, newSession);
			return $sessions;
		});

		currentSessionId.set(sessionId);

		return sessionId;
	},

	// Create a new session with context (e.g., from workflow completion)
	createSessionWithContext: (context: ChatContext): string => {
		const sessionId = crypto.randomUUID();

		// Use protocol title if available, otherwise generic title based on action
		let title = 'New Research';
		if (context.protocol?.title) {
			title = context.protocol.title;
		} else if (context.action) {
			const actionTitles: Record<string, string> = {
				email: 'Follow-up Email',
				status: 'Status Update',
				chat: 'Meeting Discussion',
				meeting: 'Meeting Follow-up'
			};
			title = actionTitles[context.action] || 'New Research';
		}

		const newSession: ChatSession = {
			id: sessionId,
			title,
			messages: [],
			createdAt: Date.now(),
			updatedAt: Date.now(),
			context
		};

		sessions.update($sessions => {
			$sessions.set(sessionId, newSession);
			return $sessions;
		});

		currentSessionId.set(sessionId);

		return sessionId;
	},

	// Add a message to current session
	addMessage: async (message: Message) => {
		let sessionId: string | null = null;
		let shouldSaveToDb = false;
		let sessionData: ChatSession | null = null;

		currentSessionId.subscribe(value => { sessionId = value; })();

		sessions.update($sessions => {
			if (sessionId) {
				const current = $sessions.get(sessionId);
				if (current) {
					current.messages.push(message);
					current.updatedAt = Date.now();

					// Auto-generate title from first user message
					if (current.messages.length === 1 && message.role === 'user') {
						current.title = message.content.slice(0, 50) + (message.content.length > 50 ? '...' : '');
						shouldSaveToDb = true;
					}

					sessionData = current;
					// Create a new Map to ensure reactivity
					return new Map($sessions);
				}
			}
			return $sessions;
		});

		const sd = sessionData as ChatSession | null;

		// Save to database when we have a complete exchange (user + assistant)
		if (sd && message.role === 'assistant' && sd.messages.length >= 2) {
			try {
				// Check if this session has a DB ID (meaning it's already saved)
				const hasDbId = (sd as any).dbId;

				if (!hasDbId) {
					// First save - create new history entry
					console.log('💾 Creating new history entry for session:', sessionId);
					const created = await createHistory(
						sd.workflowType || 'Search',
						sd.title,
						{ messages: sd.messages }
					);

					// Store the DB ID so we can update it later
					sessions.update($sessions => {
						const current = $sessions.get(sessionId!);
						if (current) {
							(current as any).dbId = created.id;
						}
						return new Map($sessions);
					});

					// Add to history store
					historyStore.addItem({
						id: created.id,
						workflow_id: created.workflow_id,
						workflow_name: created.workflow_name,
						title: created.title,
						created_at: created.created_at,
						updated_at: created.updated_at
					});

					console.log('✅ History entry created:', created.id);
				} else {
					// Update existing history entry
					console.log('💾 Updating history entry:', hasDbId);
					await updateHistoryPayload(hasDbId, { messages: sd.messages });
					console.log('✅ History entry updated');
				}
			} catch (error) {
				console.error('❌ Failed to save to database:', error);
				// Continue anyway - the chat still works locally
			}
		}
	},

	// Update a message (for streaming)
	updateMessage: (messageId: string, updates: Partial<Message>) => {
		let sessionId: string | null = null;
		currentSessionId.subscribe(value => { sessionId = value; })();

		let sessionData: ChatSession | null = null;

		sessions.update($sessions => {
			if (sessionId) {
				const current = $sessions.get(sessionId);
				if (current) {
					const message = current.messages.find(m => m.id === messageId);
					if (message) {
						// Log before update
						const beforeSources = message.sources?.length || 0;
						Object.assign(message, updates);
						current.updatedAt = Date.now();
						const afterSources = message.sources?.length || 0;
						console.log('🔧 Store: Updated message', messageId.substring(0, 20), 'with', Object.keys(updates),
							updates.sources ? `(sources: ${beforeSources} -> ${afterSources})` : '',
							'Total messages in session:', current.messages.length);

						sessionData = current;

						// Log all messages with sources
						const messagesWithSources = current.messages.filter(m => m.sources && m.sources.length > 0);
						console.log('🔧 Store: Messages with sources:', messagesWithSources.length, 'out of', current.messages.length);
						messagesWithSources.forEach((m, idx) => {
							console.log(`  ${idx + 1}. [${m.role}] ${m.sources?.length || 0} sources:`, m.sources?.map(s => s.id));
						});

						// Create a new Map to ensure reactivity
						return new Map($sessions);
					}
				}
			}
			return $sessions;
		});

		// Save to database when transitioning from streaming to not streaming
		const sd = sessionData as ChatSession | null;
		if (sd && updates.isStreaming === false) {
			const hasDbId = (sd as any).dbId;
			if (hasDbId) {
				console.log('💾 Updating history entry (streaming complete):', hasDbId);
				updateHistoryPayload(hasDbId, { messages: sd.messages }).catch(error => {
					console.error('❌ Failed to update history payload:', error);
				});
			}
		}
	},

	// Append content to a message (for streaming report chunks)
	appendToMessage: (messageId: string, content: string) => {
		let sessionId: string | null = null;
		currentSessionId.subscribe(value => { sessionId = value; })();

		sessions.update($sessions => {
			if (sessionId) {
				const current = $sessions.get(sessionId);
				if (current) {
					const messageIndex = current.messages.findIndex(m => m.id === messageId);
					if (messageIndex !== -1) {
						const oldMessage = current.messages[messageIndex];
						// Create a new message object to ensure Svelte reactivity
						const newMessage = {
							...oldMessage,
							content: (oldMessage.content || '') + content
						};
						// Create a new messages array with the updated message
						current.messages = [
							...current.messages.slice(0, messageIndex),
							newMessage,
							...current.messages.slice(messageIndex + 1)
						];
						current.updatedAt = Date.now();
						// Create a new Map to ensure reactivity
						return new Map($sessions);
					}
				}
			}
			return $sessions;
		});
	},

	// Delete a session
	deleteSession: (sessionId: string) => {
		sessions.update($sessions => {
			$sessions.delete(sessionId);
			return $sessions;
		});
	},

	// Load a session from the database
	loadSessionFromDatabase: async (sessionId: string): Promise<boolean> => {
		try {
			console.log('📂 Loading session from database:', sessionId);
			const historyRecord = await getHistoryById(sessionId);

			if (!historyRecord) {
				console.warn('⚠️  Session not found in database:', sessionId);
				return false;
			}

			// Create session from database record
			// Ensure all messages have isStreaming: false (they're completed messages from history)
			const messages = (historyRecord.payload?.messages || []).map((msg: any) => ({
				...msg,
				isStreaming: false
			}));

			const session: ChatSession = {
				id: historyRecord.id,
				title: historyRecord.title,
				messages,
				createdAt: new Date(historyRecord.created_at).getTime(),
				updatedAt: historyRecord.updated_at ? new Date(historyRecord.updated_at).getTime() : new Date(historyRecord.created_at).getTime(),
				workflowType: historyRecord.workflow_name
			};

			// Store the DB ID for future updates
			(session as any).dbId = historyRecord.id;

			// Add to sessions store
			sessions.update($sessions => {
				$sessions.set(sessionId, session);
				return new Map($sessions);
			});

			console.log('✅ Session loaded from database:', sessionId, 'with', session.messages.length, 'messages');
			return true;
		} catch (error) {
			console.error('❌ Failed to load session from database:', error);
			return false;
		}
	},

	// Clear all sessions
	clearAll: () => {
		sessions.set(new Map());
		currentSessionId.set(null);
	}
};
