<script lang="ts">
	import { onMount, createEventDispatcher } from "svelte";
	import { t } from "svelte-i18n";
	import type { PostAction } from "$lib/types";

	export let confluenceUrl: string | undefined = undefined;
	export let onActionSelected: ((action: PostAction) => void) | undefined =
		undefined;
	export let onComplete: (() => void) | undefined = undefined;

	const dispatch = createEventDispatcher();

	let showContent = false;
	let showMoreActions = false;

	onMount(() => {
		// Animate content appearance after checkmark
		setTimeout(() => {
			showContent = true;
		}, 600);
	});

	// Primary actions (shown by default)
	const primaryActions: {
		id: PostAction;
		icon: string;
		labelKey: string;
		descKey: string;
	}[] = [
		{
			id: "email",
			icon: "mail",
			labelKey: "workflow.meeting.success.actions.email.label",
			descKey: "workflow.meeting.success.actions.email.description",
		},
		{
			id: "chat",
			icon: "message",
			labelKey: "workflow.meeting.success.actions.chat.label",
			descKey: "workflow.meeting.success.actions.chat.description",
		},
	];

	// Secondary actions (hidden by default)
	const secondaryActions: {
		id: PostAction;
		icon: string;
		labelKey: string;
		descKey: string;
	}[] = [
		{
			id: "meeting",
			icon: "calendar",
			labelKey: "workflow.meeting.success.actions.meeting.label",
			descKey: "workflow.meeting.success.actions.meeting.description",
		},
		{
			id: "status",
			icon: "bell",
			labelKey: "workflow.meeting.success.actions.status.label",
			descKey: "workflow.meeting.success.actions.status.description",
		},
	];

	function selectAction(actionId: PostAction) {
		onActionSelected?.(actionId);
		dispatch("actionSelected", actionId);
	}
</script>

