<script lang="ts">
	import { goto } from "$app/navigation";
	import {
		authStore,
		isAuthenticated,
		authLoading,
	} from "$lib/stores/authStore";
	import { chatStore, currentSessionId } from "$stores/chatStore";
	import { onMount } from "svelte";

	let checkingAuth = $state(true);

	const exampleQueries = [
		"Biegeradius Hydraulikrohr",
		"Konstruktionsrichtlinien Spuranzeiger",
		"Fertigungsverfahren Änderungen",
		"Sicherheitsvorschriften Druckbehälter",
	];

	onMount(async () => {
		await authStore.initialize();
		const isAuth = await authStore.checkAuth();
		checkingAuth = false;

		if (isAuth) {
			const sessionId = chatStore.createSession();
			currentSessionId.set(sessionId);
			goto(`/chat/${sessionId}`);
		}
	});

	function handleGetStarted() {
		authStore.login();
	}

	function handleQueryChip(query: string) {
		authStore.login();
	}
</script>

<svelte:head>
	<title>Nora - KI-gestützter Wissensassistent</title>
</svelte:head>

<div class="landing-container">
	<div class="landing-content">
		<!-- Logo -->
		<div class="logo-section">
			<img src="/norizon-logo.png" alt="Norizon" class="landing-logo" />
		</div>

		<!-- Hero -->
		<div class="hero-section">
			<h1 class="hero-title">
				Frag Nora —<br />sie findet die Antwort.
			</h1>
			<p class="hero-description">
				Ihr KI-Assistent für das Unternehmenswissen. Durchsucht alle
				verbundenen Quellen – SharePoint, Confluence, Jira und mehr.
			</p>

			{#if $authLoading || checkingAuth}
				<div class="loading-state">
					<div class="spinner"></div>
					<p>Wird geladen...</p>
				</div>
			{:else}
				<button onclick={handleGetStarted} class="cta-button">
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

				<!-- Example query chips -->
				<div class="query-chips">
					<p class="chips-label">Zum Beispiel:</p>
					<div class="chips-row">
						{#each exampleQueries as query}
							<button
								class="query-chip"
								onclick={() => handleQueryChip(query)}
							>
								{query}
							</button>
						{/each}
					</div>
				</div>
			{/if}
		</div>
	</div>

	<div class="landing-footer">
		<p>Powered by Norizon · Sicher · Enterprise-Ready · DSGVO-konform</p>
	</div>
</div>

<style>
	.landing-container {
		min-height: 100vh;
		display: flex;
		flex-direction: column;
		background: #ffffff;
		position: relative;
		overflow: hidden;
	}

	/* Subtle background orb */
	.landing-container::before {
		content: "";
		position: absolute;
		top: -200px;
		right: -200px;
		width: 600px;
		height: 600px;
		background: radial-gradient(circle, rgba(249, 115, 22, 0.04) 0%, transparent 70%);
		border-radius: 50%;
		pointer-events: none;
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
		margin-bottom: 56px;
	}

	.landing-logo {
		height: 52px;
		width: auto;
	}

	.hero-section {
		text-align: center;
		max-width: 680px;
	}

	.hero-title {
		font-size: 44px;
		font-weight: 600;
		color: #111827;
		margin-bottom: 16px;
		line-height: 1.2;
		letter-spacing: -0.025em;
	}

	.hero-description {
		font-size: 16px;
		color: #6b7280;
		line-height: 1.6;
		margin-bottom: 36px;
		max-width: 480px;
		margin-left: auto;
		margin-right: auto;
	}

	.cta-button {
		display: inline-flex;
		align-items: center;
		gap: 8px;
		background: #0f172a;
		color: white;
		border: none;
		padding: 14px 28px;
		border-radius: 24px;
		font-size: 15px;
		font-weight: 600;
		cursor: pointer;
		transition: all 0.2s ease;
		box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
		margin-bottom: 36px;
	}

	.cta-button:hover {
		background: #1e293b;
		box-shadow: 0 4px 16px rgba(0, 0, 0, 0.15);
	}

	.cta-button:active {
		transform: scale(0.98);
	}

	.loading-state {
		display: flex;
		flex-direction: column;
		align-items: center;
		gap: 16px;
		color: #64748b;
		margin-bottom: 40px;
	}

	.spinner {
		width: 36px;
		height: 36px;
		border: 2px solid #e2e8f0;
		border-top-color: #f97316;
		border-radius: 50%;
		animation: spin 0.8s linear infinite;
	}

	@keyframes spin {
		to {
			transform: rotate(360deg);
		}
	}

	.query-chips {
		text-align: center;
	}

	.chips-label {
		font-size: 13px;
		color: #94a3b8;
		margin-bottom: 12px;
	}

	.chips-row {
		display: flex;
		flex-wrap: wrap;
		gap: 8px;
		justify-content: center;
	}

	.query-chip {
		display: inline-block;
		padding: 10px 18px;
		background: #f9fafb;
		border: 1px solid #e5e7eb;
		border-radius: 20px;
		font-size: 13px;
		color: #374151;
		cursor: pointer;
		transition: all 0.15s ease;
		font-family: inherit;
	}

	.query-chip:hover {
		background: #f3f4f6;
		border-color: #d1d5db;
		color: #111827;
	}

	.landing-footer {
		padding: 24px;
		text-align: center;
		color: #9ca3af;
		font-size: 12px;
		position: relative;
		z-index: 1;
	}

	@media (max-width: 640px) {
		.hero-title {
			font-size: 34px;
		}

		.hero-description {
			font-size: 15px;
		}

		.chips-row {
			gap: 6px;
		}
	}
</style>
