<script lang="ts">
	import { onMount } from "svelte";
	import { t } from "svelte-i18n";
	import type { Protocol } from "$lib/types";

	let {
		protocol = $bindable(null),
		jobId = "",
		isExporting = false,
		editable = true,
		onExport = undefined,
		onExportPdf = undefined,
		onBack = undefined,
		onNoraAction = undefined,
		onOpenRetentionSettings = undefined,
	}: {
		protocol?: Protocol | null;
		jobId?: string;
		isExporting?: boolean;
		editable?: boolean;
		onExport?: ((data: { spaceId: string; parentPageId: string }) => void) | undefined;
		onExportPdf?: (() => void) | undefined;
		onBack?: (() => void) | undefined;
		onNoraAction?: ((data: { type: "email" | "status" | "chat" }) => void) | undefined;
		onOpenRetentionSettings?: (() => void) | undefined;
	} = $props();

	// Confluence destination state
	let selectedSpace = $state("");
	let selectedParentPage = $state("");
	let spaceSearchQuery = $state("");
	let parentPageSearchQuery = $state("");
	let isSpaceDropdownOpen = $state(false);
	let isParentPageDropdownOpen = $state(false);

	// PDF export options
	let pdfUseConfluenceStyle = $state(true);
	let pdfIncludeMetadata = $state(true);
	let pdfHighlightActions = $state(true);
	let pdfIncludeNorizonWatermark = $state(true);

	// API Data
	let remoteSpaces: Array<{
		id: string;
		key: string;
		name: string;
		icon: string;
	}> = $state([]);
	let remotePages: Array<{
		id: string;
		title: string;
		hasChildren: boolean;
	}> = $state([]);
	let isLoadingSpaces = $state(false);
	let isLoadingPages = $state(false);
	let loadError = $state("");

	import { WorkflowAPI } from "$lib/api/workflowApi";
	import { workflowStore } from "$lib/stores/workflowStore";

	// Load spaces on mount
	onMount(() => {
		(async () => {
			isLoadingSpaces = true;
			try {
				const res = await WorkflowAPI.getConfluenceSpaces();
				remoteSpaces = res.spaces;
			} catch (error) {
				console.error("Failed to load Confluence spaces:", error);
				loadError = "Failed to load spaces";
			} finally {
				isLoadingSpaces = false;
			}
		})();

		document.addEventListener("click", handleClickOutside);
		return () => document.removeEventListener("click", handleClickOutside);
	});

	// Load pages when space changes
	$effect(() => {
		if (selectedSpace) {
			loadPagesForSpace(selectedSpace);
		}
	});

	async function loadPagesForSpace(spaceId: string) {
		isLoadingPages = true;
		remotePages = [];
		try {
			const space = remoteSpaces.find((s) => s.key === spaceId);
			if (space) {
				const res = await WorkflowAPI.getConfluencePages(space.key);
				remotePages = res.pages;
			}
		} catch (error) {
			console.error("Failed to load Confluence pages:", error);
		} finally {
			isLoadingPages = false;
		}
	}

	let filteredSpaces = $derived(remoteSpaces.filter((s) =>
		s.name.toLowerCase().includes(spaceSearchQuery.toLowerCase()),
	));

	let filteredParentPages = $derived(remotePages.filter((p) =>
		p.title.toLowerCase().includes(parentPageSearchQuery.toLowerCase()),
	));

	let selectedSpaceName = $derived(
		remoteSpaces.find((s) => s.key === selectedSpace)?.name || "",
	);
	let selectedParentPageName = $derived(
		remotePages.find((p) => p.id === selectedParentPage)?.title || "",
	);

	let canExport = $derived(selectedSpace && selectedParentPage);

	function openRetentionSettings() {
		onOpenRetentionSettings?.();
	}

	function handleExport() {
		if (!canExport) return;
		onExport?.({
			spaceId: selectedSpace,
			parentPageId: selectedParentPage,
		});
	}

	function handleNoraAction(type: "email" | "status" | "chat") {
		onNoraAction?.({ type });
	}

	function handleExportPdf() {
		// TODO: Backend API integration needed
		// Send PDF export options to backend
		const pdfOptions = {
			useConfluenceStyle: pdfUseConfluenceStyle,
			includeMetadata: pdfIncludeMetadata,
			highlightActions: pdfHighlightActions,
			includeNorizonWatermark: pdfIncludeNorizonWatermark,
			protocol: protocol,
		};

		console.log("PDF Export Options:", pdfOptions);
		onExportPdf?.();
	}

	function selectSpace(spaceKey: string) {
		selectedSpace = spaceKey;
		selectedParentPage = "";
		isSpaceDropdownOpen = false;
		spaceSearchQuery = "";
	}

	function selectParentPage(pageId: string) {
		selectedParentPage = pageId;
		isParentPageDropdownOpen = false;
		parentPageSearchQuery = "";
	}

	function formatDate(dateString: string): string {
		if (!dateString) return "";
		try {
			return new Date(dateString).toLocaleDateString("de-DE", {
				weekday: "long",
				year: "numeric",
				month: "long",
				day: "numeric",
			});
		} catch {
			return dateString;
		}
	}

	function handleClickOutside(event: MouseEvent) {
		const target = event.target as HTMLElement;
		if (!target.closest(".dropdown-container")) {
			isSpaceDropdownOpen = false;
			isParentPageDropdownOpen = false;
		}
	}

	let actionItems = $derived(protocol?.actionItems?.filter((a) => a.text.trim()) || []);

	let showBackConfirmDialog = $state(false);

	function removeActionItem(index: number) {
		if (protocol?.actionItems) {
			protocol.actionItems = protocol.actionItems.filter((_, i) => i !== index);
			workflowStore.setProtocol(protocol);
		}
	}

	function removeActionItemByRef(item: (typeof actionItems)[number]) {
		if (protocol?.actionItems) {
			const index = protocol.actionItems.indexOf(item);
			if (index !== -1) {
				removeActionItem(index);
			}
		}
	}
