<script lang="ts">
	import { page } from '$app/stores';
	import { onMount } from 'svelte';
	import { goto } from '$app/navigation';
	import NoraLayout from '$lib/components/NoraLayout.svelte';
	import ChatInput from '$lib/components/ChatInput.svelte';
	import SearchProgress from '$lib/components/SearchProgress.svelte';
	import SkeletonLoading from '$lib/components/SkeletonLoading.svelte';
	import SourcesSummary from '$lib/components/SourcesSummary.svelte';
	import MessageActions from '$lib/components/MessageActions.svelte';
	import ContextBanner from '$lib/components/ContextBanner.svelte';
	import { chatStore, currentSession, currentSessionId, sessions, isLoading } from '$lib/stores/chatStore';
	import { configStore } from '$lib/stores/configStore';
	import { t } from 'svelte-i18n';
	import { SearchAPI, toFrontendSource, getActiveAgent, buildConversationHistory } from '$lib/api/searchApi';
	import type { Message, Source, SearchProgress as SearchProgressType, AgentIteration, ChatContext, Protocol } from '$lib/types';
	import { marked } from 'marked';
	import DOMPurify from 'dompurify';

	let sessionId: string;
	let messages: Message[] = [];
	let messagesContainer: HTMLDivElement;
	let recentSessions: any[] = [];
	let isSearching = false;
	let currentProgress: SearchProgressType | null = null;
	let activeAgent: string | null = null;
	let agentIterations: AgentIteration[] = [];
	let sessionContext: ChatContext | null = null;
	let showContextBanner = true;
	let chatInputRef: ChatInput;

	$: sessionId = $page.params.sessionId;

	// React to session ID changes
	$: if (sessionId) {
		loadSession(sessionId);
	}

	async function loadSession(id: string) {
		if (!$sessions.has(id)) {
			// Try to load from database first
			const loaded = await chatStore.loadSessionFromDatabase(id);
			if (!loaded) {
				// If not in database, create new session
				chatStore.createSession(id);
			}
		}

		// Set current session ID - this will trigger reactive updates
		currentSessionId.set(id);

		// Wait a tick for reactivity to update
		await new Promise(resolve => setTimeout(resolve, 0));

		// Check for auto-submit query parameter after session is loaded
		const query = $page.url.searchParams.get('q');
		const session = $sessions.get(id);
		if (query && session && session.messages.length === 0) {
			setTimeout(() => {
				handleSubmit(new CustomEvent('submit', { detail: query }));
			}, 100);
		}
	}

	
	// Watch for message updates
	$: if ($currentSession) {
		messages = [...$currentSession.messages];
		console.log('📋 Reactive update - messages count:', messages.length);
		messages.forEach((m, i) => {
			console.log(`  Message ${i}:`, {
				role: m.role,
				hasContent: !!m.content,
				contentLength: m.content?.length || 0,
				isStreaming: m.isStreaming,
				hasSources: (m.sources?.length || 0) > 0
			});
			if (m.sources && m.sources.length > 0) {
				console.log(`  Message ${i} has ${m.sources.length} sources`);
			}
		});

		// Clear loading state when messages are loaded from history
		// Only keep loading state when actively searching (currentProgress exists)
		if (messages.length > 0) {
			if (!currentProgress) {
				isSearching = false;
			}
		}

		// Also update context
		sessionContext = $currentSession.context || null;
		showContextBanner = !!$currentSession.context;
	}

	// Auto-scroll
	$: if ($currentSession) {
		setTimeout(() => scrollToBottom(), 100);
	}

	function scrollToBottom() {
		if (messagesContainer) {
			messagesContainer.scrollTop = messagesContainer.scrollHeight;
		}
	}

	// Build protocol context as a markdown string for the LLM
	function buildProtocolContext(protocol: Protocol): string {
		const parts: string[] = [];

		parts.push(`# Meeting Protocol: ${protocol.title}`);
		parts.push(`**Date:** ${protocol.date}`);

		if (protocol.attendees?.length > 0) {
			parts.push(`**Attendees:** ${protocol.attendees.join(', ')}`);
		}

		if (protocol.executiveSummary) {
			parts.push(`\n## Executive Summary\n${protocol.executiveSummary}`);
		}

		if (protocol.decisions?.length > 0) {
			parts.push(`\n## Decisions\n${protocol.decisions.map((d, i) => `${i + 1}. ${d}`).join('\n')}`);
		}

		if (protocol.actionItems?.length > 0) {
			parts.push(`\n## Action Items`);
			protocol.actionItems.forEach((item, i) => {
				let actionText = `${i + 1}. ${item.text}`;
				if (item.assignee) actionText += ` (Assigned: ${item.assignee})`;
				if (item.dueDate) actionText += ` - Due: ${item.dueDate}`;
				parts.push(actionText);
			});
		}

		if (protocol.nextSteps?.length > 0) {
			parts.push(`\n## Next Steps\n${protocol.nextSteps.map((s, i) => `${i + 1}. ${s}`).join('\n')}`);
		}

		return parts.join('\n');
	}

	async function handleSubmit(event: CustomEvent<string>) {
		const query = event.detail;

		// Build conversation history from store directly (not local messages variable which updates async)
		// Read from $currentSession.messages to get the current state of the store
		const currentMessages = $currentSession?.messages || [];
		const conversationHistory = buildConversationHistory(currentMessages);

		console.log('Building conversation history from', currentMessages.length, 'messages');
		console.log('Conversation history to send:', conversationHistory);

		// Build document context from session context if available
		let documentContext: string | undefined;
		if (sessionContext?.protocol) {
			documentContext = buildProtocolContext(sessionContext.protocol);
			console.log('Including protocol context in search request');
		}

		// Add user message
		const userMessage: Message = {
			id: `msg-${Date.now()}-user`,
			role: 'user',
			content: query,
			timestamp: Date.now()
		};
		chatStore.addMessage(userMessage);

		// Add streaming assistant message
		const assistantMessageId = `msg-${Date.now()}-assistant`;
		const assistantMessage: Message = {
			id: assistantMessageId,
			role: 'assistant',
			content: '',
			timestamp: Date.now(),
			isStreaming: true,
			sources: []
		};
		chatStore.addMessage(assistantMessage);

		isLoading.set(true);
		isSearching = true;
		agentIterations = [];
		currentProgress = { phase: 'starting', message: 'Initializing search...', agentIterations: [] };
		activeAgent = null;

		try {
			// Start the search job with conversation history and document context
			const job = await SearchAPI.startSearch({
				query,
				conversation_history: conversationHistory.length > 0 ? conversationHistory : undefined,
				document_context: documentContext
			});

			chatStore.updateMessage(assistantMessageId, { jobId: job.job_id });

			// Stream the results
			for await (const event of SearchAPI.streamSearch(job.job_id)) {
				switch (event.type) {
					case 'progress':
						// Add thinking step to the list for analyzing/generating phases
						if (event.phase === 'analyzing' || event.phase === 'generating_report') {
							// Mark any previous thinking entries as done
							agentIterations = agentIterations.map(ai =>
								ai.status === 'thinking' ? { ...ai, status: 'done' as const } : ai
							);

							// Add new thinking entry
							const thinkingEntry: AgentIteration = {
								iterationNumber: agentIterations.length + 1,
								agentName: event.phase,
								status: 'thinking',
								displayName: event.phase === 'analyzing' ? 'Analyzing query' : 'Writing response',
								thinkingMessage: event.message
							};
							agentIterations = [...agentIterations, thinkingEntry];
						}

						currentProgress = {
							phase: event.phase,
							message: event.message,
							agentIterations,
							...(event.extra || {})
						};
						break;

					case 'iteration':
						// Iteration event: if no agent_status events, use tools_called as fallback
						// Mark previous iteration's agents as done (only if they're still searching)
						// Also mark thinking entries as done
						agentIterations = agentIterations.map(ai =>
							(ai.iterationNumber < event.iteration_number && ai.status === 'searching') ||
							ai.status === 'thinking'
								? { ...ai, status: 'done' as const }
								: ai
						);

						// Only add agents from tools_called if we haven't received agent_status events for them
						for (const toolName of event.tools_called) {
							const exists = agentIterations.some(
								ai => ai.iterationNumber === event.iteration_number && ai.agentName === toolName
							);
							if (!exists) {
								const newIteration: AgentIteration = {
									iterationNumber: event.iteration_number,
									agentName: toolName,
									status: 'searching'
								};
								agentIterations = [...agentIterations, newIteration];
							}
						}

						currentProgress = {
							...currentProgress!,
							currentIteration: event.iteration_number,
							toolsCalled: event.tools_called,
							agentIterations
						};

						// Update active agent based on tools called
						if (event.tools_called.length > 0) {
							activeAgent = event.tools_called[0];
							chatStore.updateMessage(assistantMessageId, { activeAgent });
						}
						break;

					case 'agent_status':
						// Per-agent status update for real-time parallel execution feedback
						if (event.status === 'searching') {
							// Mark any thinking entries as done first
							agentIterations = agentIterations.map(ai =>
								ai.status === 'thinking' ? { ...ai, status: 'done' as const } : ai
							);

							// Agent started - add new box if not exists
							const exists = agentIterations.some(
								ai => ai.iterationNumber === event.iteration_number && ai.agentName === event.agent_name
							);
							if (!exists) {
								const newIteration: AgentIteration = {
									iterationNumber: event.iteration_number,
									agentName: event.agent_name,
									searchQuery: event.search_query,
									status: 'searching',
									displayName: event.display_name,
									iconUrl: event.icon_url,
									searchingLabel: event.searching_label,
									itemLabel: event.item_label
								};
								agentIterations = [...agentIterations, newIteration];
							}
						} else if (event.status === 'done') {
							// Agent completed - update existing box with metadata
							agentIterations = agentIterations.map(ai =>
								ai.iterationNumber === event.iteration_number && ai.agentName === event.agent_name
									? {
										...ai,
										status: 'done' as const,
										resultsCount: event.results_count,
										displayName: event.display_name || ai.displayName,
										iconUrl: event.icon_url || ai.iconUrl,
										searchingLabel: event.searching_label || ai.searchingLabel,
										itemLabel: event.item_label || ai.itemLabel
									}
									: ai
							);
						}

						currentProgress = {
							...currentProgress!,
							currentIteration: event.iteration_number,
							agentIterations
						};

						activeAgent = event.agent_name;
						chatStore.updateMessage(assistantMessageId, { activeAgent });
						break;

					case 'report_chunk':
						// Append streamed report chunk to message content
						console.log('report_chunk received:', event.content.substring(0, 50) + '...');
						chatStore.appendToMessage(assistantMessageId, event.content);
						break;

					case 'complete':
						const result = event.result;
						console.log('Complete event received. Raw sources from backend:', result.sources);
						console.log('Backend sources count:', result.sources?.length || 0);

						// Convert sources to frontend format
						const sources: Source[] = result.sources.map(s => toFrontendSource(s));
						console.log('Converted sources:', sources);
						console.log('Converted sources count:', sources.length);

						// Mark all agent iterations as done for persistence
						const finalIterations = agentIterations.map(ai => ({
							...ai,
							status: 'done' as const
						}));

						// Get current message to check if content was streamed
						let currentContent = '';
						currentSession.subscribe(session => {
							const msg = session?.messages.find(m => m.id === assistantMessageId);
							currentContent = msg?.content || '';
						})();

						// Only set content if it wasn't streamed (empty or very short)
						// Streaming would have populated it already
						const shouldUseCompleteContent = currentContent.length < 100;
						console.log('Complete event: currentContent length =', currentContent.length, 'useComplete =', shouldUseCompleteContent);

						chatStore.updateMessage(assistantMessageId, {
							// Only overwrite content if streaming didn't populate it
							...(shouldUseCompleteContent ? { content: result.final_report || result.concise_answer } : {}),
							sources,
							isStreaming: false,
							confidence: result.confidence_score,
							activeAgent: activeAgent || 'Knowledge Search',
							agentIterations: finalIterations
						});
						console.log('Called chatStore.updateMessage with sources');

						currentProgress = null;
						break;

					case 'error':
						chatStore.updateMessage(assistantMessageId, {
							content: `Error: ${event.error}${event.detail ? `\n\n${event.detail}` : ''}`,
							isStreaming: false
						});
						currentProgress = null;
						break;

					case 'keepalive':
						// Ignore keepalive events
						break;
				}
			}
		} catch (error) {
			console.error('Search failed:', error);
			chatStore.updateMessage(assistantMessageId, {
				content: 'Sorry, I encountered an error while researching your question. Please try again.',
				isStreaming: false
			});
		} finally {
			isLoading.set(false);
			isSearching = false;
			currentProgress = null;
		}
	}

	function handleNewChat() {
		goto('/chat');
	}

	function handleSelectSession(event: CustomEvent<string>) {
		goto(`/chat/${event.detail}`);
	}

	function handleCopy(content: string) {
		navigator.clipboard.writeText(content);
	}

	function handleRegenerate(messageIndex: number) {
		// Find the user message before this assistant message
		const userMsg = messages.slice(0, messageIndex).reverse().find(m => m.role === 'user');
		if (userMsg) {
			// Remove the assistant message and regenerate
			// For now, just re-submit the query
			handleSubmit(new CustomEvent('submit', { detail: userMsg.content }));
		}
	}

	async function handleExportMessage(message: Message) {
		try {
			// Convert chat message to Protocol format for PDF export
			const protocol = {
				title: $currentSession?.title || "Nora Research Result",
				date: new Date(message.timestamp).toLocaleDateString('en-US', {
					year: 'numeric',
					month: 'long',
					day: 'numeric'
				}),
				attendees: [], // Empty for research results
				executiveSummary: message.content.slice(0, 300) + (message.content.length > 300 ? '...' : ''),
				actionItems: [],
				fullTranscript: message.content,
				decisions: [],
				nextSteps: [],
				customSections: message.sources && message.sources.length > 0 ? [
					{
						id: "sources",
						label: "Sources",
						content: message.sources.map((source, idx) =>
							`${idx + 1}. ${source.title}\n   ${source.url}${source.description ? '\n   ' + source.description : ''}`
						).join('\n\n')
					}
				] : []
			};

			// Call the export PDF endpoint
			const WORKFLOW_API_URL = import.meta.env.VITE_WORKFLOW_API_URL || 'http://localhost:8001';

			// Get auth token
			const { authStore } = await import('$lib/stores/authStore');
			const token = await authStore.getAccessToken();

			const response = await fetch(`${WORKFLOW_API_URL}/export/pdf`, {
				method: 'POST',
				headers: {
					'Content-Type': 'application/json',
					...(token ? { 'Authorization': `Bearer ${token}` } : {})
				},
				body: JSON.stringify({ protocol })
			});

			if (!response.ok) {
				throw new Error(`Export failed: ${response.statusText}`);
			}

			// Download the PDF
			const blob = await response.blob();
			const url = URL.createObjectURL(blob);
			const a = document.createElement('a');
			a.href = url;
			a.download = `nora-research-${new Date().toISOString().split('T')[0]}.pdf`;
			document.body.appendChild(a);
			a.click();
			document.body.removeChild(a);
			URL.revokeObjectURL(url);
		} catch (error) {
			console.error('Failed to export PDF:', error);
			alert('Failed to export PDF. Please try again.');
		}
	}

	function handleContextDismiss() {
		showContextBanner = false;
		// Note: context is still active for search, just not showing the banner
	}

	function handleSelectPrompt(event: CustomEvent<string>) {
		const prompt = event.detail;
		// Auto-fill the input and submit
		handleSubmit(new CustomEvent('submit', { detail: prompt }));
	}

	// Get source type icon class
	function getSourceTypeClass(sourceType: string | undefined): string {
		switch (sourceType) {
			case 'sharepoint': return 'sharepoint';
			case 'confluence': return 'confluence';
			case 'wiki': return 'wiki';
			case 'jira': return 'jira';
			case 'web': return 'web';
			case 'elasticsearch': return 'elasticsearch';
			default: return 'unknown';
		}
	}

	// Get source type label
	function getSourceTypeLabel(sourceType: string | undefined): string {
		switch (sourceType) {
			case 'sharepoint': return 'SharePoint';
			case 'confluence': return 'Confluence';
			case 'wiki': return 'Internal Wiki';
			case 'jira': return 'Jira';
			case 'web': return 'Web';
			case 'elasticsearch': return 'Knowledge Base';
			default: return 'Document';
		}
	}

	// Strip debug text patterns from content
	function stripDebugText(content: string): string {
		// Remove patterns like "(hypothetical...", "(placeholder...", debug markers
		let cleaned = content;
		// Remove hypothetical/placeholder notes in parentheses
		cleaned = cleaned.replace(/\(hypothetical[^)]*\)/gi, '');
		cleaned = cleaned.replace(/\(placeholder[^)]*\)/gi, '');
		// Remove any debug markers
		cleaned = cleaned.replace(/\[DEBUG[^\]]*\]/gi, '');
		cleaned = cleaned.replace(/\[PLACEHOLDER[^\]]*\]/gi, '');
		// Clean up any resulting double spaces or empty lines
		cleaned = cleaned.replace(/  +/g, ' ');
		cleaned = cleaned.replace(/\n\n\n+/g, '\n\n');
		return cleaned.trim();
	}

	// Render markdown with source citations including tooltips
	function renderContent(content: string, sources: Source[] = [], messageId: string = ''): string {
		// First, strip any debug text patterns
		let processed = stripDebugText(content);

		// Replace [1], [2], etc. with citation elements with tooltips
		if (sources.length > 0) {
			processed = processed.replace(/\[(\d+)\]/g, (match, num) => {
				const idx = parseInt(num) - 1;
				if (idx >= 0 && idx < sources.length) {
					const source = sources[idx];
					const sourceType = getSourceTypeClass(source.sourceType);
					const sourceLabel = getSourceTypeLabel(source.sourceType);
					const lastUpdated = source.lastUpdated || '';

					// Escape HTML entities in title
					const escapedTitle = source.title
						.replace(/&/g, '&amp;')
						.replace(/</g, '&lt;')
						.replace(/>/g, '&gt;')
						.replace(/"/g, '&quot;');

					return `<span class="citation" data-source="${num}" onclick="window.scrollToSource && window.scrollToSource('${messageId}', ${num})">${num}<span class="citation-tooltip"><span class="citation-tooltip-header"><span class="citation-tooltip-icon ${sourceType}"></span><span class="citation-tooltip-title">${escapedTitle}</span></span><span class="citation-tooltip-meta">${sourceLabel}${lastUpdated ? ' · ' + lastUpdated : ''}</span></span></span>`;
				}
				return match;
			});
		}

		// Parse markdown and sanitize HTML
		const html = marked(processed) as string;
		return DOMPurify.sanitize(html, {
			ADD_ATTR: ['onclick', 'data-source'], // Allow citation click handlers
			ADD_TAGS: ['span'] // Allow span elements for citations
		});
	}

	// Scroll to source function (exposed to window for onclick handlers)
	function scrollToSource(messageId: string, sourceNumber: number) {
		const sourceCard = document.getElementById(`source-${messageId}-${sourceNumber}`);
		if (sourceCard) {
			// Expand sources if collapsed
			const sourcesSummary = sourceCard.closest('.sources-summary');
			if (sourcesSummary && sourcesSummary.classList.contains('collapsed')) {
				sourcesSummary.classList.remove('collapsed');
			}

			// Scroll to the source card
			sourceCard.scrollIntoView({ behavior: 'smooth', block: 'center' });

			// Add highlight effect
			sourceCard.classList.add('highlighted');
			setTimeout(() => {
				sourceCard.classList.remove('highlighted');
			}, 2000);
		}
	}

	// Expose scrollToSource to window
	onMount(() => {
		(window as any).scrollToSource = scrollToSource;

		// Load config from YAML
		configStore.loadConfig();

		const unsubscribe = sessions.subscribe($sessions => {
			recentSessions = Array.from($sessions.values())
				.filter(session => session.messages.length > 0)
				.sort((a, b) => b.updatedAt - a.updatedAt)
				.slice(0, 10);
		});

		return () => {
			unsubscribe();
			delete (window as any).scrollToSource;
		};
	});
</script>

<svelte:head>
	<title>{$currentSession?.title || 'Research'} - Nora</title>
</svelte:head>

<NoraLayout
	sessions={recentSessions}
	currentSessionId={sessionId}
	title={$currentSession?.title || 'New Research'}
	{activeAgent}
	{isSearching}
	on:newChat={handleNewChat}
	on:selectSession={handleSelectSession}
>
	<!-- Messages -->
	<div bind:this={messagesContainer} class="messages-scroll">
		<!-- Context Banner (from workflow handoff) -->
		{#if sessionContext && showContextBanner && messages.length === 0}
			<ContextBanner
				context={sessionContext}
				on:dismiss={handleContextDismiss}
				on:selectPrompt={handleSelectPrompt}
			/>
		{/if}

		{#if messages.length === 0}
			<!-- Empty state - uses i18n for translations -->
			<div class="empty-state">
				<div class="empty-icon">
					<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
						<circle cx="11" cy="11" r="8" />
						<line x1="21" y1="21" x2="16.65" y2="16.65" />
					</svg>
				</div>
				<h2>{$t('welcome.title')}</h2>
				<p>{$t('welcome.subtitle')}</p>
				<div class="suggestion-grid">
					{#each ['processes', 'documentation', 'policies', 'contacts'] as suggestionId (suggestionId)}
						<button
							on:click={() => {
								if (suggestionId === 'processes') {
									goto('/workflow/meeting');
								} else {
									handleSubmit(new CustomEvent('submit', { detail: $t(`suggestions.${suggestionId}.question`) }));
								}
							}}
							class="suggestion-card"
						>
							<span class="suggestion-title">{$t(`suggestions.${suggestionId}.title`)}</span>
							<span class="suggestion-desc">{$t(`suggestions.${suggestionId}.question`)}</span>
						</button>
					{/each}
				</div>
			</div>
		{:else}
			{#each messages as message, idx (message.id)}
				{#if message.role === 'user'}
					<!-- User message -->
					<div class="message-user">
						<div class="user-bubble">{message.content}</div>
					</div>
				{:else if message.role === 'assistant'}
					<!-- Assistant message -->
					<div class="message-assistant">
						<div class="answer-card">
							<div class="message-header">
								<div class="message-avatar assistant">
									<svg viewBox="0 0 24 24" fill="currentColor">
										<path d="M6 4v16h2.5v-9.5L15 18.5V20h2.5V4H15v9.5L8.5 5.5V4H6z"/>
									</svg>
								</div>
								<span class="message-name">Nora</span>
								<!-- DEBUG: Show message state -->
								{#if !message.content && !message.isStreaming}
									<span style="color: red; font-size: 10px; margin-left: 8px;">
										⚠️ No content (isStreaming: {message.isStreaming}, content: {message.content?.slice(0, 20)})
									</span>
								{/if}
								<!-- Inline status: shows source pills next to avatar -->
								{#if message.agentIterations && message.agentIterations.length > 0 && !message.isStreaming}
									{@const completedProgress = {
										phase: 'complete',
										message: 'Search completed',
										agentIterations: message.agentIterations,
										isComplete: true
									}}
									<SearchProgress progress={completedProgress} isComplete={true} />
								{/if}
							</div>
							<div class="message-content">
								{#if message.isStreaming && currentProgress}
									<!-- Show search progress during streaming (hide once content arrives) -->
									{#if !message.content}
										<SearchProgress progress={currentProgress} isComplete={false} />
										<SkeletonLoading showSources={true} />
									{/if}

									<!-- Render streaming content with full markdown support -->
									{#if message.content}
										<div class="message-text streaming">
											{@html renderContent(message.content, [], message.id)}
										</div>
									{/if}
								{:else if message.content}
									<div class="message-text">
										{@html renderContent(message.content, message.sources, message.id)}
									</div>

									{#if message.sources && message.sources.length > 0}
										<SourcesSummary sources={message.sources} messageId={message.id} />
									{/if}

									<div class="message-actions-wrapper">
										<MessageActions
											showRegenerate={false}
											showFeedback={false}
											on:copy={() => handleCopy(message.content)}
											on:exportPdf={() => handleExportMessage(message)}
										/>
									</div>
								{:else if message.isStreaming}
									<div class="typing-indicator">
										<div class="typing-dot"></div>
										<div class="typing-dot"></div>
										<div class="typing-dot"></div>
									</div>
								{/if}
							</div>
						</div>
					</div>
				{/if}
			{/each}
		{/if}
	</div>

	<!-- Input -->
	<div slot="input">
		<ChatInput on:submit={handleSubmit} disabled={$isLoading} />
		<p class="input-hint">{$t('welcome.disclaimer')}</p>
	</div>
</NoraLayout>

<style>
	.messages-scroll {
		min-height: 100%;
		width: 100%;  /* Explicitly fill parent's 800px container */
	}

	/* User Message */
	.message-user {
		display: flex;
		justify-content: flex-end;
		margin-bottom: 24px;
		width: 100%;  /* Explicit: fill parent width (800px container) */
	}

	.user-bubble {
		max-width: 80%;
		padding: var(--space-3, 12px) var(--space-4, 16px);
		background: #E5E7EB;  /* Darker gray for better contrast */
		color: var(--text-primary, #1F2937);
		border-radius: 16px 16px 4px 16px;
		font-size: var(--text-base, 15px);
		line-height: var(--leading-normal, 1.5);
	}

	/* Assistant Message */
	.message-assistant {
		margin-bottom: 24px;
	}

	/* Answer card container */
	.answer-card {
		background: var(--white, #ffffff);
		border: 1px solid var(--slate-200, #e2e8f0);
		border-radius: 12px;
		padding: 20px 24px;
		box-shadow: 0 1px 3px rgba(0, 0, 0, 0.04);
	}

	.message-header {
		display: flex;
		align-items: center;
		flex-wrap: wrap;
		gap: 8px;
		padding-bottom: 12px;
		margin-bottom: 16px;
		border-bottom: 1px solid var(--slate-100, #f1f5f9);
	}

	.message-avatar {
		width: 28px;
		height: 28px;
		border-radius: 50%;
		display: flex;
		align-items: center;
		justify-content: center;
		font-size: 11px;
		font-weight: 600;
		flex-shrink: 0;
	}

	.message-avatar.assistant {
		background: var(--deep-blue, #1e3a5f);
		color: var(--white, #ffffff);
	}

	.message-avatar svg {
		width: 14px;
		height: 14px;
	}

	.message-name {
		font-size: var(--text-sm, 13px);
		font-weight: 600;
		color: var(--slate-900, #0f172a);
	}

	.message-content {
		/* Card provides structure, no extra padding needed */
	}

	.message-text {
		font-size: var(--text-base, 15px);
		color: var(--text-primary, #1F2937);
		line-height: var(--leading-relaxed, 1.7);
	}

	.message-text :global(p) {
		margin-bottom: 12px;
	}

	.message-text :global(p:last-child) {
		margin-bottom: 0;
	}

	/* Headers in reports */
	.message-text :global(h2) {
		font-size: var(--text-lg, 17px);
		font-weight: 600;
		color: var(--slate-900, #0f172a);
		margin: var(--space-6, 24px) 0 var(--space-3, 12px) 0;
		line-height: var(--leading-tight, 1.3);
	}

	.message-text :global(h3) {
		font-size: var(--text-base, 15px);
		font-weight: 600;
		color: var(--slate-800, #1e293b);
		margin: 20px 0 var(--space-2, 8px) 0;
		line-height: var(--leading-tight, 1.3);
	}

	/* Lists with custom bullets */
	.message-text :global(ul) {
		list-style: none;
		padding-left: 0;
		margin: var(--space-4, 16px) 0;
	}

	.message-text :global(ul li) {
		position: relative;
		padding-left: 20px;
		margin-bottom: 10px;
		line-height: var(--leading-relaxed, 1.7);
	}

	.message-text :global(ul li::before) {
		content: '';
		position: absolute;
		left: 0;
		top: 10px;
		width: 6px;
		height: 6px;
		background: var(--blue-500, #3b82f6);
		border-radius: 50%;
	}

	.message-text :global(ol) {
		padding-left: 20px;
		margin: var(--space-4, 16px) 0;
	}

	.message-text :global(ol li) {
		margin-bottom: 10px;
		line-height: var(--leading-relaxed, 1.7);
	}

	/* Tables */
	.message-text :global(table) {
		width: 100%;
		border-collapse: collapse;
		margin: var(--space-4, 16px) 0;
		font-size: 14px;
	}

	.message-text :global(th) {
		background: var(--slate-50, #f8fafc);
		font-weight: 600;
		text-align: left;
		padding: 10px 12px;
		border-bottom: 2px solid var(--slate-200, #e2e8f0);
		color: var(--slate-700, #334155);
	}

	.message-text :global(td) {
		padding: 10px 12px;
		border-bottom: 1px solid var(--slate-100, #f1f5f9);
		color: var(--slate-600, #475569);
	}

	.message-text :global(tr:hover td) {
		background: var(--slate-50, #f8fafc);
	}

	/* Blockquotes */
	.message-text :global(blockquote) {
		margin: var(--space-4, 16px) 0;
		padding: var(--space-3, 12px) var(--space-4, 16px);
		background: var(--slate-50, #f8fafc);
		border-left: 3px solid var(--slate-300, #cbd5e1);
		border-radius: 0 var(--radius-sm, 6px) var(--radius-sm, 6px) 0;
		color: var(--slate-600, #475569);
	}

	.message-text :global(blockquote p) {
		margin: 0;
	}

	/* Citation styles - chips instead of superscript */
	.message-text :global(.citation) {
		display: inline-flex;
		align-items: center;
		justify-content: center;
		padding: 2px 8px;
		background: var(--slate-100, #f1f5f9);
		color: var(--slate-600, #475569);
		font-size: var(--text-xs, 11px);
		font-weight: 500;
		border-radius: 4px;
		border: 1px solid var(--slate-200, #e2e8f0);
		vertical-align: baseline;
		margin: 0 2px;
		cursor: pointer;
		position: relative;
		transition: all 0.15s ease;
	}

	.message-text :global(.citation:hover) {
		background: var(--blue-50, #eff6ff);
		border-color: var(--blue-200, #bfdbfe);
		color: var(--blue-600, #2563eb);
	}

	/* Citation Tooltip */
	.message-text :global(.citation-tooltip) {
		position: absolute;
		bottom: calc(100% + 8px);
		left: 50%;
		transform: translateX(-50%);
		background: var(--slate-800, #1e293b);
		color: var(--white, #ffffff);
		padding: 10px 12px;
		border-radius: var(--radius-sm, 6px);
		font-size: 12px;
		font-weight: 400;
		white-space: nowrap;
		opacity: 0;
		visibility: hidden;
		transition: opacity 0.15s ease, visibility 0.15s ease;
		z-index: 100;
		box-shadow: var(--shadow-md, 0 4px 12px rgba(15, 23, 42, 0.08));
		pointer-events: none;
	}

	.message-text :global(.citation-tooltip::after) {
		content: '';
		position: absolute;
		top: 100%;
		left: 50%;
		transform: translateX(-50%);
		border: 6px solid transparent;
		border-top-color: var(--slate-800, #1e293b);
	}

	.message-text :global(.citation:hover .citation-tooltip) {
		opacity: 1;
		visibility: visible;
	}

	.message-text :global(.citation-tooltip-header) {
		display: flex;
		align-items: center;
		gap: 8px;
		margin-bottom: 4px;
	}

	.message-text :global(.citation-tooltip-icon) {
		width: 16px;
		height: 16px;
		border-radius: 3px;
		display: flex;
		align-items: center;
		justify-content: center;
		flex-shrink: 0;
	}

	.message-text :global(.citation-tooltip-icon.sharepoint) {
		background: #038387;
	}

	.message-text :global(.citation-tooltip-icon.confluence) {
		background: #0052CC;
	}

	.message-text :global(.citation-tooltip-icon.wiki) {
		background: var(--slate-700, #334155);
	}

	.message-text :global(.citation-tooltip-icon.jira) {
		background: #0052CC;
	}

	.message-text :global(.citation-tooltip-icon.web) {
		background: var(--slate-500, #64748b);
	}

	.message-text :global(.citation-tooltip-icon.elasticsearch) {
		background: var(--orange-500, #f97316);
	}

	.message-text :global(.citation-tooltip-title) {
		font-weight: 500;
		color: var(--white, #ffffff);
	}

	.message-text :global(.citation-tooltip-meta) {
		font-size: 11px;
		color: var(--slate-400, #94a3b8);
	}

	/* Empty state */
	.empty-state {
		display: flex;
		flex-direction: column;
		align-items: center;
		justify-content: center;
		min-height: 60vh;
		text-align: center;
		padding: 24px;
	}

	.empty-icon {
		width: 64px;
		height: 64px;
		background: var(--orange-100, #ffedd5);
		border-radius: 16px;
		display: flex;
		align-items: center;
		justify-content: center;
		margin-bottom: 24px;
	}

	.empty-icon svg {
		width: 32px;
		height: 32px;
		color: var(--orange-500, #f97316);
	}

	.empty-state h2 {
		font-size: var(--text-2xl, 24px);
		font-weight: 700;
		color: var(--slate-900, #0f172a);
		margin-bottom: var(--space-3, 12px);
		line-height: var(--leading-tight, 1.3);
	}

	.empty-state p {
		font-size: 15px;
		color: var(--slate-600, #475569);
		max-width: 400px;
		margin-bottom: 24px;
	}

	.suggestion-grid {
		display: grid;
		grid-template-columns: repeat(2, 1fr);
		gap: 12px;
		max-width: 600px;
		margin-bottom: 24px;
	}

	.source-disclaimer {
		font-size: 13px;
		color: var(--slate-500, #64748b);
		max-width: 500px;
	}

	.suggestion-card {
		padding: 16px;
		background: white;
		border: 1px solid var(--slate-200, #e2e8f0);
		border-radius: 10px;
		text-align: left;
		cursor: pointer;
		transition: all 0.15s ease;
	}

	.suggestion-card:hover {
		border-color: var(--blue-300, #93c5fd);
		box-shadow: 0 4px 12px rgba(59, 130, 246, 0.1);
	}

	.suggestion-title {
		display: block;
		font-size: 14px;
		font-weight: 600;
		color: var(--slate-900, #0f172a);
		margin-bottom: 4px;
	}

	.suggestion-desc {
		display: block;
		font-size: 13px;
		color: var(--slate-500, #64748b);
	}

	/* Typing indicator */
	.typing-indicator {
		display: flex;
		align-items: center;
		gap: 4px;
		padding: 8px 0;
	}

	.typing-dot {
		width: 6px;
		height: 6px;
		background: var(--slate-400, #94a3b8);
		border-radius: 50%;
		animation: typing 1.4s infinite ease-in-out;
	}

	.typing-dot:nth-child(1) {
		animation-delay: 0s;
	}

	.typing-dot:nth-child(2) {
		animation-delay: 0.2s;
	}

	.typing-dot:nth-child(3) {
		animation-delay: 0.4s;
	}

	@keyframes typing {
		0%, 60%, 100% {
			transform: translateY(0);
		}
		30% {
			transform: translateY(-4px);
		}
	}

	/* Streaming text with blinking cursor */
	.message-text.streaming::after {
		content: '▋';
		animation: blink 1s steps(2, start) infinite;
		color: var(--blue-500, #3b82f6);
		margin-left: 2px;
	}

	@keyframes blink {
		0%, 100% { opacity: 1; }
		50% { opacity: 0; }
	}

	/* Message actions wrapper - always visible */
	.message-actions-wrapper {
		margin-top: 12px;
	}

	/* Input hint - simplified disclaimer */
	.input-hint {
		font-size: 11px;
		color: var(--slate-400, #94a3b8);
		text-align: center;
		margin-top: 8px;
		margin-bottom: 0;
	}

	@media (max-width: 640px) {
		.suggestion-grid {
			grid-template-columns: 1fr;
		}

		.user-bubble {
			max-width: 85%;
		}
	}
</style>
