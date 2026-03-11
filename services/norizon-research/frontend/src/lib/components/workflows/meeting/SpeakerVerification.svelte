<script lang="ts">
	import { t } from "svelte-i18n";
	import { get } from "svelte/store";
	import {
		workflowStore,
		currentWorkflowId,
	} from "$lib/stores/workflowStore";
	import { formatDuration, WorkflowAPI } from "$lib/api/workflowApi";
	import type { Speaker, WorkflowFile, UserSuggestion } from "$lib/types";

	let {
		speakers = [],
		file = null,
		onconfirmed = undefined,
		onback = undefined,
	}: {
		speakers?: Speaker[];
		file?: WorkflowFile | null;
		onconfirmed?: (() => void) | undefined;
		onback?: (() => void) | undefined;
	} = $props();

	// Local state for editing
	let editingSpeaker: string | null = $state(null);
	let editValue = $state("");

	// Task 14 & 15: Track confirmed speakers
	let confirmedSpeakers = $state(new Set<string>());
	let showValidationError = $state(false);

	// Task 16: Back button confirmation dialog
	let showBackConfirmation = $state(false);

	// ISSUE 3: Delete speaker confirmation dialog
	let showDeleteDialog: string | null = $state(null);

	function handleBackClick() {
		showBackConfirmation = true;
	}

	function confirmBack() {
		showBackConfirmation = false;
		onback?.();
	}

	function cancelBack() {
		showBackConfirmation = false;
	}

	// Audio playback state
	let playingSpeakerId: string | null = $state(null);
	let audioElement: HTMLAudioElement = $state(undefined as unknown as HTMLAudioElement);

	// Autocomplete state
	let userSuggestions: UserSuggestion[] = $state([]);
	let isLoadingSuggestions = $state(false);
	let showSuggestions = $state(false);
	let searchDebounceTimer: ReturnType<typeof setTimeout> | null = null;

	// Confidence threshold - only show AI-proposed name if above this
	// Aligned with backend LLM threshold (≥70 = unambiguous evidence)
	const HIGH_CONFIDENCE_THRESHOLD = 70;

	function handleAudioEnded() {
		playingSpeakerId = null;
	}

	function toggleAudio(speakerId: string, audioUrl?: string) {
		if (!audioElement) return;

		if (playingSpeakerId === speakerId) {
			audioElement.pause();
			playingSpeakerId = null;
		} else {
			// Stop previous if playing
			audioElement.pause();

			playingSpeakerId = speakerId;

			if (!audioUrl) return;

			// Resolve relative URLs to the backend API where the /data mount is hosted
			let finalUrl: string = audioUrl;
			if (audioUrl.startsWith("/data")) {
				const baseUrl =
					import.meta.env.VITE_WORKFLOW_API_URL ||
					"http://localhost:8001";
				finalUrl = `${baseUrl}${audioUrl}`;
			}

			audioElement.src = finalUrl;
			audioElement.play().catch((e) => {
				console.error("Audio play failed:", e);
				playingSpeakerId = null;
			});
		}
	}

	function startEdit(speaker: Speaker) {
		editingSpeaker = speaker.id;
		editValue = speaker.confirmedName || speaker.detectedName;
	}

	function saveEdit(speakerId: string) {
		if (editValue.trim()) {
			workflowStore.updateSpeakerName(speakerId, editValue.trim());
			// BUG 4 FIX: Auto-confirm when name is changed from "Unknown Speaker"
			const speaker = speakers.find((s) => s.id === speakerId);
			const unknownLabel =
				$t("workflow.meeting.speakers.unknownSpeaker") ||
				"Unknown Speaker";
			if (
				speaker &&
				editValue.trim() !== unknownLabel &&
				editValue.trim() !== speaker.detectedName
			) {
				confirmedSpeakers = new Set(confirmedSpeakers).add(speakerId);
			}
		}
		editingSpeaker = null;
		editValue = "";
	}

	function cancelEdit() {
		editingSpeaker = null;
		editValue = "";
	}

	function handleKeydown(e: KeyboardEvent, speakerId: string) {
		if (e.key === "Enter") {
			saveEdit(speakerId);
		} else if (e.key === "Escape") {
			cancelEdit();
		}
	}

	function getDisplayName(speaker: Speaker): string {
		// If user confirmed a name, use that
		if (speaker.confirmedName) return speaker.confirmedName;
		// Only show AI-detected name if confidence is high
		const confidence = speaker.confidence ?? 0;
		if (confidence >= HIGH_CONFIDENCE_THRESHOLD && speaker.detectedName) {
			return speaker.detectedName;
		}
		// Otherwise show generic label
		return (
			$t("workflow.meeting.speakers.unknownSpeaker") || "Unknown Speaker"
		);
	}

	function needsReview(speaker: Speaker): boolean {
		// Needs review if no confirmed name and confidence is low
		return (
			!speaker.confirmedName &&
			(speaker.confidence ?? 0) < HIGH_CONFIDENCE_THRESHOLD
		);
	}

	function toggleExternal(speakerId: string) {
		workflowStore.toggleSpeakerExternal(speakerId);
	}

	// Debounced user search for autocomplete
	async function searchUsers(query: string) {
		if (searchDebounceTimer) {
			clearTimeout(searchDebounceTimer);
		}

		if (query.length < 2) {
			userSuggestions = [];
			showSuggestions = false;
			return;
		}

		searchDebounceTimer = setTimeout(async () => {
			isLoadingSuggestions = true;
			try {
				const response = await WorkflowAPI.searchUsers(query);
				userSuggestions = response.users;
				showSuggestions = userSuggestions.length > 0;
			} catch (error) {
				console.error("Failed to search users:", error);
				userSuggestions = [];
			} finally {
				isLoadingSuggestions = false;
			}
		}, 200);
	}

	function selectUserSuggestion(
		speakerId: string,
		suggestion: UserSuggestion,
	) {
		workflowStore.updateSpeakerName(speakerId, suggestion.name);
		editingSpeaker = null;
		editValue = "";
		userSuggestions = [];
		showSuggestions = false;
	}

	function handleNameInput(e: Event) {
		const input = e.target as HTMLInputElement;
		editValue = input.value;
		searchUsers(editValue);
	}

	// Task 14: Toggle speaker confirmation
	// Issue 6 Fix: Ensure reactivity by creating new Set
	function toggleSpeakerConfirmation(speakerId: string) {
		const newSet = new Set(confirmedSpeakers);
		if (newSet.has(speakerId)) {
			newSet.delete(speakerId);
		} else {
			newSet.add(speakerId);
		}
		confirmedSpeakers = newSet; // trigger reactivity with new Set
		showValidationError = false;
	}

	// Task 15: Validate all speakers confirmed before proceeding
	async function handleConfirm() {
		// Check if all speakers are confirmed
		const allConfirmed = speakers.every((s) => confirmedSpeakers.has(s.id));

		if (!allConfirmed) {
			showValidationError = true;
			// Scroll to first unconfirmed speaker
			const firstUnconfirmed = speakers.find(
				(s) => !confirmedSpeakers.has(s.id),
			);
			if (firstUnconfirmed) {
				const element = document.getElementById(
					`speaker-${firstUnconfirmed.id}`,
				);
				element?.scrollIntoView({
					behavior: "smooth",
					block: "center",
				});
			}
			return;
		}

		// Ensure all speakers have a confirmedName (use detectedName as fallback)
		speakers.forEach((s) => {
			if (!s.confirmedName) {
				workflowStore.updateSpeakerName(s.id, s.detectedName);
			}
		});

		// CRITICAL FIX: Send updated speakers to backend before proceeding
		// Task 3 Fix: Use get(currentWorkflowId) instead of non-existent method
		const jobId = get(currentWorkflowId);
		if (jobId) {
			try {
				await WorkflowAPI.updateSpeakers(jobId, speakers);
				console.log(
					"✅ Speakers successfully sent to backend:",
					speakers,
				);
			} catch (error) {
				console.error(
					"❌ Failed to update speakers on backend:",
					error,
				);
				// Show error to user but don't block progression
				// TODO: Add user-facing error message
			}
		}

		onconfirmed?.();
	}

	// ISSUE 3: Confirm deletion of speaker
	function confirmDeleteSpeaker(speakerId: string | null) {
		if (!speakerId) return;
		speakers = speakers.filter((s) => s.id !== speakerId);
		workflowStore.setSpeakers(speakers);
		confirmedSpeakers = new Set(
			Array.from(confirmedSpeakers).filter((id) => id !== speakerId),
		);
		showDeleteDialog = null;
	}

	function cancelDeleteSpeaker() {
		showDeleteDialog = null;
	}

	// Get card class based on state
	function getCardClass(speaker: Speaker): string {
		const classes = ["speaker-card"];
		if (speaker.confirmedName) classes.push("confirmed");
		else if (needsReview(speaker)) classes.push("needs-review");
		return classes.join(" ");
	}

	// Calculate total duration from file or speakers
	let totalDuration = $derived(
		file?.duration ||
		speakers.reduce((sum, s) => sum + (s.speakingTime || 0), 0)
	);
	let confirmedCount = $derived(speakers.filter(
		(s) => s.confirmedName && s.confirmedName.trim() !== "",
	).length);
	let meetingTitle = $derived(
		file?.name?.replace(/\.[^/.]+$/, "").replace(/[-_]/g, " ") ||
		"Meeting Recording"
	);
