<script lang="ts">
	import { t } from "svelte-i18n";

	export let currentStep = 1;

	// 3-stage display mapping from internal 9 steps
	// Upload: upload/configure/processing
	// Review: speaker verification, protocol editing
	// Done: export confirmation, success screen
	const displaySteps = [
		{
			id: 1,
			labelKey: "workflow.meeting.steps.upload",
			internalSteps: [1, 2, 3, 4, 5],
		},
		{
			id: 2,
			labelKey: "workflow.meeting.steps.review",
			internalSteps: [6, 7],
		},
		{
			id: 3,
			labelKey: "workflow.meeting.steps.done",
			internalSteps: [8, 9],
		},
	];

	function getDisplayStep(internalStep: number): number {
		for (const step of displaySteps) {
			if (step.internalSteps.includes(internalStep)) {
				return step.id;
			}
		}
		return 1;
	}

	function getStepStatus(
		stepId: number,
		currentDisplayStep: number,
	): "completed" | "current" | "pending" {
		if (stepId < currentDisplayStep) return "completed";
		if (stepId === currentDisplayStep) return "current";
		return "pending";
	}

	$: currentDisplayStep = getDisplayStep(currentStep);
</script>

<div class="step-indicator">
	{#each displaySteps as step, i}
		{@const status = getStepStatus(step.id, currentDisplayStep)}
		<div class="step {status}">
			<div class="step-marker">
				{#if status === "completed"}
					<svg
						viewBox="0 0 24 24"
						fill="none"
						stroke="currentColor"
						stroke-width="3"
					>
						<polyline points="20 6 9 17 4 12" />
					</svg>
				{:else}
					<span class="step-number">{step.id}</span>
				{/if}
			</div>
			<span class="step-label">{$t(step.labelKey)}</span>
		</div>
		{#if i < displaySteps.length - 1}
			<div
				class="step-connector"
				class:completed={step.id < currentDisplayStep}
			></div>
		{/if}
	{/each}
</div>

<style>
	.step-indicator {
		display: flex;
		align-items: center;
		gap: 0;
	}

	.step {
		display: flex;
		align-items: center;
		gap: 6px;
	}

	.step-marker {
		width: 22px;
		height: 22px;
		border-radius: 50%;
		display: flex;
		align-items: center;
		justify-content: center;
		font-size: 11px;
		font-weight: 600;
		flex-shrink: 0;
		transition: all 0.2s ease;
	}

	.step.pending .step-marker {
		background: var(--slate-100, #f1f5f9);
		color: var(--slate-400, #94a3b8);
		border: 1px solid var(--slate-200, #e2e8f0);
	}

	.step.current .step-marker {
		background: var(--blue-500, #3b82f6);
		color: white;
		border: 1px solid var(--blue-500, #3b82f6);
	}

	.step.completed .step-marker {
		background: var(--slate-100, #f1f5f9);
		color: var(--green-600, #16a34a);
		border: 1px solid var(--slate-200, #e2e8f0);
	}

	.step.completed .step-marker svg {
		width: 12px;
		height: 12px;
	}

	.step-number {
		line-height: 1;
	}

	.step-label {
		font-size: 12px;
		font-weight: 500;
		white-space: nowrap;
		transition: all 0.2s ease;
	}

	.step.pending .step-label {
		color: var(--slate-400, #94a3b8);
	}

	.step.current .step-label {
		color: var(--slate-900, #0f172a);
		font-weight: 600;
	}

	.step.completed .step-label {
		color: var(--slate-500, #64748b);
	}

	.step-connector {
		width: 24px;
		height: 2px;
		background: var(--slate-200, #e2e8f0);
		margin: 0 4px;
		transition: background 0.2s ease;
	}

	.step-connector.completed {
		background: var(--slate-300, #cbd5e1);
	}

	/* Responsive: hide labels on small screens */
	@media (max-width: 640px) {
		.step-label {
			display: none;
		}

		.step-connector {
			width: 16px;
		}
	}
</style>
