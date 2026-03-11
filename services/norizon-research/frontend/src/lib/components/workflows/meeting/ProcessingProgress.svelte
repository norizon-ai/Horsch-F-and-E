<script lang="ts">
	import { t } from "svelte-i18n";
	import { scale, fly, fade } from "svelte/transition";
	import { onMount, onDestroy } from "svelte";
	import type { WorkflowProcessingProgress } from "$lib/types";

	let {
		progress = null,
		demo = false,
		connectionError = null,
		fileName = "Recording",
		totalEstimatedMinutes = 5,
		processingComplete = false,
		onExit = undefined,
		onNext = undefined,
		onCancel = undefined,
		onRetry = undefined,
	}: {
		progress?: WorkflowProcessingProgress | null;
		demo?: boolean;
		connectionError?: string | null;
		fileName?: string;
		totalEstimatedMinutes?: number;
		processingComplete?: boolean;
		onExit?: (() => void) | undefined;
		onNext?: (() => void) | undefined;
		onCancel?: (() => void) | undefined;
		onRetry?: (() => void) | undefined;
	} = $props();

	// Stage definitions with time estimates (as percentage of total)
	const stages = [
		{
			id: "uploading",
			label: "workflow.meeting.processing.stages.uploading",
			timePercent: 25,
			subStatuses: [
				"workflow.meeting.processing.subStatus.uploading.encrypting",
				"workflow.meeting.processing.subStatus.uploading.verifying",
				"workflow.meeting.processing.subStatus.uploading.secured",
			],
		},
		{
			id: "transcribing",
			label: "workflow.meeting.processing.stages.transcribing",
			timePercent: 25,
			subStatuses: [
				"workflow.meeting.processing.subStatus.transcribing.detecting",
				"workflow.meeting.processing.subStatus.transcribing.processing",
				"workflow.meeting.processing.subStatus.transcribing.refining",
			],
		},
		{
			id: "diarizing",
			label: "workflow.meeting.processing.stages.diarizing",
			timePercent: 25,
			subStatuses: [
				"workflow.meeting.processing.subStatus.diarizing.profiling",
				"workflow.meeting.processing.subStatus.diarizing.clustering",
				"workflow.meeting.processing.subStatus.diarizing.labeling",
			],
		},
		{
			id: "identifying",
			label: "workflow.meeting.processing.stages.identifying",
			timePercent: 15,
			subStatuses: [
				"workflow.meeting.processing.subStatus.identifying.analyzing",
				"workflow.meeting.processing.subStatus.identifying.detecting",
				"workflow.meeting.processing.subStatus.identifying.inferring",
			],
		},
		{
			id: "correcting",
			label: "workflow.meeting.processing.stages.correcting",
			timePercent: 10,
			subStatuses: [
				"workflow.meeting.processing.subStatus.correcting.loading",
				"workflow.meeting.processing.subStatus.correcting.applying",
				"workflow.meeting.processing.subStatus.correcting.validating",
			],
		},
	];

	let isComplete = $state(false);
	$effect(() => { if (processingComplete) isComplete = true; });

	let showCancelDialog = $state(false);
	let currentSubStatusIndex = $state(0);
	let subStatusInterval: ReturnType<typeof setInterval> | null = null;
	let demoInterval: ReturnType<typeof setInterval> | null = null;
	let demoStarted = false;
	let elapsedSeconds = $state(0);
	let elapsedInterval: ReturnType<typeof setInterval> | null = null;

	// Demo/simulated progress - start at 100% if already complete
	let simulatedProgress: WorkflowProcessingProgress = $state(processingComplete
		? {
				stage: stages[stages.length - 1].id,
				percent: 100,
				message: "",
			}
		: {
				stage: stages[0].id,
				percent: 0,
				message: "",
			});

	// Show "connecting" state when not in demo mode, no progress yet, no error, and not complete
	let isConnecting = $derived(
		!demo && !progress && !connectionError && !processingComplete
	);
	let currentProgress = $derived(processingComplete
		? {
				stage: stages[stages.length - 1].id,
				percent: 100,
				message: "",
			}
		: demo
			? simulatedProgress
			: progress);
	let overallPercent = $derived(currentProgress?.percent || 0);

	let remainingMinutes = $derived(Math.max(
		1,
		Math.ceil(totalEstimatedMinutes * (1 - overallPercent / 100)),
	));

	function getStageStatus(
		stageId: string,
	): "completed" | "current" | "pending" {
		if (!currentProgress) return "pending";
		const currentIndex = stages.findIndex(
			(s) => s.id === currentProgress.stage,
		);
		const stageIndex = stages.findIndex((s) => s.id === stageId);
		if (stageIndex < currentIndex) return "completed";
		if (stageIndex === currentIndex) return "current";
		return "pending";
	}

	function getStageTimeEstimate(stageIndex: number): string {
		const minutes = Math.ceil(
			(stages[stageIndex].timePercent / 100) * totalEstimatedMinutes,
		);
		return minutes < 1 ? "<1" : `~${minutes}`;
	}

	function getCurrentStage() {
		if (!currentProgress) return stages[0];
		return stages.find((s) => s.id === currentProgress.stage) || stages[0];
	}

	function rotateSubStatus() {
		const stage = getCurrentStage();
		if (stage?.subStatuses) {
			currentSubStatusIndex =
				(currentSubStatusIndex + 1) % stage.subStatuses.length;
		}
	}

	let previousStage: string | undefined = undefined;
	$effect(() => {
		if (currentProgress?.stage && currentProgress.stage !== previousStage) {
			previousStage = currentProgress.stage;
			currentSubStatusIndex = 0;
		}
	});

	let currentStage = $derived(getCurrentStage());
	let currentSubStatus = $derived(
		currentStage?.subStatuses?.[currentSubStatusIndex] || ""
	);

	// Compute stage statuses reactively
	let stageStatuses = $derived(stages.map((stage) => {
		if (!currentProgress) return "pending";
		const currentIndex = stages.findIndex(
			(s) => s.id === currentProgress.stage,
		);
		const stageIndex = stages.findIndex((s) => s.id === stage.id);
		if (stageIndex < currentIndex) return "completed";
		if (stageIndex === currentIndex) return "current";
		return "pending";
	}) as Array<"completed" | "current" | "pending">);

	$effect(() => {
		if (currentProgress?.percent === 100 && !isComplete) {
			isComplete = true;
			if (subStatusInterval) clearInterval(subStatusInterval);
			if (demoInterval) clearInterval(demoInterval);
			if (elapsedInterval) clearInterval(elapsedInterval);
		}
	});

	function startDemoSimulation() {
		if (demoStarted || demoInterval) return;
		demoStarted = true;

		let demoStageIndex = 0;
		let tick = 0;

		demoInterval = setInterval(() => {
			tick++;
			if (tick % 5 === 0) {
				demoStageIndex++;
				if (demoStageIndex >= stages.length - 1) {
					simulatedProgress = {
						stage: stages[stages.length - 1].id,
						percent: 95,
						message: "",
					};
					if (demoInterval) clearInterval(demoInterval);
					return;
				}
				simulatedProgress = {
					stage: stages[demoStageIndex].id,
					percent: Math.floor((demoStageIndex / stages.length) * 100),
					message: "",
				};
			}
		}, 2500);
	}

	function formatElapsed(seconds: number): string {
		const mins = Math.floor(seconds / 60);
		const secs = seconds % 60;
		return `${mins}:${secs.toString().padStart(2, "0")}`;
	}

	function handleContinueInBackground() {
		onExit?.();
	}

	function handleCancelClick() {
		showCancelDialog = true;
	}

	function handleCancelConfirm() {
		showCancelDialog = false;
		onCancel?.();
	}

	function handleCancelDismiss() {
		showCancelDialog = false;
	}

	onMount(() => {
		// Don't start timers if processing is already complete (returning via back nav)
		if (processingComplete) {
			isComplete = true;
			return;
		}
		if (demo) startDemoSimulation();
		subStatusInterval = setInterval(rotateSubStatus, 2000);
		elapsedInterval = setInterval(() => {
			elapsedSeconds++;
		}, 1000);
	});

	onDestroy(() => {
		if (subStatusInterval) clearInterval(subStatusInterval);
		if (demoInterval) clearInterval(demoInterval);
		if (elapsedInterval) clearInterval(elapsedInterval);
	});

	function handleRetry() {
		onRetry?.();
	}
