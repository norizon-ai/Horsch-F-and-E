<script lang="ts">
	import { onMount } from "svelte";
	import { t } from "svelte-i18n";
	import { workflowStore } from "$lib/stores/workflowStore";
	import { WorkflowAPI } from "$lib/api/workflowApi";
	import type {
		Protocol,
		MeetingTemplate,
		TemplateSuggestion,
	} from "$lib/types";

	let {
		protocol = $bindable(null),
		jobId = "",
		onSaveAndContinue = undefined,
		onBack = undefined,
		onRegenerating = undefined,
	}: {
		protocol?: Protocol | null;
		jobId?: string;
		onSaveAndContinue?: (() => void) | undefined;
		onBack?: (() => void) | undefined;
		onRegenerating?: ((value: boolean) => void) | undefined;
	} = $props();

	// Template state
	let templates: MeetingTemplate[] = $state([]);
	let suggestion: TemplateSuggestion | null = $state(null);
	let selectedTemplateId: string = $state("");
	let isLoadingTemplates = $state(true);

	// Saving state
	let isSaving = $state(false);

	// Regeneration state (when switching templates)
	let isRegenerating = $state(false);

	// BUG 2 FIX: Back button confirmation dialog
	let showBackConfirmDialog = $state(false);

	// Initialize selected template when protocol prop changes
	$effect(() => {
		if (protocol) {
			selectedTemplateId = protocol.templateId || "";
		}
	});

	// Load templates on mount
	onMount(async () => {
		try {
			const response = await WorkflowAPI.getTemplates(jobId);
			templates = response.templates;
			suggestion = response.suggestion || null;

			// Auto-select suggested template if no template is selected
			if (!selectedTemplateId && suggestion) {
				selectedTemplateId = suggestion.templateId;
				applyTemplate(suggestion.templateId);
			}
		} catch (error) {
			console.error("Failed to load templates:", error);
		} finally {
			isLoadingTemplates = false;
		}
	});

	// BUG 6 FIX: Get template icon SVG with unique icons mapped from template ID
	function getTemplateIcon(template: MeetingTemplate): string {
		// Map template IDs to specific unique icon keys
		const templateIconMap: Record<string, string> = {
			CLIENT_UPDATE: "briefcase",
			CLIENT_TECHNICAL: "wrench",
			PROSPECT_SALES: "target",
			PARTNER: "handshake",
			COACH_MENTOR: "award",
			NETWORKING: "user-plus",
			TEAM_SYNC: "git-merge",
			TEAM_DESIGN: "layers",
		};

		const icons: Record<string, string> = {
			// Client Meeting (regular) - briefcase
			briefcase:
				'<path d="M16 8V4a2 2 0 00-2-2H10a2 2 0 00-2 2v4m-4 0h16a2 2 0 012 2v8a2 2 0 01-2 2H4a2 2 0 01-2-2v-8a2 2 0 012-2z"/>',
			// Client Meeting (technical) - wrench/settings
			wrench: '<path d="M14.7 6.3a1 1 0 000 1.4l1.6 1.6a1 1 0 001.4 0l3.77-3.77a6 6 0 01-7.94 7.94l-6.91 6.91a2.12 2.12 0 01-3-3l6.91-6.91a6 6 0 017.94-7.94l-3.76 3.76z"/>',
			// Prospect Meeting - target
			target: '<circle cx="12" cy="12" r="10"/><circle cx="12" cy="12" r="6"/><circle cx="12" cy="12" r="2"/>',
			// Partner Discussion - shield-check
			handshake:
				'<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/><path d="M9 12l2 2 4-4"/>',
			// Coach/Mentor Session - award
			award: '<circle cx="12" cy="8" r="7"/><polyline points="8.21 13.89 7 23 12 20 17 23 15.79 13.88"/>',
			// Networking - users-plus
			"user-plus":
				'<path d="M16 21v-2a4 4 0 00-4-4H5a4 4 0 00-4 4v2"/><circle cx="8.5" cy="7" r="4"/><line x1="20" y1="8" x2="20" y2="14"/><line x1="23" y1="11" x2="17" y2="11"/>',
			// Team Sync - git-merge
			"git-merge":
				'<circle cx="18" cy="18" r="3"/><circle cx="6" cy="6" r="3"/><path d="M6 21V9a9 9 0 009 9"/>',
			// Team Design Session - layers
			layers: '<polygon points="12 2 2 7 12 12 22 7 12 2"/><polyline points="2 17 12 22 22 17"/><polyline points="2 12 12 17 22 12"/>',
			// Fallback
			"file-text":
				'<path d="M14 2H6a2 2 0 00-2 2v16a2 2 0 002 2h12a2 2 0 002-2V8z"/><polyline points="14 2 14 8 20 8"/><line x1="16" y1="13" x2="8" y2="13"/><line x1="16" y1="17" x2="8" y2="17"/>',
		};

		// Use template ID mapping first, then fall back to icon field, then default
		const iconKey =
			templateIconMap[template.id] || template.icon || "file-text";
		return icons[iconKey] || icons["file-text"];
	}

	// Task 20: Simplified template descriptions - 3-4 bullet points, most distinguishing sections
	function getTemplateExtractionDesc(templateId: string): string {
		const extractions: Record<string, string> = {
			CLIENT_UPDATE: "Status updates • Decisions • Client sentiment",
			CLIENT_TECHNICAL:
				"Technical requirements • System landscape • Constraints",
			PROSPECT_SALES: "Pain points • Interest level • Objections",
			PARTNER: "Potential value • Decisions • Concerns",
			COACH_MENTOR: "Feedback received • Recommendations",
			NETWORKING: "Background • Mutual opportunities",
			TEAM_SYNC: "Updates by person • Blockers",
			TEAM_DESIGN: "User flow • Design decisions • Edge cases",
		};
		return extractions[templateId] || "Action items • Key insights";
	}

	// Apply template to protocol - regenerate from backend
	async function applyTemplate(templateId: string) {
		if (!protocol) return;

		// Don't reload if same template
		if (templateId === selectedTemplateId) return;

		selectedTemplateId = templateId;
		isRegenerating = true;
		onRegenerating?.(true);

		try {
			// Call backend to regenerate protocol with template-specific content
			const response = await WorkflowAPI.generateProtocol(
				jobId,
				templateId,
			);
			protocol = response.protocol;
			workflowStore.setProtocol(protocol);
		} catch (error) {
			console.error("Failed to regenerate protocol:", error);
			// Fallback: just set templateId without regenerating
			protocol.templateId = templateId;
			workflowStore.setProtocol(protocol);
		} finally {
			isRegenerating = false;
			onRegenerating?.(false);
		}
	}

	// Save and continue to export step
	async function handleSaveAndContinue() {
		if (!protocol) return;

		isSaving = true;
		try {
			workflowStore.setProtocolSaved(true);
			await new Promise((resolve) => setTimeout(resolve, 300));
			onSaveAndContinue?.();
		} finally {
			isSaving = false;
		}
	}

	// BUG 2 FIX: Back button handlers
	function handleBackClick() {
		showBackConfirmDialog = true;
	}

	function confirmBackAction() {
		showBackConfirmDialog = false;
		onBack?.();
	}

	function cancelBackAction() {
		showBackConfirmDialog = false;
	}

	// Get selected template
	let selectedTemplate = $derived(templates.find((t) => t.id === selectedTemplateId));
