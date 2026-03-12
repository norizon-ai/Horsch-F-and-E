<script lang="ts">
	import { browser } from "$app/environment";
	import Sidebar from "./Sidebar.svelte";
	import ChatHeader from "./ChatHeader.svelte";
	import { authStore, currentUser } from "$lib/stores/authStore";

	let {
		currentSessionId = null as string | null,
		onnewChat = undefined as (() => void) | undefined,
		onselectSession = undefined as ((sessionId: string) => void) | undefined,
		onshare = undefined as (() => void) | undefined,
		onmenu = undefined as (() => void) | undefined,
		children,
		input = undefined,
	} = $props();

	let sidebarOpen = $state(false);
	let sidebarCollapsed = $state(
		browser ? localStorage.getItem("sidebar-collapsed") === "true" : false,
	);

	let userEmail = $derived($currentUser?.email ?? undefined);
	let userInitial = $derived(
		$currentUser?.name
			? $currentUser.name.charAt(0).toUpperCase()
			: $currentUser?.email
				? $currentUser.email.charAt(0).toUpperCase()
				: undefined,
	);

	function handleNewChat() {
		onnewChat?.();
		sidebarOpen = false;
	}

	function handleSelectSession(sessionId: string) {
		onselectSession?.(sessionId);
		sidebarOpen = false;
	}

	function toggleSidebar() {
		sidebarOpen = !sidebarOpen;
	}

	function handleToggleCollapse() {
		sidebarCollapsed = !sidebarCollapsed;
		if (browser) {
			localStorage.setItem("sidebar-collapsed", sidebarCollapsed.toString());
		}
	}

	async function handleLogout() {
		await authStore.logout();
	}
</script>

<div class="app-container">
	<button
		class="mobile-menu-btn"
		onclick={toggleSidebar}
		aria-label="Toggle menu"
	>
		<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
			<line x1="3" y1="12" x2="21" y2="12" />
			<line x1="3" y1="6" x2="21" y2="6" />
			<line x1="3" y1="18" x2="21" y2="18" />
		</svg>
	</button>

	{#if sidebarOpen}
		<button
			class="sidebar-overlay"
			onclick={() => (sidebarOpen = false)}
			aria-label="Close menu"
		></button>
	{/if}

	<div class="sidebar-wrapper" class:open={sidebarOpen} class:collapsed={sidebarCollapsed}>
		<Sidebar
			{currentSessionId}
			collapsed={sidebarCollapsed}
			{userEmail}
			{userInitial}
			onnewChat={handleNewChat}
			onselectSession={handleSelectSession}
			ontoggleCollapse={handleToggleCollapse}
			onlogout={handleLogout}
		/>
	</div>

	<main class="main-content" class:sidebar-collapsed={sidebarCollapsed}>
		<ChatHeader onshare={onshare} onmenu={onmenu} />

		<div class="chat-messages">
			<div class="messages-container">
				{@render children?.()}
			</div>
		</div>

		<div class="chat-input-container">
			<div class="chat-input-wrapper">
				{@render input?.()}
			</div>
		</div>
	</main>
</div>

<style>
	.app-container {
		display: flex;
		min-height: 100vh;
		background: #ffffff;
	}

	.mobile-menu-btn {
		display: none;
		position: fixed;
		top: 12px;
		left: 12px;
		z-index: 20;
		width: 40px;
		height: 40px;
		border: 1px solid #e2e8f0;
		border-radius: 8px;
		background: #ffffff;
		color: #475569;
		cursor: pointer;
		align-items: center;
		justify-content: center;
	}

	.mobile-menu-btn svg {
		width: 20px;
		height: 20px;
	}

	.sidebar-overlay {
		display: none;
		position: fixed;
		inset: 0;
		background: rgba(0, 0, 0, 0.3);
		z-index: 5;
		border: none;
		cursor: pointer;
	}

	.sidebar-wrapper {
		flex-shrink: 0;
	}

	.main-content {
		position: fixed;
		top: 0;
		bottom: 0;
		left: 320px;
		right: 0;
		display: flex;
		flex-direction: column;
		transition: left 0.2s ease;
	}

	.main-content.sidebar-collapsed {
		left: 72px;
	}

	.chat-messages {
		flex: 1;
		overflow-y: auto;
		padding: 24px;
	}

	.messages-container {
		max-width: 760px;
		margin: 0 auto;
		display: flex;
		flex-direction: column;
		gap: 0;
	}

	.chat-input-container {
		padding: 0 24px 24px;
		background: transparent;
	}

	.chat-input-wrapper {
		max-width: 760px;
		margin: 0 auto;
	}

	@media (max-width: 900px) {
		.mobile-menu-btn {
			display: flex;
		}

		.sidebar-overlay {
			display: block;
		}

		.sidebar-wrapper {
			position: fixed;
			z-index: 10;
			transform: translateX(-100%);
			transition: transform 0.3s ease;
		}

		.sidebar-wrapper.open {
			transform: translateX(0);
		}

		.main-content {
			left: 0;
		}

		.chat-messages {
			padding: 16px;
			padding-top: 60px;
		}

		.chat-input-container {
			padding: 12px 16px 16px;
		}
	}
</style>