</script>

<div class="speaker-verification">
	<!-- Meeting context header -->
	<div class="context-header">
		<div class="context-info">
			<svg
				viewBox="0 0 24 24"
				fill="none"
				stroke="currentColor"
				stroke-width="2"
			>
				<path
					d="M14.5 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V7.5L14.5 2z"
				/>
				<polyline points="14 2 14 8 20 8" />
			</svg>
			<span class="context-title">{meetingTitle}</span>
			<span class="context-divider">·</span>
			<span class="context-duration">{formatDuration(totalDuration)}</span
			>
		</div>
	</div>

	<!-- Speaker list header with count -->
	<div class="speakers-header">
		<span class="speaker-count">
			{$t("workflow.meeting.speakers.speakersConfirmed", {
				values: {
					confirmed: confirmedSpeakers.size,
					total: speakers.length,
				},
			})}
		</span>
		{#if showValidationError}
			<span class="validation-error"
				>Please confirm all speakers to continue</span
			>
		{/if}
	</div>

	<!-- Compact speaker cards -->
	<div class="speakers-list">
		{#each speakers as speaker (speaker.id)}
			<div
				id="speaker-{speaker.id}"
				class={getCardClass(speaker)}
				class:speaker-confirmed={confirmedSpeakers.has(speaker.id)}
				class:speaker-error={showValidationError &&
					!confirmedSpeakers.has(speaker.id)}
			>
				<!-- Issue 4 Fix: Removed waveform visualization completely - keep only speaker name at top -->

				<!-- Main content -->
				<div class="speaker-content">
					<!-- Row 1: Name + all badges inline -->
					<div class="speaker-row-main">
						{#if editingSpeaker === speaker.id}
							<div class="name-edit-container">
								<input
									type="text"
									class="name-input"
									bind:value={editValue}
									onkeydown={(e) =>
										handleKeydown(e, speaker.id)}
									onblur={() => {
										setTimeout(
											() => saveEdit(speaker.id),
											150,
										);
									}}
									oninput={handleNameInput}
									autofocus
								/>
								{#if showSuggestions && userSuggestions.length > 0}
									<div class="suggestions-dropdown">
										{#each userSuggestions as suggestion}
											<button
												class="suggestion-item"
												onmousedown={(e) => {
													e.preventDefault();
													selectUserSuggestion(
														speaker.id,
														suggestion,
													);
												}}
											>
												<svg
													viewBox="0 0 24 24"
													fill="none"
													stroke="currentColor"
													stroke-width="2"
												>
													<path
														d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"
													/>
													<circle
														cx="12"
														cy="7"
														r="4"
													/>
												</svg>
												<div class="suggestion-info">
													<span
														class="suggestion-name"
														>{suggestion.name}</span
													>
													{#if suggestion.department}
														<span
															class="suggestion-dept"
															>({suggestion.department})</span
														>
													{/if}
												</div>
											</button>
										{/each}
									</div>
								{/if}
								{#if isLoadingSuggestions}
									<div class="suggestions-loading">
										<div class="spinner-small"></div>
									</div>
								{/if}
							</div>
						{:else}
							<button
								class="name-display"
								onclick={() => startEdit(speaker)}
							>
								<span class="name"
									>{getDisplayName(speaker)}</span
								>
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
							</button>
						{/if}

						<!-- Inline badges -->
						<div class="inline-badges">
							{#if speaker.speakingTime}
								<span class="badge time-badge">
									<svg
										viewBox="0 0 24 24"
										fill="none"
										stroke="currentColor"
										stroke-width="2"
									>
										<circle cx="12" cy="12" r="10" />
										<polyline points="12 6 12 12 16 14" />
									</svg>
									{formatDuration(speaker.speakingTime)}
								</span>
							{/if}
							<!-- ISSUE 2 FIX: Auto-translate AI-generated hints when language switches -->
							{#if speaker.hint && needsReview(speaker)}
								<span class="badge hint-badge"
									>{$t(
										`workflow.meeting.speakers.roles.${speaker.hint.toLowerCase()}`,
										{ default: speaker.hint },
									)}</span
								>
							{/if}
							<!-- Task 14: Add Confirm button to each card -->
							<!-- Issue 5 Fix: Added i18n for Confirm/Confirmed button -->
							<button
								class="confirm-speaker-btn"
								class:confirmed={confirmedSpeakers.has(
									speaker.id,
								)}
								onclick={() =>
									toggleSpeakerConfirmation(speaker.id)}
							>
								{#if confirmedSpeakers.has(speaker.id)}
									<svg
										viewBox="0 0 24 24"
										fill="none"
										stroke="currentColor"
										stroke-width="2.5"
									>
										<polyline points="20 6 9 17 4 12" />
									</svg>
									{$t("workflow.meeting.speakers.confirmed")}
								{:else}
									{$t("workflow.meeting.speakers.confirm")}
								{/if}
							</button>
							<!-- ISSUE 3 FIX: Add delete button (bin icon) to each speaker card -->
							<button
								class="delete-speaker-btn"
								onclick={() => (showDeleteDialog = speaker.id)}
								title={$t("common.delete")}
							>
								<svg
									viewBox="0 0 24 24"
									fill="none"
									stroke="currentColor"
									stroke-width="2"
								>
									<polyline points="3 6 5 6 21 6" />
									<path
										d="M19 6v14a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2V6m3 0V4a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2"
									/>
								</svg>
							</button>
						</div>
					</div>

					<!-- External toggle for unknown speakers -->
					{#if needsReview(speaker)}
						<button
							class="external-toggle"
							class:active={speaker.isExternal}
							onclick={() => toggleExternal(speaker.id)}
						>
							<svg
								viewBox="0 0 24 24"
								fill="none"
								stroke="currentColor"
								stroke-width="2"
							>
								<path
									d="M16 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"
								/>
								<circle cx="8.5" cy="7" r="4" />
								<line x1="20" y1="8" x2="20" y2="14" />
								<line x1="23" y1="11" x2="17" y2="11" />
							</svg>
							{$t("workflow.meeting.speakers.markExternal")}
						</button>
					{/if}

					<!-- Row 2: Transcript snippet (compact) -->
					{#if speaker.transcriptSnippet}
						<p class="transcript-snippet">
							"{speaker.transcriptSnippet}"
						</p>
					{/if}

					<!-- Row 3: Audio sample -->
					{#if speaker.sampleAudioUrl}
						<div class="audio-player">
							<button
								class="play-btn"
								class:playing={playingSpeakerId === speaker.id}
								onclick={() =>
									toggleAudio(
										speaker.id,
										speaker.sampleAudioUrl,
									)}
								aria-label={playingSpeakerId === speaker.id
									? "Pause"
									: "Play"}
							>
								{#if playingSpeakerId === speaker.id}
									<svg
										viewBox="0 0 24 24"
										fill="currentColor"
									>
										<rect
											x="6"
											y="4"
											width="4"
											height="16"
											rx="1"
										/>
										<rect
											x="14"
											y="4"
											width="4"
											height="16"
											rx="1"
										/>
									</svg>
								{:else}
									<svg
										viewBox="0 0 24 24"
										fill="currentColor"
									>
										<polygon points="5 3 19 12 5 21 5 3" />
									</svg>
								{/if}
							</button>
							<div class="audio-progress">
								<div class="audio-bars">
									<!-- Issue 4 Fix: Randomize waveform bars for each speaker -->
									{#each Array.from( { length: 16 }, () => Math.floor(Math.random() * 50 + 30), ) as height, i}
										<div
											class="bar"
											class:played={playingSpeakerId ===
												speaker.id && i < 8}
											style="height: {height}%"
										></div>
									{/each}
								</div>
								<span class="audio-duration">0:05</span>
							</div>
						</div>
					{/if}
				</div>
			</div>
		{/each}
	</div>

	<!-- Hidden audio element for playback -->
	<audio
		bind:this={audioElement}
		onended={handleAudioEnded}
		style="display: none;"
	></audio>

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
		<button class="btn-primary" onclick={handleConfirm}>
			{$t("workflow.meeting.speakers.confirmButton")}
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

<!-- Task 16: Back confirmation dialog -->
{#if showBackConfirmation}
	<div class="confirm-overlay" role="dialog" aria-modal="true">
		<div class="confirm-dialog">
			<h3 class="confirm-title">Go back?</h3>
			<p class="confirm-desc">Speaker verification progress will be lost and you will need to start over.</p>
			<div class="confirm-actions">
				<button class="confirm-btn confirm-cancel" onclick={cancelBack}>
					Cancel
				</button>
				<button class="confirm-btn confirm-danger" onclick={confirmBack}>
					Go back
				</button>
			</div>
		</div>
	</div>
{/if}

<!-- ISSUE 3: Delete speaker confirmation dialog -->
{#if showDeleteDialog}
	<div class="confirm-overlay" role="dialog" aria-modal="true">
		<div class="confirm-dialog">
			<h3 class="confirm-title">Remove speaker?</h3>
			<p class="confirm-desc">This speaker will be removed from the list. This action cannot be undone.</p>
			<div class="confirm-actions">
				<button class="confirm-btn confirm-cancel" onclick={cancelDeleteSpeaker}>
					Cancel
				</button>
				<button class="confirm-btn confirm-danger" onclick={() => confirmDeleteSpeaker(showDeleteDialog)}>
					Remove
				</button>
			</div>
		</div>
	</div>
{/if}

<style>
	.speaker-verification {
		display: flex;
		flex-direction: column;
		width: 100%;
		max-width: 800px;
		gap: 12px;
	}

	/* Context header */
	.context-header {
		display: flex;
		align-items: center;
		justify-content: space-between;
		gap: 16px;
		padding: 12px 16px;
		background: var(--slate-50, #f8fafc);
		border: 1px solid var(--slate-200, #e2e8f0);
		border-radius: 8px;
	}

	.context-info {
		display: flex;
		align-items: center;
		gap: 8px;
		font-size: 15px;
		color: var(--slate-600, #475569);
	}

	.context-info svg {
		width: 16px;
		height: 16px;
		color: var(--slate-400, #94a3b8);
	}

	.context-title {
		font-weight: 600;
		color: var(--slate-800, #1e293b);
		max-width: 300px;
		overflow: hidden;
		text-overflow: ellipsis;
		white-space: nowrap;
	}

	.context-divider {
		color: var(--slate-300, #cbd5e1);
	}

	.context-duration {
		font-variant-numeric: tabular-nums;
	}

	/* Speakers list header */
	.speakers-header {
		display: flex;
		align-items: center;
		justify-content: space-between;
		padding: 10px 14px;
		background: var(--slate-50, #f8fafc);
		border: 1px solid var(--slate-200, #e2e8f0);
		border-radius: 8px 8px 0 0;
		border-bottom: none;
	}

	.speaker-count {
		font-size: 15px;
		font-weight: 500;
		color: var(--slate-600, #475569);
	}

	.confirmed-progress {
		font-size: 13px;
		font-weight: 600;
		color: var(--green-600, #16a34a);
		font-variant-numeric: tabular-nums;
		margin-left: 4px;
	}

	/* Compact speaker cards */
	.speakers-list {
		display: flex;
		flex-direction: column;
		border: 1px solid var(--slate-200, #e2e8f0);
		border-radius: 0 0 8px 8px;
		overflow: hidden;
	}

	.speaker-card {
		display: flex;
		flex-direction: column;
		gap: 12px;
		padding: 12px;
		background: white;
		border-bottom: 1px solid var(--slate-100, #f1f5f9);
		transition: all 0.15s ease;
	}

	.speaker-card:last-child {
		border-bottom: none;
	}

	.speaker-card:hover {
		background: var(--slate-50, #f8fafc);
	}

	.speaker-card.confirmed {
		background: linear-gradient(
			to right,
			var(--green-50, #f0fdf4) 0%,
			white 30%
		);
		border-left: 3px solid var(--green-400, #4ade80);
		padding-left: 9px;
	}

	/* Task 14: Confirmed speaker styling */
	.speaker-card.speaker-confirmed {
		background: linear-gradient(
			to right,
			var(--green-50, #f0fdf4) 0%,
			white 30%
		);
		border-left: 3px solid var(--green-500, #22c55e);
		padding-left: 9px;
	}

	.speaker-card.needs-review {
		background: linear-gradient(
			to right,
			var(--amber-50, #fffbeb) 0%,
			white 30%
		);
		border-left: 3px solid var(--amber-400, #fbbf24);
		padding-left: 9px;
	}

	/* Issue 7 Fix: Highlight unconfirmed speakers on error */
	.speaker-card.speaker-error {
		border: 2px solid var(--red-400, #f87171);
		border-left-width: 3px;
		animation: shake 0.5s ease-in-out;
	}

	@keyframes shake {
		0%,
		100% {
			transform: translateX(0);
		}
		10%,
		30%,
		50%,
		70%,
		90% {
			transform: translateX(-5px);
		}
		20%,
		40%,
		60%,
		80% {
			transform: translateX(5px);
		}
	}

	/* Issue 4 Fix: Removed waveform container - no longer needed */

	/* Speaker content */
	.speaker-content {
		flex: 1;
		min-width: 0;
		display: flex;
		flex-direction: column;
		gap: 6px;
	}

	/* Main row: name + badges */
	.speaker-row-main {
		display: flex;
		align-items: center;
		gap: 8px;
		flex-wrap: wrap;
	}

	.name-display {
		display: flex;
		align-items: center;
		gap: 4px;
		background: transparent;
		border: none;
		cursor: pointer;
		padding: 2px 4px;
		margin: -2px -4px;
		border-radius: 4px;
		transition: background 0.15s ease;
	}

	.name-display:hover {
		background: var(--slate-100, #f1f5f9);
	}

	.name-display .name {
		font-size: 16px;
		font-weight: 600;
		color: var(--slate-900, #0f172a);
	}

	.name-display svg {
		width: 12px;
		height: 12px;
		color: var(--slate-400, #94a3b8);
		transition: color 0.15s ease;
	}

	.name-display:hover svg {
		color: var(--blue-500, #3b82f6);
	}

	.name-input {
		font-size: 16px;
		font-weight: 600;
		color: var(--slate-900, #0f172a);
		border: 1px solid var(--blue-400, #60a5fa);
		border-radius: 4px;
		padding: 2px 6px;
		outline: none;
		box-shadow: 0 0 0 2px var(--blue-100, #dbeafe);
	}

	/* Inline badges */
	.inline-badges {
		display: flex;
		align-items: center;
		gap: 6px;
		margin-left: auto;
	}

	.badge {
		display: flex;
		align-items: center;
		gap: 3px;
		font-size: 11px;
		font-weight: 500;
		padding: 2px 6px;
		border-radius: 4px;
	}

	.badge svg {
		width: 10px;
		height: 10px;
	}

	.time-badge {
		background: var(--slate-100, #f1f5f9);
		color: var(--slate-500, #64748b);
	}

	.confirmed-badge {
		background: var(--green-100, #dcfce7);
		color: var(--green-600, #16a34a);
		padding: 3px;
	}

	.external-badge {
		background: var(--purple-100, #f3e8ff);
		color: var(--purple-700, #7e22ce);
	}

	.hint-badge {
		background: var(--orange-50, #fff7ed);
		color: var(--orange-500, #f97316);
		font-weight: 600;
	}

	/* External toggle button */
	.external-toggle {
		display: flex;
		align-items: center;
		gap: 6px;
		padding: 6px 10px;
		background: var(--slate-50, #f8fafc);
		border: 1px solid var(--slate-200, #e2e8f0);
		border-radius: 6px;
		font-size: 12px;
		font-weight: 500;
		color: var(--slate-600, #475569);
		cursor: pointer;
		transition: all 0.15s ease;
		margin-top: 4px;
	}

	.external-toggle:hover {
		background: var(--purple-50, #faf5ff);
		border-color: var(--purple-200, #e9d5ff);
		color: var(--purple-700, #7e22ce);
	}

	.external-toggle.active {
		background: var(--purple-100, #f3e8ff);
		border-color: var(--purple-300, #d8b4fe);
		color: var(--purple-700, #7e22ce);
	}

	.external-toggle svg {
		width: 14px;
		height: 14px;
	}

	/* Name edit container for autocomplete */
	.name-edit-container {
		position: relative;
		flex: 1;
	}

	.suggestions-dropdown {
		position: absolute;
		top: 100%;
		left: 0;
		right: 0;
		margin-top: 4px;
		background: white;
		border: 1px solid var(--slate-200, #e2e8f0);
		border-radius: 8px;
		box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
		z-index: 50;
		max-height: 200px;
		overflow-y: auto;
	}

	.suggestion-item {
		display: flex;
		align-items: center;
		gap: 10px;
		width: 100%;
		padding: 10px 12px;
		background: transparent;
		border: none;
		text-align: left;
		cursor: pointer;
		transition: background 0.1s ease;
	}

	.suggestion-item:hover {
		background: var(--slate-50, #f8fafc);
	}

	.suggestion-item svg {
		width: 18px;
		height: 18px;
		color: var(--slate-400, #94a3b8);
		flex-shrink: 0;
	}

	.suggestion-info {
		flex: 1;
		min-width: 0;
	}

	.suggestion-name {
		font-size: 14px;
		font-weight: 500;
		color: var(--slate-900, #0f172a);
	}

	.suggestion-dept {
		font-size: 12px;
		color: var(--slate-500, #64748b);
		margin-left: 4px;
	}

	.suggestions-loading {
		position: absolute;
		top: 100%;
		left: 0;
		right: 0;
		margin-top: 4px;
		padding: 12px;
		background: white;
		border: 1px solid var(--slate-200, #e2e8f0);
		border-radius: 8px;
		display: flex;
		justify-content: center;
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
		to {
			transform: rotate(360deg);
		}
	}

	/* Transcript snippet - compact */
	.transcript-snippet {
		font-size: 14px;
		color: var(--slate-500, #64748b);
		line-height: 1.4;
		margin: 0;
		font-style: italic;
		overflow: hidden;
		text-overflow: ellipsis;
		white-space: nowrap;
	}

	/* Audio player */
	.audio-player {
		display: flex;
		align-items: center;
		gap: 10px;
		padding: 8px 12px;
		background: var(--slate-50, #f8fafc);
		border-radius: 6px;
	}

	.play-btn {
		width: 32px;
		height: 32px;
		display: flex;
		align-items: center;
		justify-content: center;
		background: var(--blue-500, #3b82f6);
		color: white;
		border: none;
		border-radius: 50%;
		cursor: pointer;
		transition: all 0.15s ease;
		flex-shrink: 0;
	}

	.play-btn:hover {
		background: var(--blue-600, #2563eb);
		transform: scale(1.05);
	}

	.play-btn.playing {
		background: var(--slate-600, #475569);
	}

	.play-btn svg {
		width: 14px;
		height: 14px;
	}

	.play-btn:not(.playing) svg {
		margin-left: 2px;
	}

	.audio-progress {
		flex: 1;
		display: flex;
		align-items: center;
		gap: 8px;
	}

	.audio-bars {
		flex: 1;
		display: flex;
		align-items: center;
		gap: 2px;
		height: 24px;
	}

	.audio-bars .bar {
		flex: 1;
		background: var(--slate-300, #cbd5e1);
		border-radius: 2px;
		min-width: 3px;
		transition: background 0.15s ease;
	}

	.audio-bars .bar.played {
		background: var(--blue-400, #60a5fa);
	}

	.audio-duration {
		font-size: 11px;
		font-weight: 500;
		color: var(--slate-500, #64748b);
		font-variant-numeric: tabular-nums;
		white-space: nowrap;
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

	.btn-primary:hover {
		background: var(--blue-600, #2563eb);
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

	/* Task 14: Confirm speaker button */
	.confirm-speaker-btn {
		display: flex;
		align-items: center;
		gap: 4px;
		padding: 6px 12px;
		background: white;
		border: 1px solid var(--slate-300, #cbd5e1);
		border-radius: 6px;
		font-size: 14px;
		font-weight: 500;
		color: var(--slate-600, #475569);
		cursor: pointer;
		transition: all 0.15s ease;
	}

	.confirm-speaker-btn:hover {
		background: var(--green-50, #f0fdf4);
		border-color: var(--green-400, #4ade80);
		color: var(--green-700, #15803d);
	}

	.confirm-speaker-btn.confirmed {
		background: var(--green-500, #22c55e);
		border-color: var(--green-500, #22c55e);
		color: white;
	}

	.confirm-speaker-btn svg {
		width: 12px;
		height: 12px;
	}

	/* ISSUE 3: Delete speaker button */
	.delete-speaker-btn {
		display: flex;
		align-items: center;
		justify-content: center;
		gap: 4px;
		padding: 4px 6px;
		background: transparent;
		border: 1px solid var(--red-200, #fecaca);
		border-radius: 6px;
		font-size: 12px;
		color: var(--red-500, #ef4444);
		cursor: pointer;
		transition: all 0.15s ease;
	}

	.delete-speaker-btn:hover {
		background: var(--red-50, #fef2f2);
		border-color: var(--red-400, #f87171);
		color: var(--red-600, #dc2626);
	}

	.delete-speaker-btn svg {
		width: 14px;
		height: 14px;
	}

	/* Task 15: Validation error */
	.validation-error {
		font-size: 12px;
		color: var(--red-600, #dc2626);
		font-weight: 500;
		padding: 4px 8px;
		background: var(--red-50, #fef2f2);
		border-radius: 4px;
		margin-left: auto;
	}

	/* Confirmation dialogs */
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

	@media (max-width: 600px) {
		.context-header {
			flex-direction: column;
			align-items: flex-start;
			gap: 10px;
		}

		.speakers-header {
			flex-direction: column;
			align-items: flex-start;
			gap: 10px;
		}

		.speaker-card {
			flex-direction: column;
		}

		.waveform-container {
			width: 100%;
			height: 40px;
		}

		.speaker-row-main {
			flex-direction: column;
			align-items: flex-start;
		}

		.inline-badges {
			margin-left: 0;
			flex-wrap: wrap;
		}

		.workflow-footer {
			flex-direction: column-reverse;
		}
	}
</style>
