<script lang="ts">
	import { onMount } from "svelte";
	import { t } from "svelte-i18n";
	import { formatFileSize, getFileTypeLabel } from "$lib/api/workflowApi";
	import type { WorkflowFile } from "$lib/types";

	let {
		file = null,
		userName = "Current User",
		onStart = undefined,
		onBack = undefined,
	}: {
		file?: WorkflowFile | null;
		userName?: string;
		onStart?: (() => void) | undefined;
		onBack?: (() => void) | undefined;
	} = $props();

	// Configuration state
	type LanguageOption = "auto" | "de" | "en";
	type TemplateOption =
		| "standard"
		| "board"
		| "technical"
		| "interview"
		| "sales"
		| "legal";
	type WorkspaceOption = "default" | "team" | "project";
	type VisibilityOption = "private" | "team";

	let selectedLanguage: LanguageOption = $state("auto");
	let selectedTemplate: TemplateOption = $state("standard");
	let selectedWorkspace: WorkspaceOption = $state("default");
	let selectedVisibility: VisibilityOption = $state("private");

	// Output toggles
	let outputActionItems = $state(true);
	let outputDecisions = $state(true);
	let outputSentiment = $state(false);
	let outputKeyTopics = $state(true);

	const languageOptions: { value: LanguageOption; labelKey: string }[] = [
		{ value: "auto", labelKey: "workflow.meeting.confirm.language.auto" },
		{ value: "de", labelKey: "workflow.meeting.confirm.language.de" },
		{ value: "en", labelKey: "workflow.meeting.confirm.language.en" },
	];

	const templateOptions: { value: TemplateOption; labelKey: string }[] = [
		{
			value: "standard",
			labelKey: "workflow.meeting.confirm.template.standard",
		},
		{ value: "board", labelKey: "workflow.meeting.confirm.template.board" },
		{
			value: "technical",
			labelKey: "workflow.meeting.confirm.template.technical",
		},
		{
			value: "interview",
			labelKey: "workflow.meeting.confirm.template.interview",
		},
		{ value: "sales", labelKey: "workflow.meeting.confirm.template.sales" },
		{ value: "legal", labelKey: "workflow.meeting.confirm.template.legal" },
	];

	const workspaceOptions: { value: WorkspaceOption; labelKey: string }[] = [
		{
			value: "default",
			labelKey: "workflow.meeting.confirm.workspace.default",
		},
		{ value: "team", labelKey: "workflow.meeting.confirm.workspace.team" },
		{
			value: "project",
			labelKey: "workflow.meeting.confirm.workspace.project",
		},
	];

	let uploadedAt: Date = $state(new Date());
	onMount(() => {
		uploadedAt = new Date();
	});

	function formatUploadTime(date: Date): string {
		if (!date) return "";
		const now = new Date();
		const diffMs = now.getTime() - date.getTime();
		const diffMins = Math.floor(diffMs / 60000);
		if (diffMins < 1) return "just now";
		if (diffMins < 60) return `${diffMins} min ago`;
		return date.toLocaleTimeString([], {
			hour: "2-digit",
			minute: "2-digit",
		});
	}

	function formatDuration(seconds: number | undefined): string {
		if (!seconds) return "";
		const mins = Math.floor(seconds / 60);
		const secs = Math.floor(seconds % 60);
		return `${mins}:${secs.toString().padStart(2, "0")}`;
	}

	function handleStart() {
		onStart?.();
	}
</script>