</script>

<div class="template-review">
	{#if protocol}
		<!-- Instruction text -->
		<div class="instruction-box">
			<svg
				viewBox="0 0 24 24"
				fill="none"
				stroke="currentColor"
				stroke-width="2"
			>
				<path
					d="M11 4H4a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2v-7"
				/>
				<path
					d="M18.5 2.5a2.121 2.121 0 0 1 3 3L12 15l-4 1 1-4 9.5-9.5z"
				/>
			</svg>
			<p>
				Edit your meeting protocol in the side panel. You can modify the
				title, attendees, summary, and action items.
			</p>
		</div>

		<!-- Template Selector -->
		<div class="template-section">
			<div class="template-header">
				<label>{$t("workflow.meeting.protocol.template")}</label>
			</div>

			{#if isLoadingTemplates}
				<div class="template-loading">
					<div class="spinner-small"></div>
					<span>{$t("common.loading")}</span>
				</div>
			{:else}
				<!-- Template cards without overlay - overlay moved to editor panel -->
				<div class="template-cards-wrapper">
					<div
						class="template-cards"
						class:is-regenerating={isRegenerating}
					>
						{#each templates as template}
							<button
								class="template-card"
								class:selected={selectedTemplateId ===
									template.id}
								class:recommended={suggestion?.templateId ===
									template.id &&
									selectedTemplateId !== template.id}
								onclick={() => applyTemplate(template.id)}
								disabled={isRegenerating}
							>
								{#if selectedTemplateId === template.id && isRegenerating}
									<div class="regenerating-indicator">
										<div class="spinner-small"></div>
									</div>
								{:else if selectedTemplateId === template.id}
									<div class="selected-check">
										<svg
											viewBox="0 0 24 24"
											fill="none"
											stroke="currentColor"
											stroke-width="3"
										>
											<polyline points="20 6 9 17 4 12" />
										</svg>
									</div>
								{/if}
								<div class="template-card-icon">
									<svg
										viewBox="0 0 24 24"
										fill="none"
										stroke="currentColor"
										stroke-width="2"
									>
										{@html getTemplateIcon(template)}
									</svg>
								</div>
								<span class="template-card-name"
									>{template.name}</span
								>
								<span class="template-card-desc"
									>{getTemplateExtractionDesc(
										template.id,
									)}</span
								>
								{#if suggestion?.templateId === template.id}
									<span class="template-card-rec"
										>{$t(
											"workflow.meeting.protocol.recommended",
										)}</span
									>
								{/if}
							</button>
						{/each}
					</div>
				</div>
			{/if}

			{#if suggestion && selectedTemplateId === suggestion.templateId}
				<p class="suggestion-reason">{suggestion.reason}</p>
			{/if}
		</div>
	{:else}
		<div class="loading-protocol">
			<div class="spinner"></div>
			<p>{$t("workflow.meeting.protocol.generating")}</p>
		</div>
	{/if}

	<div class="workflow-footer">
		<button class="btn-secondary" onclick={handleBackClick}>
			<svg
				viewBox="0 0 24 24"
				fill="none"
				stroke="currentColor"
				stroke-width="2"
			>
				<line x1="19" y1="12" x2="5" y2="12" />
				<polyline points="12 19 5 12 12 5" />
			</svg>
			{$t("common.back")}
		</button>
		<button
			class="btn-primary"
			onclick={handleSaveAndContinue}
			disabled={isSaving}
		>
			{#if isSaving}
				<div class="spinner-btn"></div>
				{$t("common.saving")}
			{:else}
				{$t("workflow.meeting.protocol.saveAndContinue")}
				<svg
					viewBox="0 0 24 24"
					fill="none"
					stroke="currentColor"
					stroke-width="2"
				>
					<line x1="5" y1="12" x2="19" y2="12" />
					<polyline points="12 5 19 12 12 19" />
				</svg>
			{/if}
		</button>
	</div>
</div>

<!-- BUG 2 FIX: Back confirmation dialog -->
{#if showBackConfirmDialog}
	<div class="confirm-overlay" role="dialog" aria-modal="true">
		<div class="confirm-dialog">
			<h3 class="confirm-title">Go back?</h3>
			<p class="confirm-desc">Your protocol changes will be saved, but you will return to speaker verification.</p>
			<div class="confirm-actions">
				<button class="confirm-btn confirm-cancel" onclick={cancelBackAction}>
					Cancel
				</button>
				<button class="confirm-btn confirm-danger" onclick={confirmBackAction}>
					Go back
				</button>
			</div>
		</div>
	</div>
{/if}

<style>
	.template-review {
		width: 100%;
		max-width: 800px;
		position: relative;
	}

	.template-cards-wrapper {
		position: relative;
	}

	/* Template Cards Grid */
	.template-cards {
		display: grid;
		grid-template-columns: repeat(auto-fill, minmax(160px, 1fr));
		gap: 12px;
		margin-bottom: 16px;
	}

	.template-card {
		display: flex;
		flex-direction: column;
		align-items: center;
		gap: 8px;
		padding: 16px 12px;
		background: white;
		border: 1px solid var(--slate-200, #e2e8f0);
		border-radius: 10px;
		cursor: pointer;
		transition: all 0.15s ease;
		text-align: center;
	}

	.template-card:hover {
		border-color: var(--blue-400, #60a5fa);
		background: var(--blue-50, #eff6ff);
	}

	.template-card.recommended {
		border-color: var(--amber-300, #fcd34d);
		background: var(--amber-50, #fffbeb);
	}

	.template-card.recommended:hover {
		border-color: var(--amber-400, #fbbf24);
		background: var(--amber-100, #fef3c7);
	}

	.template-card.selected {
		border-color: var(--blue-500, #3b82f6);
		background: var(--blue-50, #eff6ff);
		position: relative;
	}

	.template-card.selected:hover {
		border-color: var(--blue-600, #2563eb);
		background: var(--blue-100, #dbeafe);
	}

	.template-card.selected .template-card-icon {
		background: var(--blue-100, #dbeafe);
	}

	.template-card.selected .template-card-icon svg {
		color: var(--blue-600, #2563eb);
	}

	.selected-check,
	.regenerating-indicator {
		position: absolute;
		top: 8px;
		right: 8px;
		width: 20px;
		height: 20px;
		background: var(--blue-500, #3b82f6);
		border-radius: 50%;
		display: flex;
		align-items: center;
		justify-content: center;
	}

	.selected-check svg {
		width: 12px;
		height: 12px;
		color: white;
	}

	.regenerating-indicator .spinner-small {
		width: 12px;
		height: 12px;
		border-width: 2px;
		border-color: rgba(255, 255, 255, 0.3);
		border-top-color: white;
	}

	.template-cards.is-regenerating .template-card:not(.selected) {
		opacity: 0.5;
		pointer-events: none;
	}

	.template-card:disabled {
		cursor: wait;
	}

	.template-card-icon {
		width: 40px;
		height: 40px;
		display: flex;
		align-items: center;
		justify-content: center;
		background: var(--slate-100, #f1f5f9);
		border-radius: 10px;
	}

	.template-card:hover .template-card-icon {
		background: var(--blue-100, #dbeafe);
	}

	.template-card.recommended .template-card-icon {
		background: var(--amber-100, #fef3c7);
	}

	.template-card-icon svg {
		width: 22px;
		height: 22px;
		color: var(--slate-500, #64748b);
	}

	.template-card:hover .template-card-icon svg {
		color: var(--blue-600, #2563eb);
	}

	.template-card.recommended .template-card-icon svg {
		color: var(--amber-600, #d97706);
	}

	.template-card-name {
		font-size: 15px;
		font-weight: 600;
		color: var(--slate-900, #0f172a);
	}

	.template-card-desc {
		font-size: 13px;
		color: var(--slate-500, #64748b);
		line-height: 1.4;
	}

	.template-card-rec {
		font-size: 10px;
		font-weight: 600;
		text-transform: uppercase;
		color: var(--amber-700, #b45309);
		background: var(--amber-100, #fef3c7);
		padding: 2px 6px;
		border-radius: 4px;
	}

	/* Template Selector */
	.template-section {
		margin-bottom: 24px;
	}

	.template-header {
		display: flex;
		align-items: center;
		gap: 12px;
		margin-bottom: 8px;
	}

	.template-header label {
		font-size: 12px;
		font-weight: 600;
		color: var(--slate-500, #64748b);
		text-transform: uppercase;
		letter-spacing: 0.5px;
	}

	.suggestion-reason {
		font-size: 13px;
		color: var(--slate-500, #64748b);
		margin-top: 8px;
		font-style: italic;
	}

	.template-loading {
		display: flex;
		align-items: center;
		gap: 10px;
		padding: 20px;
		color: var(--slate-500, #64748b);
		font-size: 14px;
	}

	.spinner-small {
		width: 16px;
		height: 16px;
		border: 2px solid var(--slate-200, #e2e8f0);
		border-top-color: var(--blue-500, #3b82f6);
		border-radius: 50%;
		animation: spin 0.8s linear infinite;
	}

	@keyframes spin {
		from {
			transform: rotate(0deg);
		}
		to {
			transform: rotate(360deg);
		}
	}

	/* Instruction box */
	.instruction-box {
		display: flex;
		align-items: flex-start;
		gap: 12px;
		padding: 16px 20px;
		background: var(--blue-50, #eff6ff);
		border: 1px solid var(--blue-100, #dbeafe);
		border-radius: 10px;
		margin-bottom: 24px;
	}

	.instruction-box svg {
		width: 20px;
		height: 20px;
		color: var(--blue-500, #3b82f6);
		flex-shrink: 0;
		margin-top: 1px;
	}

	.instruction-box p {
		margin: 0;
		font-size: 16px;
		color: var(--blue-800, #1e40af);
		line-height: 1.5;
	}

	/* Loading state */
	.loading-protocol {
		display: flex;
		flex-direction: column;
		align-items: center;
		justify-content: center;
		padding: 60px;
		background: white;
		border: 1px solid var(--slate-200, #e2e8f0);
		border-radius: 12px;
		margin-bottom: 24px;
	}

	.spinner {
		width: 40px;
		height: 40px;
		border: 3px solid var(--slate-200, #e2e8f0);
		border-top-color: var(--blue-500, #3b82f6);
		border-radius: 50%;
		animation: spin 1s linear infinite;
		margin-bottom: 16px;
	}

	@keyframes spin {
		to {
			transform: rotate(360deg);
		}
	}

	.loading-protocol p {
		font-size: 15px;
		color: var(--slate-600, #475569);
	}

	/* Workflow Footer */
	.workflow-footer {
		display: flex;
		justify-content: space-between;
		align-items: center;
		gap: 12px;
	}

	.btn-primary,
	.btn-secondary {
		display: flex;
		align-items: center;
		justify-content: center;
		gap: 8px;
		padding: 12px 24px;
		font-size: 16px;
		font-weight: 500;
		border-radius: 8px;
		cursor: pointer;
		transition: all 0.15s ease;
	}

	.btn-primary {
		background: var(--blue-500, #3b82f6);
		color: white;
		border: none;
	}

	.btn-primary:hover:not(:disabled) {
		background: var(--blue-600, #2563eb);
	}

	.btn-primary:disabled {
		opacity: 0.7;
		cursor: not-allowed;
	}

	.btn-primary svg,
	.btn-secondary svg {
		width: 16px;
		height: 16px;
	}

	.btn-secondary {
		background: white;
		color: var(--slate-700, #334155);
		border: 1px solid var(--slate-300, #cbd5e1);
	}

	.btn-secondary:hover {
		background: var(--slate-50, #f8fafc);
	}

	.spinner-btn {
		width: 18px;
		height: 18px;
		border: 2px solid rgba(255, 255, 255, 0.3);
		border-top-color: white;
		border-radius: 50%;
		animation: spin 0.8s linear infinite;
	}

	/* Back confirmation dialog */
	.confirm-overlay {
		position: fixed;
		inset: 0;
		background: rgba(0, 0, 0, 0.5);
		display: flex;
		align-items: center;
		justify-content: center;
		z-index: 200;
	}

	.confirm-dialog {
		background: #ffffff;
		border-radius: 16px;
		padding: 24px;
		width: 340px;
		box-shadow: 0 16px 48px rgba(0, 0, 0, 0.2);
	}

	.confirm-title {
		font-size: 16px;
		font-weight: 600;
		color: #111827;
		margin: 0 0 8px;
	}

	.confirm-desc {
		font-size: 14px;
		color: #6b7280;
		line-height: 1.5;
		margin: 0 0 20px;
	}

	.confirm-actions {
		display: flex;
		gap: 8px;
		justify-content: flex-end;
	}

	.confirm-btn {
		padding: 8px 16px;
		border-radius: 8px;
		font-size: 14px;
		font-weight: 500;
		cursor: pointer;
		border: none;
		font-family: inherit;
		transition: background 0.12s ease;
	}

	.confirm-cancel {
		background: #f3f4f6;
		color: #374151;
	}

	.confirm-cancel:hover {
		background: #e5e7eb;
	}

	.confirm-danger {
		background: #ef4444;
		color: #ffffff;
	}

	.confirm-danger:hover {
		background: #dc2626;
	}

	/* Responsive */
	@media (max-width: 640px) {
		.workflow-footer {
			flex-direction: column-reverse;
		}

		.btn-primary,
		.btn-secondary {
			width: 100%;
		}
	}
</style>
