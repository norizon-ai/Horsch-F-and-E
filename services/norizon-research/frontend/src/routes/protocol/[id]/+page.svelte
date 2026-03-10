<script lang="ts">
	import { page } from "$app/stores";
	import { onMount } from "svelte";
	import { goto } from "$app/navigation";
	import { t } from "svelte-i18n";
	import NoraLayout from "$lib/components/NoraLayout.svelte";
	import ConfluencePreview from "$lib/components/workflows/meeting/ConfluencePreview.svelte";
	import ExportConfirmation from "$lib/components/workflows/meeting/ExportConfirmation.svelte";
	import { getHistoryById } from "$lib/api/historyApi";
	import type { Protocol } from "$lib/types";
	import { sessions } from "$lib/stores/chatStore";

	let protocolId: string;
	let protocol: Protocol | null = null;
	let title = "Loading...";
	let isLoading = true;
	let error: string | null = null;
	let recentSessions: any[] = [];
	let isExporting = false;

	$: protocolId = $page.params.id || "";

	// Get recent sessions for sidebar
	$: {
		recentSessions = Array.from($sessions.values())
			.filter((session) => session.messages.length > 0)
			.sort((a, b) => b.updatedAt - a.updatedAt)
			.slice(0, 10);
	}

	$: {
		if (protocolId) {
			loadProtocol();
		}
	}

	async function loadProtocol() {
		try {
			// Clear existing protocol to force ConfluencePreview remount
			// and ensure stale data doesn't persist across SvelteKit navigations
			protocol = null;
			error = null;
			isLoading = true;
			console.log("📂 Loading protocol:", protocolId);

			const historyRecord = await getHistoryById(protocolId);

			if (!historyRecord) {
				error = "Protocol not found";
				return;
			}

			if (historyRecord.workflow_name === "Meeting Documentation") {
				protocol = historyRecord.payload?.protocol;
				title = historyRecord.title;

				if (!protocol) {
					error = "Protocol data not found";
				}
			} else {
				// Not a meeting documentation workflow - redirect to chat
				goto(`/chat/${protocolId}`);
			}
		} catch (err) {
			console.error("❌ Failed to load protocol:", err);
			error =
				err instanceof Error ? err.message : "Failed to load protocol";
		} finally {
			isLoading = false;
		}
	}

	function handleNewChat() {
		goto("/chat");
	}

	function handleSelectSession(event: CustomEvent<string>) {
		goto(`/chat/${event.detail}`);
	}

	function handleBackToEdit() {
		alert(
			"This protocol is from history and cannot be edited. Please start a new workflow to edit.",
		);
	}

	async function handleExportToConfluence(
		event: CustomEvent<{ spaceId: string; parentPageId: string }>,
	) {
		const { spaceId, parentPageId } = event.detail;
		isExporting = true;
		try {
			const { WorkflowAPI } = await import("$lib/api/workflowApi");
			await WorkflowAPI.publishToConfluence(protocol!, spaceId);
			alert("Published to Confluence successfully!");
		} catch (e) {
			console.error("Failed to publish protocol:", e);
			error =
				e instanceof Error
					? e.message
					: "Failed to publish to Confluence";
		} finally {
			isExporting = false;
		}
	}

	function handleNoraAction(
		event: CustomEvent<{ type: "email" | "status" | "chat" }>,
	) {
		const actionType = event.detail.type;
		goto(
			`/chat?context=meeting-protocol&jobId=${protocolId}&action=${actionType}`,
		);
	}

	async function handleExportPdf() {
		if (!protocol) return;

		try {
			const WORKFLOW_API_URL =
				import.meta.env.VITE_WORKFLOW_API_URL ||
				"http://localhost:8001";

			// Get auth token
			const { authStore } = await import("$lib/stores/authStore");
			const token = await authStore.getAccessToken();

			const response = await fetch(`${WORKFLOW_API_URL}/export/pdf`, {
				method: "POST",
				headers: {
					"Content-Type": "application/json",
					...(token ? { Authorization: `Bearer ${token}` } : {}),
				},
				body: JSON.stringify({ protocol }),
			});

			if (!response.ok) {
				throw new Error(`Export failed: ${response.statusText}`);
			}

			// Download the PDF
			const blob = await response.blob();
			const url = URL.createObjectURL(blob);
			const a = document.createElement("a");
			a.href = url;
			a.download = `${title.replace(/[^a-z0-9]/gi, "-").toLowerCase()}.pdf`;
			document.body.appendChild(a);
			a.click();
			document.body.removeChild(a);
			URL.revokeObjectURL(url);
		} catch (err) {
			console.error("Failed to export PDF:", err);
			alert("Failed to export PDF. Please try again.");
		}
	}