</script>

<div class="export-confirmation">
	{#if protocol}
		<!-- Protocol Preview Card -->
		<div class="preview-card">
			<div class="preview-header">
				<span class="preview-label"
					>{$t("workflow.meeting.export.preview")}</span
				>
				{#if editable}
					<button class="edit-link" onclick={() => showBackConfirmDialog = true}>
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
						{$t("workflow.meeting.export.editProtocol")}
					</button>
				{/if}
			</div>

			<div class="protocol-content">
				<h2 class="protocol-title">
					{protocol.title || "Untitled Meeting"}
				</h2>
				<p class="protocol-date">{formatDate(protocol.date)}</p>

				{#if protocol.attendees?.length > 0}
					<div class="attendees">
						{#each protocol.attendees.filter( (a) => a.trim(), ) as attendee}
							<span class="attendee-chip">{attendee}</span>
						{/each}
					</div>
				{/if}

				{#if protocol.executiveSummary}
					<div class="summary-section">
						<p class="summary-text">{protocol.executiveSummary}</p>
					</div>
				{/if}

				<!-- Expanded Action Items List -->
				{#if actionItems.length > 0}
					<div class="action-items-list">
						<div class="action-items-header">
							<svg
								viewBox="0 0 24 24"
								fill="none"
								stroke="currentColor"
								stroke-width="2"
							>
								<polyline points="9 11 12 14 22 4" />
								<path
									d="M21 12v7a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h11"
								/>
							</svg>
							<span
								>{$t(
									"workflow.meeting.export.actionItemsTitle",
								)}</span
							>
						</div>
						<ul class="action-items">
							{#each actionItems as item}
								<li class="action-item">
									<span class="action-text">{item.text}</span>
									{#if item.assignee}
										<span class="action-assignee"
											>— {item.assignee}</span
										>
									{/if}
									{#if item.dueDate}
										<span class="action-due"
											>{item.dueDate}</span
										>
									{/if}
									<button
										class="action-remove-btn"
										onclick={() => removeActionItemByRef(item)}
										title="Remove"
									>
										<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
											<polyline points="3 6 5 6 21 6"/>
											<path d="M19 6v14a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2V6m3 0V4a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2"/>
										</svg>
									</button>
								</li>
							{/each}
						</ul>
					</div>
				{/if}
			</div>
		</div>

		<!-- Step 1: Select Confluence Destination -->
		<div
			class="export-step"
			class:has-open-dropdown={isSpaceDropdownOpen ||
				isParentPageDropdownOpen}
		>
			<div class="step-header">
				<div class="step-badge">1</div>
				<span class="step-title">Select Confluence Destination</span>
			</div>
			<div class="step-content">
				<div class="dropdowns-side-by-side">
					<!-- Space Dropdown -->
					<div class="dropdown-container">
						<label class="dropdown-label">Space</label>
						<button
							class="dropdown-trigger"
							class:has-value={selectedSpace}
							onclick={(e) => {
								e.stopPropagation();
								isSpaceDropdownOpen = !isSpaceDropdownOpen;
								isParentPageDropdownOpen = false;
							}}
						>
							<!-- Confluence Logo -->
							<svg
								class="dropdown-icon confluence-icon"
								viewBox="0 0 24 24"
								fill="currentColor"
							>
								<path
									d="M5.436 14.585c-.3.458-.6.99-.9 1.386a.378.378 0 0 0 .108.522l3.036 1.998a.378.378 0 0 0 .522-.084c.24-.36.528-.84.84-1.38 1.26-2.1 2.52-1.8 4.8-.66l3.06 1.56a.378.378 0 0 0 .504-.168l1.62-3.18a.378.378 0 0 0-.156-.498c-.96-.54-2.82-1.5-4.62-2.46-3.6-1.86-6.66-1.62-8.814 2.964zm13.128-5.17c.3-.458.6-.99.9-1.386a.378.378 0 0 0-.108-.522l-3.036-1.998a.378.378 0 0 0-.522.084c-.24.36-.528.84-.84 1.38-1.26 2.1-2.52 1.8-4.8.66l-3.06-1.56a.378.378 0 0 0-.504.168l-1.62 3.18a.378.378 0 0 0 .156.498c.96.54 2.82 1.5 4.62 2.46 3.6 1.86 6.66 1.62 8.814-2.964z"
								/>
							</svg>
							<span class="dropdown-text">
								{selectedSpaceName || "Choose space..."}
							</span>
							<svg
								class="dropdown-chevron"
								viewBox="0 0 24 24"
								fill="none"
								stroke="currentColor"
								stroke-width="2"
							>
								<polyline points="6 9 12 15 18 9" />
							</svg>
						</button>
						{#if isSpaceDropdownOpen}
							<div class="dropdown-menu">
								<input
									type="text"
									class="dropdown-search"
									placeholder="Search spaces..."
									bind:value={spaceSearchQuery}
									onclick={(e) => e.stopPropagation()}
								/>
								<div class="dropdown-options">
									{#each filteredSpaces as space}
										<button
											class="dropdown-option"
											class:selected={selectedSpace ===
												space.key}
											onclick={(e) => {
												e.stopPropagation();
												selectSpace(space.key);
											}}
										>
											{space.name}
										</button>
									{/each}
									{#if isLoadingSpaces}
										<div class="dropdown-empty">
											Loading spaces...
										</div>
									{:else if filteredSpaces.length === 0}
										<div class="dropdown-empty">
											No spaces found
										</div>
									{/if}
								</div>
							</div>
						{/if}
					</div>

					<!-- Parent Page Dropdown -->
					<div
						class="dropdown-container"
						class:disabled={!selectedSpace}
					>
						<label class="dropdown-label"
							>Parent Page (optional)</label
						>
						<button
							class="dropdown-trigger"
							class:has-value={selectedParentPage}
							disabled={!selectedSpace}
							onclick={(e) => {
								e.stopPropagation();
								if (selectedSpace) {
									isParentPageDropdownOpen =
										!isParentPageDropdownOpen;
									isSpaceDropdownOpen = false;
								}
							}}
						>
							<svg
								class="dropdown-icon"
								viewBox="0 0 24 24"
								fill="none"
								stroke="currentColor"
								stroke-width="2"
							>
								<path
									d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"
								/>
								<polyline points="14 2 14 8 20 8" />
							</svg>
							<span class="dropdown-text">
								{selectedParentPageName ||
									"Choose parent page..."}
							</span>
							<svg
								class="dropdown-chevron"
								viewBox="0 0 24 24"
								fill="none"
								stroke="currentColor"
								stroke-width="2"
							>
								<polyline points="6 9 12 15 18 9" />
							</svg>
						</button>
						{#if isParentPageDropdownOpen && selectedSpace}
							<div class="dropdown-menu">
								<input
									type="text"
									class="dropdown-search"
									placeholder="Search pages..."
									bind:value={parentPageSearchQuery}
									onclick={(e) => e.stopPropagation()}
								/>
								<div class="dropdown-options">
									{#each filteredParentPages as page}
										<button
											class="dropdown-option"
											class:selected={selectedParentPage ===
												page.id}
											onclick={(e) => {
												e.stopPropagation();
												selectParentPage(page.id);
											}}
										>
											{page.title}
										</button>
									{/each}
									{#if isLoadingPages}
										<div class="dropdown-empty">
											Loading pages...
										</div>
									{:else if filteredParentPages.length === 0}
										<div class="dropdown-empty">
											No pages found
										</div>
									{/if}
								</div>
							</div>
						{/if}
					</div>
				</div>

				{#if selectedParentPage}
					<div class="destination-path">
						<svg
							viewBox="0 0 24 24"
							fill="none"
							stroke="currentColor"
							stroke-width="2"
						>
							<polyline points="9 18 15 12 9 6" />
						</svg>
						<span>{selectedSpaceName}</span>
						<svg
							viewBox="0 0 24 24"
							fill="none"
							stroke="currentColor"
							stroke-width="2"
						>
							<polyline points="9 18 15 12 9 6" />
						</svg>
						<span>{selectedParentPageName}</span>
						<svg
							viewBox="0 0 24 24"
							fill="none"
							stroke="currentColor"
							stroke-width="2"
						>
							<polyline points="9 18 15 12 9 6" />
						</svg>
						<span class="path-new"
							>{protocol.title || "New Protocol"}</span
						>
					</div>
				{/if}
			</div>
		</div>

		<!-- Step 2: Export Options -->
		<div class="export-step">
			<div class="step-header">
				<div class="step-badge">2</div>
				<span class="step-title">Export Options</span>
			</div>
			<div class="step-content">
				<!-- Export Buttons -->
				<div class="export-buttons-grid">
					<button
						class="export-btn confluence primary"
						onclick={handleExport}
						disabled={isExporting || !canExport}
					>
						{#if isExporting}
							<div class="spinner"></div>
							Exporting...
						{:else}
							<svg viewBox="0 0 24 24" fill="currentColor">
								<path
									d="M18.87 14.77a4.25 4.25 0 0 0-3.91-2.27h-.01a4.21 4.21 0 0 0-2.7.97 4.17 4.17 0 0 0-2.69-.97h-.01a4.25 4.25 0 0 0-3.91 2.27l-1.77 4.18a.5.5 0 0 0 .46.7h2.07a.5.5 0 0 0 .46-.3l1.03-2.43c.37-.87 1.21-1.43 2.14-1.43h.01c.93 0 1.78.56 2.14 1.43l1.03 2.43a.5.5 0 0 0 .46.3h2.07a.5.5 0 0 0 .46-.7l-1.77-4.18zm-3.03-4.27a3.75 3.75 0 0 0 0-5.3 3.75 3.75 0 0 0-5.3 0 3.75 3.75 0 0 0 0 5.3 3.75 3.75 0 0 0 5.3 0z"
								/>
							</svg>
							Publish to Confluence
						{/if}
					</button>
					<button
						class="export-btn pdf secondary"
						onclick={handleExportPdf}
						disabled={isExporting}
					>
						<svg
							viewBox="0 0 24 24"
							fill="none"
							stroke="currentColor"
							stroke-width="2"
						>
							<path
								d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"
							/>
							<polyline points="14 2 14 8 20 8" />
							<line x1="16" y1="13" x2="8" y2="13" />
							<line x1="16" y1="17" x2="8" y2="17" />
							<polyline points="10 9 9 9 8 9" />
						</svg>
						Download as PDF
					</button>
				</div>

				{#if !canExport}
					<p class="export-hint">
						Select a Confluence space and parent page to publish
					</p>
				{/if}
			</div>
		</div>

		<!-- Divider -->
		<div class="divider"></div>

		<!-- Next Steps Panel with Workflow Visualization -->
		<div class="next-steps-panel">
			<span class="panel-label"
				>{$t("workflow.meeting.export.nextStepsTitle")}</span
			>
			<div class="workflow-steps">
				<div class="workflow-step completed">
					<div class="step-icon">
						<svg
							viewBox="0 0 24 24"
							fill="none"
							stroke="currentColor"
							stroke-width="2"
						>
							<path
								d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"
							/>
							<polyline points="14 2 14 8 20 8" />
						</svg>
					</div>
					<span class="step-label"
						>{$t("workflow.meeting.export.steps.protocol")}</span
					>
					<svg
						class="step-check"
						viewBox="0 0 24 24"
						fill="none"
						stroke="currentColor"
						stroke-width="2"
					>
						<polyline points="20 6 9 17 4 12" />
					</svg>
				</div>
				<svg
					class="step-arrow"
					viewBox="0 0 24 24"
					fill="none"
					stroke="currentColor"
					stroke-width="2"
				>
					<polyline points="9 18 15 12 9 6" />
				</svg>
				<button
					class="workflow-step optional"
					onclick={() => handleNoraAction("email")}
				>
					<div class="step-icon">
						<svg
							viewBox="0 0 24 24"
							fill="none"
							stroke="currentColor"
							stroke-width="2"
						>
							<path
								d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"
							/>
							<polyline points="22,6 12,13 2,6" />
						</svg>
					</div>
					<span class="step-label"
						>{$t("workflow.meeting.export.steps.email")}</span
					>
				</button>
				<svg
					class="step-arrow"
					viewBox="0 0 24 24"
					fill="none"
					stroke="currentColor"
					stroke-width="2"
				>
					<polyline points="9 18 15 12 9 6" />
				</svg>
				<button
					class="workflow-step optional"
					onclick={() => handleNoraAction("status")}
				>
					<div class="step-icon">
						<svg
							viewBox="0 0 24 24"
							fill="none"
							stroke="currentColor"
							stroke-width="2"
						>
							<path
								d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"
							/>
						</svg>
					</div>
					<span class="step-label"
						>{$t("workflow.meeting.export.steps.status")}</span
					>
				</button>
			</div>
		</div>

		<!-- Security Footer -->
		<div class="security-footer">
			<svg
				viewBox="0 0 24 24"
				fill="none"
				stroke="currentColor"
				stroke-width="2"
			>
				<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z" />
			</svg>
			<span>{$t("workflow.meeting.export.securityNote")}</span>
			<button class="retention-link" onclick={openRetentionSettings}>
				{$t("workflow.meeting.export.adjustRetention")}
				<svg
					viewBox="0 0 24 24"
					fill="none"
					stroke="currentColor"
					stroke-width="2"
				>
					<polyline points="9 18 15 12 9 6" />
				</svg>
			</button>
		</div>
	{/if}
</div>

{#if showBackConfirmDialog}
	<div class="confirm-overlay" role="dialog" aria-modal="true">
		<div class="confirm-dialog">
			<h3 class="confirm-title">Go back to editing?</h3>
			<p class="confirm-desc">You will return to the protocol editor. Your export settings will be reset.</p>
			<div class="confirm-actions">
				<button class="confirm-btn confirm-cancel" onclick={() => showBackConfirmDialog = false}>
					Cancel
				</button>
				<button class="confirm-btn confirm-danger" onclick={() => { showBackConfirmDialog = false; onBack?.(); }}>
					Go back
				</button>
			</div>
		</div>
	</div>
{/if}

<style>
	.export-confirmation {
		width: 100%;
		max-width: 800px;
		display: flex;
		flex-direction: column;
		gap: 24px;
	}

	/* Preview Card */
	.preview-card {
		background: white;
		border: 1px solid var(--slate-200, #e2e8f0);
		border-radius: 12px;
		overflow: hidden;
	}

	.preview-header {
		display: flex;
		justify-content: space-between;
		align-items: center;
		padding: 12px 20px;
		background: var(--slate-50, #f8fafc);
		border-bottom: 1px solid var(--slate-100, #f1f5f9);
	}

	.preview-label {
		font-size: 12px;
		font-weight: 600;
		color: var(--slate-500, #64748b);
		text-transform: uppercase;
		letter-spacing: 0.5px;
	}

	.edit-link {
		display: flex;
		align-items: center;
		gap: 6px;
		font-size: 13px;
		font-weight: 500;
		color: var(--blue-600, #2563eb);
		background: none;
		border: none;
		cursor: pointer;
		padding: 4px 8px;
		margin: -4px -8px;
		border-radius: 6px;
		transition: background 0.15s;
	}

	.edit-link:hover {
		background: var(--blue-50, #eff6ff);
	}

	.edit-link svg {
		width: 14px;
		height: 14px;
	}

	.protocol-content {
		padding: 20px;
	}

	.protocol-title {
		font-size: 20px;
		font-weight: 700;
		color: var(--slate-900, #0f172a);
		margin: 0 0 4px 0;
		line-height: 1.3;
	}

	.protocol-date {
		font-size: 13px;
		color: var(--slate-500, #64748b);
		margin: 0 0 12px 0;
	}

	.attendees {
		display: flex;
		flex-wrap: wrap;
		gap: 6px;
		margin-bottom: 12px;
	}

	.attendee-chip {
		display: inline-flex;
		align-items: center;
		padding: 3px 8px;
		background: var(--slate-100, #f1f5f9);
		color: var(--slate-700, #334155);
		border-radius: 12px;
		font-size: 12px;
		font-weight: 500;
	}

	.summary-section {
		padding: 12px 14px;
		background: var(--slate-50, #f8fafc);
		border-radius: 8px;
		margin-bottom: 12px;
		max-height: 120px;
		overflow-y: auto;
	}

	.summary-text {
		font-size: 13px;
		line-height: 1.5;
		color: var(--slate-600, #475569);
		margin: 0;
		white-space: pre-wrap;
	}

	/* Expanded Action Items */
	.action-items-list {
		border-top: 1px solid var(--slate-100, #f1f5f9);
		padding-top: 12px;
	}

	.action-items-header {
		display: flex;
		align-items: center;
		gap: 8px;
		margin-bottom: 10px;
		color: var(--green-700, #15803d);
		font-size: 13px;
		font-weight: 600;
	}

	.action-items-header svg {
		width: 16px;
		height: 16px;
	}

	.action-items {
		list-style: none;
		padding: 0;
		margin: 0;
		display: flex;
		flex-direction: column;
		gap: 8px;
	}

	.action-item {
		display: flex;
		flex-wrap: wrap;
		align-items: center;
		gap: 6px;
		font-size: 13px;
		padding: 8px 10px;
		background: var(--green-50, #f0fdf4);
		border-radius: 6px;
		border-left: 3px solid var(--green-500, #22c55e);
	}

	.action-text {
		color: var(--slate-800, #1e293b);
		flex: 1;
		min-width: 200px;
	}

	.action-assignee {
		color: var(--slate-600, #475569);
		font-weight: 500;
	}

	.action-due {
		color: var(--slate-500, #64748b);
		font-size: 12px;
		padding: 2px 6px;
		background: white;
		border-radius: 4px;
	}

	.action-remove-btn {
		display: flex;
		align-items: center;
		justify-content: center;
		padding: 4px;
		background: transparent;
		border: none;
		cursor: pointer;
		color: #d1d5db;
		border-radius: 4px;
		transition: all 0.15s ease;
		flex-shrink: 0;
		opacity: 0;
		margin-left: auto;
	}

	.action-item:hover .action-remove-btn {
		opacity: 1;
	}

	.action-remove-btn:hover {
		color: #ef4444;
		background: #fef2f2;
	}

	.action-remove-btn svg {
		width: 14px;
		height: 14px;
	}

	/* Export Steps */
	.export-step {
		background: white;
		border: 1px solid var(--slate-200, #e2e8f0);
		border-radius: 12px;
		overflow: visible; /* Allow dropdowns to overflow */
		margin-bottom: 16px;
		position: relative;
		z-index: 1; /* Base z-index for sections */
	}

	.export-step.has-open-dropdown {
		z-index: 100; /* Elevated z-index when dropdown is open */
	}

	.step-header {
		display: flex;
		align-items: center;
		gap: 12px;
		padding: 16px 20px;
		background: var(--slate-50, #f8fafc);
		border-bottom: 1px solid var(--slate-200, #e2e8f0);
	}

	.step-badge {
		width: 32px;
		height: 32px;
		display: flex;
		align-items: center;
		justify-content: center;
		background: #3b82f6; /* Solid blue instead of gradient */
		color: white;
		font-size: 16px;
		font-weight: 700;
		border-radius: 50%;
		flex-shrink: 0;
	}

	.step-title {
		font-size: 17px;
		font-weight: 600;
		color: var(--slate-900, #0f172a);
	}

	.step-content {
		padding: 20px;
	}

	/* Dropdowns Side by Side */
	.dropdowns-side-by-side {
		display: grid;
		grid-template-columns: 1fr 1fr;
		gap: 16px;
		margin-bottom: 16px;
	}

	.dropdown-label {
		display: block;
		font-size: 13px;
		font-weight: 600;
		color: var(--slate-700, #334155);
		margin-bottom: 8px;
	}

	.dropdown-container.disabled {
		opacity: 0.6;
		pointer-events: none;
	}

	.dropdown-container {
		position: relative;
		margin-bottom: 0;
		z-index: 10; /* Ensure dropdowns appear above other content */
	}

	.dropdown-trigger {
		width: 100%;
		display: flex;
		align-items: center;
		gap: 10px;
		padding: 12px 14px;
		background: white;
		border: 1px solid var(--slate-300, #cbd5e1);
		border-radius: 8px;
		cursor: pointer;
		transition: all 0.15s;
		text-align: left;
	}

	.dropdown-trigger:hover:not(:disabled) {
		border-color: var(--slate-400, #94a3b8);
	}

	.dropdown-trigger.has-value {
		border-color: var(--blue-500, #3b82f6);
		background: var(--blue-50, #eff6ff);
	}

	.dropdown-trigger.disabled {
		opacity: 0.5;
		cursor: not-allowed;
		background: var(--slate-50, #f8fafc);
	}

	.dropdown-icon {
		width: 18px;
		height: 18px;
		color: var(--slate-400, #94a3b8);
		flex-shrink: 0;
	}

	.dropdown-icon.confluence-icon {
		color: var(--blue-500, #3b82f6);
	}

	.dropdown-trigger.has-value .dropdown-icon {
		color: var(--blue-600, #2563eb);
	}

	.dropdown-text {
		flex: 1;
		font-size: 14px;
		color: var(--slate-600, #475569);
		white-space: nowrap;
		overflow: hidden;
		text-overflow: ellipsis;
	}

	.dropdown-trigger.has-value .dropdown-text {
		color: var(--slate-900, #0f172a);
		font-weight: 500;
	}

	.dropdown-chevron {
		width: 16px;
		height: 16px;
		color: var(--slate-400, #94a3b8);
		flex-shrink: 0;
	}

	.dropdown-menu {
		position: absolute;
		top: 100%;
		left: 0;
		right: 0;
		margin-top: 4px;
		background: white;
		border: 1px solid var(--slate-200, #e2e8f0);
		border-radius: 8px;
		box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
		z-index: 200; /* Higher z-index to appear above sections */
		overflow: hidden;
	}

	.dropdown-search {
		width: 100%;
		padding: 10px 12px;
		border: none;
		border-bottom: 1px solid var(--slate-100, #f1f5f9);
		font-size: 14px;
		outline: none;
	}

	.dropdown-search::placeholder {
		color: var(--slate-400, #94a3b8);
	}

	.dropdown-options {
		max-height: 180px;
		overflow-y: auto;
	}

	.dropdown-option {
		width: 100%;
		padding: 10px 14px;
		text-align: left;
		background: none;
		border: none;
		font-size: 14px;
		color: var(--slate-700, #334155);
		cursor: pointer;
		transition: background 0.1s;
	}

	.dropdown-option:hover {
		background: var(--slate-50, #f8fafc);
	}

	.dropdown-option.selected {
		background: var(--blue-50, #eff6ff);
		color: var(--blue-700, #1d4ed8);
		font-weight: 500;
	}

	.dropdown-empty {
		padding: 12px 14px;
		font-size: 13px;
		color: var(--slate-400, #94a3b8);
		text-align: center;
	}

	.destination-path {
		display: flex;
		align-items: center;
		gap: 4px;
		font-size: 12px;
		color: var(--slate-500, #64748b);
		padding: 8px 12px;
		background: var(--slate-50, #f8fafc);
		border-radius: 6px;
	}

	.destination-path svg {
		width: 12px;
		height: 12px;
		color: var(--slate-400, #94a3b8);
	}

	.destination-path .path-new {
		color: var(--blue-600, #2563eb);
		font-weight: 500;
	}

	/* Nora Actions */
	.nora-actions {
		display: flex;
		flex-direction: column;
		gap: 8px;
	}

	.nora-action-btn {
		display: flex;
		align-items: center;
		gap: 14px;
		padding: 14px 16px;
		background: white;
		border: 1px solid var(--slate-200, #e2e8f0);
		border-radius: 10px;
		cursor: pointer;
		transition: all 0.15s ease;
		text-align: left;
	}

	.nora-action-btn:hover {
		background: var(--slate-50, #f8fafc);
		border-color: var(--slate-300, #cbd5e1);
	}

	.nora-action-icon {
		width: 40px;
		height: 40px;
		display: flex;
		align-items: center;
		justify-content: center;
		background: var(--slate-100, #f1f5f9);
		border-radius: 10px;
		flex-shrink: 0;
	}

	.nora-action-icon svg {
		width: 20px;
		height: 20px;
		color: var(--slate-600, #475569);
	}

	.nora-action-icon.nora-gradient {
		background: linear-gradient(135deg, #f97316 0%, #3b82f6 100%);
	}

	.nora-action-icon.nora-gradient svg {
		color: white;
	}

	.nora-action-content {
		flex: 1;
		display: flex;
		flex-direction: column;
		gap: 2px;
	}

	.nora-action-label {
		font-size: 14px;
		font-weight: 600;
		color: var(--slate-900, #0f172a);
	}

	.nora-action-desc {
		font-size: 13px;
		color: var(--slate-500, #64748b);
	}

	.nora-action-arrow {
		width: 18px;
		height: 18px;
		color: var(--slate-400, #94a3b8);
		flex-shrink: 0;
	}

	/* Export Buttons */
	.export-buttons-grid {
		display: flex;
		flex-wrap: wrap;
		gap: 12px;
	}

	.export-btn {
		flex: 1;
		display: flex;
		align-items: center;
		justify-content: center;
		gap: 10px;
		padding: 14px 20px;
		font-size: 16px;
		font-weight: 600;
		border-radius: 10px;
		cursor: pointer;
		transition: all 0.15s ease;
	}

	.export-btn svg {
		width: 20px;
		height: 20px;
	}

	.export-btn.primary {
		background: var(--blue-600, #2563eb);
		color: white;
		border: none;
		box-shadow: 0 2px 8px rgba(37, 99, 235, 0.2);
	}

	.export-btn.primary:hover:not(:disabled) {
		background: var(--blue-700, #1d4ed8);
		box-shadow: 0 4px 16px rgba(37, 99, 235, 0.3);
		transform: translateY(-1px);
	}

	.export-btn.secondary {
		background: white;
		color: var(--slate-700, #334155);
		border: 2px solid var(--slate-300, #cbd5e1);
	}

	.export-btn.secondary:hover:not(:disabled) {
		background: var(--slate-50, #f8fafc);
		border-color: var(--slate-400, #94a3b8);
		transform: translateY(-1px);
		box-shadow: 0 2px 8px rgba(0, 0, 0, 0.05);
	}

	.export-btn:disabled {
		opacity: 0.5;
		cursor: not-allowed;
		transform: none !important;
	}

	.export-hint {
		font-size: 13px;
		color: var(--amber-700, #b45309);
		margin: 12px 0 0 0;
		display: flex;
		align-items: center;
		gap: 6px;
		background: var(--amber-50, #fffbeb);
		padding: 10px 12px;
		border-radius: 6px;
		border-left: 3px solid var(--amber-500, #f59e0b);
	}

	.export-hint::before {
		content: "⚠";
		font-size: 16px;
	}

	/* Divider */
	.divider {
		height: 1px;
		background: var(--slate-200, #e2e8f0);
		margin: 4px 0;
	}

	/* Next Steps Panel */
	.next-steps-panel {
		background: linear-gradient(
			135deg,
			var(--blue-50, #eff6ff) 0%,
			var(--orange-50, #fff7ed) 100%
		);
		border: 1px solid var(--slate-200, #e2e8f0);
		border-radius: 12px;
		padding: 20px;
	}

	.panel-label {
		display: block;
		font-size: 12px;
		font-weight: 600;
		color: var(--slate-600, #475569);
		text-transform: uppercase;
		letter-spacing: 0.5px;
		margin-bottom: 16px;
	}

	.workflow-steps {
		display: flex;
		align-items: center;
		justify-content: center;
		gap: 8px;
		flex-wrap: wrap;
	}

	.workflow-step {
		display: flex;
		flex-direction: column;
		align-items: center;
		gap: 8px;
		padding: 12px 16px;
		background: white;
		border: 1px solid var(--slate-200, #e2e8f0);
		border-radius: 10px;
		min-width: 100px;
		transition: all 0.15s ease;
	}

	.workflow-step.completed {
		background: var(--green-50, #f0fdf4);
		border-color: var(--green-300, #86efac);
	}

	.workflow-step.optional {
		cursor: pointer;
	}

	.workflow-step.optional:hover {
		background: var(--blue-50, #eff6ff);
		border-color: var(--blue-300, #93c5fd);
		transform: translateY(-2px);
		box-shadow: 0 4px 12px rgba(59, 130, 246, 0.15);
	}

	.step-icon {
		width: 36px;
		height: 36px;
		display: flex;
		align-items: center;
		justify-content: center;
		background: var(--slate-100, #f1f5f9);
		border-radius: 8px;
	}

	.workflow-step.completed .step-icon {
		background: var(--green-100, #dcfce7);
	}

	.workflow-step.optional:hover .step-icon {
		background: var(--blue-100, #dbeafe);
	}

	.step-icon svg {
		width: 18px;
		height: 18px;
		color: var(--slate-500, #64748b);
	}

	.workflow-step.completed .step-icon svg {
		color: var(--green-600, #16a34a);
	}

	.workflow-step.optional:hover .step-icon svg {
		color: var(--blue-600, #2563eb);
	}

	.step-label {
		font-size: 12px;
		font-weight: 500;
		color: var(--slate-700, #334155);
		text-align: center;
	}

	.step-check {
		width: 16px;
		height: 16px;
		color: var(--green-500, #22c55e);
	}

	.step-arrow {
		width: 20px;
		height: 20px;
		color: var(--slate-300, #cbd5e1);
		flex-shrink: 0;
	}

	/* Retention link */
	.retention-link {
		display: inline-flex;
		align-items: center;
		gap: 4px;
		padding: 0;
		background: none;
		border: none;
		font-size: 12px;
		font-weight: 500;
		color: var(--blue-600, #2563eb);
		cursor: pointer;
		transition: color 0.15s ease;
		margin-left: auto;
	}

	.retention-link:hover {
		color: var(--blue-700, #1d4ed8);
	}

	.retention-link svg {
		width: 14px;
		height: 14px;
	}

	/* Security Footer */
	.security-footer {
		display: flex;
		align-items: center;
		gap: 8px;
		padding: 12px 16px;
		font-size: 12px;
		color: var(--slate-400, #94a3b8);
		border-top: 1px solid var(--slate-100, #f1f5f9);
		margin-top: 8px;
	}

	.security-footer > svg {
		width: 14px;
		height: 14px;
		flex-shrink: 0;
	}

	.security-footer > span {
		flex: 1;
	}

	/* Spinner */
	.spinner {
		width: 18px;
		height: 18px;
		border: 2px solid rgba(255, 255, 255, 0.3);
		border-top-color: white;
		border-radius: 50%;
		animation: spin 0.8s linear infinite;
	}

	.spinner.dark {
		border-color: rgba(0, 0, 0, 0.1);
		border-top-color: var(--slate-600, #475569);
	}

	@keyframes spin {
		to {
			transform: rotate(360deg);
		}
	}

	/* Responsive */
	@media (max-width: 640px) {
		.dropdowns-side-by-side {
			grid-template-columns: 1fr;
			gap: 12px;
		}

		.export-buttons-grid {
			flex-direction: column;
		}

		.action-item {
			flex-direction: column;
			gap: 4px;
		}

		.action-text {
			min-width: unset;
		}

		.step-content {
			padding: 16px;
		}
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
</style>
