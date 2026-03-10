<script lang="ts">
	import { t } from 'svelte-i18n';
	import { slide } from 'svelte/transition';
	import { isValidAudioFile, formatFileSize } from '$lib/api/workflowApi';

	let {
		onFileSelected
	}: {
		onFileSelected?: (file: File) => void;
	} = $props();

	let isDragging = $state(false);
	let error: string | null = $state(null);
	let fileInput: HTMLInputElement;
	let activeTutorial: 'teams' | 'iphone' = $state('teams');
	let bestPracticesExpanded = $state(false);
	let helpExpanded = $state(false);

	const ACCEPTED_TYPES = '.mp3,.mp4,.m4a,.wav,.webm';
	const MAX_FILE_SIZE = 500 * 1024 * 1024; // 500MB

	function handleDragEnter(e: DragEvent) {
		e.preventDefault();
		isDragging = true;
	}

	function handleDragLeave(e: DragEvent) {
		e.preventDefault();
		isDragging = false;
	}

	function handleDragOver(e: DragEvent) {
		e.preventDefault();
	}

	function handleDrop(e: DragEvent) {
		e.preventDefault();
		isDragging = false;
		error = null;

		const files = e.dataTransfer?.files;
		if (files && files.length > 0) {
			validateAndSelect(files[0]);
		}
	}

	function handleFileInput(e: Event) {
		const input = e.target as HTMLInputElement;
		error = null;

		if (input.files && input.files.length > 0) {
			validateAndSelect(input.files[0]);
		}
	}

	function validateAndSelect(file: File) {
		// Check file type
		if (!isValidAudioFile(file)) {
			error = $t('workflow.meeting.upload.errorType');
			return;
		}

		// Check file size
		if (file.size > MAX_FILE_SIZE) {
			error = $t('workflow.meeting.upload.errorSize', { values: { maxSize: formatFileSize(MAX_FILE_SIZE) } });
			return;
		}

		onFileSelected?.(file);
	}

	function openFilePicker() {
		fileInput?.click();
	}
</script>