<div class="file-confirmation">
	<div class="header">
		<h2>{$t("workflow.meeting.confirm.title")}</h2>
		<p class="subtitle">{$t("workflow.meeting.confirm.subtitle")}</p>
	</div>

	{#if file}
		<div class="content-layout">
			<!-- Main Configuration Column -->
			<div class="main-column">
				<!-- File Well -->
				<div class="file-well">
					<div class="well-header">
						<div
							class="file-type-badge"
							class:video={file.type?.includes("video")}
						>
							{#if file.type?.includes("video")}
								<svg
									viewBox="0 0 24 24"
									fill="none"
									stroke="currentColor"
									stroke-width="2"
								>
									<polygon points="23 7 16 12 23 17 23 7" />
									<rect
										x="1"
										y="5"
										width="15"
										height="14"
										rx="2"
										ry="2"
									/>
								</svg>
								<span>Video</span>
							{:else}
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
								<span>Audio</span>
							{/if}
						</div>
						<button class="replace-btn" onclick={() => onBack?.()}>
							<svg
								viewBox="0 0 24 24"
								fill="none"
								stroke="currentColor"
								stroke-width="2"
							>
								<path
									d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"
								/>
								<polyline points="17 8 12 3 7 8" />
								<line x1="12" y1="3" x2="12" y2="15" />
							</svg>
							{$t("workflow.meeting.confirm.replaceFile")}
						</button>
					</div>
					<div class="file-info">
						<span class="file-name">{file.name}</span>
						<div class="file-meta">
							<span>{formatFileSize(file.size)}</span>
							{#if file.duration}
								<span class="meta-sep">·</span>
								<span>{formatDuration(file.duration)}</span>
							{/if}
							<span class="meta-sep">·</span>
							<span
								>{getFileTypeLabel({
									name: file.name,
									type: file.type,
								})}</span
							>

							{#if uploadedAt}
								<span class="meta-sep">·</span>
								<span class="meta-time"
									>{formatUploadTime(uploadedAt)}</span
								>
							{/if}
						</div>
					</div>
					{#if file.url && (file.type?.includes("audio") || file.type?.includes("video"))}
						<div class="audio-preview">
							<audio controls src={file.url}
								><track kind="captions" /></audio
							>
						</div>
					{/if}
				</div>

				<!-- Intelligence Configuration -->
				<div class="config-card">
					<h3 class="config-card-title">
						<svg
							viewBox="0 0 24 24"
							fill="none"
							stroke="currentColor"
							stroke-width="2"
						>
							<circle cx="12" cy="12" r="3" />
							<path
								d="M19.4 15a1.65 1.65 0 0 0 .33 1.82l.06.06a2 2 0 0 1 0 2.83 2 2 0 0 1-2.83 0l-.06-.06a1.65 1.65 0 0 0-1.82-.33 1.65 1.65 0 0 0-1 1.51V21a2 2 0 0 1-2 2 2 2 0 0 1-2-2v-.09A1.65 1.65 0 0 0 9 19.4a1.65 1.65 0 0 0-1.82.33l-.06.06a2 2 0 0 1-2.83 0 2 2 0 0 1 0-2.83l.06-.06a1.65 1.65 0 0 0 .33-1.82 1.65 1.65 0 0 0-1.51-1H3a2 2 0 0 1-2-2 2 2 0 0 1 2-2h.09A1.65 1.65 0 0 0 4.6 9a1.65 1.65 0 0 0-.33-1.82l-.06-.06a2 2 0 0 1 0-2.83 2 2 0 0 1 2.83 0l.06.06a1.65 1.65 0 0 0 1.82.33H9a1.65 1.65 0 0 0 1-1.51V3a2 2 0 0 1 2-2 2 2 0 0 1 2 2v.09a1.65 1.65 0 0 0 1 1.51 1.65 1.65 0 0 0 1.82-.33l.06-.06a2 2 0 0 1 2.83 0 2 2 0 0 1 0 2.83l-.06.06a1.65 1.65 0 0 0-.33 1.82V9a1.65 1.65 0 0 0 1.51 1H21a2 2 0 0 1 2 2 2 2 0 0 1-2 2h-.09a1.65 1.65 0 0 0-1.51 1z"
							/>
						</svg>
						Intelligence
					</h3>

					<div class="config-grid">
						<div class="config-field">
							<label for="template-select"
								>{$t(
									"workflow.meeting.confirm.template.label",
								)}</label
							>
							<select
								id="template-select"
								bind:value={selectedTemplate}
							>
								{#each templateOptions as option}
									<option value={option.value}
										>{$t(option.labelKey)}</option
									>
								{/each}
							</select>
						</div>
						<div class="config-field">
							<label for="language-select"
								>{$t(
									"workflow.meeting.confirm.language.label",
								)}</label
							>
							<select
								id="language-select"
								bind:value={selectedLanguage}
							>
								{#each languageOptions as option}
									<option value={option.value}
										>{$t(option.labelKey)}</option
									>
								{/each}
							</select>
						</div>
					</div>

					<div class="output-toggles">
						<span class="toggles-label"
							>{$t(
								"workflow.meeting.confirm.outputs.label",
							)}</span
						>
						<div class="toggles-grid">
							<label class="toggle-item">
								<input
									type="checkbox"
									bind:checked={outputActionItems}
								/>
								<span class="toggle-switch"></span>
								<span
									>{$t(
										"workflow.meeting.confirm.outputs.actionItems",
									)}</span
								>
							</label>
							<label class="toggle-item">
								<input
									type="checkbox"
									bind:checked={outputDecisions}
								/>
								<span class="toggle-switch"></span>
								<span
									>{$t(
										"workflow.meeting.confirm.outputs.decisions",
									)}</span
								>
							</label>
							<label class="toggle-item">
								<input
									type="checkbox"
									bind:checked={outputKeyTopics}
								/>
								<span class="toggle-switch"></span>
								<span
									>{$t(
										"workflow.meeting.confirm.outputs.keyTopics",
									)}</span
								>
							</label>
							<label class="toggle-item">
								<input
									type="checkbox"
									bind:checked={outputSentiment}
								/>
								<span class="toggle-switch"></span>
								<span
									>{$t(
										"workflow.meeting.confirm.outputs.sentiment",
									)}</span
								>
							</label>
						</div>
					</div>
				</div>

				<!-- Workspace & Governance -->
				<div class="config-card">
					<h3 class="config-card-title">
						<svg
							viewBox="0 0 24 24"
							fill="none"
							stroke="currentColor"
							stroke-width="2"
						>
							<path
								d="M22 19a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h5l2 3h9a2 2 0 0 1 2 2z"
							/>
						</svg>
						Workspace
					</h3>

					<div class="config-grid">
						<div class="config-field">
							<label for="workspace-select"
								>{$t(
									"workflow.meeting.confirm.workspace.label",
								)}</label
							>
							<select
								id="workspace-select"
								bind:value={selectedWorkspace}
							>
								{#each workspaceOptions as option}
									<option value={option.value}
										>{$t(option.labelKey)}</option
									>
								{/each}
							</select>
						</div>
						<div class="config-field">
							<label
								>{$t(
									"workflow.meeting.confirm.visibility.label",
								)}</label
							>
							<div class="visibility-toggle">
								<button
									class="visibility-option"
									class:active={selectedVisibility ===
										"private"}
									onclick={() =>
										(selectedVisibility = "private")}
								>
									<svg
										viewBox="0 0 24 24"
										fill="none"
										stroke="currentColor"
										stroke-width="2"
									>
										<rect
											x="3"
											y="11"
											width="18"
											height="11"
											rx="2"
											ry="2"
										/>
										<path d="M7 11V7a5 5 0 0 1 10 0v4" />
									</svg>
									{$t(
										"workflow.meeting.confirm.visibility.private",
									)}
								</button>
								<button
									class="visibility-option"
									class:active={selectedVisibility === "team"}
									onclick={() =>
										(selectedVisibility = "team")}
								>
									<svg
										viewBox="0 0 24 24"
										fill="none"
										stroke="currentColor"
										stroke-width="2"
									>
										<path
											d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"
										/>
										<circle cx="9" cy="7" r="4" />
										<path d="M23 21v-2a4 4 0 0 0-3-3.87" />
										<path d="M16 3.13a4 4 0 0 1 0 7.75" />
									</svg>
									{$t(
										"workflow.meeting.confirm.visibility.team",
									)}
								</button>
							</div>
						</div>
					</div>

					<!-- Audit info -->
					<div class="audit-row">
						<span class="audit-label">
							<svg
								viewBox="0 0 24 24"
								fill="none"
								stroke="currentColor"
								stroke-width="2"
							>
								<path
									d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"
								/>
								<circle cx="12" cy="7" r="4" />
							</svg>
							{$t("workflow.meeting.confirm.requestedBy")}
						</span>
						<span class="audit-value">{userName}</span>
					</div>
				</div>

				<!-- Primary Action -->
				<button class="btn-primary" onclick={handleStart}>
					{$t("workflow.meeting.confirm.startProcessing")}
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

			<!-- Sidebar -->
			<div class="sidebar">
				<!-- Security Card -->
				<div class="sidebar-card security-card">
					<h4>
						<svg
							viewBox="0 0 24 24"
							fill="none"
							stroke="currentColor"
							stroke-width="2"
						>
							<path
								d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"
							/>
						</svg>
						{$t("workflow.meeting.confirm.sidebar.securityTitle")}
					</h4>
					<ul class="security-list">
						<li>
							<svg
								viewBox="0 0 24 24"
								fill="none"
								stroke="currentColor"
								stroke-width="2"
							>
								<polyline points="20 6 9 17 4 12" />
							</svg>
							{$t(
								"workflow.meeting.confirm.sidebar.securityItems.encrypted",
							)}
						</li>
						<li>
							<svg
								viewBox="0 0 24 24"
								fill="none"
								stroke="currentColor"
								stroke-width="2"
							>
								<polyline points="20 6 9 17 4 12" />
							</svg>
							{$t(
								"workflow.meeting.confirm.sidebar.securityItems.gdpr",
							)}
						</li>
						<li>
							<svg
								viewBox="0 0 24 24"
								fill="none"
								stroke="currentColor"
								stroke-width="2"
							>
								<polyline points="20 6 9 17 4 12" />
							</svg>
							{$t(
								"workflow.meeting.confirm.sidebar.securityItems.noTraining",
							)}
						</li>
						<li>
							<svg
								viewBox="0 0 24 24"
								fill="none"
								stroke="currentColor"
								stroke-width="2"
							>
								<polyline points="20 6 9 17 4 12" />
							</svg>
							{$t(
								"workflow.meeting.confirm.sidebar.securityItems.euServers",
							)}
						</li>
					</ul>
				</div>

				<!-- Tips Card -->
				<div class="sidebar-card tips-card">
					<h4>
						<svg
							viewBox="0 0 24 24"
							fill="none"
							stroke="currentColor"
							stroke-width="2"
						>
							<circle cx="12" cy="12" r="10" />
							<line x1="12" y1="16" x2="12" y2="12" />
							<line x1="12" y1="8" x2="12.01" y2="8" />
						</svg>
						{$t("workflow.meeting.confirm.sidebar.tipsTitle")}
					</h4>
					<ul class="tips-list">
						<li>
							{$t("workflow.meeting.confirm.sidebar.tips.names")}
						</li>
						<li>
							{$t(
								"workflow.meeting.confirm.sidebar.tips.quality",
							)}
						</li>
						<li>
							{$t("workflow.meeting.confirm.sidebar.tips.length")}
						</li>
					</ul>
				</div>
			</div>
		</div>
	{:else}
		<div class="no-file">
			<p>{$t("workflow.meeting.confirm.noFile")}</p>
			<button class="btn-secondary" onclick={() => onBack?.()}>
				{$t("workflow.meeting.confirm.selectFile")}
			</button>
		</div>
	{/if}
</div>

<style>
	.file-confirmation {
		width: 100%;
		max-width: 900px;
	}

	.header {
		text-align: center;
		margin-bottom: 24px;
	}

	h2 {
		font-size: 24px;
		font-weight: 700;
		color: var(--slate-900, #0f172a);
		margin-bottom: 8px;
	}

	.subtitle {
		font-size: 15px;
		color: var(--slate-600, #475569);
	}

	/* Two-column layout */
	.content-layout {
		display: grid;
		grid-template-columns: 1fr 280px;
		gap: 24px;
		align-items: start;
	}

	.main-column {
		display: flex;
		flex-direction: column;
		gap: 16px;
	}

	/* File Well */
	.file-well {
		background: var(--slate-50, #f8fafc);
		border: 1px solid var(--slate-200, #e2e8f0);
		border-radius: 12px;
		padding: 16px 20px;
	}

	.well-header {
		display: flex;
		align-items: center;
		justify-content: space-between;
		margin-bottom: 12px;
	}

	.file-type-badge {
		display: inline-flex;
		align-items: center;
		gap: 6px;
		padding: 4px 10px;
		background: var(--blue-100, #dbeafe);
		color: var(--blue-700, #1d4ed8);
		border-radius: 6px;
		font-size: 12px;
		font-weight: 500;
	}

	.file-type-badge.video {
		background: var(--purple-100, #f3e8ff);
		color: var(--purple-700, #7e22ce);
	}

	.file-type-badge svg {
		width: 14px;
		height: 14px;
	}

	.replace-btn {
		display: inline-flex;
		align-items: center;
		gap: 4px;
		font-size: 12px;
		font-weight: 500;
		color: var(--slate-500, #64748b);
		background: white;
		border: 1px solid var(--slate-200, #e2e8f0);
		border-radius: 6px;
		padding: 6px 10px;
		cursor: pointer;
		transition: all 0.15s ease;
	}

	.replace-btn:hover {
		color: var(--slate-700, #334155);
		border-color: var(--slate-300, #cbd5e1);
	}

	.replace-btn svg {
		width: 14px;
		height: 14px;
	}

	.file-info {
		margin-bottom: 12px;
	}

	.file-name {
		display: block;
		font-size: 15px;
		font-weight: 600;
		color: var(--slate-900, #0f172a);
		margin-bottom: 4px;
		white-space: nowrap;
		overflow: hidden;
		text-overflow: ellipsis;
	}

	.file-meta {
		display: flex;
		align-items: center;
		flex-wrap: wrap;
		gap: 6px;
		font-size: 12px;
		color: var(--slate-500, #64748b);
	}

	.meta-sep {
		color: var(--slate-300, #cbd5e1);
	}

	.meta-time {
		color: var(--slate-400, #94a3b8);
	}

	.audio-preview {
		padding-top: 12px;
		border-top: 1px solid var(--slate-200, #e2e8f0);
	}

	.audio-preview audio {
		width: 100%;
		height: 36px;
		border-radius: 6px;
	}

	/* Config Cards */
	.config-card {
		background: white;
		border: 1px solid var(--slate-200, #e2e8f0);
		border-radius: 12px;
		padding: 20px;
	}

	.config-card-title {
		display: flex;
		align-items: center;
		gap: 8px;
		font-size: 14px;
		font-weight: 600;
		color: var(--slate-900, #0f172a);
		margin-bottom: 16px;
	}

	.config-card-title svg {
		width: 18px;
		height: 18px;
		color: var(--slate-400, #94a3b8);
	}

	.config-grid {
		display: grid;
		grid-template-columns: 1fr 1fr;
		gap: 16px;
		margin-bottom: 16px;
	}

	.config-field label {
		display: block;
		font-size: 12px;
		font-weight: 500;
		color: var(--slate-600, #475569);
		margin-bottom: 6px;
	}

	.config-field select {
		width: 100%;
		padding: 10px 12px;
		font-size: 14px;
		color: var(--slate-700, #334155);
		background: var(--slate-50, #f8fafc);
		border: 1px solid var(--slate-200, #e2e8f0);
		border-radius: 8px;
		cursor: pointer;
		transition: all 0.15s ease;
	}

	.config-field select:hover {
		border-color: var(--slate-300, #cbd5e1);
	}

	.config-field select:focus {
		outline: none;
		border-color: var(--blue-500, #3b82f6);
		box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.1);
	}

	/* Output Toggles */
	.output-toggles {
		padding-top: 16px;
		border-top: 1px solid var(--slate-100, #f1f5f9);
	}

	.toggles-label {
		display: block;
		font-size: 12px;
		font-weight: 500;
		color: var(--slate-600, #475569);
		margin-bottom: 12px;
	}

	.toggles-grid {
		display: grid;
		grid-template-columns: 1fr 1fr;
		gap: 10px;
	}

	.toggle-item {
		display: flex;
		align-items: center;
		gap: 10px;
		font-size: 13px;
		color: var(--slate-700, #334155);
		cursor: pointer;
	}

	.toggle-item input {
		display: none;
	}

	.toggle-switch {
		width: 36px;
		height: 20px;
		background: var(--slate-200, #e2e8f0);
		border-radius: 10px;
		position: relative;
		transition: background 0.2s ease;
		flex-shrink: 0;
	}

	.toggle-switch::after {
		content: "";
		position: absolute;
		top: 2px;
		left: 2px;
		width: 16px;
		height: 16px;
		background: white;
		border-radius: 50%;
		transition: transform 0.2s ease;
		box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
	}

	.toggle-item input:checked + .toggle-switch {
		background: var(--blue-500, #3b82f6);
	}

	.toggle-item input:checked + .toggle-switch::after {
		transform: translateX(16px);
	}

	/* Visibility Toggle */
	.visibility-toggle {
		display: flex;
		gap: 8px;
	}

	.visibility-option {
		flex: 1;
		display: flex;
		align-items: center;
		justify-content: center;
		gap: 6px;
		padding: 10px 12px;
		font-size: 13px;
		font-weight: 500;
		color: var(--slate-600, #475569);
		background: var(--slate-50, #f8fafc);
		border: 1px solid var(--slate-200, #e2e8f0);
		border-radius: 8px;
		cursor: pointer;
		transition: all 0.15s ease;
	}

	.visibility-option:hover {
		border-color: var(--slate-300, #cbd5e1);
	}

	.visibility-option.active {
		background: var(--blue-50, #eff6ff);
		border-color: var(--blue-500, #3b82f6);
		color: var(--blue-700, #1d4ed8);
	}

	.visibility-option svg {
		width: 16px;
		height: 16px;
	}

	/* Audit Row */
	.audit-row {
		display: flex;
		align-items: center;
		justify-content: space-between;
		padding-top: 16px;
		border-top: 1px solid var(--slate-100, #f1f5f9);
	}

	.audit-label {
		display: flex;
		align-items: center;
		gap: 8px;
		font-size: 12px;
		color: var(--slate-500, #64748b);
	}

	.audit-label svg {
		width: 14px;
		height: 14px;
	}

	.audit-value {
		font-size: 13px;
		font-weight: 500;
		color: var(--slate-700, #334155);
	}

	/* Primary Button */
	.btn-primary {
		display: flex;
		align-items: center;
		justify-content: center;
		gap: 8px;
		width: 100%;
		padding: 14px 24px;
		font-size: 15px;
		font-weight: 600;
		color: white;
		background: var(--blue-500, #3b82f6);
		border: none;
		border-radius: 10px;
		cursor: pointer;
		transition: all 0.15s ease;
	}

	.btn-primary:hover {
		background: var(--blue-600, #2563eb);
		box-shadow: 0 4px 12px rgba(59, 130, 246, 0.3);
	}

	.btn-primary svg {
		width: 18px;
		height: 18px;
	}

	/* Sidebar */
	.sidebar {
		display: flex;
		flex-direction: column;
		gap: 16px;
	}

	.sidebar-card {
		border-radius: 12px;
		padding: 16px;
	}

	.sidebar-card h4 {
		display: flex;
		align-items: center;
		gap: 8px;
		font-size: 13px;
		font-weight: 600;
		margin-bottom: 12px;
	}

	.sidebar-card h4 svg {
		width: 16px;
		height: 16px;
	}

	/* Security Card */
	.security-card {
		background: var(--green-50, #f0fdf4);
		border: 1px solid var(--green-200, #bbf7d0);
	}

	.security-card h4 {
		color: var(--green-700, #15803d);
	}

	.security-card h4 svg {
		color: var(--green-600, #16a34a);
	}

	.security-list {
		list-style: none;
		padding: 0;
		margin: 0;
		display: flex;
		flex-direction: column;
		gap: 8px;
	}

	.security-list li {
		display: flex;
		align-items: center;
		gap: 8px;
		font-size: 12px;
		color: var(--green-700, #15803d);
	}

	.security-list li svg {
		width: 14px;
		height: 14px;
		color: var(--green-500, #22c55e);
		flex-shrink: 0;
	}

	/* Tips Card */
	.tips-card {
		background: var(--slate-50, #f8fafc);
		border: 1px solid var(--slate-200, #e2e8f0);
	}

	.tips-card h4 {
		color: var(--slate-700, #334155);
	}

	.tips-card h4 svg {
		color: var(--slate-400, #94a3b8);
	}

	.tips-list {
		list-style: none;
		padding: 0;
		margin: 0;
		display: flex;
		flex-direction: column;
		gap: 10px;
	}

	.tips-list li {
		font-size: 12px;
		color: var(--slate-600, #475569);
		line-height: 1.5;
		padding-left: 12px;
		border-left: 2px solid var(--slate-200, #e2e8f0);
	}

	/* No File State */
	.no-file {
		text-align: center;
		padding: 40px;
	}

	.no-file p {
		color: var(--slate-600, #475569);
		margin-bottom: 16px;
	}

	.btn-secondary {
		display: inline-flex;
		align-items: center;
		gap: 8px;
		padding: 12px 24px;
		font-size: 15px;
		font-weight: 600;
		color: var(--slate-700, #334155);
		background: white;
		border: 1px solid var(--slate-300, #cbd5e1);
		border-radius: 8px;
		cursor: pointer;
		transition: all 0.15s ease;
	}

	.btn-secondary:hover {
		background: var(--slate-50, #f8fafc);
		border-color: var(--slate-400, #94a3b8);
	}

	/* Responsive */
	@media (max-width: 768px) {
		.content-layout {
			grid-template-columns: 1fr;
		}

		.sidebar {
			flex-direction: row;
			flex-wrap: wrap;
		}

		.sidebar-card {
			flex: 1;
			min-width: 200px;
		}

		.config-grid {
			grid-template-columns: 1fr;
		}

		.toggles-grid {
			grid-template-columns: 1fr;
		}

		.visibility-toggle {
			flex-direction: column;
		}
	}
</style>
