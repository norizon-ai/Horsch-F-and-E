<script lang="ts">
	import { goto } from "$app/navigation";
	import {
		authStore,
		isAuthenticated,
		authLoading,
	} from "$lib/stores/authStore";
	import { chatStore, currentSessionId } from "$stores/chatStore";
	import { onMount } from "svelte";

	let checkingAuth = true;

	onMount(async () => {
		// Wait for auth initialization to complete directly via Promise
		await authStore.initialize();

		// Check if user is already authenticated
		const isAuth = await authStore.checkAuth();

		checkingAuth = false;

		if (isAuth) {
			// Redirect authenticated users to chat
			const sessionId = chatStore.createSession();
			currentSessionId.set(sessionId);
			goto(`/chat/${sessionId}`);
		}
	});

	function handleGetStarted() {
		authStore.login();
	}
</script>

<svelte:head>
	<title>Nora - KI-gestützter Wissensassistent</title>
</svelte:head>

<div class="landing-container">
	<div class="landing-content">
		<div class="logo-section">
			<img src="/norizon-logo.png" alt="Norizon" class="landing-logo" />
		</div>

		<div class="hero-section">
			<h1 class="hero-title">
				Ihr KI-gestützter<br />Wissensassistent
			</h1>
			<p class="hero-description">
				Greifen Sie sofort auf das Wissen Ihres Unternehmens zu – mit
				intelligenter Suche,<br />
				automatisierter Dokumentation und Workflow-Automatisierung.
			</p>

			{#if $authLoading || checkingAuth}
				<div class="loading-state">
					<div class="spinner"></div>
					<p>Wird geladen...</p>
				</div>
			{:else}
				<button on:click={handleGetStarted} class="cta-button">
					Jetzt starten
					<svg
						width="20"
						height="20"
						viewBox="0 0 20 20"
						fill="none"
						xmlns="http://www.w3.org/2000/svg"
					>
						<path
							d="M7.5 15L12.5 10L7.5 5"
							stroke="currentColor"
							stroke-width="2"
							stroke-linecap="round"
							stroke-linejoin="round"
						/>
					</svg>
				</button>
			{/if}
		</div>
	</div>

	<div class="landing-footer">
		<p>Powered by Norizon • Sicher • Enterprise-Ready</p>
	</div>
</div>

<style>
	.landing-container {
		min-height: 100vh;
		display: flex;
		flex-direction: column;
		background: white;
		position: relative;
		overflow: hidden;
	}

	.landing-content {
		flex: 1;
		display: flex;
		flex-direction: column;
		align-items: center;
		justify-content: center;
		padding: 60px 20px;
		position: relative;
		z-index: 1;
	}

	.logo-section {
		margin-bottom: 48px;
	}

	.landing-logo {
		height: 48px;
		width: auto;
	}

	.hero-section {
		text-align: center;
		max-width: 800px;
	}

	.hero-title {
		font-size: 56px;
		font-weight: 700;
		color: var(--deep-blue);
		margin-bottom: 24px;
		line-height: 1.2;
	}

	.hero-description {
		font-size: 18px;
		color: var(--slate-600);
		line-height: 1.7;
		margin-bottom: 40px;
	}

	.cta-button {
		display: inline-flex;
		align-items: center;
		gap: 8px;
		background: linear-gradient(
			135deg,
			var(--orange-500) 0%,
			var(--orange-400) 100%
		);
		color: white;
		border: none;
		padding: 16px 32px;
		border-radius: var(--radius-md);
		font-size: 16px;
		font-weight: 600;
		cursor: pointer;
		transition: all 0.3s ease;
		box-shadow: 0 4px 20px rgba(249, 115, 22, 0.3);
	}

	.cta-button:hover {
		transform: translateY(-2px);
		box-shadow: 0 8px 30px rgba(249, 115, 22, 0.4);
	}

	.loading-state {
		display: flex;
		flex-direction: column;
		align-items: center;
		gap: 16px;
		color: var(--slate-600);
	}

	.spinner {
		width: 40px;
		height: 40px;
		border: 3px solid var(--slate-200);
		border-top-color: var(--orange-500);
		border-radius: 50%;
		animation: spin 0.8s linear infinite;
	}

	@keyframes spin {
		to {
			transform: rotate(360deg);
		}
	}

	.landing-footer {
		padding: 24px;
		text-align: center;
		color: var(--slate-500);
		font-size: 14px;
		position: relative;
		z-index: 1;
	}

	/* Responsive */
	@media (max-width: 768px) {
		.hero-title {
			font-size: 36px;
		}

		.hero-description {
			font-size: 16px;
		}
	}
</style>
