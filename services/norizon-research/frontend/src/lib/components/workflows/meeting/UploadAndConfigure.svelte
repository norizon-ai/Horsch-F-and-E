<script lang="ts">
	import { onMount } from "svelte";
	import { t } from "svelte-i18n";
	import { fly, slide, fade } from "svelte/transition";
	import {
		isValidAudioFile,
		formatFileSize,
		getFileTypeLabel,
		WorkflowAPI,
		type ConfluenceSpace,
		type ConfluencePage,
	} from "$lib/api/workflowApi";
	import { workflowStore } from "$lib/stores/workflowStore";
	import type { WorkflowFile } from "$lib/types";
	import TeamsImport from "./TeamsImport.svelte";

	let {
		file = null,
		userName = "Current User",
		jobId = "",
		onFileSelected = undefined,
		onStart = undefined,
		onBack = undefined,
	}: {
		file?: WorkflowFile | null;
		userName?: string;
		jobId?: string;
		onFileSelected?: ((file: File) => void) | undefined;
		onStart?: (() => void) | undefined;
		onBack?: (() => void) | undefined;
	} = $props();

	// Source selection
	type SourceTab = "upload" | "teams";
	let sourceTab: SourceTab = $state("upload");

	// Upload state
	let isDragging = $state(false);
	let uploadError: string | null = $state(null);
	let fileInput: HTMLInputElement = $state(null as unknown as HTMLInputElement);
	let activeTutorial: "teams" | "iphone" = $state("teams");
	let bestPracticesExpanded = $state(false);
	let helpExpanded = $state(false);
	let showUploadTooltip = $state(false);

	// Issue 2 Fix: Back button confirmation dialog
	let showBackConfirmDialog = $state(false);

	function handleDisabledAdvance() {
		showUploadTooltip = true;
		helpExpanded = true;
		setTimeout(() => {
			showUploadTooltip = false;
		}, 3000);
	}

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

	// Metadata fields (pre-flight context for AI)
	let meetingTitle = $state("");
	let meetingDate = $state(new Date().toISOString().split("T")[0]);

	// Auto-populate meeting title and date from file
	$effect(() => {
		if (file && !meetingTitle) {
			// Extract title from filename, remove extension and clean up
			meetingTitle = file.name
				.replace(/\.[^/.]+$/, "")
				.replace(/[-_]/g, " ")
				.replace(/\b\w/g, (c) => c.toUpperCase());
		}
		if (file && file.lastModified) {
			// Set date from file's last modified
			const fileDate = new Date(file.lastModified);
			meetingDate = fileDate.toISOString().split("T")[0];
		}
	});

	// Processing options
	type LanguageOption = "auto" | "de" | "en";
	let selectedLanguage: LanguageOption = $state("auto");

	// Destination selection (moved from ExportConfirmation)
	let selectedSpace = $state("");
	let selectedParentPage = $state("");
	let spaceSearchQuery = $state("");
	let parentPageSearchQuery = $state("");
	let isSpaceDropdownOpen = $state(false);
	let isParentPageDropdownOpen = $state(false);

	// Confluence data from API
	let confluenceSpaces: ConfluenceSpace[] = $state([]);
	let availableParentPages: ConfluencePage[] = $state([]);
	let isLoadingSpaces = $state(true);
	let isLoadingPages = $state(false);

	// Load Confluence spaces on mount
	onMount(async () => {
		try {
			const response = await WorkflowAPI.getConfluenceSpaces();
			confluenceSpaces = response.spaces;
		} catch (error) {
			console.error("Failed to load Confluence spaces:", error);
		} finally {
			isLoadingSpaces = false;
		}
	});

	// Load pages when space is selected
	async function loadPagesForSpace(spaceKey: string) {
		isLoadingPages = true;
		try {
			const response = await WorkflowAPI.getConfluencePages(spaceKey);
			availableParentPages = response.pages;
		} catch (error) {
			console.error("Failed to load Confluence pages:", error);
			availableParentPages = [];
		} finally {
			isLoadingPages = false;
		}
	}

	let filteredSpaces = $derived(confluenceSpaces.filter((s) =>
		s.name.toLowerCase().includes(spaceSearchQuery.toLowerCase()),
	));

	let filteredParentPages = $derived(availableParentPages.filter((p) =>
		p.title.toLowerCase().includes(parentPageSearchQuery.toLowerCase()),
	));

	let selectedSpaceName = $derived(
		confluenceSpaces.find((s) => s.id === selectedSpace)?.name || ""
	);
	let selectedParentPageName = $derived(
		availableParentPages.find((p) => p.id === selectedParentPage)?.title || ""
	);

	function selectSpace(space: ConfluenceSpace) {
		selectedSpace = space.id;
		selectedParentPage = "";
		isSpaceDropdownOpen = false;
		spaceSearchQuery = "";
		// Load pages for the selected space using the space key
		loadPagesForSpace(space.key);
	}

	function selectParentPage(pageId: string) {
		selectedParentPage = pageId;
		isParentPageDropdownOpen = false;
		parentPageSearchQuery = "";
		saveDestination();
	}

	function saveDestination() {
		if (selectedSpace && selectedParentPage) {
			workflowStore.setDestination(selectedSpace, selectedParentPage);
		}
	}

	function handleDestinationClickOutside(event: MouseEvent) {
		const target = event.target as HTMLElement;
		if (!target.closest(".dest-dropdown-container")) {
			isSpaceDropdownOpen = false;
			isParentPageDropdownOpen = false;
		}
	}

	const ACCEPTED_TYPES = ".mp3,.mp4,.m4a,.wav,.webm";
	const MAX_FILE_SIZE = 500 * 1024 * 1024; // 500MB

	// Estimate processing time based on file size (rough: 1 min per 10MB)
	let estimatedMinutes = $derived(file
		? Math.max(2, Math.ceil(file.size / (10 * 1024 * 1024)))
		: 3);

	let uploadedAt: Date | null = null;
	$effect(() => {
		if (file && !uploadedAt) {
			uploadedAt = new Date();
		}
	});

	// Drag and drop handlers
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
		uploadError = null;

		const files = e.dataTransfer?.files;
		if (files && files.length > 0) {
			validateAndSelect(files[0]);
		}
	}

	function handleFileInput(e: Event) {
		const input = e.target as HTMLInputElement;
		uploadError = null;

		if (input.files && input.files.length > 0) {
			validateAndSelect(input.files[0]);
		}
	}

	function validateAndSelect(selectedFile: File) {
		if (!isValidAudioFile(selectedFile)) {
			uploadError = $t("workflow.meeting.upload.errorType");
			return;
		}

		if (selectedFile.size > MAX_FILE_SIZE) {
			uploadError = $t("workflow.meeting.upload.errorSize", {
				values: { maxSize: formatFileSize(MAX_FILE_SIZE) },
			});
			return;
		}

		// Close FAQ sections when file is selected
		bestPracticesExpanded = false;
		helpExpanded = false;

		onFileSelected?.(selectedFile);
	}

	function openFilePicker() {
		fileInput?.click();
	}

	function clearFile() {
		uploadedAt = null;
		// Parent will handle clearing the file
		onFileSelected?.(null as unknown as File);
	}

	function handleTeamsImported(data: {
		fileName: string;
		fileSize: number;
		duration: number;
		meetingTitle: string;
		meetingDate: string;
	}) {
		// Create a synthetic WorkflowFile-like object and dispatch fileSelected
		// The parent component handles this the same way as a manual upload
		const syntheticFile = new File([], data.fileName, {
			type: "video/mp4",
		});
		// Auto-populate metadata from Teams
		if (data.meetingTitle) meetingTitle = data.meetingTitle;
		if (data.meetingDate) meetingDate = data.meetingDate;
		onFileSelected?.(syntheticFile);
	}

	function formatUploadTime(date: Date | null): string {
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

<div class="upload-and-configure">
	<!-- Trust Indicators - always visible -->
	<div class="trust-indicators">
		<div class="trust-item">
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
		<div class="trust-item">
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

	<!-- Source Toggle Tabs + Drop Zone / File Preview -->
	{#if !file}
		<!-- Source Toggle (Task 2: Swapped tab order - Teams left, Upload right) -->
		<div class="source-tabs">
			<button
				class="source-tab"
				class:active={sourceTab === "teams"}
				onclick={() => (sourceTab = "teams")}
			>
				<!-- Task 3: Microsoft Teams logo -->
				<svg
					viewBox="0 0 2228.833 2073.333"
					fill="currentColor"
					class="teams-logo"
				>
					<path
						d="M1554.637 777.5h575.713c54.391 0 98.483 44.092 98.483 98.483v524.398c0 199.901-162.051 361.952-361.952 361.952h-1.711c-199.901.028-361.975-162-362.004-361.901V828.971c.001-28.427 23.045-51.471 51.471-51.471z"
						fill="#5059C9"
					/>
					<circle
						cx="1943.75"
						cy="440.583"
						r="233.25"
						fill="#5059C9"
					/>
					<circle
						cx="1218.083"
						cy="336.917"
						r="336.917"
						fill="#7B83EB"
					/>
					<path
						d="M1667.323 777.5H717.01c-53.743 1.33-96.257 45.931-95.01 99.676v598.105c-7.505 322.519 247.657 590.16 570.167 598.053 322.51-7.893 577.671-275.534 570.167-598.053V877.176c1.245-53.745-41.268-98.346-95.011-99.676z"
						fill="#7B83EB"
					/>
					<path
						d="M1244 777.5v838.145c-.258 38.435-23.549 72.964-59.09 87.598-11.316 4.787-23.478 7.254-35.765 7.257H667.613c-6.738-17.105-12.958-34.21-18.142-51.833a598.053 598.053 0 0 1 0-318.08c5.184-17.623 11.404-34.728 18.142-51.833h293.265c38.744-.565 70.445-30.657 71.333-69.39V806.941c.094-16.249 13.253-29.409 29.502-29.502 16.249.094 29.409 13.253 29.502 29.502v112.61c0 38.744 31.39 70.134 70.134 70.134h112.61c16.249-.094 29.409 13.253 29.502 29.502-.094 16.249-13.253 29.409-29.502 29.502h-112.61c-38.744 0-70.134 31.39-70.134 70.134v112.61c0 38.744 31.39 70.134 70.134 70.134h112.61c16.249-.094 29.409 13.253 29.502 29.502-.094 16.249-13.253 29.409-29.502 29.502H1161.6c-38.744 0-70.134 31.39-70.134 70.134v112.61c0 38.744 31.39 70.134 70.134 70.134h112.61c16.249-.094 29.409 13.253 29.502 29.502-.094 16.249-13.253 29.409-29.502 29.502h-112.61c-38.744 0-70.134 31.39-70.134 70.134v112.61c0 38.744 31.39 70.134 70.134 70.134h112.61c16.249-.094 29.409 13.253 29.502 29.502z"
						fill="#5059C9"
						opacity=".1"
					/>
					<path
						d="M1192.167 777.5H717.01c-53.743 1.33-96.257 45.931-95.01 99.676v598.105c-7.505 322.519 247.657 590.16 570.167 598.053z"
						fill="#7B83EB"
						opacity=".2"
					/>
					<path
						d="M1192.167 777.5H717.01c-53.743 1.33-96.257 45.931-95.01 99.676v598.105c-7.505 322.519 247.657 590.16 570.167 598.053z"
						fill="#7B83EB"
						opacity=".2"
					/>
					<path
						d="M1192.167 777.5H717.01c-53.743 1.33-96.257 45.931-95.01 99.676v598.105c-7.505 322.519 247.657 590.16 570.167 598.053z"
						fill="#7B83EB"
						opacity=".2"
					/>
				</svg>
				{$t("workflow.meeting.teams.tabLabel")}
			</button>
			<button
				class="source-tab"
				class:active={sourceTab === "upload"}
				onclick={() => (sourceTab = "upload")}
			>
				<svg
					viewBox="0 0 24 24"
					fill="none"
					stroke="currentColor"
					stroke-width="2"
				>
					<path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4" />
					<polyline points="17 8 12 3 7 8" />
					<line x1="12" y1="3" x2="12" y2="15" />
				</svg>
				{$t("workflow.meeting.upload.title")}
			</button>
		</div>

		{#if sourceTab === "teams"}
			<!-- Teams Import Mode -->
			<TeamsImport {jobId} onImported={handleTeamsImported} />
		{:else}
			<!-- Upload Mode -->
			<div
				class="drop-zone"
				class:dragging={isDragging}
				class:error={!!uploadError}
				role="button"
				tabindex="0"
				ondragenter={handleDragEnter}
				ondragleave={handleDragLeave}
				ondragover={handleDragOver}
				ondrop={handleDrop}
				onclick={openFilePicker}
				onkeypress={(e) => e.key === "Enter" && openFilePicker()}
				in:fade={{ duration: 200 }}
			>
				<input
					bind:this={fileInput}
					type="file"
					accept={ACCEPTED_TYPES}
					onchange={handleFileInput}
					hidden
				/>

				<div class="drop-icon">
					<svg
						viewBox="0 0 24 24"
						fill="none"
						stroke="currentColor"
						stroke-width="2"
					>
						<path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4" />
						<polyline points="17 8 12 3 7 8" />
						<line x1="12" y1="3" x2="12" y2="15" />
					</svg>
				</div>

				<div class="drop-text">
					<span class="drop-primary">
						{#if isDragging}
							{$t("workflow.meeting.upload.dropHere")}
						{:else}
							{$t("workflow.meeting.upload.dropOrClick")}
						{/if}
					</span>
					<span class="drop-secondary"
						>MP3, MP4, WAV, M4A (max. 500MB)</span
					>
				</div>
			</div>
		{/if}
	{:else}
		<!-- File Preview Mode (compact) -->
		<div class="file-well" in:fly={{ y: -20, duration: 300 }}>
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
				<button class="replace-btn" onclick={openFilePicker}>
					<svg
						viewBox="0 0 24 24"
						fill="none"
						stroke="currentColor"
						stroke-width="2"
					>
						<path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4" />
						<polyline points="17 8 12 3 7 8" />
						<line x1="12" y1="3" x2="12" y2="15" />
					</svg>
					{$t("workflow.meeting.confirm.replaceFile")}
				</button>
				<input
					bind:this={fileInput}
					type="file"
					accept={ACCEPTED_TYPES}
					onchange={handleFileInput}
					hidden
				/>
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
	{/if}

	{#if uploadError}
		<div class="error-message" transition:slide={{ duration: 200 }}>
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
			<span>{uploadError}</span>
		</div>
	{/if}

	<!-- Configuration Section (only when file is present) -->
	{#if file}
		<div
			class="config-section"
			in:fly={{ y: 30, duration: 400, delay: 150 }}
		>
			<!-- Meeting Metadata (seeds AI with context) -->
			<!-- Task 8: Rearranged form layout - Title full-width, Date+Language on row below -->
			<div class="metadata-section">
				<div class="section-header">
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
					</svg>
					<span>{$t("workflow.meeting.confirm.metadata.title")}</span>
					<span class="optional-badge"
						>{$t(
							"workflow.meeting.confirm.metadata.optional",
						)}</span
					>
				</div>
				<div class="metadata-grid-custom">
					<!-- Row 1: Title full-width -->
					<div class="metadata-field full-width">
						<label for="meeting-title"
							>{$t(
								"workflow.meeting.confirm.metadata.meetingTitle",
							)}</label
						>
						<input
							type="text"
							id="meeting-title"
							bind:value={meetingTitle}
							placeholder={$t(
								"workflow.meeting.confirm.metadata.meetingTitlePlaceholder",
							)}
						/>
					</div>
					<!-- Row 2: Date + Language -->
					<div class="metadata-field">
						<label for="meeting-date"
							>{$t(
								"workflow.meeting.confirm.metadata.meetingDate",
							)}</label
						>
						<input
							type="date"
							id="meeting-date"
							bind:value={meetingDate}
						/>
					</div>
					<div class="metadata-field">
						<label for="language-select"
							>{$t(
								"workflow.meeting.confirm.language.label",
							)}</label
						>
						<select
							id="language-select"
							bind:value={selectedLanguage}
						>
							<option value="auto"
								>{$t(
									"workflow.meeting.confirm.language.auto",
								)}</option
							>
							<option value="de"
								>{$t(
									"workflow.meeting.confirm.language.de",
								)}</option
							>
							<option value="en"
								>{$t(
									"workflow.meeting.confirm.language.en",
								)}</option
							>
						</select>
					</div>
				</div>
			</div>

			<!-- Destination Selection -->
			<!-- Task 9: Moved "Save to my personal space" below shared space options -->
			<div
				class="destination-section"
				onclick={handleDestinationClickOutside}
			>
				<div class="section-header">
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
					<span>{$t("workflow.meeting.export.destination")}</span>
				</div>

				<div class="destination-selector">
					<!-- Space Dropdown -->
					<div class="dest-dropdown-container">
						<button
							class="dest-dropdown-trigger"
							class:has-value={selectedSpace}
							onclick={(e) => {
								e.stopPropagation();
								isSpaceDropdownOpen = !isSpaceDropdownOpen;
								isParentPageDropdownOpen = false;
							}}
						>
							<!-- Confluence Logo -->
							<svg
								class="dest-dropdown-icon confluence-icon"
								viewBox="0 0 24 24"
								fill="currentColor"
							>
								<path
									d="M5.436 14.585c-.3.458-.6.99-.9 1.386a.378.378 0 0 0 .108.522l3.036 1.998a.378.378 0 0 0 .522-.084c.24-.36.528-.84.84-1.38 1.26-2.1 2.52-1.8 4.8-.66l3.06 1.56a.378.378 0 0 0 .504-.168l1.62-3.18a.378.378 0 0 0-.156-.498c-.96-.54-2.82-1.5-4.62-2.46-3.6-1.86-6.66-1.62-8.814 2.964zm13.128-5.17c.3-.458.6-.99.9-1.386a.378.378 0 0 0-.108-.522l-3.036-1.998a.378.378 0 0 0-.522.084c-.24.36-.528.84-.84 1.38-1.26 2.1-2.52 1.8-4.8.66l-3.06-1.56a.378.378 0 0 0-.504.168l-1.62 3.18a.378.378 0 0 0 .156.498c.96.54 2.82 1.5 4.62 2.46 3.6 1.86 6.66 1.62 8.814-2.964z"
								/>
							</svg>
							<span class="dest-dropdown-text">
								{selectedSpaceName ||
									$t("workflow.meeting.export.selectSpace")}
							</span>
							<svg
								class="dest-dropdown-chevron"
								viewBox="0 0 24 24"
								fill="none"
								stroke="currentColor"
								stroke-width="2"
							>
								<polyline points="6 9 12 15 18 9" />
							</svg>
						</button>
						{#if isSpaceDropdownOpen}
							<div class="dest-dropdown-menu">
								<input
									type="text"
									class="dest-dropdown-search"
									placeholder={$t(
										"workflow.meeting.export.searchSpaces",
									)}
									bind:value={spaceSearchQuery}
									onclick={(e) => e.stopPropagation()}
								/>
								<div class="dest-dropdown-options">
									{#each filteredSpaces as space}
										<button
											class="dest-dropdown-option"
											class:selected={selectedSpace ===
												space.id}
											onclick={(e) => {
												e.stopPropagation();
												selectSpace(space);
											}}
										>
											{space.name}
										</button>
									{/each}
									{#if filteredSpaces.length === 0}
										<div class="dest-dropdown-empty">
											{$t(
												"workflow.meeting.export.noSpacesFound",
											)}
										</div>
									{/if}
								</div>
							</div>
						{/if}
					</div>

					<!-- Parent Page Dropdown -->
					<div class="dest-dropdown-container">
						<button
							class="dest-dropdown-trigger"
							class:has-value={selectedParentPage}
							class:disabled={!selectedSpace}
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
								class="dest-dropdown-icon"
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
							<span class="dest-dropdown-text">
								{selectedParentPageName ||
									$t(
										"workflow.meeting.export.selectParentPage",
									)}
							</span>
							<svg
								class="dest-dropdown-chevron"
								viewBox="0 0 24 24"
								fill="none"
								stroke="currentColor"
								stroke-width="2"
							>
								<polyline points="6 9 12 15 18 9" />
							</svg>
						</button>
						{#if isParentPageDropdownOpen}
							<div class="dest-dropdown-menu">
								<input
									type="text"
									class="dest-dropdown-search"
									placeholder={$t(
										"workflow.meeting.export.searchPages",
									)}
									bind:value={parentPageSearchQuery}
									onclick={(e) => e.stopPropagation()}
								/>
								<div class="dest-dropdown-options">
									{#each filteredParentPages as page}
										<button
											class="dest-dropdown-option"
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
									{#if filteredParentPages.length === 0}
										<div class="dest-dropdown-empty">
											{$t(
												"workflow.meeting.export.noPagesFound",
											)}
										</div>
									{/if}
								</div>
							</div>
						{/if}
					</div>
				</div>
				{#if selectedSpace && selectedParentPage}
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
					</div>
				{/if}

				<div class="or-divider">
					<span>{$t("common.or")}</span>
				</div>

				<!-- Personal Space Quick Action (moved below) -->
				<button
					class="personal-space-btn"
					class:selected={selectedSpace === "PERSONAL"}
					onclick={() => {
						selectedSpace = "PERSONAL";
						selectedParentPage = "meetings";
						saveDestination();
					}}
				>
					<svg
						viewBox="0 0 24 24"
						fill="none"
						stroke="currentColor"
						stroke-width="2"
					>
						<path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2" />
						<circle cx="12" cy="7" r="4" />
					</svg>
					{$t("workflow.meeting.export.saveToPersonalSpace")}
				</button>
			</div>

			<!-- Footer Actions -->
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
				<div class="footer-right">
					<span class="time-estimate">
						<svg
							viewBox="0 0 24 24"
							fill="none"
							stroke="currentColor"
							stroke-width="2"
						>
							<circle cx="12" cy="12" r="10" />
							<polyline points="12 6 12 12 16 14" />
						</svg>
						{$t("workflow.meeting.confirm.timeEstimate", {
							values: { minutes: estimatedMinutes },
						})}
					</span>
					<button class="btn-primary" onclick={handleStart}>
						{$t("workflow.meeting.confirm.startButton")}
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
			</div>
		</div>
	{:else}
		<!-- FAQ Section (only when no file) -->
		<div class="faq-section" out:slide={{ duration: 200 }}>
			<!-- Best Practices -->
			<button
				class="help-trigger"
				class:expanded={bestPracticesExpanded}
				onclick={() =>
					(bestPracticesExpanded = !bestPracticesExpanded)}
			>
				<svg
					class="help-icon"
					viewBox="0 0 24 24"
					fill="none"
					stroke="currentColor"
					stroke-width="2"
				>
					<path d="M12 2L2 7l10 5 10-5-10-5z" />
					<path d="M2 17l10 5 10-5" />
					<path d="M2 12l10 5 10-5" />
				</svg>
				<span>{$t("workflow.meeting.upload.bestPracticesTitle")}</span>
				<svg
					class="chevron"
					class:rotated={bestPracticesExpanded}
					viewBox="0 0 24 24"
					fill="none"
					stroke="currentColor"
					stroke-width="2"
				>
					<polyline points="6 9 12 15 18 9" />
				</svg>
			</button>

			{#if bestPracticesExpanded}
				<div class="help-content" transition:slide={{ duration: 200 }}>
					<div class="best-practices-grid">
						<div class="practice-item">
							<div class="practice-icon">
								<svg
									viewBox="0 0 24 24"
									fill="none"
									stroke="currentColor"
									stroke-width="2"
								>
									<path
										d="M12 1a3 3 0 0 0-3 3v8a3 3 0 0 0 6 0V4a3 3 0 0 0-3-3z"
									/>
									<path d="M19 10v2a7 7 0 0 1-14 0v-2" />
									<line x1="12" y1="19" x2="12" y2="23" />
									<line x1="8" y1="23" x2="16" y2="23" />
								</svg>
							</div>
							<div class="practice-text">
								<strong
									>{$t(
										"workflow.meeting.upload.bestPractices.audio.title",
									)}</strong
								>
								<span
									>{$t(
										"workflow.meeting.upload.bestPractices.audio.description",
									)}</span
								>
							</div>
						</div>
						<div class="practice-item">
							<div class="practice-icon">
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
							</div>
							<div class="practice-text">
								<strong
									>{$t(
										"workflow.meeting.upload.bestPractices.speakers.title",
									)}</strong
								>
								<span
									>{$t(
										"workflow.meeting.upload.bestPractices.speakers.description",
									)}</span
								>
							</div>
						</div>
						<div class="practice-item">
							<div class="practice-icon">
								<svg
									viewBox="0 0 24 24"
									fill="none"
									stroke="currentColor"
									stroke-width="2"
								>
									<circle cx="12" cy="12" r="10" />
									<polyline points="12 6 12 12 16 14" />
								</svg>
							</div>
							<div class="practice-text">
								<strong
									>{$t(
										"workflow.meeting.upload.bestPractices.duration.title",
									)}</strong
								>
								<span
									>{$t(
										"workflow.meeting.upload.bestPractices.duration.description",
									)}</span
								>
							</div>
						</div>
						<div class="practice-item">
							<div class="practice-icon">
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
							</div>
							<div class="practice-text">
								<strong
									>{$t(
										"workflow.meeting.upload.bestPractices.recording.title",
									)}</strong
								>
								<span
									>{$t(
										"workflow.meeting.upload.bestPractices.recording.description",
									)}</span
								>
							</div>
						</div>
					</div>
				</div>
			{/if}

			<!-- Where to find recordings -->
			<button
				class="help-trigger"
				class:expanded={helpExpanded}
				onclick={() => (helpExpanded = !helpExpanded)}
			>
				<svg
					class="help-icon"
					viewBox="0 0 24 24"
					fill="none"
					stroke="currentColor"
					stroke-width="2"
				>
					<circle cx="12" cy="12" r="10" />
					<path d="M9.09 9a3 3 0 0 1 5.83 1c0 2-3 3-3 3" />
					<line x1="12" y1="17" x2="12.01" y2="17" />
				</svg>
				<span>{$t("workflow.meeting.upload.tutorialTitle")}</span>
				<svg
					class="chevron"
					class:rotated={helpExpanded}
					viewBox="0 0 24 24"
					fill="none"
					stroke="currentColor"
					stroke-width="2"
				>
					<polyline points="6 9 12 15 18 9" />
				</svg>
			</button>

			{#if helpExpanded}
				<div class="help-content" transition:slide={{ duration: 200 }}>
					<div class="tutorial-tabs">
						<button
							class="tutorial-tab"
							class:active={activeTutorial === "teams"}
							onclick={() => (activeTutorial = "teams")}
						>
							<!-- Microsoft Teams logo -->
							<svg
								viewBox="0 0 2228.833 2073.333"
								fill="currentColor"
								class="teams-logo-small"
							>
								<path
									d="M1554.637 777.5h575.713c54.391 0 98.483 44.092 98.483 98.483v524.398c0 199.901-162.051 361.952-361.952 361.952h-1.711c-199.901.028-361.975-162-362.004-361.901V828.971c.001-28.427 23.045-51.471 51.471-51.471z"
									fill="#5059C9"
								/>
								<circle
									cx="1943.75"
									cy="440.583"
									r="233.25"
									fill="#5059C9"
								/>
								<circle
									cx="1218.083"
									cy="336.917"
									r="336.917"
									fill="#7B83EB"
								/>
								<path
									d="M1667.323 777.5H717.01c-53.743 1.33-96.257 45.931-95.01 99.676v598.105c-7.505 322.519 247.657 590.16 570.167 598.053 322.51-7.893 577.671-275.534 570.167-598.053V877.176c1.245-53.745-41.268-98.346-95.011-99.676z"
									fill="#7B83EB"
								/>
							</svg>
							Microsoft Teams
						</button>
						<button
							class="tutorial-tab"
							class:active={activeTutorial === "iphone"}
							onclick={() => (activeTutorial = "iphone")}
						>
							<svg
								viewBox="0 0 24 24"
								fill="none"
								stroke="currentColor"
								stroke-width="2"
							>
								<rect
									x="5"
									y="2"
									width="14"
									height="20"
									rx="2"
									ry="2"
								/>
								<line x1="12" y1="18" x2="12.01" y2="18" />
							</svg>
							iPhone
						</button>
					</div>

					<div class="tutorial-content">
						{#if activeTutorial === "teams"}
							<div class="tutorial-steps">
								<div class="tutorial-step">
									<span class="step-number">1</span>
									<span class="step-text"
										>{@html $t(
											"workflow.meeting.upload.tutorial.teams.step1",
										)}</span
									>
								</div>
								<div class="tutorial-step">
									<span class="step-number">2</span>
									<span class="step-text"
										>{@html $t(
											"workflow.meeting.upload.tutorial.teams.step2",
										)}</span
									>
								</div>
								<div class="tutorial-step">
									<span class="step-number">3</span>
									<span class="step-text"
										>{@html $t(
											"workflow.meeting.upload.tutorial.teams.step3",
										)}</span
									>
								</div>
								<div class="tutorial-step">
									<span class="step-number">4</span>
									<span class="step-text"
										>{@html $t(
											"workflow.meeting.upload.tutorial.teams.step4",
										)}</span
									>
								</div>
							</div>
						{:else}
							<div class="tutorial-steps">
								<div class="tutorial-step">
									<span class="step-number">1</span>
									<span class="step-text"
										>{@html $t(
											"workflow.meeting.upload.tutorial.iphone.step1",
										)}</span
									>
								</div>
								<div class="tutorial-step">
									<span class="step-number">2</span>
									<span class="step-text"
										>{@html $t(
											"workflow.meeting.upload.tutorial.iphone.step2",
										)}</span
									>
								</div>
								<div class="tutorial-step">
									<span class="step-number">3</span>
									<span class="step-text"
										>{@html $t(
											"workflow.meeting.upload.tutorial.iphone.step3",
										)}</span
									>
								</div>
								<div class="tutorial-step">
									<span class="step-number">4</span>
									<span class="step-text"
										>{@html $t(
											"workflow.meeting.upload.tutorial.iphone.step4",
										)}</span
									>
								</div>
							</div>
						{/if}
					</div>
				</div>
			{/if}
		</div>

		<!-- Footer with disabled advance button -->
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
			<div class="advance-container">
				{#if showUploadTooltip}
					<div
						class="upload-tooltip"
						transition:fade={{ duration: 150 }}
					>
						{$t("workflow.meeting.upload.uploadRequired")}
					</div>
				{/if}
				<button
					class="btn-primary disabled"
					onclick={handleDisabledAdvance}
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
		</div>
	{/if}
</div>

<!-- Issue 2 Fix: Back confirmation dialog -->
{#if showBackConfirmDialog}
	<div class="confirm-overlay" role="dialog" aria-modal="true">
		<div class="confirm-dialog">
			<h3 class="confirm-title">{$t("workflow.meeting.upload.backConfirm.title")}</h3>
			<p class="confirm-desc">{$t("workflow.meeting.upload.backConfirm.message")}</p>
			<div class="confirm-actions">
				<button class="confirm-btn confirm-cancel" onclick={cancelBackAction}>
					{$t("workflow.meeting.upload.backConfirm.continue")}
				</button>
				<button class="confirm-btn confirm-danger" onclick={confirmBackAction}>
					{$t("workflow.meeting.upload.backConfirm.confirm")}
				</button>
			</div>
		</div>
	</div>
{/if}

<style>
	.upload-and-configure {
		display: flex;
		flex-direction: column;
		align-items: center;
		width: 100%;
		max-width: 800px;
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

	/* Source Toggle Tabs */
	.source-tabs {
		display: flex;
		gap: 8px;
		width: 100%;
		margin-bottom: 12px;
	}

	.source-tab {
		flex: 1;
		display: flex;
		align-items: center;
		justify-content: center;
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

	.source-tab:hover {
		border-color: var(--slate-300, #cbd5e1);
		background: var(--slate-50, #f8fafc);
	}

	/* Task 4: Reduced tab highlighting intensity - subtler indicator */
	.source-tab.active {
		background: var(--blue-50, #eff6ff);
		border-color: var(--blue-500, #3b82f6);
		color: var(--blue-700, #1d4ed8);
	}

	.source-tab svg {
		width: 18px;
		height: 18px;
	}

	/* Microsoft Teams logo styling */
	.teams-logo {
		width: 16px;
		height: 16px;
	}

	.teams-logo-small {
		width: 20px;
		height: 20px;
	}

	/* Drop Zone */
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

	/* File Well */
	.file-well {
		width: 100%;
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

	/* Error Message */
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

	/* Config Section */
	.config-section {
		width: 100%;
		margin-top: 24px;
		display: flex;
		flex-direction: column;
		gap: 20px;
	}

	/* Section Header */
	.section-header {
		display: flex;
		align-items: center;
		gap: 8px;
		margin-bottom: 12px;
		font-size: 13px;
		font-weight: 600;
		color: var(--slate-700, #334155);
	}

	.section-header svg {
		width: 16px;
		height: 16px;
		color: var(--slate-400, #94a3b8);
	}

	.optional-badge {
		font-size: 11px;
		font-weight: 500;
		color: var(--slate-400, #94a3b8);
		background: var(--slate-100, #f1f5f9);
		padding: 2px 8px;
		border-radius: 4px;
		margin-left: auto;
	}

	/* Metadata Section */
	.metadata-section {
		background: var(--slate-50, #f8fafc);
		border: 1px solid var(--slate-200, #e2e8f0);
		border-radius: 10px;
		padding: 16px;
	}

	.metadata-grid {
		display: grid;
		grid-template-columns: repeat(2, 1fr);
		gap: 12px;
	}

	.metadata-grid.three-cols {
		grid-template-columns: repeat(3, 1fr);
	}

	/* Task 7 & 8: Custom metadata grid layout */
	.metadata-grid-custom {
		display: grid;
		grid-template-columns: 1fr 1fr;
		gap: 12px;
	}

	.metadata-grid-custom .metadata-field.full-width {
		grid-column: 1 / -1;
	}

	/* Issue 1 Fix: Equal width for Date and Language fields */
	.metadata-grid-custom .metadata-field {
		min-width: 0;
	}

	.metadata-field label {
		display: block;
		font-size: 12px;
		font-weight: 500;
		color: var(--slate-600, #475569);
		margin-bottom: 6px;
	}

	.metadata-field input,
	.metadata-field select {
		width: 100%;
		height: 42px;
		padding: 10px 12px;
		font-size: 14px;
		color: var(--slate-700, #334155);
		background: white;
		border: 1px solid var(--slate-200, #e2e8f0);
		border-radius: 8px;
		transition: all 0.15s ease;
		box-sizing: border-box;
	}

	.metadata-field select {
		cursor: pointer;
	}

	.metadata-field input::placeholder {
		color: var(--slate-400, #94a3b8);
	}

	.metadata-field input:hover,
	.metadata-field select:hover {
		border-color: var(--slate-300, #cbd5e1);
	}

	.metadata-field input:focus,
	.metadata-field select:focus {
		outline: none;
		border-color: var(--blue-500, #3b82f6);
		box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.1);
	}

	/* Destination Selection */
	.destination-section {
		background: var(--slate-50, #f8fafc);
		border: 1px solid var(--slate-200, #e2e8f0);
		border-radius: 10px;
		padding: 16px;
	}

	.personal-space-btn {
		display: flex;
		align-items: center;
		justify-content: center;
		gap: 10px;
		width: 100%;
		padding: 12px 16px;
		background: white;
		border: 1px solid var(--slate-200, #e2e8f0);
		border-radius: 8px;
		font-size: 14px;
		font-weight: 500;
		color: var(--slate-700, #334155);
		cursor: pointer;
		transition: all 0.15s ease;
	}

	.personal-space-btn:hover {
		border-color: var(--blue-300, #93c5fd);
		background: var(--blue-50, #eff6ff);
	}

	.personal-space-btn.selected {
		background: var(--blue-50, #eff6ff);
		border-color: var(--blue-500, #3b82f6);
		color: var(--blue-700, #1d4ed8);
	}

	.personal-space-btn svg {
		width: 18px;
		height: 18px;
	}

	.or-divider {
		display: flex;
		align-items: center;
		margin-bottom: 12px;
	}

	.or-divider::before,
	.or-divider::after {
		content: "";
		flex: 1;
		height: 1px;
		background: var(--slate-200, #e2e8f0);
	}

	.or-divider span {
		padding: 0 12px;
		font-size: 12px;
		color: var(--slate-400, #94a3b8);
		text-transform: uppercase;
		padding: 16px;
	}

	.destination-selector {
		display: flex;
		gap: 12px;
	}

	.dest-dropdown-container {
		flex: 1;
		position: relative;
	}

	.dest-dropdown-trigger {
		width: 100%;
		display: flex;
		align-items: center;
		gap: 10px;
		padding: 10px 12px;
		background: white;
		border: 1px solid var(--slate-300, #cbd5e1);
		border-radius: 8px;
		cursor: pointer;
		transition: all 0.15s;
		text-align: left;
	}

	.dest-dropdown-trigger:hover:not(:disabled) {
		border-color: var(--slate-400, #94a3b8);
	}

	.dest-dropdown-trigger.has-value {
		border-color: var(--blue-500, #3b82f6);
		background: var(--blue-50, #eff6ff);
	}

	.dest-dropdown-trigger.disabled {
		opacity: 0.5;
		cursor: not-allowed;
		background: var(--slate-100, #f1f5f9);
	}

	.dest-dropdown-icon {
		width: 16px;
		height: 16px;
		color: var(--slate-400, #94a3b8);
		flex-shrink: 0;
	}

	.dest-dropdown-icon.confluence-icon {
		color: var(--blue-500, #3b82f6);
	}

	.dest-dropdown-trigger.has-value .dest-dropdown-icon {
		color: var(--blue-600, #2563eb);
	}

	.dest-dropdown-text {
		flex: 1;
		font-size: 13px;
		color: var(--slate-600, #475569);
		white-space: nowrap;
		overflow: hidden;
		text-overflow: ellipsis;
	}

	.dest-dropdown-trigger.has-value .dest-dropdown-text {
		color: var(--slate-900, #0f172a);
		font-weight: 500;
	}

	.dest-dropdown-chevron {
		width: 14px;
		height: 14px;
		color: var(--slate-400, #94a3b8);
		flex-shrink: 0;
	}

	.dest-dropdown-menu {
		position: absolute;
		top: 100%;
		left: 0;
		right: 0;
		margin-top: 4px;
		background: white;
		border: 1px solid var(--slate-200, #e2e8f0);
		border-radius: 8px;
		box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
		z-index: 100;
		overflow: hidden;
	}

	.dest-dropdown-search {
		width: 100%;
		padding: 10px 12px;
		border: none;
		border-bottom: 1px solid var(--slate-100, #f1f5f9);
		font-size: 13px;
		outline: none;
	}

	.dest-dropdown-search::placeholder {
		color: var(--slate-400, #94a3b8);
	}

	.dest-dropdown-options {
		max-height: 160px;
		overflow-y: auto;
	}

	.dest-dropdown-option {
		width: 100%;
		padding: 10px 12px;
		text-align: left;
		background: none;
		border: none;
		font-size: 13px;
		color: var(--slate-700, #334155);
		cursor: pointer;
		transition: background 0.1s;
	}

	.dest-dropdown-option:hover {
		background: var(--slate-50, #f8fafc);
	}

	.dest-dropdown-option.selected {
		background: var(--blue-50, #eff6ff);
		color: var(--blue-700, #1d4ed8);
		font-weight: 500;
	}

	.dest-dropdown-empty {
		padding: 12px;
		font-size: 12px;
		color: var(--slate-400, #94a3b8);
		text-align: center;
	}

	.destination-path {
		display: flex;
		align-items: center;
		gap: 4px;
		font-size: 12px;
		color: var(--slate-500, #64748b);
		padding: 8px 10px;
		background: white;
		border-radius: 6px;
		margin-top: 10px;
	}

	.destination-path svg {
		width: 12px;
		height: 12px;
		color: var(--slate-400, #94a3b8);
	}

	/* Processing Options */
	.processing-options {
		background: var(--slate-50, #f8fafc);
		border: 1px solid var(--slate-200, #e2e8f0);
		border-radius: 10px;
		padding: 16px;
	}

	.options-row {
		display: flex;
		gap: 16px;
		flex-wrap: wrap;
	}

	.option-item {
		flex: 1;
		min-width: 140px;
	}

	.option-item label {
		display: block;
		font-size: 12px;
		font-weight: 500;
		color: var(--slate-600, #475569);
		margin-bottom: 6px;
	}

	.option-item select {
		width: 100%;
		padding: 8px 10px;
		font-size: 13px;
		color: var(--slate-600, #475569);
		background: var(--slate-50, #f8fafc);
		border: 1px solid var(--slate-200, #e2e8f0);
		border-radius: 6px;
		cursor: pointer;
		transition: all 0.15s ease;
	}

	.option-item select:hover {
		border-color: var(--slate-300, #cbd5e1);
	}

	.option-item select:focus {
		outline: none;
		border-color: var(--slate-300, #cbd5e1);
		box-shadow: none;
	}

	/* Toggle Item */
	.toggle-item {
		display: flex;
		flex-direction: column;
		gap: 6px;
	}

	.toggle-label {
		font-size: 12px;
		font-weight: 500;
		color: var(--slate-600, #475569);
	}

	.toggle-switch {
		position: relative;
		width: 44px;
		height: 24px;
		cursor: pointer;
	}

	.toggle-switch input {
		opacity: 0;
		width: 0;
		height: 0;
	}

	.toggle-slider {
		position: absolute;
		top: 0;
		left: 0;
		right: 0;
		bottom: 0;
		background: var(--slate-300, #cbd5e1);
		border-radius: 12px;
		transition: all 0.2s ease;
	}

	.toggle-slider::before {
		content: "";
		position: absolute;
		width: 18px;
		height: 18px;
		left: 3px;
		top: 3px;
		background: white;
		border-radius: 50%;
		transition: all 0.2s ease;
		box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
	}

	.toggle-switch input:checked + .toggle-slider {
		background: var(--blue-500, #3b82f6);
	}

	.toggle-switch input:checked + .toggle-slider::before {
		transform: translateX(20px);
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
		gap: 16px;
	}

	/* Secondary Button */
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

	/* Primary Button */
	.btn-primary {
		display: flex;
		align-items: center;
		justify-content: center;
		gap: 8px;
		padding: 12px 24px;
		font-size: 16px;
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

	.btn-primary.disabled {
		background: var(--slate-300, #cbd5e1);
		cursor: pointer;
	}

	.btn-primary.disabled:hover {
		background: var(--slate-400, #94a3b8);
	}

	/* Advance container with tooltip */
	.advance-container {
		position: relative;
	}

	.upload-tooltip {
		position: absolute;
		bottom: calc(100% + 8px);
		left: 50%;
		transform: translateX(-50%);
		background: var(--slate-900, #0f172a);
		color: white;
		padding: 8px 12px;
		border-radius: 6px;
		font-size: 13px;
		white-space: nowrap;
		z-index: 10;
	}

	.upload-tooltip::after {
		content: "";
		position: absolute;
		top: 100%;
		left: 50%;
		transform: translateX(-50%);
		border: 6px solid transparent;
		border-top-color: var(--slate-900, #0f172a);
	}

	.btn-primary svg {
		width: 16px;
		height: 16px;
	}

	/* Time Estimate */
	.time-estimate {
		display: flex;
		align-items: center;
		gap: 6px;
		font-size: 13px;
		color: var(--slate-500, #64748b);
	}

	.time-estimate svg {
		width: 14px;
		height: 14px;
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
		background: var(--deep-blue, #1e3a5f);
		border-color: var(--deep-blue, #1e3a5f);
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
		font-family:
			"SF Mono", "Monaco", "Inconsolata", "Roboto Mono", monospace;
		font-size: 13px;
		background: var(--slate-200, #e2e8f0);
		padding: 2px 6px;
		border-radius: 4px;
		color: var(--slate-700, #334155);
	}

	/* Responsive */
	@media (max-width: 600px) {
		.best-practices-grid {
			grid-template-columns: 1fr;
		}

		.metadata-grid,
		.metadata-grid.three-cols {
			grid-template-columns: 1fr;
		}

		.options-row {
			flex-direction: column;
		}

		.option-item {
			min-width: unset;
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
