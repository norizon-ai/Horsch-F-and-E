<script lang="ts">
	import { onMount, untrack } from "svelte";
	import { goto } from "$app/navigation";
	import { browser } from "$app/environment";
	import type { ChatSession, DateGroup } from "$lib/types";
	import { t } from "svelte-i18n";
	import { historyStore, historySessions } from "$lib/stores/historyStore";
	import { isAuthenticated } from "$lib/stores/authStore";

	let {
		currentSessionId = null as string | null,
		collapsed = false,
		userEmail = undefined as string | undefined,
		userInitial = undefined as string | undefined,
		onnewChat = undefined as (() => void) | undefined,
		onselectSession = undefined as ((sessionId: string) => void) | undefined,
		ontoggleCollapse = undefined as (() => void) | undefined,
		onlogout = undefined as (() => void) | undefined,
	} = $props();

	let sessions = $derived($historySessions);
	let searchQuery = $state("");
	let searchVisible = $state(false);
	let editingId = $state<string | null>(null);
	let editingTitle = $state("");
	let openMenuId = $state<string | null>(null);
	let userDropdownOpen = $state(false);
	let deleteConfirmId = $state<string | null>(null);

	let userName = $derived.by(() => {
		if (!userEmail) return undefined;
		const local = userEmail.split("@")[0] ?? "";
		const first = local.split(".")[0] ?? local;
		return first.charAt(0).toUpperCase() + first.slice(1);
	});

	function loadPinned(): Set<string> {
		if (!browser) return new Set();
		try {
			const raw = localStorage.getItem("pinned-sessions");
			if (raw) return new Set(JSON.parse(raw) as string[]);
		} catch { /* ignore */ }
		return new Set();
	}

	function savePinned(set: Set<string>) {
		if (!browser) return;
		localStorage.setItem("pinned-sessions", JSON.stringify([...set]));
	}

	let pinnedIds = $state<Set<string>>(loadPinned());

	function togglePin(sessionId: string) {
		const next = new Set(pinnedIds);
		if (next.has(sessionId)) next.delete(sessionId);
		else next.add(sessionId);
		pinnedIds = next;
		savePinned(next);
	}

	$effect(() => {
		if ($isAuthenticated) {
			untrack(() => {
				historyStore.loadHistory();
			});
		}
	});

	$effect(() => {
		if (!browser) return;
		function handleDocClick(e: MouseEvent) {
			const target = e.target as Element;
			if (!target.closest(".context-menu-wrapper")) openMenuId = null;
			if (!target.closest(".user-footer-btn") && !target.closest(".user-dropdown")) userDropdownOpen = false;
		}
		document.addEventListener("click", handleDocClick);
		return () => document.removeEventListener("click", handleDocClick);
	});

	function handleDelete(sessionId: string) {
		openMenuId = null;
		deleteConfirmId = sessionId;
	}

	async function confirmDelete() {
		if (deleteConfirmId) {
			const wasCurrentSession = deleteConfirmId === currentSessionId;
			await historyStore.deleteItem(deleteConfirmId);
			deleteConfirmId = null;
			if (wasCurrentSession) {
				goto("/");
			}
		}
	}

	function cancelDelete() {
		deleteConfirmId = null;
	}

	function startRename(session: ChatSession) {
		openMenuId = null;
		editingId = session.id;
		editingTitle = session.title;
	}

	function handleDoubleClick(session: ChatSession, event: MouseEvent) {
		event.stopPropagation();
		editingId = session.id;
		editingTitle = session.title;
	}

	async function handleRenameSubmit(sessionId: string) {
		if (editingTitle.trim() && editingTitle !== sessions.find((s) => s.id === sessionId)?.title) {
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
		if (event.key === "Enter") { event.preventDefault(); handleRenameSubmit(sessionId); }
		else if (event.key === "Escape") { event.preventDefault(); handleRenameCancel(); }
	}

	function openContextMenu(sessionId: string, event: MouseEvent) {
		event.stopPropagation();
		openMenuId = openMenuId === sessionId ? null : sessionId;
	}

	function toggleSearch() {
		searchVisible = !searchVisible;
		if (!searchVisible) searchQuery = "";
	}

	function clearSearch() {
		searchQuery = "";
	}

	let filteredSessions = $derived(
		searchQuery
			? sessions.filter((s) => s.title.toLowerCase().includes(searchQuery.toLowerCase()))
			: sessions,
	);

	let sortedSessions = $derived(
		filteredSessions.slice().sort((a, b) => b.updatedAt - a.updatedAt),
	);

	let pinnedSessions = $derived(sortedSessions.filter((s) => pinnedIds.has(s.id)));
	let unpinnedSessions = $derived(sortedSessions.filter((s) => !pinnedIds.has(s.id)));
	let groupedSessions = $derived(groupByDate(unpinnedSessions));

	function groupByDate(sessionList: ChatSession[]): DateGroup[] {
		const now = new Date();
		const today = new Date(now.getFullYear(), now.getMonth(), now.getDate());
		const yesterday = new Date(today); yesterday.setDate(yesterday.getDate() - 1);
		const lastWeek = new Date(today); lastWeek.setDate(lastWeek.getDate() - 7);

		const groups: DateGroup[] = [];
		const todaySessions = sessionList.filter((s) => s.updatedAt >= today.getTime());
		const yesterdaySessions = sessionList.filter((s) => s.updatedAt >= yesterday.getTime() && s.updatedAt < today.getTime());
		const lastWeekSessions = sessionList.filter((s) => s.updatedAt >= lastWeek.getTime() && s.updatedAt < yesterday.getTime());
		const olderSessions = sessionList.filter((s) => s.updatedAt < lastWeek.getTime());

		if (todaySessions.length > 0) groups.push({ label: $t("chat.today"), sessions: todaySessions });
		if (yesterdaySessions.length > 0) groups.push({ label: $t("chat.yesterday"), sessions: yesterdaySessions });
		if (lastWeekSessions.length > 0) groups.push({ label: $t("chat.last_week"), sessions: lastWeekSessions });
		if (olderSessions.length > 0) groups.push({ label: $t("chat.older"), sessions: olderSessions });
		return groups;
	}

	function handleSessionClick(session: ChatSession) {
		if (session.workflowType === "Meeting Documentation") goto(`/protocol/${session.id}`);
		else onselectSession?.(session.id);
	}
</script>

<aside class="sidebar" class:collapsed>
	<!-- Header: logo + collapse toggle -->
	<div class="sidebar-header">
		{#if collapsed}
			<button
				class="icon-btn collapse-toggle"
				onclick={() => ontoggleCollapse?.()}
				title="Expand sidebar"
				aria-label="Expand sidebar"
			>
				<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
					<rect x="3" y="3" width="18" height="18" rx="2"/>
					<line x1="9" y1="3" x2="9" y2="21"/>
				</svg>
			</button>
		{:else}
			<button class="logo-btn" onclick={() => onnewChat?.()} title="Nora">
				<img src="/favicon.png" alt="Nora" class="logo-img" />
			</button>

			<button
				class="icon-btn collapse-toggle"
				onclick={() => ontoggleCollapse?.()}
				title="Collapse sidebar"
				aria-label="Collapse sidebar"
			>
				<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
					<rect x="3" y="3" width="18" height="18" rx="2"/>
					<line x1="9" y1="3" x2="9" y2="21"/>
				</svg>
			</button>
		{/if}
	</div>

	<!-- Action items: New Chat + Search (like Claude) -->
	<div class="action-items">
		<button
			class="action-item"
			onclick={() => onnewChat?.()}
			title={$t("chat.new_chat")}
		>
			<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
				<path d="M12 20h9"/>
				<path d="M16.5 3.5a2.121 2.121 0 0 1 3 3L7 19l-4 1 1-4L16.5 3.5z"/>
			</svg>
			{#if !collapsed}
				<span>{$t("chat.new_chat")}</span>
			{/if}
		</button>

		<button
			class="action-item"
			class:action-item-active={searchVisible}
			onclick={toggleSearch}
			title={$t("chat.search_placeholder")}
		>
			<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
				<circle cx="11" cy="11" r="8" />
				<path d="m21 21-4.35-4.35" />
			</svg>
			{#if !collapsed}
				<span>{$t("chat.search") ?? "Search"}</span>
			{/if}
		</button>

		<button
			class="action-item"
			onclick={() => goto("/workflow/meeting")}
			title={$t("workflow.meeting.title")}
		>
			<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
				<path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/>
				<polyline points="14 2 14 8 20 8"/>
				<line x1="16" y1="13" x2="8" y2="13"/>
				<line x1="16" y1="17" x2="8" y2="17"/>
				<polyline points="10 9 9 9 8 9"/>
			</svg>
			{#if !collapsed}
				<span>{$t("workflow.meeting.title") ?? "Meeting Documentation"}</span>
			{/if}
		</button>
	</div>

	<!-- Search bar (toggled) -->
	{#if searchVisible && !collapsed}
		<div class="search-bar-container">
			<svg class="search-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
				<circle cx="11" cy="11" r="8" />
				<path d="m21 21-4.35-4.35" />
			</svg>
			<input
				type="text"
				bind:value={searchQuery}
				placeholder={$t("chat.search_placeholder")}
				class="search-input"
				autofocus
			/>
			{#if searchQuery}
				<button class="search-clear" onclick={clearSearch} aria-label="Clear search">
					<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
						<line x1="18" y1="6" x2="6" y2="18" />
						<line x1="6" y1="6" x2="18" y2="18" />
					</svg>
				</button>
			{/if}
		</div>
	{/if}

	<!-- Chat history list -->
	<div class="chat-history">
		{#if pinnedSessions.length > 0}
			<div class="history-section">
				{#if !collapsed}
					<div class="history-label">{$t("chat.pinned") ?? "Pinned"}</div>
				{/if}
				{#each pinnedSessions as session (session.id)}
					<div class="history-item-wrapper">
						<button
							class="history-item"
							class:active={session.id === currentSessionId}
							onclick={() => handleSessionClick(session)}
							ondblclick={(e) => handleDoubleClick(session, e)}
							title={session.title}
						>
							{#if editingId === session.id && !collapsed}
								<input
									class="rename-input"
									type="text"
									bind:value={editingTitle}
									onblur={() => handleRenameSubmit(session.id)}
									onkeydown={(e) => handleRenameKeydown(e, session.id)}
									onclick={(e) => e.stopPropagation()}
								/>
							{:else}
								{#if !collapsed}
									{#if session.workflowType === "Meeting Documentation"}
										<svg class="history-type-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
											<path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/>
											<polyline points="14 2 14 8 20 8"/>
											<line x1="16" y1="13" x2="8" y2="13"/>
											<line x1="16" y1="17" x2="8" y2="17"/>
										</svg>
									{:else}
										<svg class="history-type-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
											<circle cx="11" cy="11" r="8"/>
											<line x1="21" y1="21" x2="16.65" y2="16.65"/>
										</svg>
									{/if}
								{/if}
								<span class="history-title">{collapsed ? session.title.charAt(0) : session.title}</span>
								{#if !collapsed}
									<svg class="pin-indicator" viewBox="0 0 24 24" fill="currentColor" stroke="none">
										<path d="M16 12V4h1V2H7v2h1v8l-2 2v2h5.2v6h1.6v-6H18v-2l-2-2z"/>
									</svg>
								{/if}
							{/if}
						</button>

						{#if !collapsed && editingId !== session.id}
							<div class="context-menu-wrapper">
								<button class="menu-trigger" onclick={(e) => openContextMenu(session.id, e)} aria-label="Session options">
									<svg viewBox="0 0 24 24" fill="currentColor" stroke="none">
										<circle cx="12" cy="5" r="1.5" /><circle cx="12" cy="12" r="1.5" /><circle cx="12" cy="19" r="1.5" />
									</svg>
								</button>
								{#if openMenuId === session.id}
									<div class="context-dropdown">
										<button class="context-item" onclick={() => startRename(session)}>
											<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M11 4H4a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2v-7"/><path d="M18.5 2.5a2.121 2.121 0 0 1 3 3L12 15l-4 1 1-4 9.5-9.5z"/></svg>
											<span>{$t("chat.rename") ?? "Rename"}</span>
										</button>
										<button class="context-item" onclick={() => { togglePin(session.id); openMenuId = null; }}>
											<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="12" y1="17" x2="12" y2="22"/><path d="M5 17h14v-1.76a2 2 0 0 0-1.11-1.79l-1.78-.9A2 2 0 0 1 15 10.76V6h1a2 2 0 0 0 0-4H8a2 2 0 0 0 0 4h1v4.76a2 2 0 0 1-1.11 1.79l-1.78.9A2 2 0 0 0 5 15.24Z"/></svg>
											<span>{pinnedIds.has(session.id) ? ($t("chat.unpin") ?? "Unpin") : ($t("chat.pin") ?? "Pin")}</span>
										</button>
										<div class="context-divider"></div>
										<button class="context-item context-item-danger" onclick={() => handleDelete(session.id)}>
											<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 6h18M19 6v14a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2V6m3 0V4a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2"/></svg>
											<span>{$t("common.delete") ?? "Delete"}</span>
										</button>
									</div>
								{/if}
							</div>
						{/if}
					</div>
				{/each}
			</div>
		{/if}

		{#each groupedSessions as group (group.label)}
			<div class="history-section">
				{#if !collapsed}
					<div class="history-label">{group.label}</div>
				{/if}
				{#each group.sessions as session (session.id)}
					<div class="history-item-wrapper">
						<button
							class="history-item"
							class:active={session.id === currentSessionId}
							onclick={() => handleSessionClick(session)}
							ondblclick={(e) => handleDoubleClick(session, e)}
							title={session.title}
						>
							{#if editingId === session.id && !collapsed}
								<input
									class="rename-input"
									type="text"
									bind:value={editingTitle}
									onblur={() => handleRenameSubmit(session.id)}
									onkeydown={(e) => handleRenameKeydown(e, session.id)}
									onclick={(e) => e.stopPropagation()}
								/>
							{:else}
								{#if !collapsed}
									{#if session.workflowType === "Meeting Documentation"}
										<svg class="history-type-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
											<path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/>
											<polyline points="14 2 14 8 20 8"/>
											<line x1="16" y1="13" x2="8" y2="13"/>
											<line x1="16" y1="17" x2="8" y2="17"/>
										</svg>
									{:else}
										<svg class="history-type-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
											<circle cx="11" cy="11" r="8"/>
											<line x1="21" y1="21" x2="16.65" y2="16.65"/>
										</svg>
									{/if}
								{/if}
								<span class="history-title">{collapsed ? session.title.charAt(0) : session.title}</span>
							{/if}
						</button>

						{#if !collapsed && editingId !== session.id}
							<div class="context-menu-wrapper">
								<button class="menu-trigger" onclick={(e) => openContextMenu(session.id, e)} aria-label="Session options">
									<svg viewBox="0 0 24 24" fill="currentColor" stroke="none">
										<circle cx="12" cy="5" r="1.5" /><circle cx="12" cy="12" r="1.5" /><circle cx="12" cy="19" r="1.5" />
									</svg>
								</button>
								{#if openMenuId === session.id}
									<div class="context-dropdown">
										<button class="context-item" onclick={() => startRename(session)}>
											<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M11 4H4a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2v-7"/><path d="M18.5 2.5a2.121 2.121 0 0 1 3 3L12 15l-4 1 1-4 9.5-9.5z"/></svg>
											<span>{$t("chat.rename") ?? "Rename"}</span>
										</button>
										<button class="context-item" onclick={() => { togglePin(session.id); openMenuId = null; }}>
											<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="12" y1="17" x2="12" y2="22"/><path d="M5 17h14v-1.76a2 2 0 0 0-1.11-1.79l-1.78-.9A2 2 0 0 1 15 10.76V6h1a2 2 0 0 0 0-4H8a2 2 0 0 0 0 4h1v4.76a2 2 0 0 1-1.11 1.79l-1.78.9A2 2 0 0 0 5 15.24Z"/></svg>
											<span>{pinnedIds.has(session.id) ? ($t("chat.unpin") ?? "Unpin") : ($t("chat.pin") ?? "Pin")}</span>
										</button>
										<div class="context-divider"></div>
										<button class="context-item context-item-danger" onclick={() => handleDelete(session.id)}>
											<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 6h18M19 6v14a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2V6m3 0V4a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2"/></svg>
											<span>{$t("common.delete") ?? "Delete"}</span>
										</button>
									</div>
								{/if}
							</div>
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
				<p>{$t("chat.no_results") ?? "No results"}</p>
			</div>
		{/if}
	</div>

	<!-- User footer -->
	{#if userEmail || userInitial}
		<div class="user-footer-container">
			{#if userDropdownOpen && !collapsed}
				<div class="user-dropdown">
					<div class="user-dropdown-email">{userEmail ?? ""}</div>
					<div class="user-dropdown-divider"></div>
					{#if onlogout}
						<button class="user-dropdown-logout" onclick={() => { onlogout?.(); userDropdownOpen = false; }}>
							<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
								<path d="M9 21H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h4"/><polyline points="16 17 21 12 16 7"/><line x1="21" y1="12" x2="9" y2="12"/>
							</svg>
							<span>{$t("auth.logout") ?? "Log out"}</span>
						</button>
					{/if}
				</div>
			{/if}

			<button
				class="user-footer-btn"
				onclick={() => { if (collapsed) { ontoggleCollapse?.(); } else { userDropdownOpen = !userDropdownOpen; } }}
				aria-label="User menu"
			>
				<div class="user-avatar">{userInitial ?? "?"}</div>
				{#if !collapsed}
					<span class="user-name">{userName ?? userEmail ?? ""}</span>
				{/if}
			</button>
		</div>
	{/if}

	<!-- Delete confirmation dialog -->
	{#if deleteConfirmId}
		<div class="confirm-overlay" role="dialog" aria-modal="true">
			<div class="confirm-dialog">
				<h3 class="confirm-title">{$t("chat.delete_confirm_title") ?? "Delete chat?"}</h3>
				<p class="confirm-desc">{$t("chat.delete_confirm_desc") ?? "This will delete the chat from your history. This action cannot be undone."}</p>
				<div class="confirm-actions">
					<button class="confirm-btn confirm-cancel" onclick={cancelDelete}>
						{$t("common.cancel") ?? "Cancel"}
					</button>
					<button class="confirm-btn confirm-delete" onclick={confirmDelete}>
						{$t("common.delete") ?? "Delete"}
					</button>
				</div>
			</div>
		</div>
	{/if}
</aside>

<style>
	.sidebar {
		width: 320px;
		background: #f7f7f5;
		border-right: none;
		display: flex;
		flex-direction: column;
		flex-shrink: 0;
		position: fixed;
		height: 100vh;
		z-index: 10;
		overflow: hidden;
		transition: width 0.2s ease;
	}

	.sidebar.collapsed {
		width: 72px;
	}

	/* ===== Header ===== */
	.sidebar-header {
		height: 56px;
		padding: 0 14px 0 18px;
		display: flex;
		align-items: center;
		justify-content: space-between;
		flex-shrink: 0;
	}

	.sidebar.collapsed .sidebar-header {
		padding: 0;
		justify-content: center;
	}

	.logo-btn {
		display: flex;
		align-items: center;
		background: none;
		border: none;
		padding: 4px;
		cursor: pointer;
		border-radius: 8px;
		transition: opacity 0.15s ease;
	}

	.logo-btn:hover { opacity: 0.7; }

	.logo-img {
		width: 38px;
		height: 38px;
		object-fit: contain;
	}

	.sidebar.collapsed .logo-img {
		width: 34px;
		height: 34px;
	}

	/* ===== Icon buttons ===== */
	.icon-btn {
		width: 34px;
		height: 34px;
		background: transparent;
		border: none;
		border-radius: 8px;
		cursor: pointer;
		color: #6b7280;
		display: flex;
		align-items: center;
		justify-content: center;
		transition: background 0.12s ease, color 0.12s ease;
		padding: 0;
	}

	.icon-btn svg { width: 18px; height: 18px; }

	.icon-btn:hover {
		background: rgba(0, 0, 0, 0.06);
		color: #374151;
	}

	.collapse-toggle { color: #9ca3af; }
	.collapse-toggle:hover { color: #6b7280; }

	/* ===== Action items (New Chat + Search) ===== */
	.action-items {
		padding: 4px 10px 8px;
		display: flex;
		flex-direction: column;
		gap: 2px;
		flex-shrink: 0;
	}

	.sidebar.collapsed .action-items {
		padding: 4px 10px 8px;
		align-items: center;
	}

	.action-item {
		display: flex;
		align-items: center;
		gap: 12px;
		padding: 10px 14px;
		border: none;
		background: none;
		border-radius: 10px;
		cursor: pointer;
		color: #374151;
		font-size: 17px;
		font-weight: 400;
		font-family: inherit;
		text-align: left;
		width: 100%;
		transition: background 0.12s ease;
	}

	.sidebar.collapsed .action-item {
		width: 48px;
		height: 48px;
		padding: 0;
		justify-content: center;
		border-radius: 10px;
	}

	.action-item:hover {
		background: rgba(0, 0, 0, 0.05);
	}

	.action-item-active {
		background: rgba(0, 0, 0, 0.05);
	}

	.action-item svg {
		width: 18px;
		height: 18px;
		flex-shrink: 0;
		color: #6b7280;
	}

	.action-item:hover svg { color: #374151; }

	/* ===== Search bar ===== */
	.search-bar-container {
		margin: 0 10px 8px;
		position: relative;
		display: flex;
		align-items: center;
		flex-shrink: 0;
	}

	.search-icon {
		position: absolute;
		left: 10px;
		width: 14px;
		height: 14px;
		color: #9ca3af;
		pointer-events: none;
	}

	.search-input {
		width: 100%;
		padding: 8px 32px 8px 32px;
		border: 1px solid rgba(0, 0, 0, 0.08);
		border-radius: 10px;
		font-size: 13px;
		color: #374151;
		background: rgba(255, 255, 255, 0.6);
		outline: none;
		transition: border-color 0.15s ease, background 0.15s ease;
		font-family: inherit;
	}

	.search-input:focus {
		border-color: rgba(0, 0, 0, 0.15);
		background: #ffffff;
	}

	.search-input::placeholder { color: #9ca3af; }

	.search-clear {
		position: absolute;
		right: 8px;
		width: 18px;
		height: 18px;
		padding: 0;
		border: none;
		background: none;
		color: #9ca3af;
		cursor: pointer;
		display: flex;
		align-items: center;
		justify-content: center;
		border-radius: 4px;
	}

	.search-clear:hover { color: #374151; }
	.search-clear svg { width: 12px; height: 12px; }

	/* ===== Chat history list ===== */
	.chat-history {
		flex: 1;
		overflow-y: auto;
		overflow-x: hidden;
		padding: 4px 8px 8px;
		scrollbar-width: thin;
		scrollbar-color: rgba(0, 0, 0, 0.08) transparent;
	}

	.chat-history::-webkit-scrollbar { width: 3px; }
	.chat-history::-webkit-scrollbar-track { background: transparent; }
	.chat-history::-webkit-scrollbar-thumb { background: rgba(0, 0, 0, 0.08); border-radius: 4px; }

	.history-section { margin-bottom: 16px; }

	.history-label {
		font-size: 11px;
		font-weight: 500;
		color: #9ca3af;
		padding: 8px 6px 4px;
		letter-spacing: 0.1px;
	}

	/* ===== Chat item ===== */
	.history-item-wrapper { position: relative; }

	.history-item {
		display: flex;
		align-items: center;
		gap: 6px;
		padding: 10px 12px;
		border-radius: 10px;
		cursor: pointer;
		transition: background 0.12s ease;
		width: 100%;
		border: none;
		background: none;
		text-align: left;
		margin-bottom: 1px;
		box-sizing: border-box;
		min-width: 0;
		padding-right: 32px;
	}

	.sidebar.collapsed .history-item {
		padding: 8px;
		justify-content: center;
		padding-right: 8px;
	}

	.history-item:hover { background: rgba(0, 0, 0, 0.04); }
	.history-item.active { background: rgba(0, 0, 0, 0.07); }

	.history-title {
		font-size: 17px;
		font-weight: 400;
		color: #374151;
		white-space: nowrap;
		overflow: hidden;
		text-overflow: ellipsis;
		display: block;
		line-height: 1.4;
		flex: 1;
		min-width: 0;
	}

	.sidebar.collapsed .history-title {
		font-size: 12px;
		text-align: center;
		overflow: visible;
	}

	.history-item.active .history-title {
		font-weight: 500;
		color: #111827;
	}

	.history-type-icon {
		width: 14px;
		height: 14px;
		flex-shrink: 0;
		color: #9ca3af;
		margin-right: 2px;
	}

	.pin-indicator {
		width: 10px;
		height: 10px;
		color: #f97316;
		flex-shrink: 0;
		margin-left: 4px;
	}

	/* ===== Context menu ===== */
	.context-menu-wrapper {
		position: absolute;
		right: 4px;
		top: 50%;
		transform: translateY(-50%);
		z-index: 20;
	}

	.menu-trigger {
		width: 26px;
		height: 26px;
		border: none;
		background: transparent;
		border-radius: 6px;
		cursor: pointer;
		color: #9ca3af;
		display: none;
		align-items: center;
		justify-content: center;
		transition: background 0.12s ease, color 0.12s ease;
		padding: 0;
	}

	.menu-trigger svg { width: 14px; height: 14px; }

	.history-item-wrapper:hover .menu-trigger,
	.history-item-wrapper:has(.context-dropdown) .menu-trigger {
		display: flex;
	}

	.menu-trigger:hover {
		background: rgba(0, 0, 0, 0.08);
		color: #374151;
	}

	.context-dropdown {
		position: absolute;
		right: 0;
		top: calc(100% + 4px);
		width: 160px;
		background: #ffffff;
		border: 1px solid rgba(0, 0, 0, 0.08);
		border-radius: 12px;
		box-shadow: 0 4px 16px rgba(0, 0, 0, 0.1), 0 1px 3px rgba(0, 0, 0, 0.06);
		overflow: hidden;
		z-index: 50;
		padding: 4px;
	}

	.context-item {
		display: flex;
		align-items: center;
		gap: 10px;
		width: 100%;
		padding: 8px 12px;
		border: none;
		background: none;
		cursor: pointer;
		font-size: 13px;
		color: #374151;
		border-radius: 8px;
		text-align: left;
		transition: background 0.1s ease;
		font-family: inherit;
	}

	.context-item:hover { background: #f3f4f6; }
	.context-item svg { width: 14px; height: 14px; flex-shrink: 0; color: #6b7280; }
	.context-item-danger { color: #dc2626; }
	.context-item-danger svg { color: #dc2626; }
	.context-item-danger:hover { background: #fef2f2; }
	.context-divider { height: 1px; background: #f3f4f6; margin: 3px 0; }

	/* ===== Rename ===== */
	.rename-input {
		width: 100%;
		padding: 4px 8px;
		font-size: 13px;
		font-weight: 500;
		color: #111827;
		background: #ffffff;
		border: 1px solid #3b82f6;
		border-radius: 6px;
		outline: none;
		font-family: inherit;
	}

	.rename-input:focus {
		border-color: #2563eb;
		box-shadow: 0 0 0 2px rgba(59, 130, 246, 0.12);
	}

	/* ===== Empty state ===== */
	.empty-state { padding: 24px 16px; text-align: center; color: #9ca3af; }
	.empty-state p { margin: 0; font-size: 13px; }
	.empty-hint { font-size: 12px !important; margin-top: 6px !important; }

	/* ===== User footer ===== */
	.user-footer-container {
		flex-shrink: 0;
		border-top: 1px solid rgba(0, 0, 0, 0.06);
		position: relative;
	}

	.user-footer-btn {
		width: 100%;
		display: flex;
		align-items: center;
		gap: 12px;
		padding: 18px 18px;
		background: none;
		border: none;
		cursor: pointer;
		border-radius: 0;
		transition: background 0.12s ease;
		min-width: 0;
		text-align: left;
	}

	.sidebar.collapsed .user-footer-btn {
		padding: 16px 0;
		justify-content: center;
	}

	.user-footer-btn:hover { background: rgba(0, 0, 0, 0.04); }

	.user-avatar {
		width: 38px;
		height: 38px;
		border-radius: 50%;
		background: #F97316;
		color: #ffffff;
		font-size: 16px;
		font-weight: 600;
		display: flex;
		align-items: center;
		justify-content: center;
		flex-shrink: 0;
		text-transform: uppercase;
	}

	.sidebar.collapsed .user-avatar {
		width: 34px;
		height: 34px;
		font-size: 14px;
	}

	.user-name {
		flex: 1;
		min-width: 0;
		font-size: 15px;
		font-weight: 500;
		color: #374151;
		overflow: hidden;
		text-overflow: ellipsis;
		white-space: nowrap;
	}

	/* ===== User dropdown ===== */
	.user-dropdown {
		position: absolute;
		bottom: calc(100% + 8px);
		left: 10px;
		right: 10px;
		background: #ffffff;
		border: 1px solid rgba(0, 0, 0, 0.08);
		border-radius: 12px;
		box-shadow: 0 -4px 20px rgba(0, 0, 0, 0.1), 0 2px 8px rgba(0, 0, 0, 0.05);
		padding: 6px;
		z-index: 50;
	}

	.user-dropdown-email {
		padding: 8px 12px;
		font-size: 13px;
		color: #6b7280;
		overflow: hidden;
		text-overflow: ellipsis;
		white-space: nowrap;
	}

	.user-dropdown-divider { height: 1px; background: #f3f4f6; margin: 2px 0; }

	.user-dropdown-logout {
		display: flex;
		align-items: center;
		gap: 10px;
		width: 100%;
		padding: 10px 12px;
		border: none;
		background: none;
		cursor: pointer;
		font-size: 14px;
		color: #374151;
		border-radius: 8px;
		text-align: left;
		transition: background 0.1s ease;
		font-family: inherit;
	}

	.user-dropdown-logout:hover { background: #fef2f2; color: #dc2626; }
	.user-dropdown-logout svg { width: 16px; height: 16px; flex-shrink: 0; color: inherit; }

	/* ===== Delete confirmation dialog ===== */
	.confirm-overlay {
		position: fixed;
		inset: 0;
		background: rgba(0, 0, 0, 0.5);
		display: flex;
		align-items: center;
		justify-content: center;
		z-index: 100;
	}

	.confirm-dialog {
		background: #ffffff;
		border-radius: 16px;
		padding: 24px;
		width: 340px;
		box-shadow: 0 16px 48px rgba(0, 0, 0, 0.2);
	}

	.confirm-title {
		font-size: 16px;
		font-weight: 600;
		color: #111827;
		margin: 0 0 8px;
	}

	.confirm-desc {
		font-size: 14px;
		color: #6b7280;
		line-height: 1.5;
		margin: 0 0 20px;
	}

	.confirm-actions {
		display: flex;
		gap: 8px;
		justify-content: flex-end;
	}

	.confirm-btn {
		padding: 8px 16px;
		border-radius: 8px;
		font-size: 14px;
		font-weight: 500;
		cursor: pointer;
		border: none;
		font-family: inherit;
		transition: background 0.12s ease;
	}

	.confirm-cancel {
		background: #f3f4f6;
		color: #374151;
	}

	.confirm-cancel:hover {
		background: #e5e7eb;
	}

	.confirm-delete {
		background: #ef4444;
		color: #ffffff;
	}

	.confirm-delete:hover {
		background: #dc2626;
	}

	/* ===== Responsive ===== */
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