<div class="file-uploader">
	<!-- Trust Indicators -->
	<div class="trust-indicators">
		<div class="trust-item">
			<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
				<rect x="3" y="11" width="18" height="11" rx="2" ry="2" />
				<path d="M7 11V7a5 5 0 0 1 10 0v4" />
			</svg>
			<span>{$t('workflow.meeting.confirm.securityBadge')}</span>
		</div>
		<div class="trust-item">
			<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
				<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z" />
			</svg>
			<span>{$t('workflow.meeting.processing.trustBadge')}</span>
		</div>
	</div>

	<div
		class="drop-zone"
		class:dragging={isDragging}
		class:error={!!error}
		role="button"
		tabindex="0"
		on:dragenter={handleDragEnter}
		on:dragleave={handleDragLeave}
		on:dragover={handleDragOver}
		on:drop={handleDrop}
		on:click={openFilePicker}
		on:keypress={(e) => e.key === 'Enter' && openFilePicker()}
	>
		<input
			bind:this={fileInput}
			type="file"
			accept={ACCEPTED_TYPES}
			on:change={handleFileInput}
			hidden
		/>

		<div class="drop-icon">
			<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
				<path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4" />
				<polyline points="17 8 12 3 7 8" />
				<line x1="12" y1="3" x2="12" y2="15" />
			</svg>
		</div>

		<div class="drop-text">
			<span class="drop-primary">
				{#if isDragging}
					{$t('workflow.meeting.upload.dropHere')}
				{:else}
					{$t('workflow.meeting.upload.dropOrClick')}
				{/if}
			</span>
			<span class="drop-secondary">MP3, MP4, WAV, M4A (max. 500MB)</span>
		</div>
	</div>

	{#if error}
		<div class="error-message">
			<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
				<circle cx="12" cy="12" r="10" />
				<line x1="12" y1="8" x2="12" y2="12" />
				<line x1="12" y1="16" x2="12.01" y2="16" />
			</svg>
			<span>{error}</span>
		</div>
	{/if}

	<!-- FAQ Section -->
	<div class="faq-section">
		<!-- Best Practices -->
		<button
			class="help-trigger"
			class:expanded={bestPracticesExpanded}
			on:click={() => bestPracticesExpanded = !bestPracticesExpanded}
		>
			<svg class="help-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
				<path d="M12 2L2 7l10 5 10-5-10-5z" />
				<path d="M2 17l10 5 10-5" />
				<path d="M2 12l10 5 10-5" />
			</svg>
			<span>{$t('workflow.meeting.upload.bestPracticesTitle')}</span>
			<svg class="chevron" class:rotated={bestPracticesExpanded} viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
				<polyline points="6 9 12 15 18 9" />
			</svg>
		</button>

		{#if bestPracticesExpanded}
			<div class="help-content" transition:slide={{ duration: 200 }}>
				<div class="best-practices-grid">
					<div class="practice-item">
						<div class="practice-icon">
							<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
								<path d="M12 1a3 3 0 0 0-3 3v8a3 3 0 0 0 6 0V4a3 3 0 0 0-3-3z" />
								<path d="M19 10v2a7 7 0 0 1-14 0v-2" />
								<line x1="12" y1="19" x2="12" y2="23" />
								<line x1="8" y1="23" x2="16" y2="23" />
							</svg>
						</div>
						<div class="practice-text">
							<strong>{$t('workflow.meeting.upload.bestPractices.audio.title')}</strong>
							<span>{$t('workflow.meeting.upload.bestPractices.audio.description')}</span>
						</div>
					</div>
					<div class="practice-item">
						<div class="practice-icon">
							<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
								<path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2" />
								<circle cx="9" cy="7" r="4" />
								<path d="M23 21v-2a4 4 0 0 0-3-3.87" />
								<path d="M16 3.13a4 4 0 0 1 0 7.75" />
							</svg>
						</div>
						<div class="practice-text">
							<strong>{$t('workflow.meeting.upload.bestPractices.speakers.title')}</strong>
							<span>{$t('workflow.meeting.upload.bestPractices.speakers.description')}</span>
						</div>
					</div>
					<div class="practice-item">
						<div class="practice-icon">
							<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
								<circle cx="12" cy="12" r="10" />
								<polyline points="12 6 12 12 16 14" />
							</svg>
						</div>
						<div class="practice-text">
							<strong>{$t('workflow.meeting.upload.bestPractices.duration.title')}</strong>
							<span>{$t('workflow.meeting.upload.bestPractices.duration.description')}</span>
						</div>
					</div>
					<div class="practice-item">
						<div class="practice-icon">
							<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
								<polygon points="23 7 16 12 23 17 23 7" />
								<rect x="1" y="5" width="15" height="14" rx="2" ry="2" />
							</svg>
						</div>
						<div class="practice-text">
							<strong>{$t('workflow.meeting.upload.bestPractices.recording.title')}</strong>
							<span>{$t('workflow.meeting.upload.bestPractices.recording.description')}</span>
						</div>
					</div>
				</div>
			</div>
		{/if}

		<!-- Where to find recordings -->
		<button
			class="help-trigger"
			class:expanded={helpExpanded}
			on:click={() => helpExpanded = !helpExpanded}
		>
			<svg class="help-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
				<circle cx="12" cy="12" r="10" />
				<path d="M9.09 9a3 3 0 0 1 5.83 1c0 2-3 3-3 3" />
				<line x1="12" y1="17" x2="12.01" y2="17" />
			</svg>
			<span>{$t('workflow.meeting.upload.tutorialTitle')}</span>
			<svg class="chevron" class:rotated={helpExpanded} viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
				<polyline points="6 9 12 15 18 9" />
			</svg>
		</button>

	{#if helpExpanded}
		<div class="help-content" transition:slide={{ duration: 200 }}>
			<div class="tutorial-tabs">
				<button
					class="tutorial-tab"
					class:active={activeTutorial === 'teams'}
					on:click={() => activeTutorial = 'teams'}
				>
					<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
						<path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2" />
						<circle cx="9" cy="7" r="4" />
						<path d="M23 21v-2a4 4 0 0 0-3-3.87" />
						<path d="M16 3.13a4 4 0 0 1 0 7.75" />
					</svg>
					Microsoft Teams
				</button>
				<button
					class="tutorial-tab"
					class:active={activeTutorial === 'iphone'}
					on:click={() => activeTutorial = 'iphone'}
				>
					<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
						<rect x="5" y="2" width="14" height="20" rx="2" ry="2" />
						<line x1="12" y1="18" x2="12.01" y2="18" />
					</svg>
					iPhone
				</button>
			</div>

			<div class="tutorial-content">
				{#if activeTutorial === 'teams'}
					<div class="tutorial-steps">
						<div class="tutorial-step">
							<span class="step-number">1</span>
							<span class="step-text">{@html $t('workflow.meeting.upload.tutorial.teams.step1')}</span>
						</div>
						<div class="tutorial-step">
							<span class="step-number">2</span>
							<span class="step-text">{@html $t('workflow.meeting.upload.tutorial.teams.step2')}</span>
						</div>
						<div class="tutorial-step">
							<span class="step-number">3</span>
							<span class="step-text">{@html $t('workflow.meeting.upload.tutorial.teams.step3')}</span>
						</div>
						<div class="tutorial-step">
							<span class="step-number">4</span>
							<span class="step-text">{@html $t('workflow.meeting.upload.tutorial.teams.step4')}</span>
						</div>
					</div>
				{:else}
					<div class="tutorial-steps">
						<div class="tutorial-step">
							<span class="step-number">1</span>
							<span class="step-text">{@html $t('workflow.meeting.upload.tutorial.iphone.step1')}</span>
						</div>
						<div class="tutorial-step">
							<span class="step-number">2</span>
							<span class="step-text">{@html $t('workflow.meeting.upload.tutorial.iphone.step2')}</span>
						</div>
						<div class="tutorial-step">
							<span class="step-number">3</span>
							<span class="step-text">{@html $t('workflow.meeting.upload.tutorial.iphone.step3')}</span>
						</div>
						<div class="tutorial-step">
							<span class="step-number">4</span>
							<span class="step-text">{@html $t('workflow.meeting.upload.tutorial.iphone.step4')}</span>
						</div>
					</div>
				{/if}
			</div>
		</div>
	{/if}
	</div>
</div>

<style>
	.file-uploader {
		display: flex;
		flex-direction: column;
		align-items: center;
		width: 100%;
		max-width: 800px;
	}

	.drop-zone {
		width: 100%;
		padding: 48px 32px;
		border: 2px dashed var(--slate-300, #cbd5e1);
		border-radius: 12px;
		background: white;
		display: flex;
		flex-direction: column;
		align-items: center;
		gap: 16px;
		cursor: pointer;
		transition: all 0.15s ease;
	}

	.drop-zone:hover {
		border-color: var(--blue-400, #60a5fa);
		background: var(--blue-50, #eff6ff);
	}

	.drop-zone.dragging {
		border-color: var(--blue-500, #3b82f6);
		background: var(--blue-50, #eff6ff);
		transform: scale(1.01);
	}

	.drop-zone.error {
		border-color: var(--red-400, #f87171);
		background: var(--red-50, #fef2f2);
	}

	.drop-zone:focus {
		outline: none;
		border-color: var(--blue-500, #3b82f6);
		box-shadow: 0 0 0 3px var(--blue-100, #dbeafe);
	}

	.drop-icon {
		width: 48px;
		height: 48px;
		display: flex;
		align-items: center;
		justify-content: center;
	}

	.drop-icon svg {
		width: 32px;
		height: 32px;
		color: var(--slate-400, #94a3b8);
		transition: color 0.15s ease;
	}

	.drop-zone:hover .drop-icon svg,
	.drop-zone.dragging .drop-icon svg {
		color: var(--blue-500, #3b82f6);
	}

	.drop-text {
		display: flex;
		flex-direction: column;
		align-items: center;
		gap: 4px;
	}

	.drop-primary {
		font-size: 15px;
		font-weight: 600;
		color: var(--slate-900, #0f172a);
	}

	.drop-secondary {
		font-size: 13px;
		color: var(--slate-500, #64748b);
	}

	.error-message {
		display: flex;
		align-items: center;
		gap: 8px;
		margin-top: 16px;
		padding: 12px 16px;
		background: var(--red-50, #fef2f2);
		border: 1px solid var(--red-200, #fecaca);
		border-radius: 8px;
		color: var(--red-700, #b91c1c);
		font-size: 14px;
		width: 100%;
	}

	.error-message svg {
		width: 18px;
		height: 18px;
		flex-shrink: 0;
	}

	/* Trust Indicators */
	.trust-indicators {
		display: flex;
		justify-content: center;
		gap: 12px;
		margin-bottom: 16px;
		width: 100%;
	}

	.trust-item {
		display: flex;
		align-items: center;
		gap: 8px;
		padding: 8px 14px;
		background: var(--green-50, #f0fdf4);
		border: 1px solid var(--green-200, #bbf7d0);
		border-radius: 8px;
		font-size: 13px;
		font-weight: 500;
		color: var(--green-700, #15803d);
	}

	.trust-item svg {
		width: 16px;
		height: 16px;
		color: var(--green-600, #16a34a);
	}

	/* FAQ Section */
	.faq-section {
		width: 100%;
		margin-top: 24px;
		display: flex;
		flex-direction: column;
		gap: 8px;
	}

	/* Best Practices Grid */
	.best-practices-grid {
		display: grid;
		grid-template-columns: repeat(2, 1fr);
		gap: 12px;
	}

	.practice-item {
		display: flex;
		align-items: flex-start;
		gap: 12px;
		padding: 14px;
		background: white;
		border: 1px solid var(--slate-200, #e2e8f0);
		border-radius: 8px;
	}

	.practice-icon {
		width: 36px;
		height: 36px;
		background: var(--blue-50, #eff6ff);
		border-radius: 8px;
		display: flex;
		align-items: center;
		justify-content: center;
		flex-shrink: 0;
	}

	.practice-icon svg {
		width: 18px;
		height: 18px;
		color: var(--blue-600, #2563eb);
	}

	.practice-text {
		display: flex;
		flex-direction: column;
		gap: 2px;
	}

	.practice-text strong {
		font-size: 13px;
		font-weight: 600;
		color: var(--slate-900, #0f172a);
	}

	.practice-text span {
		font-size: 12px;
		color: var(--slate-500, #64748b);
		line-height: 1.4;
	}

	/* Collapsible Help Trigger */
	.help-trigger {
		display: flex;
		align-items: center;
		gap: 8px;
		width: 100%;
		padding: 12px 16px;
		background: var(--slate-50, #f8fafc);
		border: 1px solid var(--slate-200, #e2e8f0);
		border-radius: 8px;
		font-size: 14px;
		color: var(--slate-600, #475569);
		cursor: pointer;
		transition: all 0.15s ease;
		margin-top: 0;
	}

	.help-trigger:hover {
		background: var(--slate-100, #f1f5f9);
		border-color: var(--slate-300, #cbd5e1);
	}

	.help-trigger.expanded {
		border-bottom-left-radius: 0;
		border-bottom-right-radius: 0;
		border-bottom-color: transparent;
	}

	.help-icon {
		width: 18px;
		height: 18px;
		color: var(--slate-400, #94a3b8);
	}

	.help-trigger span {
		flex: 1;
		text-align: left;
		font-weight: 500;
	}

	.chevron {
		width: 16px;
		height: 16px;
		color: var(--slate-400, #94a3b8);
		transition: transform 0.2s ease;
	}

	.chevron.rotated {
		transform: rotate(180deg);
	}

	/* Help Content */
	.help-content {
		padding: 16px;
		background: var(--slate-50, #f8fafc);
		border: 1px solid var(--slate-200, #e2e8f0);
		border-top: none;
		border-radius: 0 0 8px 8px;
	}

	.tutorial-tabs {
		display: flex;
		gap: 8px;
		margin-bottom: 16px;
	}

	.tutorial-tab {
		display: flex;
		align-items: center;
		gap: 8px;
		padding: 10px 16px;
		background: white;
		border: 1px solid var(--slate-200, #e2e8f0);
		border-radius: 8px;
		font-size: 14px;
		font-weight: 500;
		color: var(--slate-600, #475569);
		cursor: pointer;
		transition: all 0.15s ease;
	}

	.tutorial-tab:hover {
		border-color: var(--slate-300, #cbd5e1);
		background: white;
	}

	.tutorial-tab.active {
		background: var(--deep-blue, #1E3A5F);
		border-color: var(--deep-blue, #1E3A5F);
		color: white;
	}

	.tutorial-tab svg {
		width: 18px;
		height: 18px;
	}

	.tutorial-content {
		background: white;
		border: 1px solid var(--slate-200, #e2e8f0);
		border-radius: 8px;
		padding: 16px 20px;
	}

	.tutorial-steps {
		display: flex;
		flex-direction: column;
		gap: 12px;
	}

	.tutorial-step {
		display: flex;
		align-items: flex-start;
		gap: 12px;
	}

	.step-number {
		width: 24px;
		height: 24px;
		background: var(--blue-100, #dbeafe);
		color: var(--blue-700, #1d4ed8);
		border-radius: 50%;
		display: flex;
		align-items: center;
		justify-content: center;
		font-size: 12px;
		font-weight: 600;
		flex-shrink: 0;
	}

	.step-text {
		font-size: 14px;
		color: var(--slate-700, #334155);
		line-height: 1.5;
		padding-top: 2px;
	}

	.step-text :global(strong) {
		font-weight: 600;
		color: var(--slate-900, #0f172a);
	}

	.step-text :global(code) {
		font-family: 'SF Mono', 'Monaco', 'Inconsolata', 'Roboto Mono', monospace;
		font-size: 13px;
		background: var(--slate-200, #e2e8f0);
		padding: 2px 6px;
		border-radius: 4px;
		color: var(--slate-700, #334155);
	}

	@media (max-width: 600px) {
		.best-practices-grid {
			grid-template-columns: 1fr;
		}
	}

	@media (max-width: 480px) {
		.drop-zone {
			padding: 32px 24px;
		}

		.trust-indicators {
			flex-direction: column;
			align-items: stretch;
		}

		.trust-item {
			justify-content: center;
		}

		.tutorial-tabs {
			flex-direction: column;
		}

		.tutorial-tab {
			justify-content: center;
		}
	}
</style>