</script>

<div class="processing-container">
	<!-- Connection error state -->
	{#if connectionError}
		<div class="connection-error" transition:fade={{ duration: 200 }}>
			<div class="error-icon">
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
			</div>
			<h3>{$t("workflow.meeting.processing.connectionError.title")}</h3>
			<p class="error-message">{connectionError}</p>
			<div class="error-actions">
				<button class="btn-primary" onclick={handleRetry}>
					<svg
						viewBox="0 0 24 24"
						fill="none"
						stroke="currentColor"
						stroke-width="2"
					>
						<polyline points="23 4 23 10 17 10" />
						<path d="M20.49 15a9 9 0 1 1-2.12-9.36L23 10" />
					</svg>
					{$t("workflow.meeting.processing.connectionError.retry")}
				</button>
				<button
					class="btn-secondary"
					onclick={() => onCancel?.()}
				>
					{$t("workflow.meeting.processing.cancel")}
				</button>
			</div>
		</div>
	{:else if isConnecting}
		<!-- Connecting state — waiting for first progress event -->
		<div class="connecting-state" transition:fade={{ duration: 200 }}>
			<div class="connecting-spinner"></div>
			<p class="connecting-text">
				{$t("workflow.meeting.processing.connecting")}
			</p>
		</div>
	{/if}

	<!-- Header with ETA -->
	<div class="progress-header" class:hidden={isConnecting || connectionError}>
		<div class="file-info">
			<svg
				viewBox="0 0 24 24"
				fill="none"
				stroke="currentColor"
				stroke-width="2"
			>
				<path d="M9 18V5l12-2v13" />
				<circle cx="6" cy="18" r="3" />
				<circle cx="18" cy="16" r="3" />
			</svg>
			<span class="file-name">{fileName}</span>
		</div>
		<div class="time-info">
			<div class="elapsed">
				<span class="time-label"
					>{$t("workflow.meeting.processing.elapsed")}</span
				>
				<span class="time-value">{formatElapsed(elapsedSeconds)}</span>
			</div>
			<div class="divider"></div>
			<div class="remaining">
				<span class="time-label"
					>{$t("workflow.meeting.processing.remaining")}</span
				>
				<span class="time-value highlight">~{remainingMinutes} min</span
				>
			</div>
		</div>
	</div>

	<!-- Overall progress bar -->
	<div
		class="overall-progress"
		class:hidden={isConnecting || connectionError}
	>
		<div class="progress-bar">
			<div class="progress-fill" style="width: {overallPercent}%"></div>
		</div>
		<span class="progress-percent">{overallPercent}%</span>
	</div>

	<!-- Issue 3 Fix: Horizontal timeline showing all steps -->
	<div
		class="timeline-container"
		class:hidden={isConnecting || connectionError}
	>
		{#each stages as stage, index}
			<div
				class="timeline-step"
				class:completed={stageStatuses[index] === "completed"}
				class:current={stageStatuses[index] === "current"}
				class:pending={stageStatuses[index] === "pending"}
			>
				<div class="timeline-dot">
					{#if stageStatuses[index] === "completed"}
						<svg
							viewBox="0 0 24 24"
							fill="none"
							stroke="currentColor"
							stroke-width="3"
						>
							<polyline points="20 6 9 17 4 12" />
						</svg>
					{/if}
				</div>
				<span class="timeline-label">{$t(stage.label)}</span>
				{#if index < stages.length - 1}
					<div
						class="timeline-connector"
						class:active={stageStatuses[index] === "completed"}
					></div>
				{/if}
			</div>
		{/each}
	</div>

	<!-- Vertical pipeline with time estimates -->
	<!-- Task 10: Scrolling/flipping animation - show only current step, one before, one after -->
	<div class="pipeline" class:hidden={isConnecting || connectionError}>
		{#each stages as stage, index}
			{@const shouldShow =
				stageStatuses[index] === "current" ||
				(index > 0 && stageStatuses[index - 1] === "current") ||
				(index < stages.length - 1 &&
					stageStatuses[index + 1] === "current")}
			{#if shouldShow}
				<div
					class="stage"
					class:current={stageStatuses[index] === "current"}
					class:completed={stageStatuses[index] === "completed"}
					class:pending={stageStatuses[index] === "pending"}
					class:adjacent={stageStatuses[index] !== "current"}
					in:fly={{
						y: stageStatuses[index] === "pending" ? 20 : -20,
						duration: 300,
					}}
					out:fly={{
						y: stageStatuses[index] === "completed" ? -20 : 20,
						duration: 300,
					}}
				>
					<!-- Dot indicator -->
					<div class="dot-container">
						<div
							class="dot"
							class:pulse={stageStatuses[index] === "current"}
							class:done={stageStatuses[index] === "completed"}
						></div>
						{#if index < stages.length - 1}
							<div
								class="connector"
								class:done={stageStatuses[index] ===
									"completed"}
							></div>
						{/if}
					</div>

					<!-- Stage content -->
					<div class="stage-content">
						<div class="stage-row">
							<span class="stage-label">{$t(stage.label)}</span>
							<span
								class="stage-time"
								class:active={stageStatuses[index] ===
									"current"}
							>
								{#if stageStatuses[index] === "completed"}
									<svg
										viewBox="0 0 24 24"
										fill="none"
										stroke="currentColor"
										stroke-width="2.5"
									>
										<polyline points="20 6 9 17 4 12" />
									</svg>
								{:else}
									{getStageTimeEstimate(index)} min
								{/if}
							</span>
						</div>
						{#if stageStatuses[index] === "current" && currentSubStatus}
							{#key currentSubStatus}
								<span
									class="stage-substatus"
									in:fly={{ y: 4, duration: 150 }}
								>
									{$t(currentSubStatus)}
								</span>
							{/key}
						{/if}
					</div>
				</div>
			{/if}
		{/each}
	</div>

	<!-- Trust badges -->
	<div class="trust-badges" class:hidden={isConnecting || connectionError}>
		<div class="trust-badge">
			<svg
				viewBox="0 0 24 24"
				fill="none"
				stroke="currentColor"
				stroke-width="2"
			>
				<rect x="3" y="11" width="18" height="11" rx="2" ry="2" />
				<path d="M7 11V7a5 5 0 0 1 10 0v4" />
			</svg>
			<span>{$t("workflow.meeting.confirm.securityBadge")}</span>
		</div>
		<div class="trust-badge">
			<svg
				viewBox="0 0 24 24"
				fill="none"
				stroke="currentColor"
				stroke-width="2"
			>
				<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z" />
			</svg>
			<span>{$t("workflow.meeting.processing.trustBadge")}</span>
		</div>
	</div>

	<!-- Footer Actions -->
	{#if connectionError}
		<!-- No footer when error state is shown (has its own actions) -->
	{:else if isConnecting}
		<!-- No footer when connecting -->
	{:else if isComplete}
		<!-- Completed state footer - show continue button -->
		<div class="workflow-footer">
			<div></div>
			<button
				class="btn-primary"
				onclick={() => onNext?.()}
			>
				{$t("common.next")}
				<svg
					viewBox="0 0 24 24"
					fill="none"
					stroke="currentColor"
					stroke-width="2"
				>
					<line x1="5" y1="12" x2="19" y2="12" />
					<polyline points="12 5 19 12 12 19" />
				</svg>
			</button>
		</div>
	{:else}
		<div class="workflow-footer">
			<button class="btn-secondary" onclick={handleCancelClick}>
				<svg
					viewBox="0 0 24 24"
					fill="none"
					stroke="currentColor"
					stroke-width="2"
				>
					<line x1="18" y1="6" x2="6" y2="18" />
					<line x1="6" y1="6" x2="18" y2="18" />
				</svg>
				{$t("workflow.meeting.processing.cancel")}
			</button>
			<div class="footer-right">
				<button
					class="btn-primary"
					onclick={handleContinueInBackground}
				>
					{$t("workflow.meeting.processing.continueBackground")}
					<svg
						viewBox="0 0 24 24"
						fill="none"
						stroke="currentColor"
						stroke-width="2"
					>
						<rect
							x="2"
							y="3"
							width="20"
							height="14"
							rx="2"
							ry="2"
						/>
						<line x1="8" y1="21" x2="16" y2="21" />
						<line x1="12" y1="17" x2="12" y2="21" />
					</svg>
				</button>
				{#if demo}
					<button
						class="btn-primary"
						onclick={() => {
							onNext?.();
						}}
					>
						{$t("common.next")}
						<svg
							viewBox="0 0 24 24"
							fill="none"
							stroke="currentColor"
							stroke-width="2"
						>
							<line x1="5" y1="12" x2="19" y2="12" />
							<polyline points="12 5 19 12 12 19" />
						</svg>
					</button>
				{/if}
			</div>
		</div>
	{/if}
</div>

<!-- Cancel confirmation dialog -->
{#if showCancelDialog}
	<div class="dialog-overlay" transition:fade={{ duration: 150 }}>
		<div class="dialog" transition:scale={{ duration: 200, start: 0.95 }}>
			<div class="dialog-icon warning">
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
			</div>
			<h3>{$t("workflow.meeting.processing.cancelDialog.title")}</h3>
			<p>{$t("workflow.meeting.processing.cancelDialog.message")}</p>
			<div class="dialog-actions">
				<button
					class="dialog-btn secondary"
					onclick={handleCancelDismiss}
				>
					{$t("workflow.meeting.processing.cancelDialog.continue")}
				</button>
				<button
					class="dialog-btn danger"
					onclick={handleCancelConfirm}
				>
					{$t("workflow.meeting.processing.cancelDialog.confirm")}
				</button>
			</div>
		</div>
	</div>
{/if}

<style>
	.processing-container {
		display: flex;
		flex-direction: column;
		gap: 20px;
		width: 100%;
		max-width: 800px;
	}

	/* Progress Header */
	.progress-header {
		display: flex;
		justify-content: space-between;
		align-items: center;
		padding: 12px 16px;
		background: var(--slate-50, #f8fafc);
		border: 1px solid var(--slate-200, #e2e8f0);
		border-radius: 10px;
	}

	.file-info {
		display: flex;
		align-items: center;
		gap: 8px;
	}

	.file-info svg {
		width: 18px;
		height: 18px;
		color: var(--slate-400, #94a3b8);
	}

	.file-name {
		font-size: 14px;
		font-weight: 600;
		color: var(--slate-700, #334155);
		max-width: 160px;
		overflow: hidden;
		text-overflow: ellipsis;
		white-space: nowrap;
	}

	.time-info {
		display: flex;
		align-items: center;
		gap: 12px;
	}

	.elapsed,
	.remaining {
		display: flex;
		flex-direction: column;
		align-items: flex-end;
		gap: 1px;
	}

	.time-label {
		font-size: 10px;
		text-transform: uppercase;
		letter-spacing: 0.5px;
		color: var(--slate-400, #94a3b8);
	}

	.time-value {
		font-size: 14px;
		font-weight: 600;
		color: var(--slate-600, #475569);
		font-variant-numeric: tabular-nums;
	}

	.time-value.highlight {
		color: var(--blue-600, #2563eb);
	}

	.divider {
		width: 1px;
		height: 28px;
		background: var(--slate-200, #e2e8f0);
	}

	/* Overall Progress Bar */
	.overall-progress {
		display: flex;
		align-items: center;
		gap: 12px;
	}

	.progress-bar {
		flex: 1;
		height: 8px;
		background: var(--slate-200, #e2e8f0);
		border-radius: 4px;
		overflow: hidden;
	}

	.progress-fill {
		height: 100%;
		background: linear-gradient(
			90deg,
			var(--blue-500, #3b82f6),
			var(--blue-400, #60a5fa)
		);
		border-radius: 4px;
		transition: width 0.5s ease;
	}

	.progress-percent {
		font-size: 14px;
		font-weight: 700;
		color: var(--slate-700, #334155);
		min-width: 40px;
		text-align: right;
		font-variant-numeric: tabular-nums;
	}

	/* Issue 3 Fix: Horizontal timeline */
	.timeline-container {
		display: flex;
		align-items: center;
		justify-content: space-between;
		padding: 16px 20px;
		background: var(--slate-50, #f8fafc);
		border: 1px solid var(--slate-200, #e2e8f0);
		border-radius: 10px;
		margin-bottom: 12px;
	}

	.timeline-step {
		display: flex;
		flex-direction: column;
		align-items: center;
		gap: 6px;
		flex: 1;
		position: relative;
	}

	.timeline-dot {
		width: 24px;
		height: 24px;
		border-radius: 50%;
		background: var(--slate-200, #e2e8f0);
		border: 2px solid var(--slate-200, #e2e8f0);
		display: flex;
		align-items: center;
		justify-content: center;
		transition: all 0.3s ease;
		z-index: 1;
	}

	.timeline-step.completed .timeline-dot {
		background: var(--green-500, #22c55e);
		border-color: var(--green-500, #22c55e);
	}

	.timeline-step.completed .timeline-dot svg {
		width: 14px;
		height: 14px;
		color: white;
	}

	.timeline-step.current .timeline-dot {
		background: var(--blue-500, #3b82f6);
		border-color: var(--blue-500, #3b82f6);
		box-shadow: 0 0 0 4px rgba(59, 130, 246, 0.2);
		animation: pulse-dot 1.5s ease-in-out infinite;
	}

	@keyframes pulse-dot {
		0%,
		100% {
			box-shadow: 0 0 0 4px rgba(59, 130, 246, 0.2);
		}
		50% {
			box-shadow: 0 0 0 8px rgba(59, 130, 246, 0.1);
		}
	}

	.timeline-label {
		font-size: 10px;
		font-weight: 500;
		color: var(--slate-400, #94a3b8);
		text-align: center;
		line-height: 1.2;
	}

	.timeline-step.current .timeline-label {
		color: var(--blue-700, #1d4ed8);
		font-weight: 600;
	}

	.timeline-step.completed .timeline-label {
		color: var(--green-700, #15803d);
		font-weight: 500;
	}

	.timeline-connector {
		position: absolute;
		left: 50%;
		top: 12px;
		width: 100%;
		height: 2px;
		background: var(--slate-200, #e2e8f0);
		transform: translateY(-50%);
		transition: background 0.3s ease;
	}

	.timeline-connector.active {
		background: var(--green-400, #4ade80);
	}

	.timeline-step:last-child .timeline-connector {
		display: none;
	}

	/* Pipeline */
	.pipeline {
		display: flex;
		flex-direction: column;
		gap: 0;
		padding: 8px 0;
	}

	/* Stage row */
	.stage {
		display: flex;
		align-items: flex-start;
		gap: 12px;
		padding: 8px 0;
		transition:
			opacity 0.3s ease,
			transform 0.3s ease;
	}

	/* Task 10: Fade adjacent stages slightly */
	.stage.adjacent {
		opacity: 0.5;
		transform: scale(0.95);
	}

	/* Dot container with connector */
	.dot-container {
		display: flex;
		flex-direction: column;
		align-items: center;
		width: 12px;
		flex-shrink: 0;
	}

	.dot {
		width: 10px;
		height: 10px;
		margin-top: 3px;
		border-radius: 50%;
		background: var(--slate-300, #cbd5e1);
		flex-shrink: 0;
		transition: all 0.2s ease;
	}

	.dot.pulse {
		background: var(--blue-500, #3b82f6);
		box-shadow: 0 0 0 4px rgba(59, 130, 246, 0.2);
		animation: pulse 1.5s ease-in-out infinite;
	}

	.dot.done {
		background: var(--blue-500, #3b82f6);
	}

	.connector {
		width: 2px;
		height: 24px;
		background: var(--slate-200, #e2e8f0);
		margin-top: 4px;
	}

	.connector.done {
		background: var(--blue-300, #93c5fd);
	}

	@keyframes pulse {
		0%,
		100% {
			box-shadow: 0 0 0 4px rgba(59, 130, 246, 0.2);
		}
		50% {
			box-shadow: 0 0 0 8px rgba(59, 130, 246, 0.1);
		}
	}

	/* Stage content */
	.stage-content {
		flex: 1;
		display: flex;
		flex-direction: column;
		gap: 2px;
		min-width: 0;
	}

	.stage-row {
		display: flex;
		justify-content: space-between;
		align-items: center;
	}

	.stage-label {
		font-size: 14px;
		color: var(--slate-400, #94a3b8);
		transition: color 0.2s ease;
	}

	.stage.current .stage-label {
		color: var(--slate-800, #1e293b);
		font-weight: 600;
	}

	.stage.completed .stage-label {
		color: var(--slate-500, #64748b);
	}

	.stage-time {
		font-size: 12px;
		color: var(--slate-400, #94a3b8);
		display: flex;
		align-items: center;
		gap: 4px;
	}

	.stage-time.active {
		color: var(--blue-500, #3b82f6);
		font-weight: 500;
	}

	.stage-time svg {
		width: 14px;
		height: 14px;
		color: var(--blue-500, #3b82f6);
	}

	.stage-substatus {
		font-size: 12px;
		color: var(--blue-500, #3b82f6);
	}

	/* Trust badges */
	.trust-badges {
		display: flex;
		justify-content: center;
		gap: 10px;
		flex-wrap: wrap;
	}

	.trust-badge {
		display: flex;
		align-items: center;
		gap: 6px;
		padding: 6px 12px;
		background: var(--blue-50, #eff6ff);
		border: 1px solid var(--blue-200, #bfdbfe);
		border-radius: 6px;
		font-size: 12px;
		font-weight: 500;
		color: var(--blue-700, #1d4ed8);
	}

	.trust-badge svg {
		width: 14px;
		height: 14px;
		color: var(--blue-600, #2563eb);
	}

	/* Workflow Footer */
	.workflow-footer {
		display: flex;
		justify-content: space-between;
		align-items: center;
		gap: 12px;
		padding-top: 16px;
		border-top: 1px solid var(--slate-200, #e2e8f0);
		margin-top: 8px;
	}

	.footer-right {
		display: flex;
		align-items: center;
		gap: 12px;
	}

	.btn-secondary {
		display: flex;
		align-items: center;
		gap: 8px;
		padding: 10px 20px;
		font-size: 14px;
		font-weight: 500;
		color: var(--slate-700, #334155);
		background: white;
		border: 1px solid var(--slate-300, #cbd5e1);
		border-radius: 8px;
		cursor: pointer;
		transition: all 0.15s ease;
	}

	.btn-secondary:hover {
		background: var(--slate-50, #f8fafc);
	}

	.btn-secondary svg {
		width: 16px;
		height: 16px;
	}

	.btn-primary {
		display: flex;
		align-items: center;
		justify-content: center;
		gap: 8px;
		padding: 10px 20px;
		font-size: 14px;
		font-weight: 500;
		color: white;
		background: var(--blue-500, #3b82f6);
		border: none;
		border-radius: 8px;
		cursor: pointer;
		transition: all 0.15s ease;
	}

	.btn-primary:hover {
		background: var(--blue-600, #2563eb);
	}

	.btn-primary svg {
		width: 16px;
		height: 16px;
	}

	/* Cancel Dialog */
	.dialog-overlay {
		position: fixed;
		top: 0;
		left: 0;
		right: 0;
		bottom: 0;
		background: rgba(15, 23, 42, 0.5);
		display: flex;
		align-items: center;
		justify-content: center;
		z-index: 200;
		padding: 20px;
	}

	.dialog {
		background: white;
		border-radius: 16px;
		padding: 24px;
		max-width: 360px;
		width: 100%;
		text-align: center;
		box-shadow: 0 20px 40px rgba(0, 0, 0, 0.15);
	}

	.dialog-icon {
		width: 56px;
		height: 56px;
		border-radius: 50%;
		display: flex;
		align-items: center;
		justify-content: center;
		margin: 0 auto 16px;
	}

	.dialog-icon.warning {
		background: var(--amber-100, #fef3c7);
	}

	.dialog-icon.warning svg {
		width: 28px;
		height: 28px;
		color: var(--amber-600, #d97706);
	}

	.dialog h3 {
		font-size: 18px;
		font-weight: 700;
		color: var(--slate-900, #0f172a);
		margin: 0 0 8px 0;
	}

	.dialog p {
		font-size: 14px;
		color: var(--slate-600, #475569);
		line-height: 1.5;
		margin: 0 0 20px 0;
	}

	.dialog-actions {
		display: flex;
		gap: 10px;
	}

	.dialog-btn {
		flex: 1;
		padding: 12px 16px;
		font-size: 14px;
		font-weight: 600;
		border-radius: 8px;
		cursor: pointer;
		transition: all 0.15s ease;
	}

	.dialog-btn.secondary {
		background: var(--slate-100, #f1f5f9);
		border: 1px solid var(--slate-200, #e2e8f0);
		color: var(--slate-700, #334155);
	}

	.dialog-btn.secondary:hover {
		background: var(--slate-200, #e2e8f0);
	}

	.dialog-btn.danger {
		background: var(--red-500, #ef4444);
		border: none;
		color: white;
	}

	.dialog-btn.danger:hover {
		background: var(--red-600, #dc2626);
	}

	/* Hidden state */
	.hidden {
		display: none !important;
	}

	/* Connecting state */
	.connecting-state {
		display: flex;
		flex-direction: column;
		align-items: center;
		gap: 16px;
		padding: 48px 24px;
	}

	.connecting-spinner {
		width: 36px;
		height: 36px;
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

	.connecting-text {
		font-size: 14px;
		color: var(--slate-500, #64748b);
		margin: 0;
	}

	/* Connection error state */
	.connection-error {
		display: flex;
		flex-direction: column;
		align-items: center;
		gap: 12px;
		padding: 40px 24px;
		text-align: center;
	}

	.error-icon {
		width: 48px;
		height: 48px;
		border-radius: 50%;
		background: var(--red-50, #fef2f2);
		display: flex;
		align-items: center;
		justify-content: center;
	}

	.error-icon svg {
		width: 24px;
		height: 24px;
		color: var(--red-500, #ef4444);
	}

	.connection-error h3 {
		font-size: 16px;
		font-weight: 600;
		color: var(--slate-900, #0f172a);
		margin: 4px 0 0 0;
	}

	.error-message {
		font-size: 14px;
		color: var(--slate-500, #64748b);
		margin: 0;
		max-width: 360px;
		line-height: 1.5;
	}

	.error-actions {
		display: flex;
		gap: 12px;
		margin-top: 8px;
	}

	/* Mobile */
	@media (max-width: 480px) {
		.progress-header {
			flex-direction: column;
			gap: 12px;
			align-items: stretch;
		}

		.file-info {
			justify-content: center;
		}

		.time-info {
			justify-content: center;
		}

		.trust-badges {
			flex-direction: column;
			align-items: stretch;
		}

		.trust-badge {
			justify-content: center;
		}

		.primary-actions {
			flex-direction: column;
		}
	}
</style>
