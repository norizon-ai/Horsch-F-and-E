<script lang="ts">
	import { page } from "$app/stores";
	import { onMount } from "svelte";
	import { browser } from "$app/environment";
	import { goto } from "$app/navigation";
	import { t } from "svelte-i18n";
	import NoraLayout from "$lib/components/NoraLayout.svelte";
	import { sessions } from "$lib/stores/chatStore";
	import {
		workflowStore,
		currentWorkflow,
		currentWorkflowId,
	} from "$lib/stores/workflowStore";
	import { WorkflowAPI } from "$lib/api/workflowApi";
	import { createHistory, updateHistoryPayload } from "$lib/api/historyApi";
	import { historyStore } from "$lib/stores/historyStore";
	import type { WorkflowStep, Speaker, Protocol } from "$lib/types";

	// Components
	import StepIndicator from "$lib/components/workflows/StepIndicator.svelte";
	import UploadAndConfigure from "$lib/components/workflows/meeting/UploadAndConfigure.svelte";
	import ProcessingProgress from "$lib/components/workflows/meeting/ProcessingProgress.svelte";
	import SpeakerVerification from "$lib/components/workflows/meeting/SpeakerVerification.svelte";
	import TemplateReview from "$lib/components/workflows/meeting/TemplateReview.svelte";
	import ExportConfirmation from "$lib/components/workflows/meeting/ExportConfirmation.svelte";
	import SuccessScreen from "$lib/components/workflows/meeting/SuccessScreen.svelte";
	import FollowUpPromptEditor from "$lib/components/workflows/meeting/FollowUpPromptEditor.svelte";
	import ConfluencePreview from "$lib/components/workflows/meeting/ConfluencePreview.svelte";

	let isExporting = $state(false);
	let isRegenerating = $state(false);
	let regenerationMessage = $state("Loading template...");
	let messageInterval: ReturnType<typeof setInterval> | null = $state(null);
	let showSplitView = $state(false);

	let isInitialized = $state(false);
	let error: string | null = $state(null);
	let recentSessions: any[] = $state([]);

	let jobId = $derived($page.params.jobId ?? '');

	// Initialize workflow state when jobId changes
	$effect(() => {
		if (jobId && !isInitialized) {
			initializeWorkflow();
		}
	});

	// Get recent sessions for sidebar
	$effect(() => {
		recentSessions = Array.from($sessions.values())
			.filter((session) => session.messages.length > 0)
			.sort((a, b) => b.updatedAt - a.updatedAt)
			.slice(0, 10);
	});

	async function initializeWorkflow() {
		// Try to load existing state from localStorage
		const existingState = workflowStore.loadJob(jobId);

		if (!existingState) {
			// Initialize new workflow if not found
			workflowStore.initJob(jobId);
			// Start at step 3 (upload)
			workflowStore.setStep(3);
		}

		isInitialized = true;

		// If we're at step 5 (processing) and streaming is enabled, start the SSE stream
		const state = workflowStore.loadJob(jobId);
		if (state?.currentStep === 5 && useStreamingApi) {
			startStreaming();
		}
	}

	// Start SSE streaming for transcription progress
	async function startStreaming() {
		try {
			for await (const event of WorkflowAPI.streamTranscription(jobId)) {
				if (event.type === "progress") {
					workflowStore.setProgress({
						stage: event.stage || "",
						percent: event.percent || 0,
						message: event.message || "",
					});
				} else if (event.type === "complete") {
					if (event.speakers) {
						workflowStore.setSpeakers(event.speakers);
					}
					workflowStore.setProcessingComplete(true);
					await new Promise((resolve) => setTimeout(resolve, 800));
					workflowStore.setProgress(null);
					workflowStore.setStep(6);
				} else if (event.type === "error") {
					error = event.error || "Transcription failed";
					workflowStore.setProgress(null);
				}
			}
		} catch (e) {
			console.error("Streaming failed:", e);
			error = e instanceof Error ? e.message : "Streaming failed";
			workflowStore.setProgress(null);
		}
	}

	// Get the appropriate greeting message based on current step
	function getGreetingKey(step: number): string {
		if (step <= 4) return "workflow.meeting.greeting.upload";
		if (step === 5) return "workflow.meeting.greeting.processing";
		if (step === 6) return "workflow.meeting.greeting.speakers";
		if (step === 7) return "workflow.meeting.greeting.protocol";
		if (step === 8) return "workflow.meeting.greeting.export";
		return "workflow.meeting.greeting.success";
	}

	let selectedFileObj: File | null = null;

	// Handle file upload
	async function handleFileSelected(file: File) {
		selectedFileObj = file;
		workflowStore.setFile({
			name: file.name,
			size: file.size,
			type: file.type,
			url: URL.createObjectURL(file),
		});
		workflowStore.setStep(4);
	}

	// Handle processing start
	let useStreamingApi = true; // Set to true to use real backend streaming

	async function handleStartProcessing() {
		workflowStore.setStep(5);

		// Skip real API call if not using streaming API
		if (!useStreamingApi) {
			return;
		}

		// Emit initial progress to immediately transition from "connecting" to processing stages
		workflowStore.setProgress({
			stage: "uploading",
			percent: 0,
			message: "Datei wird hochgeladen...",
		});

		// Upload the file first
		try {
			const state = $currentWorkflow;
			if (!state?.file?.url && !selectedFileObj) {
				console.error("No file selected for upload");
				error = "No file selected. Please select a file first.";
				workflowStore.setStep(4);
				return;
			}

			// Get the File object (use the raw memory file, or fallback to fetching the blob)
			let fileToUpload: File;
			if (selectedFileObj) {
				fileToUpload = selectedFileObj;
			} else {
				const response = await fetch(state!.file!.url!);
				const blob = await response.blob();
				fileToUpload = new File([blob], state!.file!.name, {
					type: state!.file!.type,
				});
			}

			// Upload the file to the backend
			console.log(
				`Uploading file: ${fileToUpload.name} (${fileToUpload.size} bytes)`,
			);
			await WorkflowAPI.uploadFile(jobId, fileToUpload);
			console.log(
				"File uploaded successfully, starting transcription stream...",
			);
		} catch (e) {
			console.error("Failed to upload file:", e);
			error = e instanceof Error ? e.message : "Failed to upload file";
			workflowStore.setStep(4);
			return;
		}

		// Start the SSE stream
		startStreaming();
	}

	// Handle exit from processing (back to chat while processing continues)
	function handleProcessingExit() {
		// Processing continues in background via workflowStore persistence
		goto("/chat");
	}

	// Handle Next button from processing
	function handleProcessingNext() {
		// If using real API, just proceed to next step (data is already loaded)
		if (useStreamingApi) {
			workflowStore.setStep(6);
			return;
		}

		// DEMO ONLY: Set mock speakers
		// Set mock file for context header if not already set
		if (!$currentWorkflow?.file) {
			workflowStore.setFile({
				name: "Q2-Budget-Planning-2024-01-15.mp4",
				size: 156000000,
				type: "video/mp4",
				duration: 1992, // 33:12
			});
		}

		// Set mock speakers for demo/testing with realistic enterprise data
		// High confidence (>=85) shows detected name, low confidence shows "Unknown Speaker"
		const mockSpeakers = [
			{
				id: "speaker-1",
				detectedName: "Thomas Müller",
				confirmedName: "",
				sampleAudioUrl: "/audio/sample1.mp3", // Demo URL
				speakingTime: 847, // 14:07
				transcriptSnippet:
					"Guten Morgen zusammen, fangen wir mit dem Budget für Q2 an...",
				confidence: 96, // High - will show "Thomas Müller"
				waveformData: [
					0.2, 0.4, 0.8, 0.6, 0.9, 0.5, 0.7, 0.3, 0.6, 0.8, 0.4, 0.5,
					0.7, 0.9, 0.6,
				],
			},
			{
				id: "speaker-2",
				detectedName: "Anna Schmidt",
				confirmedName: "",
				sampleAudioUrl: "/audio/sample2.mp3",
				speakingTime: 623, // 10:23
				transcriptSnippet:
					"Ich möchte kurz auf die technischen Herausforderungen eingehen...",
				confidence: 91, // High - will show "Anna Schmidt"
				waveformData: [
					0.3, 0.6, 0.4, 0.8, 0.5, 0.7, 0.9, 0.4, 0.6, 0.3, 0.7, 0.8,
					0.5, 0.4, 0.6,
				],
			},
			{
				id: "speaker-3",
				detectedName: "Unbekannt",
				confirmedName: "",
				sampleAudioUrl: "/audio/sample3.mp3",
				speakingTime: 312, // 5:12
				transcriptSnippet:
					"Aus unserer Sicht als Partner wäre es wichtig...",
				confidence: 62, // Low - will show "Unknown Speaker"
				waveformData: [
					0.5, 0.3, 0.7, 0.4, 0.6, 0.8, 0.3, 0.5, 0.9, 0.6, 0.4, 0.7,
					0.5, 0.3, 0.8,
				],
			},
			{
				id: "speaker-4",
				detectedName: "Michael Weber",
				confirmedName: "",
				sampleAudioUrl: "/audio/sample4.mp3",
				speakingTime: 189, // 3:09
				transcriptSnippet:
					"Das Projekt-Timeline sieht momentan noch sehr eng aus...",
				confidence: 88, // High - will show "Michael Weber"
				waveformData: [
					0.4, 0.7, 0.5, 0.3, 0.8, 0.6, 0.4, 0.9, 0.5, 0.7, 0.3, 0.6,
					0.8, 0.4, 0.5,
				],
			},
		];
		workflowStore.setSpeakers(mockSpeakers);
		workflowStore.setProcessingComplete(true);
		workflowStore.setStep(6);
	}

	// Handle speaker confirmation
	async function handleSpeakersConfirmed() {
		workflowStore.setStep(7);
		showSplitView = false; // Start with centered view

		// Generate protocol
		try {
			const response = await WorkflowAPI.generateProtocol(jobId);
			workflowStore.setProtocol(response.protocol);

			// Trigger split view after 500ms delay for smooth animation
			setTimeout(() => {
				showSplitView = true;
			}, 500);
		} catch (e) {
			console.error("Failed to generate protocol:", e);
			// Still trigger split view even if protocol generation fails
			setTimeout(() => {
				showSplitView = true;
			}, 500);
		}
	}

	// Handle protocol save and continue to export confirmation
	async function handleProtocolSaveAndContinue() {
		// Save protocol to history database
		const state = $currentWorkflow;
		if (state?.protocol) {
			try {
				if (state.historyId) {
					// Update existing history record (prevent duplicates)
					console.log("💾 Updating existing protocol in history:", state.historyId);
					await updateHistoryPayload(state.historyId, { protocol: state.protocol });
					console.log("✅ Protocol updated in history");
				} else {
					// Create new history record
					console.log("💾 Creating new meeting protocol in history...");
					const created = await createHistory(
						"Meeting Documentation",
						state.protocol.title,
						{ protocol: state.protocol },
					);
					console.log("✅ Protocol saved to history:", created.id);

					// Store history ID to prevent duplicates on re-save
					workflowStore.updateWorkflow({ historyId: created.id });

					// Add to history store for sidebar
					historyStore.addItem({
						id: created.id,
						workflow_id: created.workflow_id,
						workflow_name: created.workflow_name,
						title: created.title,
						created_at: created.created_at,
						updated_at: created.updated_at,
					});
				}
			} catch (error) {
				console.error("❌ Failed to save protocol to history:", error);
				// Continue anyway - don't block the workflow
			}
		}

		// Move to export confirmation step
		workflowStore.setStep(8);
	}

	// Handle actual export to Confluence
	async function handleExportToConfluence(
		data: { spaceId: string; parentPageId: string },
	) {
		const { spaceId, parentPageId } = data;
		isExporting = true;
		try {
			const state = $currentWorkflow;
			if (state?.protocol) {
				// Publish to Confluence with destination
				const response = await WorkflowAPI.publishToConfluence(
					state.protocol,
					spaceId,
				);
				workflowStore.setConfluenceUrl(response.confluence_url);
			}
			workflowStore.setStep(9);
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

	// Go back to editing from export confirmation
	function handleBackToEdit() {
		workflowStore.setProtocolSaved(false);
		workflowStore.setStep(7);
	}

	// Handle PDF export
	async function handleExportPdf() {
		isExporting = true;
		try {
			const state = $currentWorkflow;
			if (state?.protocol && jobId) {
				// Generate PDF and trigger download (handled by API)
				await WorkflowAPI.exportToPdf(state.protocol, jobId);
			}
		} catch (e) {
			console.error("Failed to export PDF:", e);
			error = e instanceof Error ? e.message : "Failed to export PDF";
		} finally {
			isExporting = false;
		}
	}

	// Handle Nora action - navigate to chat with protocol loaded as context
	function handleNoraAction(
		data: { type: "email" | "status" | "chat" },
	) {
		const actionType = data.type;
		workflowStore.setPostAction(actionType as any);
		goto(
			`/chat?context=meeting-protocol&jobId=${jobId}&action=${actionType}`,
		);
	}

	// Handle post-action selection
	function handlePostActionSelected(action: string) {
		workflowStore.setPostAction(action as any);
		workflowStore.setStep(9);
	}

	// Handle workflow completion
	function handleComplete() {
		goto("/chat");
	}

	// Sidebar handlers
	function handleNewChat() {
		goto("/chat");
	}

	function handleSelectSession(sessionId: string) {
		goto(`/chat/${sessionId}`);
	}

	// Handle regenerating state from TemplateReview
	function handleRegenerating(value: boolean) {
		isRegenerating = value;

		if (isRegenerating) {
			// Start progressive message cycle
			regenerationMessage = "Loading template...";
			let messageIndex = 0;
			const messages = [
				"Loading template...",
				"Generating preview...",
				"Almost done...",
			];

			messageInterval = setInterval(() => {
				messageIndex = (messageIndex + 1) % messages.length;
				regenerationMessage = messages[messageIndex];
			}, 2000);
		} else {
			// Clear interval when regeneration completes
			if (messageInterval) {
				clearInterval(messageInterval);
				messageInterval = null;
			}
		}
	}
</script>

<svelte:head>
	<title>{$t("workflow.meeting.title")} - Nora</title>
</svelte:head>

<NoraLayout
	currentSessionId={null}
	onnewChat={handleNewChat}
	onselectSession={handleSelectSession}
>
	<!-- Workflow Content - matching chat container width -->
	<div
		class="workflow-content"
		class:with-preview={$currentWorkflow?.currentStep === 7}
	>
		<!-- Back link removed as per user request -->

		<!-- Error Banner -->
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
				<button onclick={() => (error = null)}>
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
			</div>
		{/if}

		<!-- Nora Action Card (mimics answer-card from chat) -->
		{#if $currentWorkflow}
			{@const step = $currentWorkflow.currentStep}
			<div class="action-card">
				<!-- Message header with avatar -->
				<div class="message-header">
					<div class="message-avatar">
						<img src="/favicon.png" alt="Nora" class="avatar-img" />
					</div>
					<span class="message-name">Nora</span>
					{#if step < 9}
						<div class="header-progress">
							<StepIndicator currentStep={step} />
						</div>
					{/if}
				</div>

				<!-- Nora's greeting message -->
				<p class="nora-greeting">{$t(getGreetingKey(step))}</p>

				<!-- The actual step content (dropzone, progress, etc.) -->
				<div class="step-content">
					<!-- Step 1-4: Upload + Configure (combined single-page flow) -->
					{#if step === 1 || step === 2 || step === 3 || step === 4}
						<UploadAndConfigure
							file={$currentWorkflow.file}
							{jobId}
							onFileSelected={handleFileSelected}
							onStart={handleStartProcessing}
							onBack={() => goto('/chat')}
						/>

						<!-- Step 5: Processing -->
					{:else if step === 5}
						<ProcessingProgress
							progress={$currentWorkflow.processingProgress}
							demo={!useStreamingApi}
							processingComplete={$currentWorkflow.processingComplete ||
								false}
							onExit={handleProcessingExit}
							onNext={handleProcessingNext}
						/>

						<!-- Step 6: Speaker Verification -->
					{:else if step === 6}
						<SpeakerVerification
							speakers={$currentWorkflow.speakers}
							file={$currentWorkflow.file}
							onconfirmed={handleSpeakersConfirmed}
							onback={() => workflowStore.setStep(5)}
						/>

						<!-- Step 7: Protocol Review with Template Selection -->
					{:else if step === 7}
						<TemplateReview
							protocol={$currentWorkflow.protocol}
							{jobId}
							onSaveAndContinue={handleProtocolSaveAndContinue}
							onBack={() => workflowStore.setStep(6)}
							onRegenerating={handleRegenerating}
						/>

						<!-- Step 8: Export Confirmation -->
					{:else if step === 8}
						<ExportConfirmation
							protocol={$currentWorkflow.protocol}
							{isExporting}
							onExport={handleExportToConfluence}
							onExportPdf={handleExportPdf}
							onBack={handleBackToEdit}
							onNoraAction={handleNoraAction}
						/>

						<!-- Step 9: Success -->
					{:else if step === 9}
						<SuccessScreen
							confluenceUrl={$currentWorkflow.confluenceUrl}
							onActionSelected={handlePostActionSelected}
							onComplete={handleComplete}
						/>
					{/if}
				</div>
			</div>
		{:else}
			<div class="action-card">
				<div class="loading">
					<div class="spinner"></div>
					<p>{$t("common.loading")}</p>
				</div>
			</div>
		{/if}
	</div>

	<!-- Editor Side Panel (flat, integrated - like Claude's artifacts) -->
	{#if $currentWorkflow?.currentStep === 7 && $currentWorkflow?.protocol}
		<div class="preview-side-panel" class:split-view-active={showSplitView}>
			<div class="preview-panel-header">
				<span>Editor</span>
			</div>
			<div class="preview-panel-content">
				{#if isRegenerating}
					<div class="regenerating-overlay">
						<div class="regenerating-content">
							<div class="spinner-large pulse"></div>
							<p class="regenerating-text">
								{regenerationMessage}
							</p>
						</div>
					</div>
				{/if}
				<ConfluencePreview
					protocol={$currentWorkflow.protocol}
					editable={true}
				/>
			</div>
		</div>
	{/if}

	<!-- Mobile Preview Drawer -->
	{#if $currentWorkflow?.currentStep === 7 && $currentWorkflow?.protocol}
		<div class="mobile-preview-drawer">
			<div class="drawer-handle"></div>
			<div class="drawer-header">
				<span>Editor</span>
			</div>
			<div class="drawer-content">
				{#if isRegenerating}
					<div class="regenerating-overlay">
						<div class="regenerating-content">
							<div class="spinner-large pulse"></div>
							<p class="regenerating-text">
								{regenerationMessage}
							</p>
						</div>
					</div>
				{/if}
				<ConfluencePreview
					protocol={$currentWorkflow.protocol}
					editable={true}
				/>
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

	/* Shift content left when preview panel is open */
	.workflow-content.with-preview {
		margin-left: 0;
		margin-right: auto;
		/* Initial state: centered, full width */
		max-width: 100%;
		transition:
			transform 300ms ease-in-out,
			max-width 300ms ease-in-out;
	}

	/* When split view is active, slide to the left */
	.workflow-content.with-preview {
		transform: translateX(-380px);
		max-width: 800px;
	}

	@media (max-width: 1280px) {
		.workflow-content.with-preview {
			margin-left: auto;
			transform: none;
		}
	}

	/* Breadcrumb-style back link */
	.back-link {
		display: inline-flex;
		align-items: center;
		gap: 6px;
		font-size: 13px;
		color: var(--slate-500, #64748b);
		text-decoration: none;
		margin-bottom: 16px;
		transition: color 0.15s ease;
	}

	.back-link:hover {
		color: var(--slate-700, #334155);
	}

	.back-link svg {
		width: 16px;
		height: 16px;
	}

	/* Action card - clean, borderless like chat messages */
	.action-card {
		background: transparent;
		padding: 20px 24px;
	}

	/* Message header with avatar */
	.message-header {
		display: flex;
		align-items: center;
		gap: 10px;
		margin-bottom: 16px;
	}

	.message-avatar {
		width: 28px;
		height: 28px;
		border-radius: 50%;
		background: transparent;
		display: flex;
		align-items: center;
		justify-content: center;
		flex-shrink: 0;
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

	/* Header progress indicator - positioned on the right */
	.header-progress {
		margin-left: auto;
	}

	/* Nora's greeting message */
	.nora-greeting {
		font-size: 17px;
		color: var(--slate-700, #334155);
		line-height: 1.6;
		margin: 0 0 20px 0;
	}

	/* Step content container */
	.step-content {
		display: flex;
		flex-direction: column;
		align-items: center;
	}

	/* Error banner */
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

	.error-banner button {
		background: transparent;
		border: none;
		cursor: pointer;
		padding: 4px;
	}

	.error-banner button svg {
		width: 16px;
		height: 16px;
		color: var(--red-500, #ef4444);
	}

	/* Loading state */
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

	.loading p {
		font-size: 14px;
		color: var(--slate-500, #64748b);
		margin: 0;
	}

	@media (max-width: 768px) {
		.workflow-content {
			padding: 16px;
		}

		.action-card {
			padding: 16px;
		}
	}

	/* ============================================
	   Editor Side Panel
	   (Flat, integrated - like Claude's artifacts)
	   ============================================ */
	.preview-side-panel {
		position: fixed;
		top: 57px;
		right: 0;
		width: 850px;
		height: calc(100vh - 57px);
		background: white;
		border-left: 1px solid var(--slate-200, #e2e8f0);
		border-radius: 0;
		/* NO box-shadow - flat, integrated look */
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

	/* Regenerating overlay for editor panel */
	.regenerating-overlay {
		position: absolute;
		top: 0;
		left: 0;
		right: 0;
		bottom: 0;
		background: rgba(255, 255, 255, 0.95);
		display: flex;
		align-items: center;
		justify-content: center;
		z-index: 10;
		backdrop-filter: blur(4px);
		animation: fadeIn 150ms ease-out;
	}

	@keyframes fadeIn {
		from {
			opacity: 0;
		}
		to {
			opacity: 1;
		}
	}

	.regenerating-content {
		display: flex;
		flex-direction: column;
		align-items: center;
		gap: 16px;
	}

	.spinner-large {
		width: 48px;
		height: 48px;
		border: 4px solid var(--slate-200, #e2e8f0);
		border-top-color: var(--blue-500, #3b82f6);
		border-radius: 50%;
		animation: spin 1s linear infinite;
	}

	.spinner-large.pulse {
		animation:
			spin 1s linear infinite,
			pulse 2s ease-in-out infinite;
	}

	@keyframes pulse {
		0%,
		100% {
			transform: scale(1);
			opacity: 1;
		}
		50% {
			transform: scale(1.1);
			opacity: 0.8;
		}
	}

	.regenerating-text {
		font-size: 15px;
		font-weight: 500;
		color: var(--slate-700, #334155);
		margin: 0;
		transition: opacity 300ms ease-in-out;
	}

	/* Hide desktop panel on smaller screens */
	@media (max-width: 1280px) {
		.preview-side-panel {
			display: none;
		}
	}

	/* ============================================
	   Mobile Preview Drawer
	   ============================================ */
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
