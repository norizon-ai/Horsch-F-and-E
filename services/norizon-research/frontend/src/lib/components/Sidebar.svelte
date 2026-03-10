<script lang="ts">
	import { createEventDispatcher, onMount } from "svelte";
	import { goto } from "$app/navigation";
	import type { ChatSession, DateGroup } from "$lib/types";
	import { t } from "svelte-i18n";
	import { historyStore, historySessions } from "$lib/stores/historyStore";
	import { isAuthenticated } from "$lib/stores/authStore";

	export let currentSessionId: string | null = null;
	export let collapsed: boolean = false;

	const dispatch = createEventDispatcher<{
		newChat: void;
		selectSession: string;
		toggleCollapse: void;
	}>();

	// Load sessions from history store
	$: sessions = $historySessions;

	// Search state
	let searchQuery = "";

	// Rename state
	let editingId: string | null = null;
	let editingTitle: string = "";

	// Load history when authenticated
	onMount(() => {
		if ($isAuthenticated) {
			historyStore.loadHistory();
		}
	});

	// Reload history when authentication status changes
	$: if ($isAuthenticated) {
		historyStore.loadHistory();
	}

	async function handleDelete(sessionId: string, event: MouseEvent) {
		event.stopPropagation();

		if (confirm("Are you sure you want to delete this chat?")) {
			await historyStore.deleteItem(sessionId);
		}
	}

	function handleDoubleClick(session: ChatSession, event: MouseEvent) {
		event.stopPropagation();
		editingId = session.id;
		editingTitle = session.title;
	}

	async function handleRenameSubmit(sessionId: string) {
		if (
			editingTitle.trim() &&
			editingTitle !== sessions.find((s) => s.id === sessionId)?.title
		) {
			await historyStore.updateTitle(sessionId, editingTitle.trim());
		}
		editingId = null;
		editingTitle = "";
	}

	function handleRenameCancel() {
		editingId = null;
		editingTitle = "";
	}

	function handleRenameKeydown(event: KeyboardEvent, sessionId: string) {
		if (event.key === "Enter") {
			event.preventDefault();
			handleRenameSubmit(sessionId);
		} else if (event.key === "Escape") {
			event.preventDefault();
			handleRenameCancel();
		}
	}

	function toggleCollapse() {
		dispatch("toggleCollapse");
	}

	// Format timestamp for display
	function formatTimestamp(timestamp: number): string {
		const date = new Date(timestamp);
		const now = new Date();
		const today = new Date(
			now.getFullYear(),
			now.getMonth(),
			now.getDate(),
		);
		const yesterday = new Date(today);
		yesterday.setDate(yesterday.getDate() - 1);

		if (timestamp >= today.getTime()) {
			// Today: show time only "14:32"
			return date.toLocaleTimeString("de-DE", {
				hour: "2-digit",
				minute: "2-digit",
			});
		} else if (timestamp >= yesterday.getTime()) {
			// Yesterday: show time
			return date.toLocaleTimeString("de-DE", {
				hour: "2-digit",
				minute: "2-digit",
			});
		} else {
			// Older: show date "12. Jan"
			return date.toLocaleDateString("de-DE", {
				day: "numeric",
				month: "short",
			});
		}
	}

	// Filter sessions based on search query
	$: filteredSessions = searchQuery
		? sessions.filter((s) =>
				s.title.toLowerCase().includes(searchQuery.toLowerCase()),
			)
		: sessions;

	// Group sessions by date (reactive to translations and filtered sessions)
	$: groupedSessions = groupByDate(
		filteredSessions.sort((a, b) => b.updatedAt - a.updatedAt),
	);

	function groupByDate(sessions: ChatSession[]): DateGroup[] {
		const now = new Date();
		const today = new Date(
			now.getFullYear(),
			now.getMonth(),
			now.getDate(),
		);
		const yesterday = new Date(today);
		yesterday.setDate(yesterday.getDate() - 1);
		const lastWeek = new Date(today);
		lastWeek.setDate(lastWeek.getDate() - 7);

		const groups: DateGroup[] = [];

		const todaySessions = sessions.filter(
			(s) => s.updatedAt >= today.getTime(),
		);
		const yesterdaySessions = sessions.filter(
			(s) =>
				s.updatedAt >= yesterday.getTime() &&
				s.updatedAt < today.getTime(),
		);
		const lastWeekSessions = sessions.filter(
			(s) =>
				s.updatedAt >= lastWeek.getTime() &&
				s.updatedAt < yesterday.getTime(),
		);
		const olderSessions = sessions.filter(
			(s) => s.updatedAt < lastWeek.getTime(),
		);

		if (todaySessions.length > 0) {
			groups.push({ label: $t("chat.today"), sessions: todaySessions });
		}
		if (yesterdaySessions.length > 0) {
			groups.push({
				label: $t("chat.yesterday"),
				sessions: yesterdaySessions,
			});
		}
		if (lastWeekSessions.length > 0) {
			groups.push({
				label: $t("chat.last_week"),
				sessions: lastWeekSessions,
			});
		}
		if (olderSessions.length > 0) {
			groups.push({ label: $t("chat.older"), sessions: olderSessions });
		}

		return groups;
	}

	function clearSearch() {
		searchQuery = "";
	}

	function handleSessionClick(session: ChatSession) {
		// Route to appropriate viewer based on workflow type
		if (session.workflowType === "Meeting Documentation") {
			goto(`/protocol/${session.id}`);
		} else {
			// Default to chat view for Search and other workflows
			dispatch("selectSession", session.id);
		}
	}
