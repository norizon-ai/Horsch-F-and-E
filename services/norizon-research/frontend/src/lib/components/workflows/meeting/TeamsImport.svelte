<script lang="ts">
	import { onMount } from "svelte";
	import { t } from "svelte-i18n";
	import { fade, slide } from "svelte/transition";
	import { WorkflowAPI, type TeamsMeeting } from "$lib/api/workflowApi";

	let {
		jobId = "",
		onImported = undefined,
		onCancel = undefined,
	}: {
		jobId?: string;
		onImported?: ((data: {
			fileName: string;
			fileSize: number;
			duration: number;
			meetingTitle: string;
			meetingDate: string;
		}) => void) | undefined;
		onCancel?: (() => void) | undefined;
	} = $props();

	type State =
		| "checking"
		| "not_configured"
		| "disconnected"
		| "connecting"
		| "loading"
		| "ready"
		| "importing"
		| "error";

	let connectionState: State = $state("checking");
	let meetings: TeamsMeeting[] = $state([]);
	let userName = $state("");
	let errorMessage = $state("");
	let importingMeetingId = $state("");

	onMount(async () => {
		await checkAuthStatus();
	});

	async function checkAuthStatus() {
		connectionState = "checking";
		try {
			const status = await WorkflowAPI.getTeamsAuthStatus();
			if (!status.configured) {
				connectionState = "not_configured";
			} else if (status.connected) {
				userName = status.userName || "";
				await loadMeetings();
			} else {
				connectionState = "disconnected";
			}
		} catch {
			connectionState = "disconnected";
		}
	}

	async function loadMeetings() {
		connectionState = "loading";
		try {
			const response = await WorkflowAPI.getTeamsMeetings();
			meetings = response.meetings;
			connectionState = "ready";
		} catch (e) {
			errorMessage = e instanceof Error ? e.message : "Unknown error";
			connectionState = "error";
		}
	}

	async function startOAuth() {
		connectionState = "connecting";
		try {
			const authUrl = await WorkflowAPI.getTeamsLoginUrl();

			const popup = window.open(
				authUrl,
				"ms-auth",
				"width=600,height=700,scrollbars=yes",
			);
			if (!popup) {
				errorMessage = $t("workflow.meeting.teams.popupBlocked");
				connectionState = "error";
				return;
			}

			// Listen for the postMessage from the popup
			const handler = async (event: MessageEvent) => {
				if (event.data?.type === "ms-auth") {
					window.removeEventListener("message", handler);
					if (event.data.status === "success") {
						await checkAuthStatus();
					} else {
						connectionState = "disconnected";
					}
				}
			};
			window.addEventListener("message", handler);

			// Fallback: check periodically in case postMessage fails
			const interval = setInterval(async () => {
				if (popup.closed) {
					clearInterval(interval);
					window.removeEventListener("message", handler);
					if (connectionState === "connecting") {
						await checkAuthStatus();
					}
				}
			}, 500);
		} catch (e) {
			errorMessage = e instanceof Error ? e.message : "Unknown error";
			connectionState = "error";
		}
	}

	async function disconnect() {
		await WorkflowAPI.disconnectTeams();
		userName = "";
		meetings = [];
		connectionState = "disconnected";
	}

	async function importRecording(meeting: TeamsMeeting) {
		if (!meeting.recordingId || !jobId) return;

		importingMeetingId = meeting.id;
		connectionState = "importing";
		try {
			const result = await WorkflowAPI.importTeamsRecording(
				jobId,
				meeting.meetingId || null,
				meeting.recordingId,
				meeting.subject,
				meeting.startDateTime,
			);

			if (result.success) {
				const meetingDate = meeting.startDateTime
					? new Date(meeting.startDateTime)
							.toISOString()
							.split("T")[0]
					: new Date().toISOString().split("T")[0];

				onImported?.({
					fileName: `${meeting.subject || "Teams Recording"}.mp4`,
					fileSize: result.file_size || 0,
					duration: result.duration_seconds,
					meetingTitle: meeting.subject || "",
					meetingDate,
				});
			}
		} catch (e) {
			errorMessage = e instanceof Error ? e.message : "Import failed";
			connectionState = "error";
		} finally {
			importingMeetingId = "";
		}
	}

	function formatMeetingTime(dateStr: string): string {
		if (!dateStr) return "";
		const date = new Date(dateStr);
		return date.toLocaleDateString(undefined, {
			weekday: "short",
			month: "short",
			day: "numeric",
			hour: "2-digit",
			minute: "2-digit",
		});
	}

	function formatDuration(startStr: string, endStr: string): string {
		if (!startStr || !endStr) return "";
		const start = new Date(startStr);
		const end = new Date(endStr);
		const mins = Math.round((end.getTime() - start.getTime()) / 60000);
		if (mins < 60) return `${mins} min`;
		const hours = Math.floor(mins / 60);
		const remaining = mins % 60;
		return remaining > 0 ? `${hours}h ${remaining}m` : `${hours}h`;
	}
