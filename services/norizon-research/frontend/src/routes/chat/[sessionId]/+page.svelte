<script lang="ts">
	import { page } from '$app/stores';
	import { onMount, untrack } from 'svelte';
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
	import { currentUser } from '$lib/stores/authStore';
	import { t } from 'svelte-i18n';
	import { SearchAPI, toFrontendSource, getActiveAgent, buildConversationHistory } from '$lib/api/searchApi';
	import type { Message, Source, SearchProgress as SearchProgressType, AgentIteration, ChatContext, Protocol } from '$lib/types';
	import { marked } from 'marked';
	import DOMPurify from 'dompurify';

	let userName = $derived.by(() => {
		const email = $currentUser?.email;
		if (!email) return '';
		const localPart = email.split('@')[0];
		const firstName = localPart.split('.')[0];
		return firstName.charAt(0).toUpperCase() + firstName.slice(1).toLowerCase();
	});

	const suggestionQueries = [
		'Biegeradius Hydraulikrohr',
		'Konstruktionsrichtlinien Spuranzeiger',
		'Fertigungsverfahren Änderungen',
		'Sicherheitsvorschriften Druckbehälter',
	];

	let sessionId = $state('');
	let messages = $state<Message[]>([]);
	let messagesContainer = $state<HTMLDivElement | undefined>(undefined);
	let recentSessions = $state<any[]>([]);
	let isSearching = $state(false);
	let currentProgress = $state<SearchProgressType | null>(null);
	let activeAgent = $state<string | null>(null);
	let agentIterations = $state<AgentIteration[]>([]);
	let sessionContext = $state<ChatContext | null>(null);
	let showContextBanner = $state(true);

	$effect(() => {
		const newId = $page.params.sessionId ?? '';
		untrack(() => {
			if (newId !== sessionId) {
				sessionId = newId;
				if (newId) loadSession(newId);
			}
		});
	});

	async function loadSession(id: string) {
		const sessionsMap = $sessions;
		if (!sessionsMap.has(id)) {
			const loaded = await chatStore.loadSessionFromDatabase(id);
			if (!loaded) {
				chatStore.createSession(id);
			}
		}

		currentSessionId.set(id);
		await new Promise(resolve => setTimeout(resolve, 0));

		const query = $page.url.searchParams.get('q');
		const session = $sessions.get(id);
		if (query && session && session.messages.length === 0) {
			setTimeout(() => {
				handleSubmit(query);
			}, 100);
		}
	}

	$effect(() => {
		const session = $currentSession;
		untrack(() => {
			if (session) {
				messages = [...session.messages];

				if (messages.length > 0) {
					if (!currentProgress) {
						isSearching = false;
					}
				}

				sessionContext = session.context || null;
				showContextBanner = !!session.context;
			}
		});
	});

	$effect(() => {
		if ($currentSession) {
			setTimeout(() => scrollToBottom(), 100);
		}
	});

	function scrollToBottom() {
		if (messagesContainer) {
			messagesContainer.scrollTop = messagesContainer.scrollHeight;
		}
	}

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

		if (protocol.decisions && protocol.decisions.length > 0) {
			parts.push(`\n## Decisions\n${protocol.decisions.map((d: string, i: number) => `${i + 1}. ${d}`).join('\n')}`);
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

		if (protocol.nextSteps && protocol.nextSteps.length > 0) {
			parts.push(`\n## Next Steps\n${protocol.nextSteps.map((s: string, i: number) => `${i + 1}. ${s}`).join('\n')}`);
		}

		return parts.join('\n');
	}

	async function handleSubmit(query: string) {
		const currentMessages = $currentSession?.messages || [];
		const conversationHistory = buildConversationHistory(currentMessages);

		let documentContext: string | undefined;
		if (sessionContext?.protocol) {
			documentContext = buildProtocolContext(sessionContext.protocol);
		}

		const userMessage: Message = {
			id: `msg-${Date.now()}-user`,
			role: 'user',
			content: query,
			timestamp: Date.now()
		};
		chatStore.addMessage(userMessage);

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
			const job = await SearchAPI.startSearch({
				query,
				conversation_history: conversationHistory.length > 0 ? conversationHistory : undefined,
				document_context: documentContext
			});

			chatStore.updateMessage(assistantMessageId, { jobId: job.job_id });

			for await (const event of SearchAPI.streamSearch(job.job_id)) {
				switch (event.type) {
					case 'progress':
						if (event.phase === 'analyzing' || event.phase === 'generating_report') {
							agentIterations = agentIterations.map(ai =>
								ai.status === 'thinking' ? { ...ai, status: 'done' as const } : ai
							);

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
						agentIterations = agentIterations.map(ai =>
							(ai.iterationNumber < event.iteration_number && ai.status === 'searching') ||
							ai.status === 'thinking'
								? { ...ai, status: 'done' as const }
								: ai
						);

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

						if (event.tools_called.length > 0) {
							activeAgent = event.tools_called[0];
							chatStore.updateMessage(assistantMessageId, { activeAgent });
						}
						break;

					case 'agent_status':
						if (event.status === 'searching') {
							agentIterations = agentIterations.map(ai =>
								ai.status === 'thinking' ? { ...ai, status: 'done' as const } : ai
							);

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
						chatStore.appendToMessage(assistantMessageId, event.content);
						break;

					case 'complete':
						const result = event.result;
						const sources: Source[] = result.sources.map((s: any) => toFrontendSource(s));

						const finalIterations = agentIterations.map(ai => ({
							...ai,
							status: 'done' as const
						}));

						let currentContent = '';
						currentSession.subscribe(session => {
							const msg = session?.messages.find(m => m.id === assistantMessageId);
							currentContent = msg?.content || '';
						})();

						const shouldUseCompleteContent = currentContent.length < 100;

						chatStore.updateMessage(assistantMessageId, {
							...(shouldUseCompleteContent ? { content: result.final_report || result.concise_answer } : {}),
							sources,
							isStreaming: false,
							confidence: result.confidence_score,
							activeAgent: activeAgent || 'Knowledge Search',
							agentIterations: finalIterations
						});

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
						break;
				}
			}
		} catch (error) {
			console.error('Search failed:', error);
			chatStore.updateMessage(assistantMessageId, {
				content: 'Es ist ein Fehler aufgetreten. Bitte versuchen Sie es erneut.',
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

	function handleSelectSession(sessionId: string) {
		goto(`/chat/${sessionId}`);
	}

	function handleCopy(content: string) {
		navigator.clipboard.writeText(content);
	}

	async function handleExportMessage(message: Message) {
		try {
			const protocol = {
				title: $currentSession?.title || "Nora Research Result",
				date: new Date(message.timestamp).toLocaleDateString('de-DE', {
					year: 'numeric',
					month: 'long',
					day: 'numeric'
				}),
				attendees: [],
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
							`${idx + 1}. ${source.title}\n   ${source.url}${source.snippet ? '\n   ' + source.snippet : ''}`
						).join('\n\n')
					}
				] : []
			};

			const WORKFLOW_API_URL = import.meta.env.VITE_WORKFLOW_API_URL || 'http://localhost:8001';
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
			alert('Export fehlgeschlagen. Bitte erneut versuchen.');
		}
	}

	function handleContextDismiss() {
		showContextBanner = false;
	}

	function handleSelectPrompt(prompt: string) {
		handleSubmit(prompt);
	}

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

	function stripDebugText(content: string): string {
		let cleaned = content;
		cleaned = cleaned.replace(/\(hypothetical[^)]*\)/gi, '');
		cleaned = cleaned.replace(/\(placeholder[^)]*\)/gi, '');
		cleaned = cleaned.replace(/\[DEBUG[^\]]*\]/gi, '');
		cleaned = cleaned.replace(/\[PLACEHOLDER[^\]]*\]/gi, '');
		cleaned = cleaned.replace(/  +/g, ' ');
		cleaned = cleaned.replace(/\n\n\n+/g, '\n\n');
		return cleaned.trim();
	}

	function renderContent(content: string, sources: Source[] = [], messageId: string = ''): string {
		let processed = stripDebugText(content);

		if (sources.length > 0) {
			processed = processed.replace(/\[(\d+)\]/g, (match, num) => {
				const idx = parseInt(num) - 1;
				if (idx >= 0 && idx < sources.length) {
					const source = sources[idx];
					const sourceType = getSourceTypeClass(source.sourceType);
					const sourceLabel = getSourceTypeLabel(source.sourceType);
					const lastUpdated = source.lastUpdated || '';

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

		const html = marked(processed) as string;
		return DOMPurify.sanitize(html, {
			ADD_ATTR: ['onclick', 'data-source'],
			ADD_TAGS: ['span']
		});
	}

	function scrollToSource(messageId: string, sourceNumber: number) {
		const sourceCard = document.getElementById(`source-${messageId}-${sourceNumber}`);
		if (sourceCard) {
			sourceCard.scrollIntoView({ behavior: 'smooth', block: 'center' });
			sourceCard.classList.add('highlighted');
			setTimeout(() => {
				sourceCard.classList.remove('highlighted');
			}, 2000);
		}
	}

	onMount(() => {
		(window as any).scrollToSource = scrollToSource;
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
	currentSessionId={sessionId}
	onnewChat={handleNewChat}
	onselectSession={handleSelectSession}
>
	{#snippet children()}
		<div bind:this={messagesContainer} class="messages-scroll">
			{#if sessionContext && showContextBanner && messages.length === 0}
				<ContextBanner
					context={sessionContext}
					ondismiss={handleContextDismiss}
					onselectPrompt={handleSelectPrompt}
				/>
			{/if}

			{#if messages.length === 0}
				<div class="empty-state">
					<div class="greeting-section">
						<div class="greeting-row">
							<img src="/favicon.png" alt="Nora" class="greeting-logo" />
							<h1 class="greeting-title">{$t('welcome.greeting', { values: { name: userName } })}</h1>
						</div>
					</div>
					<div class="centered-input">
						<ChatInput onSubmit={handleSubmit} disabled={$isLoading} />
						<p class="input-hint">{$t('welcome.disclaimer')}</p>
						<div class="source-logos">
							<div class="source-logo" title="Confluence">
								<svg viewBox="0 0 256 246" width="24" height="24">
									<defs><linearGradient id="conf-a" x1="99.14%" y1="112.05%" x2="33.86%" y2="69.22%"><stop offset="0%" stop-color="#0052CC"/><stop offset="92.3%" stop-color="#2684FF"/></linearGradient><linearGradient id="conf-b" x1=".86%" y1="-12.31%" x2="66.14%" y2="30.54%"><stop offset="0%" stop-color="#0052CC"/><stop offset="92.3%" stop-color="#2684FF"/></linearGradient></defs>
									<path d="M9.26 187.38c-3.6 5.98-7.74 13-10.7 18.1a8.58 8.58 0 0 0 3.2 11.72l56.16 33.68a8.58 8.58 0 0 0 11.88-2.98c2.58-4.42 5.88-10.14 9.52-16.46 25.64-44.56 51.34-39.2 98.18-17.94l55.66 25.08a8.58 8.58 0 0 0 11.24-4.5l25.2-58.28a8.58 8.58 0 0 0-4.32-11.1c-16.78-7.66-50.26-22.92-83.88-38.32C111.18 93.2 42.96 117.78 9.26 187.38Z" fill="url(#conf-a)"/>
									<path d="M246.74 58.86c3.6-5.98 7.74-13 10.7-18.1a8.58 8.58 0 0 0-3.2-11.72L198.08-4.64a8.58 8.58 0 0 0-11.88 2.98c-2.58 4.42-5.88 10.14-9.52 16.46-25.64 44.56-51.34 39.2-98.18 17.94L23.08 7.88a8.58 8.58 0 0 0-11.24 4.5L-13.36 70.66a8.58 8.58 0 0 0 4.32 11.1c16.78 7.66 50.26 22.92 83.88 38.32 69.22 33.18 137.44 8.6 171.14-60.98l.76-.24Z" fill="url(#conf-b)"/>
								</svg>
							</div>
							<div class="source-logo" title="Jira">
								<svg viewBox="0 0 256 256" width="24" height="24">
									<defs><linearGradient id="jira-a" x1="98.03%" y1="0.22%" x2="58.17%" y2="40.08%"><stop offset="18%" stop-color="#0052CC"/><stop offset="100%" stop-color="#2684FF"/></linearGradient><linearGradient id="jira-b" x1="100.97%" y1=".44%" x2="55.94%" y2="44.47%"><stop offset="18%" stop-color="#0052CC"/><stop offset="100%" stop-color="#2684FF"/></linearGradient></defs>
									<path d="M244.66 0H121.72L0 121.72l61.2 61.2 60.52-60.52L182.92 61.2 244.66 0Z" fill="#2684FF"/>
									<path d="M182.52 121.32 121.72 182.12 61.2 121.72 0 182.92l121.72 121.72 121.72-121.72-60.92-61.6Z" fill="#2684FF"/>
									<path d="M121.72 61.2 61.2 121.72 121.72 182.12l60.8-60.8-60.8-60.12Z" fill="url(#jira-a)"/>
								</svg>
							</div>
							<div class="source-logo" title="Internal Knowledge Base">
								<svg viewBox="0 0 24 24" width="24" height="24" fill="none" stroke="#6366f1" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
									<ellipse cx="12" cy="5" rx="9" ry="3"/>
									<path d="M3 5v14c0 1.66 4.03 3 9 3s9-1.34 9-3V5"/>
									<path d="M3 12c0 1.66 4.03 3 9 3s9-1.34 9-3"/>
								</svg>
							</div>
						</div>
					</div>
					<div class="suggestion-chips">
						{#each suggestionQueries as query}
							<button class="suggestion-chip" onclick={() => handleSubmit(query)}>
								{query}
								<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" class="chip-arrow">
									<path d="M5 12h14M12 5l7 7-7 7"/>
								</svg>
							</button>
						{/each}
					</div>
				</div>
			{:else}
				{#each messages as message, idx (message.id)}
					{#if message.role === 'user'}
						<div class="message-user">
							<div class="user-bubble">{message.content}</div>
						</div>
					{:else if message.role === 'assistant'}
						<div class="message-assistant">
							<div class="answer-card">
								<div class="message-header">
									<div class="message-avatar assistant">
										<img src="/favicon.png" alt="Nora" class="avatar-img" />
									</div>
									<span class="message-name">Nora</span>
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
										{#if !message.content}
											<SearchProgress progress={currentProgress} isComplete={false} />
											<SkeletonLoading showSources={true} />
										{/if}

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
												oncopy={() => handleCopy(message.content)}
												onexportPdf={() => handleExportMessage(message)}
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
	{/snippet}

	{#snippet input()}
		{#if messages.length > 0}
			<ChatInput onSubmit={handleSubmit} disabled={$isLoading} />
			<p class="input-hint">{$t('welcome.disclaimer')}</p>
		{/if}
	{/snippet}
</NoraLayout>

<style>
	.messages-scroll {
		min-height: 100%;
		width: 100%;
	}

	/* User Message */
	.message-user {
		display: flex;
		justify-content: flex-end;
		margin-bottom: 24px;
		width: 100%;
	}

	.user-bubble {
		max-width: 70%;
		padding: 12px 18px;
		background: #f3f4f6;
		color: #111827;
		border-radius: 20px 20px 4px 20px;
		font-size: 17px;
		line-height: 1.55;
		border: none;
	}

	/* Assistant Message */
	.message-assistant {
		margin-bottom: 24px;
	}

	.answer-card {
		background: transparent;
		border: none;
		border-radius: 0;
		padding: 0;
	}

	.message-header {
		display: flex;
		align-items: center;
		flex-wrap: wrap;
		gap: 10px;
		margin-bottom: 12px;
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
		background: transparent;
	}

	.message-avatar svg {
		width: 14px;
		height: 14px;
	}

	.avatar-img {
		width: 28px;
		height: 28px;
		object-fit: contain;
	}

	.message-name {
		font-size: 17px;
		font-weight: 600;
		color: #111827;
	}

	.message-content {
		/* Card provides structure */
	}

	.message-text {
		font-size: 17px;
		color: #374151;
		line-height: 1.7;
	}

	.message-text :global(p) {
		margin-bottom: 12px;
	}

	.message-text :global(p:last-child) {
		margin-bottom: 0;
	}

	.message-text :global(h2) {
		font-size: 20px;
		font-weight: 600;
		color: #111827;
		margin: 24px 0 12px 0;
		line-height: 1.3;
	}

	.message-text :global(h3) {
		font-size: 18px;
		font-weight: 600;
		color: #111827;
		margin: 20px 0 8px 0;
		line-height: 1.3;
	}

	.message-text :global(ul) {
		list-style: none;
		padding-left: 0;
		margin: 16px 0;
	}

	.message-text :global(ul li) {
		position: relative;
		padding-left: 20px;
		margin-bottom: 10px;
		line-height: 1.7;
	}

	.message-text :global(ul li::before) {
		content: '';
		position: absolute;
		left: 0;
		top: 10px;
		width: 6px;
		height: 6px;
		background: #3b82f6;
		border-radius: 50%;
	}

	.message-text :global(ol) {
		padding-left: 20px;
		margin: 16px 0;
	}

	.message-text :global(ol li) {
		margin-bottom: 10px;
		line-height: 1.7;
	}

	.message-text :global(table) {
		width: 100%;
		border-collapse: collapse;
		margin: 16px 0;
		font-size: 16px;
	}

	.message-text :global(th) {
		background: #f8fafc;
		font-weight: 600;
		text-align: left;
		padding: 10px 12px;
		border-bottom: 2px solid #e2e8f0;
		color: #334155;
	}

	.message-text :global(td) {
		padding: 10px 12px;
		border-bottom: 1px solid #f1f5f9;
		color: #475569;
	}

	.message-text :global(tr:hover td) {
		background: #f8fafc;
	}

	.message-text :global(blockquote) {
		margin: 16px 0;
		padding: 12px 16px;
		background: #f8fafc;
		border-left: 3px solid #cbd5e1;
		border-radius: 0 6px 6px 0;
		color: #475569;
	}

	.message-text :global(blockquote p) {
		margin: 0;
	}

	/* Citation styles */
	.message-text :global(.citation) {
		display: inline-flex;
		align-items: center;
		justify-content: center;
		padding: 1px 6px;
		background: #ffedd5;
		color: #c2410c;
		font-size: 11px;
		font-weight: 600;
		border-radius: 4px;
		border: 1px solid #fed7aa;
		vertical-align: baseline;
		margin: 0 2px;
		cursor: pointer;
		position: relative;
		transition: all 0.15s ease;
	}

	.message-text :global(.citation:hover) {
		background: #eff6ff;
		border-color: #bfdbfe;
		color: #2563eb;
	}

	.message-text :global(.citation-tooltip) {
		position: absolute;
		bottom: calc(100% + 8px);
		left: 50%;
		transform: translateX(-50%);
		background: #1e293b;
		color: #ffffff;
		padding: 10px 12px;
		border-radius: 6px;
		font-size: 12px;
		font-weight: 400;
		white-space: nowrap;
		opacity: 0;
		visibility: hidden;
		transition: opacity 0.15s ease, visibility 0.15s ease;
		z-index: 100;
		box-shadow: 0 4px 12px rgba(15, 23, 42, 0.08);
		pointer-events: none;
	}

	.message-text :global(.citation-tooltip::after) {
		content: '';
		position: absolute;
		top: 100%;
		left: 50%;
		transform: translateX(-50%);
		border: 6px solid transparent;
		border-top-color: #1e293b;
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

	.message-text :global(.citation-tooltip-icon.sharepoint) { background: #038387; }
	.message-text :global(.citation-tooltip-icon.confluence) { background: #0052CC; }
	.message-text :global(.citation-tooltip-icon.wiki) { background: #334155; }
	.message-text :global(.citation-tooltip-icon.jira) { background: #0052CC; }
	.message-text :global(.citation-tooltip-icon.web) { background: #64748b; }
	.message-text :global(.citation-tooltip-icon.elasticsearch) { background: #f97316; }

	.message-text :global(.citation-tooltip-title) {
		font-weight: 500;
		color: #ffffff;
	}

	.message-text :global(.citation-tooltip-meta) {
		font-size: 11px;
		color: #94a3b8;
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

	.greeting-section {
		display: flex;
		flex-direction: column;
		align-items: center;
		margin-bottom: 32px;
	}

	.greeting-row {
		display: flex;
		align-items: center;
		gap: 16px;
		margin-bottom: 8px;
	}

	.greeting-logo {
		width: 56px;
		height: 56px;
		object-fit: contain;
		flex-shrink: 0;
	}

	.greeting-title {
		font-size: 32px;
		font-weight: 600;
		color: #111827;
		margin: 0;
	}

	.greeting-subtitle {
		font-size: 16px;
		color: #6b7280;
		margin-bottom: 32px;
	}

	.centered-input {
		width: 100%;
		max-width: 680px;
		margin-bottom: 24px;
	}

	.suggestion-chips {
		display: flex;
		flex-direction: column;
		gap: 8px;
		max-width: 480px;
		width: 100%;
	}

	.suggestion-chip {
		display: flex;
		flex-direction: row;
		justify-content: space-between;
		align-items: center;
		padding: 14px 18px;
		background: #f9fafb;
		border: 1px solid #e5e7eb;
		border-radius: 12px;
		font-size: 16px;
		color: #374151;
		cursor: pointer;
		text-align: left;
		width: 100%;
		transition: background 0.15s, border-color 0.15s;
	}

	.suggestion-chip:hover {
		background: #f3f4f6;
		border-color: #d1d5db;
	}

	.chip-arrow {
		width: 16px;
		height: 16px;
		color: #9ca3af;
		flex-shrink: 0;
		transition: color 0.15s;
	}

	.suggestion-chip:hover .chip-arrow {
		color: #6b7280;
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
		background: #94a3b8;
		border-radius: 50%;
		animation: typing 1.4s infinite ease-in-out;
	}

	.typing-dot:nth-child(1) { animation-delay: 0s; }
	.typing-dot:nth-child(2) { animation-delay: 0.2s; }
	.typing-dot:nth-child(3) { animation-delay: 0.4s; }

	@keyframes typing {
		0%, 60%, 100% { transform: translateY(0); }
		30% { transform: translateY(-4px); }
	}

	.message-text.streaming::after {
		content: '▋';
		animation: blink 1s steps(2, start) infinite;
		color: #3b82f6;
		margin-left: 2px;
	}

	@keyframes blink {
		0%, 100% { opacity: 1; }
		50% { opacity: 0; }
	}

	.message-actions-wrapper {
		margin-top: 12px;
	}

	.input-hint {
		font-size: 12px;
		color: #9ca3af;
		text-align: center;
		margin-top: 10px;
		margin-bottom: 0;
	}

	.source-logos {
		display: flex;
		justify-content: center;
		gap: 32px;
		margin-top: 16px;
	}

	.source-logo {
		display: flex;
		flex-direction: column;
		align-items: center;
		gap: 6px;
		opacity: 0.65;
		transition: opacity 0.2s;
	}

	.source-logo:hover {
		opacity: 0.9;
	}


	@media (max-width: 640px) {
		.suggestion-chips {
			max-width: 100%;
		}

		.user-bubble {
			max-width: 85%;
		}
	}
</style>