</script>

<svelte:head>
	<title>{title} - Nora</title>
</svelte:head>

<NoraLayout
	currentSessionId={protocolId}
	forceCollapsed={true}
	on:newChat={handleNewChat}
	on:selectSession={handleSelectSession}
>
	<div class="workflow-content with-preview">
		{#if error}
			<div class="error-banner">
				<svg
					viewBox="0 0 24 24"
					fill="none"
					stroke="currentColor"
					stroke-width="2"
				>
					<circle cx="12" cy="12" r="10" />
					<line x1="12" y1="8" x2="12" y2="12" />
					<line x1="12" y1="16" x2="12.01" y2="16" />
				</svg>
				<span>{error}</span>
				<button class="btn-primary" on:click={() => goto("/")}
					>Go Back</button
				>
			</div>
		{/if}

		{#if isLoading}
			<div class="action-card">
				<div class="loading">
					<div class="spinner"></div>
					<p>Loading protocol...</p>
				</div>
			</div>
		{:else if protocol}
			<div class="action-card">
				<div class="message-header">
					<div class="message-avatar">
						<svg viewBox="0 0 24 24" fill="currentColor">
							<path
								d="M6 4v16h2.5v-9.5L15 18.5V20h2.5V4H15v9.5L8.5 5.5V4H6z"
							/>
						</svg>
					</div>
					<span class="message-name">Nora</span>
				</div>
				<p class="nora-greeting">
					Here is the historical workflow. You can export it or follow
					up on it below.
				</p>

				<div class="step-content">
					<ExportConfirmation
						{protocol}
						{isExporting}
						editable={false}
						on:export={handleExportToConfluence}
						on:exportPdf={handleExportPdf}
						on:back={handleBackToEdit}
						on:noraAction={handleNoraAction}
					/>
				</div>
			</div>
		{/if}
	</div>

	<!-- Editor Side Panel (flat, integrated - like Claude's artifacts) -->
	{#if protocol}
		<div class="preview-side-panel split-view-active">
			<div class="preview-panel-header">
				<span>Historical Protocol Mode</span>
			</div>
			<div class="preview-panel-content">
				<ConfluencePreview {protocol} editable={false} />
			</div>
		</div>

		<!-- Mobile Preview Drawer -->
		<div class="mobile-preview-drawer">
			<div class="drawer-handle"></div>
			<div class="drawer-header">
				<span>Historical Protocol Mode</span>
			</div>
			<div class="drawer-content">
				<ConfluencePreview {protocol} editable={false} />
			</div>
		</div>
	{/if}
</NoraLayout>

<style>
	/* Match chat interface container width and structure */
	.workflow-content {
		max-width: 800px;
		margin: 0 auto;
		padding: 24px 0 40px;
		transition:
			transform 0.3s ease,
			margin 0.3s ease;
	}

	.workflow-content.with-preview {
		margin-left: 0;
		margin-right: auto;
		max-width: 100%;
		transition:
			transform 300ms ease-in-out,
			max-width 300ms ease-in-out;
		transform: translateX(-380px);
		max-width: 800px;
	}

	@media (max-width: 1280px) {
		.workflow-content.with-preview {
			margin-left: auto;
			transform: none;
		}
	}

	.action-card {
		background: var(--white, #ffffff);
		border: 1px solid var(--slate-200, #e2e8f0);
		border-radius: 12px;
		padding: 20px 24px;
		box-shadow: 0 1px 3px rgba(0, 0, 0, 0.04);
	}

	.message-header {
		display: flex;
		align-items: center;
		gap: 8px;
		padding-bottom: 12px;
		margin-bottom: 16px;
		border-bottom: 1px solid var(--slate-100, #f1f5f9);
	}

	.message-avatar {
		width: 28px;
		height: 28px;
		border-radius: 50%;
		background: var(--deep-blue, #1e3a5f);
		color: white;
		display: flex;
		align-items: center;
		justify-content: center;
	}

	.message-avatar svg {
		width: 14px;
		height: 14px;
	}

	.message-name {
		font-size: 13px;
		font-weight: 600;
		color: var(--slate-900, #0f172a);
	}

	.nora-greeting {
		font-size: 15px;
		color: var(--slate-700, #334155);
		line-height: 1.6;
		margin: 0 0 20px 0;
	}

	.step-content {
		display: flex;
		flex-direction: column;
		align-items: center;
	}

	.error-banner {
		display: flex;
		align-items: center;
		gap: 12px;
		padding: 12px 16px;
		background: var(--red-50, #fef2f2);
		border: 1px solid var(--red-200, #fecaca);
		border-radius: 8px;
		color: var(--red-700, #b91c1c);
		font-size: 14px;
		margin-bottom: 16px;
	}

	.error-banner svg {
		width: 20px;
		height: 20px;
		flex-shrink: 0;
	}

	.error-banner span {
		flex: 1;
	}

	.loading {
		display: flex;
		flex-direction: column;
		align-items: center;
		gap: 16px;
		padding: 40px 0;
	}

	.spinner {
		width: 40px;
		height: 40px;
		border: 3px solid var(--slate-200, #e2e8f0);
		border-top-color: var(--blue-500, #3b82f6);
		border-radius: 50%;
		animation: spin 1s linear infinite;
	}

	@keyframes spin {
		to {
			transform: rotate(360deg);
		}
	}

	@media (max-width: 768px) {
		.workflow-content {
			padding: 16px;
		}
		.action-card {
			padding: 16px;
		}
	}

	.preview-side-panel {
		position: fixed;
		top: 57px;
		right: 0;
		width: 850px;
		height: calc(100vh - 57px);
		background: white;
		border-left: 1px solid var(--slate-200, #e2e8f0);
		display: flex;
		flex-direction: column;
		z-index: 50;
		transform: translateX(100%);
		transition: transform 300ms ease-in-out;
	}

	.preview-side-panel.split-view-active {
		transform: translateX(0);
	}

	.preview-panel-header {
		display: flex;
		align-items: center;
		justify-content: space-between;
		padding: 12px 16px;
		border-bottom: 1px solid var(--slate-100, #f1f5f9);
		background: white;
	}

	.preview-panel-header span {
		font-size: 12px;
		font-weight: 500;
		color: var(--slate-400, #94a3b8);
		text-transform: uppercase;
		letter-spacing: 0.5px;
	}

	.preview-panel-content {
		flex: 1;
		overflow-y: auto;
		overflow-x: hidden;
		position: relative;
	}

	@media (max-width: 1280px) {
		.preview-side-panel {
			display: none;
		}
	}

	.mobile-preview-drawer {
		display: none;
	}

	@media (max-width: 1280px) {
		.mobile-preview-drawer {
			display: flex;
			flex-direction: column;
			position: fixed;
			bottom: 0;
			left: 0;
			right: 0;
			max-height: 85vh;
			background: white;
			border-top-left-radius: 16px;
			border-top-right-radius: 16px;
			box-shadow: 0 -4px 24px rgba(0, 0, 0, 0.15);
			z-index: 101;
			animation: slideUp 0.3s ease-out;
		}

		@keyframes slideUp {
			from {
				transform: translateY(100%);
			}
			to {
				transform: translateY(0);
			}
		}

		.drawer-handle {
			width: 36px;
			height: 4px;
			background: var(--slate-300, #cbd5e1);
			border-radius: 2px;
			margin: 10px auto 0;
		}

		.drawer-header {
			display: flex;
			align-items: center;
			justify-content: center;
			padding: 12px 16px;
			border-bottom: 1px solid var(--slate-200, #e2e8f0);
		}

		.drawer-header span {
			font-size: 15px;
			font-weight: 600;
			color: var(--slate-900, #0f172a);
		}

		.drawer-content {
			flex: 1;
			overflow-y: auto;
			max-height: calc(85vh - 80px);
			position: relative;
		}
	}
</style>