</script>

<div class="teams-import">
	{#if connectionState === "checking"}
		<div class="teams-loading" in:fade={{ duration: 150 }}>
			<div class="spinner" />
		</div>
	{:else if connectionState === "not_configured"}
		<div class="teams-notice" in:fade={{ duration: 150 }}>
			<svg
				class="notice-icon"
				viewBox="0 0 24 24"
				fill="none"
				stroke="currentColor"
				stroke-width="2"
			>
				<circle cx="12" cy="12" r="10" />
				<line x1="12" y1="8" x2="12" y2="12" />
				<line x1="12" y1="16" x2="12.01" y2="16" />
			</svg>
			<span
				>Microsoft Teams integration is not configured for this
				instance.</span
			>
		</div>
	{:else if connectionState === "disconnected"}
		<div class="teams-connect" in:fade={{ duration: 150 }}>
			<button class="connect-btn" onclick={startOAuth}>
				<svg class="ms-icon" viewBox="0 0 24 24" fill="currentColor">
					<path
						d="M11.4 24H0V12.6h11.4V24zM24 24H12.6V12.6H24V24zM11.4 11.4H0V0h11.4v11.4zM24 11.4H12.6V0H24v11.4z"
					/>
				</svg>
				{$t("workflow.meeting.teams.connect")}
			</button>
			<p class="connect-description">
				{$t("workflow.meeting.teams.connectDescription")}
			</p>
		</div>
	{:else if connectionState === "connecting"}
		<div class="teams-loading" in:fade={{ duration: 150 }}>
			<div class="spinner" />
			<span>Signing in with Microsoft...</span>
		</div>
	{:else if connectionState === "loading"}
		<div class="teams-header" in:fade={{ duration: 150 }}>
			<span class="connected-label"
				>{$t("workflow.meeting.teams.connected", {
					values: { name: userName },
				})}</span
			>
			<button class="disconnect-btn" onclick={disconnect}
				>{$t("workflow.meeting.teams.disconnect")}</button
			>
		</div>
		<div class="teams-loading">
			<div class="spinner" />
			<span>{$t("workflow.meeting.teams.loadingMeetings")}</span>
		</div>
	{:else if connectionState === "ready"}
		<div class="teams-header" in:fade={{ duration: 150 }}>
			<span class="connected-label"
				>{$t("workflow.meeting.teams.connected", {
					values: { name: userName },
				})}</span
			>
			<button class="disconnect-btn" onclick={disconnect}
				>{$t("workflow.meeting.teams.disconnect")}</button
			>
		</div>
		{#if meetings.length === 0}
			<div class="teams-empty">
				<span>{$t("workflow.meeting.teams.noRecordings")}</span>
			</div>
		{:else}
			<div class="meetings-list" in:slide={{ duration: 200 }}>
				{#each meetings as meeting (meeting.id)}
					<div
						class="meeting-item"
						class:has-recording={meeting.hasRecording}
					>
						<div class="meeting-info">
							<span class="meeting-subject"
								>{meeting.subject}</span
							>
							<div class="meeting-meta">
								<span
									>{formatMeetingTime(
										meeting.startDateTime,
									)}</span
								>
								{#if meeting.startDateTime && meeting.endDateTime}
									<span class="meta-sep">·</span>
									<span
										>{formatDuration(
											meeting.startDateTime,
											meeting.endDateTime,
										)}</span
									>
								{/if}
								{#if meeting.attendeeCount > 0}
									<span class="meta-sep">·</span>
									<span
										>{$t(
											"workflow.meeting.teams.attendees",
											{
												values: {
													count: meeting.attendeeCount,
												},
											},
										)}</span
									>
								{/if}
							</div>
						</div>
						<div class="meeting-actions">
							{#if meeting.hasRecording && meeting.recordingId}
								<span class="recording-badge">
									<svg
										viewBox="0 0 24 24"
										fill="none"
										stroke="currentColor"
										stroke-width="2"
									>
										<circle cx="12" cy="12" r="10" />
										<circle
											cx="12"
											cy="12"
											r="3"
											fill="currentColor"
										/>
									</svg>
								</span>
								<button
									class="import-btn"
									disabled={importingMeetingId !== ""}
									onclick={() => importRecording(meeting)}
								>
									{$t("workflow.meeting.teams.import")}
								</button>
							{:else}
								<span class="no-recording">--</span>
							{/if}
						</div>
					</div>
				{/each}
			</div>
		{/if}
	{:else if connectionState === "importing"}
		<div class="teams-header">
			<span class="connected-label"
				>{$t("workflow.meeting.teams.connected", {
					values: { name: userName },
				})}</span
			>
		</div>
		<div class="teams-importing" in:fade={{ duration: 150 }}>
			<div class="spinner" />
			<span>{$t("workflow.meeting.teams.importing")}</span>
		</div>
	{:else if connectionState === "error"}
		<div class="teams-error-card" in:fade={{ duration: 150 }}>
			<div class="error-icon">
				<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
					<circle cx="12" cy="12" r="10" />
					<line x1="12" y1="8" x2="12" y2="12" />
					<line x1="12" y1="16" x2="12.01" y2="16" />
				</svg>
			</div>
			<p class="error-text">{errorMessage || $t("workflow.meeting.teams.error")}</p>
			<div class="error-actions">
				<button class="error-btn secondary" onclick={() => onCancel?.()}>
					{$t("common.cancel") ?? "Cancel"}
				</button>
				<button class="error-btn primary" onclick={() => { connectionState = "ready"; errorMessage = ""; }}>
					{$t("workflow.meeting.teams.tryAnother") ?? "Try another recording"}
				</button>
			</div>
		</div>
	{/if}
</div>

<style>
	.teams-import {
		width: 100%;
		display: flex;
		flex-direction: column;
		gap: 12px;
	}

	/* Header with connection status */
	.teams-header {
		display: flex;
		align-items: center;
		justify-content: space-between;
		padding: 10px 16px;
		background: var(--green-50, #f0fdf4);
		border: 1px solid var(--green-200, #bbf7d0);
		border-radius: 8px;
	}

	.connected-label {
		font-size: 13px;
		font-weight: 500;
		color: var(--green-700, #15803d);
	}

	.disconnect-btn {
		font-size: 12px;
		color: var(--slate-500, #64748b);
		background: none;
		border: none;
		cursor: pointer;
		text-decoration: underline;
		padding: 0;
	}

	.disconnect-btn:hover {
		color: var(--slate-700, #334155);
	}

	/* Connect button */
	.teams-connect {
		display: flex;
		flex-direction: column;
		align-items: center;
		gap: 12px;
		padding: 32px;
		background: white;
		border: 2px dashed var(--slate-300, #cbd5e1);
		border-radius: 12px;
	}

	.connect-btn {
		display: flex;
		align-items: center;
		gap: 10px;
		padding: 12px 24px;
		background: var(--slate-900, #0f172a);
		color: white;
		border: none;
		border-radius: 8px;
		font-size: 14px;
		font-weight: 500;
		cursor: pointer;
		transition: background 0.15s ease;
	}

	.connect-btn:hover {
		background: var(--slate-700, #334155);
	}

	.ms-icon {
		width: 18px;
		height: 18px;
	}

	.connect-description {
		font-size: 13px;
		color: var(--slate-500, #64748b);
		margin: 0;
	}

	/* Loading states */
	.teams-loading,
	.teams-importing {
		display: flex;
		align-items: center;
		justify-content: center;
		gap: 10px;
		padding: 32px;
		background: var(--slate-50, #f8fafc);
		border: 1px solid var(--slate-200, #e2e8f0);
		border-radius: 12px;
		font-size: 13px;
		color: var(--slate-500, #64748b);
	}

	.spinner {
		width: 18px;
		height: 18px;
		border: 2px solid var(--slate-200, #e2e8f0);
		border-top-color: var(--blue-500, #3b82f6);
		border-radius: 50%;
		animation: spin 0.6s linear infinite;
	}

	@keyframes spin {
		to {
			transform: rotate(360deg);
		}
	}

	/* Meetings list */
	.meetings-list {
		display: flex;
		flex-direction: column;
		border: 1px solid var(--slate-200, #e2e8f0);
		border-radius: 10px;
		overflow: hidden;
		max-height: 340px;
		overflow-y: auto;
	}

	.meeting-item {
		display: flex;
		align-items: center;
		justify-content: space-between;
		padding: 12px 16px;
		background: white;
		border-bottom: 1px solid var(--slate-100, #f1f5f9);
		transition: background 0.1s ease;
	}

	.meeting-item:last-child {
		border-bottom: none;
	}

	.meeting-item:hover {
		background: var(--slate-50, #f8fafc);
	}

	.meeting-info {
		flex: 1;
		min-width: 0;
	}

	.meeting-subject {
		display: block;
		font-size: 14px;
		font-weight: 500;
		color: var(--slate-900, #0f172a);
		white-space: nowrap;
		overflow: hidden;
		text-overflow: ellipsis;
	}

	.meeting-meta {
		display: flex;
		align-items: center;
		gap: 6px;
		font-size: 12px;
		color: var(--slate-500, #64748b);
		margin-top: 2px;
	}

	.meta-sep {
		color: var(--slate-300, #cbd5e1);
	}

	.meeting-actions {
		display: flex;
		align-items: center;
		gap: 8px;
		flex-shrink: 0;
		margin-left: 12px;
	}

	.recording-badge {
		display: flex;
		align-items: center;
		color: var(--red-500, #ef4444);
	}

	.recording-badge svg {
		width: 16px;
		height: 16px;
	}

	.import-btn {
		padding: 6px 14px;
		font-size: 13px;
		font-weight: 500;
		color: white;
		background: var(--blue-500, #3b82f6);
		border: none;
		border-radius: 6px;
		cursor: pointer;
		transition: background 0.15s ease;
	}

	.import-btn:hover:not(:disabled) {
		background: var(--blue-600, #2563eb);
	}

	.import-btn:disabled {
		opacity: 0.5;
		cursor: not-allowed;
	}

	.no-recording {
		font-size: 12px;
		color: var(--slate-400, #94a3b8);
	}

	/* Empty state */
	.teams-empty {
		padding: 32px;
		text-align: center;
		background: var(--slate-50, #f8fafc);
		border: 1px solid var(--slate-200, #e2e8f0);
		border-radius: 12px;
		font-size: 13px;
		color: var(--slate-500, #64748b);
	}

	/* Error state */
	.teams-error-card {
		display: flex;
		flex-direction: column;
		align-items: center;
		gap: 12px;
		padding: 24px;
		background: var(--red-50, #fef2f2);
		border: 1px solid var(--red-200, #fecaca);
		border-radius: 12px;
		text-align: center;
	}

	.error-icon {
		width: 40px;
		height: 40px;
		color: var(--red-500, #ef4444);
	}

	.error-icon svg {
		width: 100%;
		height: 100%;
	}

	.error-text {
		font-size: 14px;
		line-height: 1.5;
		color: var(--red-700, #b91c1c);
		margin: 0;
		max-width: 380px;
	}

	.error-actions {
		display: flex;
		gap: 10px;
		margin-top: 4px;
	}

	.error-btn {
		padding: 8px 18px;
		font-size: 13px;
		font-weight: 500;
		border-radius: 8px;
		cursor: pointer;
		transition: background 0.15s, border-color 0.15s;
	}

	.error-btn.secondary {
		color: var(--slate-600, #475569);
		background: white;
		border: 1px solid var(--slate-200, #e2e8f0);
	}

	.error-btn.secondary:hover {
		background: var(--slate-50, #f8fafc);
	}

	.error-btn.primary {
		color: white;
		background: var(--deep-blue, #1E3A5F);
		border: 1px solid var(--deep-blue, #1E3A5F);
	}

	.error-btn.primary:hover {
		background: var(--deep-blue-hover, #162d4a);
	}

	/* Notice state */
	.teams-notice {
		display: flex;
		align-items: center;
		gap: 8px;
		padding: 16px;
		background: var(--slate-50, #f8fafc);
		border: 1px solid var(--slate-200, #e2e8f0);
		border-radius: 8px;
		font-size: 13px;
		color: var(--slate-500, #64748b);
	}

	.notice-icon {
		width: 18px;
		height: 18px;
		flex-shrink: 0;
		color: var(--slate-400, #94a3b8);
	}
</style>
