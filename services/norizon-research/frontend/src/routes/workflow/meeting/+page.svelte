<script lang="ts">
	import { onMount } from 'svelte';
	import { goto } from '$app/navigation';
	import { WorkflowAPI } from '$lib/api/workflowApi';
	import { workflowStore } from '$lib/stores/workflowStore';
	import { t } from 'svelte-i18n';

	let error: string | null = null;
	let isCreating = true;

	onMount(async () => {
		try {
			// Create a new workflow job
			const response = await WorkflowAPI.createJob();

			// Initialize the workflow state
			workflowStore.initJob(response.job_id);

			// Redirect to the job-specific route
			await goto(`/workflow/meeting/${response.job_id}`, { replaceState: true });
		} catch (e) {
			console.error('Failed to create workflow job:', e);
			error = e instanceof Error ? e.message : 'Failed to create workflow';
			isCreating = false;
		}
	});
</script>

<svelte:head>
	<title>{$t('workflow.meeting.title')} - Nora</title>
</svelte:head>

<div class="loading-container">
	{#if error}
		<div class="error-state">
			<div class="error-icon">
				<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
					<circle cx="12" cy="12" r="10" />
					<line x1="12" y1="8" x2="12" y2="12" />
					<line x1="12" y1="16" x2="12.01" y2="16" />
				</svg>
			</div>
			<h2>{$t('workflow.meeting.error.title')}</h2>
			<p>{error}</p>
			<button class="btn-primary" on:click={() => goto('/chat')}>
				{$t('workflow.meeting.error.backToChat')}
			</button>
		</div>
	{:else}
		<div class="spinner-container">
			<div class="spinner"></div>
			<p>{$t('workflow.meeting.creating')}</p>
		</div>
	{/if}
</div>

<style>
	.loading-container {
		display: flex;
		align-items: center;
		justify-content: center;
		min-height: 100vh;
		background: var(--slate-50, #f8fafc);
	}

	.spinner-container {
		display: flex;
		flex-direction: column;
		align-items: center;
		gap: 16px;
	}

	.spinner {
		width: 48px;
		height: 48px;
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

	.spinner-container p {
		font-size: 15px;
		color: var(--slate-600, #475569);
	}

	.error-state {
		display: flex;
		flex-direction: column;
		align-items: center;
		text-align: center;
		padding: 40px;
		background: white;
		border-radius: 12px;
		box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
		max-width: 400px;
	}

	.error-icon {
		width: 64px;
		height: 64px;
		background: var(--red-100, #fee2e2);
		border-radius: 50%;
		display: flex;
		align-items: center;
		justify-content: center;
		margin-bottom: 16px;
	}

	.error-icon svg {
		width: 32px;
		height: 32px;
		color: var(--red-500, #ef4444);
	}

	.error-state h2 {
		font-size: 18px;
		font-weight: 600;
		color: var(--slate-900, #0f172a);
		margin-bottom: 8px;
	}

	.error-state p {
		font-size: 14px;
		color: var(--slate-600, #475569);
		margin-bottom: 20px;
	}

	.btn-primary {
		padding: 10px 20px;
		background: var(--blue-500, #3b82f6);
		color: white;
		border: none;
		border-radius: 8px;
		font-size: 14px;
		font-weight: 500;
		cursor: pointer;
		transition: background 0.15s ease;
	}

	.btn-primary:hover {
		background: var(--blue-600, #2563eb);
	}
</style>
