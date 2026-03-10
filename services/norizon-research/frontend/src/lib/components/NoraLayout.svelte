<script lang="ts">
	import { createEventDispatcher } from "svelte";
	import { browser } from "$app/environment";
	import Sidebar from "./Sidebar.svelte";
	import ChatHeader from "./ChatHeader.svelte";
	import type { ChatSession } from "$lib/types";

	export let currentSessionId: string | null = null;
	// Optional: force sidebar collapsed state from parent
	export let forceCollapsed: boolean | null = null;

	const dispatch = createEventDispatcher<{
		newChat: void;
		selectSession: string;
		share: void;
		menu: void;
	}>();

	let forceCollapsedOverride = false;
	let sidebarOpen = false;
	let userCollapsed = browser
		? localStorage.getItem("sidebar-collapsed") === "true"
		: false;

	// Use forceCollapsed if set (and not overridden), otherwise use user preference
	$: sidebarCollapsed =
		forceCollapsed !== null && !forceCollapsedOverride
			? forceCollapsed
			: userCollapsed;

	function handleNewChat() {
		dispatch("newChat");
		sidebarOpen = false;
	}

	function handleSelectSession(event: CustomEvent<string>) {
		dispatch("selectSession", event.detail);
		sidebarOpen = false;
	}

	function toggleSidebar() {
		sidebarOpen = !sidebarOpen;
	}

	function handleToggleCollapse() {
		userCollapsed = !userCollapsed;
		if (browser) {
			localStorage.setItem("sidebar-collapsed", userCollapsed.toString());
		}
	}
</script>

<div class="app-container">
	<!-- Mobile menu button -->
	<button
		class="mobile-menu-btn"
		on:click={toggleSidebar}
		aria-label="Toggle menu"
	>
		<svg
			viewBox="0 0 24 24"
			fill="none"
			stroke="currentColor"
			stroke-width="2"
		>
			<line x1="3" y1="12" x2="21" y2="12" />
			<line x1="3" y1="6" x2="21" y2="6" />
			<line x1="3" y1="18" x2="21" y2="18" />
		</svg>
	</button>

	<!-- Sidebar overlay for mobile -->
	{#if sidebarOpen}
		<button
			class="sidebar-overlay"
			on:click={() => (sidebarOpen = false)}
			aria-label="Close menu"
		></button>
	{/if}

	<!-- Sidebar -->
	<div
		class="sidebar-wrapper"
		class:open={sidebarOpen}
		class:collapsed={sidebarCollapsed}
	>
		<Sidebar
			{currentSessionId}
			collapsed={sidebarCollapsed}
			on:newChat={handleNewChat}
			on:selectSession={handleSelectSession}
			on:toggleCollapse={handleToggleCollapse}
		/>
	</div>

	<!-- Main Content -->
	<main class="main-content" class:sidebar-collapsed={sidebarCollapsed}>
		<ChatHeader on:share on:menu />

		<div class="chat-messages">
			<div class="messages-container">
				<slot />
			</div>
		</div>

		<div class="chat-input-container">
			<div class="chat-input-wrapper">
				<slot name="input" />
			</div>
		</div>
	</main>
</div>

<style>
	.app-container {
		display: flex;
		min-height: 100vh;
		background: var(--slate-50, #f8fafc);
	}

	.mobile-menu-btn {
		display: none;
		position: fixed;
		top: 12px;
		left: 12px;
		z-index: 20;
		width: 40px;
		height: 40px;
		border: 1px solid var(--slate-200, #e2e8f0);
		border-radius: 8px;
		background: var(--white, #ffffff);
		color: var(--slate-600, #475569);
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
		flex: 1;
		margin-left: 280px;
		display: flex;
		flex-direction: column;
		height: 100vh;
		transition: margin-left 0.2s ease;
	}

	.main-content.sidebar-collapsed {
		margin-left: 72px;
	}

	.chat-messages {
		flex: 1;
		overflow-y: auto;
		padding: var(--space-6, 24px);
	}

	.messages-container {
		max-width: 800px;
		margin: 0 auto;
		display: flex;
		flex-direction: column;
		gap: var(--space-6, 24px);
	}

	.chat-input-container {
		padding: var(--space-4, 16px) var(--space-6, 24px) var(--space-6, 24px);
		background: rgba(255, 255, 255, 0.85);
		backdrop-filter: blur(10px);
		-webkit-backdrop-filter: blur(10px);
		border-top: 1px solid var(--slate-200, #e2e8f0);
	}

	.chat-input-wrapper {
		max-width: 800px;
		margin: 0 auto;
	}

	/* Responsive */
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
			margin-left: 0;
		}

		.chat-messages {
			padding: 16px;
			padding-top: 60px; /* Space for mobile menu button */
		}

		.chat-input-container {
			padding: 12px 16px 16px;
		}
	}
</style>