<div class="success-screen">
	<!-- Success animation -->
	<div class="success-animation">
		<div class="check-circle">
			<svg
				viewBox="0 0 24 24"
				fill="none"
				stroke="currentColor"
				stroke-width="3"
			>
				<polyline points="20 6 9 17 4 12" class="check-mark" />
			</svg>
		</div>
	</div>

	<div class="content" class:visible={showContent}>
		<h2>{$t("workflow.meeting.success.title")}</h2>
		<p class="subtitle">{$t("workflow.meeting.success.subtitle")}</p>

		<!-- Time saved metric -->
		<div class="time-saved">
			<svg
				viewBox="0 0 24 24"
				fill="none"
				stroke="currentColor"
				stroke-width="2"
			>
				<circle cx="12" cy="12" r="10" />
				<polyline points="12 6 12 12 16 14" />
			</svg>
			<span
				>{$t("workflow.meeting.success.timeSaved", {
					values: { actual: "4", manual: "20" },
				})}</span
			>
		</div>

		{#if confluenceUrl}
			<a
				href={confluenceUrl}
				target="_blank"
				rel="noopener noreferrer"
				class="confluence-link"
			>
				<svg
					viewBox="0 0 24 24"
					fill="none"
					stroke="currentColor"
					stroke-width="2"
				>
					<path
						d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"
					/>
					<polyline points="15 3 21 3 21 9" />
					<line x1="10" y1="14" x2="21" y2="3" />
				</svg>
				{$t("workflow.meeting.success.viewInConfluence")}
			</a>
		{/if}

		<div class="divider">
			<span>{$t("workflow.meeting.success.nextSteps")}</span>
		</div>

		<!-- Primary actions (always visible) -->
		<div class="post-actions">
			{#each primaryActions as action}
				<button
					class="action-card"
					on:click={() => selectAction(action.id)}
				>
					<div class="action-icon">
						{#if action.icon === "mail"}
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
						{:else if action.icon === "message"}
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
						{/if}
					</div>
					<div class="action-text">
						<span class="action-label">{$t(action.labelKey)}</span>
						<span class="action-desc">{$t(action.descKey)}</span>
					</div>
					<div class="action-arrow">
						<svg
							viewBox="0 0 24 24"
							fill="none"
							stroke="currentColor"
							stroke-width="2"
						>
							<polyline points="9 18 15 12 9 6" />
						</svg>
					</div>
				</button>
			{/each}
		</div>

		<!-- Expandable secondary actions -->
		<button
			class="more-actions-toggle"
			on:click={() => (showMoreActions = !showMoreActions)}
		>
			<span>{$t("workflow.meeting.success.moreActions")}</span>
			<svg
				viewBox="0 0 24 24"
				fill="none"
				stroke="currentColor"
				stroke-width="2"
				class:expanded={showMoreActions}
			>
				<polyline points="6 9 12 15 18 9" />
			</svg>
		</button>

		{#if showMoreActions}
			<div class="secondary-actions">
				{#each secondaryActions as action}
					<button
						class="action-card secondary"
						on:click={() => selectAction(action.id)}
					>
						<div class="action-icon">
							{#if action.icon === "calendar"}
								<svg
									viewBox="0 0 24 24"
									fill="none"
									stroke="currentColor"
									stroke-width="2"
								>
									<rect
										x="3"
										y="4"
										width="18"
										height="18"
										rx="2"
										ry="2"
									/>
									<line x1="16" y1="2" x2="16" y2="6" />
									<line x1="8" y1="2" x2="8" y2="6" />
									<line x1="3" y1="10" x2="21" y2="10" />
								</svg>
							{:else if action.icon === "bell"}
								<svg
									viewBox="0 0 24 24"
									fill="none"
									stroke="currentColor"
									stroke-width="2"
								>
									<path
										d="M18 8A6 6 0 0 0 6 8c0 7-3 9-3 9h18s-3-2-3-9"
									/>
									<path d="M13.73 21a2 2 0 0 1-3.46 0" />
								</svg>
							{/if}
						</div>
						<div class="action-text">
							<span class="action-label"
								>{$t(action.labelKey)}</span
							>
							<span class="action-desc">{$t(action.descKey)}</span
							>
						</div>
						<div class="action-arrow">
							<svg
								viewBox="0 0 24 24"
								fill="none"
								stroke="currentColor"
								stroke-width="2"
							>
								<polyline points="9 18 15 12 9 6" />
							</svg>
						</div>
					</button>
				{/each}
			</div>
		{/if}

		<button
			class="done-btn"
			on:click={() => {
				onComplete?.();
				dispatch("complete");
			}}
		>
			{$t("workflow.meeting.success.done")}
		</button>
	</div>
</div>

<style>
	.success-screen {
		display: flex;
		flex-direction: column;
		align-items: center;
		width: 100%;
		max-width: 800px;
	}

	.success-animation {
		margin-bottom: 32px;
	}

	.check-circle {
		width: 112px;
		height: 112px;
		background: var(--green-500, #22c55e);
		border-radius: 50%;
		display: flex;
		align-items: center;
		justify-content: center;
		animation: pop-in 0.5s cubic-bezier(0.175, 0.885, 0.32, 1.275);
	}

	@keyframes pop-in {
		0% {
			transform: scale(0);
			opacity: 0;
		}
		50% {
			transform: scale(1.1);
		}
		100% {
			transform: scale(1);
			opacity: 1;
		}
	}

	.check-circle svg {
		width: 56px;
		height: 56px;
		color: white;
	}

	.check-mark {
		stroke-dasharray: 30;
		stroke-dashoffset: 30;
		animation: draw-check 0.4s ease-out 0.3s forwards;
	}

	@keyframes draw-check {
		to {
			stroke-dashoffset: 0;
		}
	}

	.content {
		width: 100%;
		opacity: 0;
		transform: translateY(20px);
		transition: all 0.4s ease;
	}

	.content.visible {
		opacity: 1;
		transform: translateY(0);
	}

	h2 {
		font-size: 24px;
		font-weight: 700;
		color: var(--slate-900, #0f172a);
		text-align: center;
		margin-bottom: 8px;
	}

	.subtitle {
		font-size: 15px;
		color: var(--slate-600, #475569);
		text-align: center;
		margin-bottom: 16px;
	}

	.time-saved {
		display: flex;
		align-items: center;
		justify-content: center;
		gap: 8px;
		padding: 10px 16px;
		background: var(--green-50, #f0fdf4);
		border: 1px solid var(--green-200, #bbf7d0);
		border-radius: 10px;
		font-size: 14px;
		color: var(--green-700, #15803d);
		margin-bottom: 24px;
	}

	.time-saved svg {
		width: 18px;
		height: 18px;
	}

	.confluence-link {
		display: flex;
		align-items: center;
		justify-content: center;
		gap: 8px;
		padding: 12px 20px;
		background: var(--blue-50, #eff6ff);
		border: 1px solid var(--blue-200, #bfdbfe);
		border-radius: 10px;
		color: var(--blue-700, #1d4ed8);
		font-size: 14px;
		font-weight: 500;
		text-decoration: none;
		transition: all 0.15s ease;
		margin-bottom: 32px;
	}

	.confluence-link:hover {
		background: var(--blue-100, #dbeafe);
		border-color: var(--blue-300, #93c5fd);
	}

	.confluence-link svg {
		width: 18px;
		height: 18px;
	}

	.divider {
		display: flex;
		align-items: center;
		gap: 16px;
		margin-bottom: 24px;
	}

	.divider::before,
	.divider::after {
		content: "";
		flex: 1;
		height: 1px;
		background: var(--slate-200, #e2e8f0);
	}

	.divider span {
		font-size: 12px;
		font-weight: 500;
		color: var(--slate-500, #64748b);
		text-transform: uppercase;
		letter-spacing: 0.5px;
	}

	.post-actions {
		display: flex;
		flex-direction: column;
		gap: 12px;
		margin-bottom: 16px;
	}

	.action-card {
		display: flex;
		align-items: center;
		gap: 16px;
		padding: 16px 20px;
		background: white;
		border: 1px solid var(--slate-200, #e2e8f0);
		border-radius: 10px;
		cursor: pointer;
		text-align: left;
		box-shadow: 0 1px 2px rgba(15, 23, 42, 0.05);
		transition: all 0.15s ease;
	}

	.action-card:hover {
		border-color: var(--blue-300, #93c5fd);
		box-shadow: 0 4px 12px rgba(59, 130, 246, 0.1);
	}

	.action-card.secondary {
		background: var(--slate-50, #f8fafc);
	}

	.action-icon {
		width: 44px;
		height: 44px;
		background: var(--slate-100, #f1f5f9);
		border-radius: 10px;
		display: flex;
		align-items: center;
		justify-content: center;
		flex-shrink: 0;
		transition: all 0.15s ease;
	}

	.action-card:hover .action-icon {
		background: var(--blue-100, #dbeafe);
	}

	.action-icon svg {
		width: 22px;
		height: 22px;
		color: var(--slate-600, #475569);
		transition: color 0.15s ease;
	}

	.action-card:hover .action-icon svg {
		color: var(--blue-600, #2563eb);
	}

	.action-text {
		flex: 1;
		min-width: 0;
	}

	.action-label {
		display: block;
		font-size: 15px;
		font-weight: 600;
		color: var(--slate-900, #0f172a);
		margin-bottom: 2px;
	}

	.action-desc {
		display: block;
		font-size: 14px;
		color: var(--slate-500, #64748b);
	}

	.action-arrow {
		flex-shrink: 0;
	}

	.action-arrow svg {
		width: 20px;
		height: 20px;
		color: var(--slate-400, #94a3b8);
		transition: all 0.15s ease;
	}

	.action-card:hover .action-arrow svg {
		color: var(--blue-500, #3b82f6);
		transform: translateX(4px);
	}

	.more-actions-toggle {
		display: flex;
		align-items: center;
		justify-content: center;
		gap: 6px;
		width: 100%;
		padding: 12px;
		background: transparent;
		border: none;
		font-size: 13px;
		font-weight: 500;
		color: var(--slate-500, #64748b);
		cursor: pointer;
		transition: color 0.15s ease;
		margin-bottom: 8px;
	}

	.more-actions-toggle:hover {
		color: var(--slate-700, #334155);
	}

	.more-actions-toggle svg {
		width: 16px;
		height: 16px;
		transition: transform 0.15s ease;
	}

	.more-actions-toggle svg.expanded {
		transform: rotate(180deg);
	}

	.secondary-actions {
		display: flex;
		flex-direction: column;
		gap: 12px;
		margin-bottom: 16px;
		animation: fade-in 0.2s ease;
	}

	@keyframes fade-in {
		from {
			opacity: 0;
			transform: translateY(-8px);
		}
		to {
			opacity: 1;
			transform: translateY(0);
		}
	}

	.done-btn {
		width: 100%;
		padding: 12px 24px;
		background: transparent;
		border: 1px solid var(--slate-300, #cbd5e1);
		border-radius: 6px;
		font-size: 15px;
		font-weight: 500;
		color: var(--slate-700, #334155);
		cursor: pointer;
		transition: all 0.15s ease;
	}

	.done-btn:hover {
		background: var(--slate-50, #f8fafc);
		border-color: var(--slate-400, #94a3b8);
	}
</style>