</script>

<aside class="sidebar" class:collapsed>
	<div class="sidebar-header">
		<button
			class="logo"
			on:click={() => dispatch("newChat")}
			title="New Chat"
		>
			<img src="/norizon-logo.png" alt="Norizon" class="logo-img" />
			{#if !collapsed}
				<span class="logo-text">Nora</span>
			{/if}
		</button>
		<button
			class="collapse-btn"
			on:click={toggleCollapse}
			title={collapsed ? "Expand" : "Collapse"}
		>
			<svg
				viewBox="0 0 24 24"
				fill="none"
				stroke="currentColor"
				stroke-width="2"
			>
				{#if collapsed}
					<polyline points="9 18 15 12 9 6" />
				{:else}
					<polyline points="15 18 9 12 15 6" />
				{/if}
			</svg>
		</button>
	</div>

	<button
		class="new-chat-btn"
		on:click={() => dispatch("newChat")}
		title={$t("chat.new_chat")}
	>
		<svg
			viewBox="0 0 24 24"
			fill="none"
			stroke="currentColor"
			stroke-width="2"
		>
			<line x1="12" y1="5" x2="12" y2="19" />
			<line x1="5" y1="12" x2="19" y2="12" />
		</svg>
		{#if !collapsed}
			<span>{$t("chat.new_chat")}</span>
		{/if}
	</button>

	<!-- Search bar (only when expanded) -->
	{#if !collapsed}
		<div class="search-bar-container">
			<svg
				class="search-icon"
				viewBox="0 0 24 24"
				fill="none"
				stroke="currentColor"
				stroke-width="2"
			>
				<circle cx="11" cy="11" r="8" />
				<path d="m21 21-4.35-4.35" />
			</svg>
			<input
				type="text"
				bind:value={searchQuery}
				placeholder={$t("chat.search_placeholder")}
				class="search-input"
			/>
			{#if searchQuery}
				<button class="search-clear" on:click={clearSearch}>
					<svg
						viewBox="0 0 24 24"
						fill="none"
						stroke="currentColor"
						stroke-width="2"
					>
						<line x1="18" y1="6" x2="6" y2="18" />
						<line x1="6" y1="6" x2="18" y2="18" />
					</svg>
				</button>
			{/if}
		</div>
	{/if}

	<div class="chat-history">
		{#each groupedSessions as group}
			<div class="history-section">
				{#if !collapsed}
					<div class="history-label">{group.label}</div>
				{/if}
				{#each group.sessions as session}
					<div class="history-item-wrapper">
						<button
							class="history-item"
							class:active={session.id === currentSessionId}
							on:click={() => handleSessionClick(session)}
							on:dblclick={(e) => handleDoubleClick(session, e)}
							title={session.title}
						>
							{#if !collapsed}
								<div class="history-icon">
									{#if session.workflowType === "Meeting Documentation"}
										<svg
											viewBox="0 0 24 24"
											fill="none"
											stroke="currentColor"
											stroke-width="2"
										>
											<path
												d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"
											></path>
											<polyline points="14 2 14 8 20 8"
											></polyline>
											<line x1="16" y1="13" x2="8" y2="13"
											></line>
											<line x1="16" y1="17" x2="8" y2="17"
											></line>
											<polyline points="10 9 9 9 8 9"
											></polyline>
										</svg>
									{:else}
										<svg
											viewBox="0 0 24 24"
											fill="none"
											stroke="currentColor"
											stroke-width="2"
										>
											<circle cx="11" cy="11" r="8" />
											<path d="m21 21-4.35-4.35" />
										</svg>
									{/if}
								</div>
								<div class="history-content">
									{#if editingId === session.id}
										<input
											class="rename-input"
											type="text"
											bind:value={editingTitle}
											on:blur={() =>
												handleRenameSubmit(session.id)}
											on:keydown={(e) =>
												handleRenameKeydown(
													e,
													session.id,
												)}
											on:click={(e) =>
												e.stopPropagation()}
										/>
									{:else}
										<div class="history-title">
											{session.title}
										</div>
										<span class="history-timestamp"
											>{formatTimestamp(
												session.updatedAt,
											)}</span
										>
									{/if}
								</div>
							{:else}
								<!-- Show icon only in collapsed state for navigation -->
								<div class="history-icon collapsed-icon">
									{#if session.workflowType === "Meeting Documentation"}
										<svg
											viewBox="0 0 24 24"
											fill="none"
											stroke="currentColor"
											stroke-width="2"
										>
											<path
												d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"
											></path>
											<polyline points="14 2 14 8 20 8"
											></polyline>
											<line x1="16" y1="13" x2="8" y2="13"
											></line>
											<line x1="16" y1="17" x2="8" y2="17"
											></line>
											<polyline points="10 9 9 9 8 9"
											></polyline>
										</svg>
									{:else}
										<svg
											viewBox="0 0 24 24"
											fill="none"
											stroke="currentColor"
											stroke-width="2"
										>
											<circle cx="11" cy="11" r="8" />
											<path d="m21 21-4.35-4.35" />
										</svg>
									{/if}
								</div>
							{/if}
						</button>
						{#if !collapsed && editingId !== session.id}
							<button
								class="delete-btn"
								on:click={(e) => handleDelete(session.id, e)}
								title="Delete chat"
								aria-label="Delete chat"
							>
								<svg
									viewBox="0 0 24 24"
									fill="none"
									stroke="currentColor"
									stroke-width="2"
								>
									<path
										d="M3 6h18M19 6v14a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2V6m3 0V4a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2"
									/>
								</svg>
							</button>
						{/if}
					</div>
				{/each}
			</div>
		{/each}

		{#if sessions.length === 0 && !collapsed}
			<div class="empty-state">
				<p>{$t("chat.no_chats")}</p>
				<p class="empty-hint">{$t("chat.no_chats_hint")}</p>
			</div>
		{/if}

		{#if searchQuery && filteredSessions.length === 0 && !collapsed}
			<div class="empty-state">
				<p>Keine Ergebnisse</p>
			</div>
		{/if}
	</div>
</aside>

<style>
	.sidebar {
		width: 280px;
		background: var(--white, #ffffff);
		border-right: 1px solid var(--slate-200, #e2e8f0);
		display: flex;
		flex-direction: column;
		flex-shrink: 0;
		position: fixed;
		height: 100vh;
		z-index: 10;
		transition: width 0.2s ease;
	}

	.sidebar.collapsed {
		width: 72px;
	}

	.sidebar-header {
		padding: 16px;
		border-bottom: 1px solid var(--slate-100, #f1f5f9);
		display: flex;
		align-items: center;
		justify-content: space-between;
		gap: 8px;
	}

	.sidebar.collapsed .sidebar-header {
		padding: 16px 12px;
		justify-content: center;
	}

	.logo {
		display: flex;
		align-items: center;
		gap: 10px;
		text-decoration: none;
		background: none;
		border: none;
		padding: 0;
		cursor: pointer;
		transition: opacity 0.15s ease;
	}

	.logo:hover {
		opacity: 0.8;
	}

	.logo-img {
		width: 36px;
		height: 36px;
		object-fit: contain;
		flex-shrink: 0;
	}

	.logo-text {
		font-family: "Inter", sans-serif;
		font-size: 22px;
		font-weight: 700;
		color: var(--deep-blue, #1e3a5f);
	}

	.collapse-btn {
		width: 28px;
		height: 28px;
		background: transparent;
		border: 1px solid var(--slate-200, #e2e8f0);
		border-radius: var(--radius-sm, 6px);
		cursor: pointer;
		color: var(--slate-400, #94a3b8);
		display: flex;
		align-items: center;
		justify-content: center;
		transition: all 0.15s ease;
		flex-shrink: 0;
	}

	.collapse-btn:hover {
		background: var(--slate-100, #f1f5f9);
		color: var(--slate-600, #475569);
	}

	.collapse-btn svg {
		width: 14px;
		height: 14px;
	}

	.sidebar.collapsed .collapse-btn {
		position: absolute;
		right: -14px;
		top: 20px;
		background: var(--white, #ffffff);
		border: 1px solid var(--slate-200, #e2e8f0);
		box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
	}

	.new-chat-btn {
		margin: 16px 16px 12px;
		padding: 10px 16px;
		background: var(--deep-blue, #1e3a5f);
		color: var(--white, #ffffff);
		border: none;
		border-radius: var(--radius-md, 10px);
		font-size: 13px;
		font-weight: 500;
		cursor: pointer;
		display: flex;
		align-items: center;
		justify-content: center;
		gap: 8px;
		transition: background 0.15s ease;
	}

	.sidebar.collapsed .new-chat-btn {
		margin: 12px;
		padding: 10px;
	}

	.new-chat-btn:hover {
		background: #162d4a;
	}

	.new-chat-btn svg {
		width: 16px;
		height: 16px;
		flex-shrink: 0;
	}

	/* Search bar */
	.search-bar-container {
		margin: 0 16px 12px;
		position: relative;
		display: flex;
		align-items: center;
	}

	.search-icon {
		position: absolute;
		left: 10px;
		width: 14px;
		height: 14px;
		color: var(--slate-400, #94a3b8);
		pointer-events: none;
	}

	.search-input {
		width: 100%;
		padding: 8px 32px 8px 32px;
		border: 1px solid var(--slate-200, #e2e8f0);
		border-radius: var(--radius-sm, 6px);
		font-size: 13px;
		color: var(--slate-700, #334155);
		background: var(--slate-50, #f8fafc);
		outline: none;
		transition:
			border-color 0.15s ease,
			background 0.15s ease;
	}

	.search-input:focus {
		border-color: var(--blue-300, #93c5fd);
		background: var(--white, #ffffff);
	}

	.search-input::placeholder {
		color: var(--slate-400, #94a3b8);
	}

	.search-clear {
		position: absolute;
		right: 8px;
		width: 18px;
		height: 18px;
		padding: 0;
		border: none;
		background: none;
		color: var(--slate-400, #94a3b8);
		cursor: pointer;
		display: flex;
		align-items: center;
		justify-content: center;
	}

	.search-clear:hover {
		color: var(--slate-600, #475569);
	}

	.search-clear svg {
		width: 12px;
		height: 12px;
	}

	.chat-history {
		flex: 1;
		overflow-y: auto;
		padding: 8px 12px;
	}

	.sidebar.collapsed .chat-history {
		padding: 8px;
	}

	.history-section {
		margin-bottom: 20px;
	}

	.sidebar.collapsed .history-section {
		margin-bottom: 8px;
	}

	.history-label {
		font-size: 10px;
		font-weight: 600;
		text-transform: uppercase;
		letter-spacing: 0.8px;
		color: var(--slate-400, #94a3b8);
		padding: 8px 8px 6px;
		margin-bottom: 4px;
	}

	.history-item {
		display: flex;
		align-items: flex-start;
		gap: 10px;
		padding: 10px 12px;
		min-height: 56px;
		border-radius: 10px;
		cursor: pointer;
		transition: background 0.15s ease;
		width: 100%;
		border: none;
		background: none;
		text-align: left;
		margin-bottom: 2px;
		box-sizing: border-box;
	}

	.sidebar.collapsed .history-item {
		padding: var(--space-2, 8px);
		justify-content: center;
		min-height: 40px;
		margin-bottom: 2px;
	}

	.history-item:hover {
		background: var(--slate-100, #f1f5f9);
	}

	.history-item.active {
		background: var(--blue-50, #eff6ff);
	}

	.history-icon {
		width: 28px;
		height: 28px;
		background: var(--slate-100, #f1f5f9);
		border-radius: var(--radius-sm, 6px);
		display: flex;
		align-items: center;
		justify-content: center;
		color: var(--slate-500, #64748b);
		flex-shrink: 0;
		margin-top: 2px;
	}

	.history-icon svg {
		width: 14px;
		height: 14px;
	}

	.history-item.active .history-icon {
		background: var(--blue-100, #dbeafe);
		color: var(--blue-600, #2563eb);
	}

	.history-content {
		flex: 1;
		min-width: 0;
		overflow: hidden;
	}

	.history-title {
		font-size: 13px;
		font-weight: 500;
		color: var(--slate-900, #0f172a);
		display: -webkit-box;
		-webkit-line-clamp: 2;
		-webkit-box-orient: vertical;
		overflow: hidden;
		line-height: 1.35;
		margin-bottom: 2px;
	}

	.history-item.active .history-title {
		font-weight: 600;
	}

	.history-timestamp {
		font-size: 11px;
		color: #9ca3af;
	}

	.empty-state {
		padding: 20px;
		text-align: center;
		color: var(--slate-400, #94a3b8);
	}

	.empty-state p {
		margin: 0;
		font-size: 14px;
	}

	.empty-hint {
		font-size: 12px !important;
		margin-top: 4px !important;
	}

	.history-item-wrapper {
		position: relative;
	}

	.delete-btn {
		position: absolute;
		right: 8px;
		top: 50%;
		transform: translateY(-50%);
		width: 28px;
		height: 28px;
		background: transparent;
		border: none;
		border-radius: var(--radius-sm, 6px);
		cursor: pointer;
		color: var(--slate-400, #94a3b8);
		display: none;
		align-items: center;
		justify-content: center;
		transition: all 0.15s ease;
		z-index: 1;
	}

	.history-item-wrapper:hover .delete-btn {
		display: flex;
	}

	.delete-btn:hover {
		background: var(--red-50, #fef2f2);
		color: var(--red-500, #ef4444);
	}

	.delete-btn svg {
		width: 14px;
		height: 14px;
	}

	.rename-input {
		width: 100%;
		padding: 4px 8px;
		font-size: 13px;
		font-weight: 500;
		color: var(--slate-900, #0f172a);
		background: var(--white, #ffffff);
		border: 1px solid var(--blue-500, #3b82f6);
		border-radius: var(--radius-sm, 6px);
		outline: none;
		font-family: inherit;
	}

	.rename-input:focus {
		border-color: var(--blue-600, #2563eb);
		box-shadow: 0 0 0 2px rgba(59, 130, 246, 0.1);
	}

	@media (max-width: 900px) {
		.sidebar {
			transform: translateX(-100%);
			transition: transform 0.3s ease;
		}

		.sidebar.open {
			transform: translateX(0);
		}
	}
</style>
