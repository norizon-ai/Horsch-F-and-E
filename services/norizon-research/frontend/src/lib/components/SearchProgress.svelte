<script lang="ts">
	import type { SearchProgress, AgentIteration } from "$lib/types";
	import { t } from "svelte-i18n";

	let {
		progress,
		isComplete = false,
	}: { progress: SearchProgress; isComplete?: boolean } = $props();

	function getFallbackDisplayName(agentName: string): string {
		const name = agentName.toLowerCase();
		if (
			name.includes("websearch") ||
			name.includes("web_search") ||
			name.includes("web_researcher")
		)
			return $t("sources.types.web");
		if (name.includes("confluence")) return $t("sources.types.confluence");
		if (name.includes("sharepoint")) return $t("sources.types.sharepoint");
		if (
			name.includes("elasticsearch") ||
			name.includes("kb") ||
			name.includes("knowledge")
		)
			return $t("sources.types.elasticsearch");
		if (name.includes("jira")) return $t("sources.types.jira");
		if (name.includes("wiki") || name.includes("intranet"))
			return $t("sources.types.wiki");
		if (name.startsWith("delegate_to_") || name.startsWith("delegate to ")) {
			const target = name.replace(/^delegate[_ ]to[_ ]/i, "");
			return getFallbackDisplayName(target);
		}
		return $t("sources.types.document");
	}

	function getFallbackIconUrl(agentName: string): string {
		const name = agentName.toLowerCase();
		if (name.includes("websearch") || name.includes("web_search"))
			return "/icons/web.svg";
		if (name.includes("confluence")) return "/icons/confluence.svg";
		if (name.includes("sharepoint")) return "/icons/sharepoint.svg";
		if (name.includes("jira")) return "/icons/jira.svg";
		if (name.includes("intranet")) return "/icons/intranet.svg";
		return "/icons/elasticsearch.svg";
	}

	let sourceStatuses = $derived(
		progress.agentIterations
			?.filter(
				(ai) =>
					ai.agentName !== "analyzing" &&
					ai.agentName !== "generating_report",
			)
			.map((ai) => ({
				name: ai.agentName,
				displayName: ai.displayName || getFallbackDisplayName(ai.agentName),
				iconUrl: ai.iconUrl || getFallbackIconUrl(ai.agentName),
				status: ai.status,
				resultsCount: ai.resultsCount,
				searchingLabel: ai.searchingLabel,
				itemLabel: ai.itemLabel,
			})) ?? [],
	);

	let isThinking = $derived(
		progress.phase === "analyzing" ||
			progress.agentIterations?.some(
				(ai) => ai.agentName === "analyzing" && ai.status === "thinking",
			),
	);

	let completedSources = $derived(
		sourceStatuses.filter((s) => s.status === "done").length,
	);
	let totalSources = $derived(sourceStatuses.length);

	let statusMessage = $derived((() => {
		if (isComplete) return "";
		if (progress.phase === "generating_report") return $t("search.writing");
		if (totalSources > 0 && completedSources < totalSources)
			return $t("search.gatheringSources");
		if (totalSources > 0 && completedSources === totalSources)
			return $t("search.analyzing");
		if (isThinking) return $t("search.thinking");
		return $t("search.starting");
	})());
</script>

{#if !isComplete}
	<!-- Active search state -->
	<div class="search-status">
		<span class="status-dot"></span>
		<span class="status-text">{statusMessage}</span>
	</div>

	{#if sourceStatuses.length > 0}
		<div class="source-pills">
			{#each sourceStatuses as source}
				<div
					class="source-pill"
					class:searching={source.status === "searching"}
					class:done={source.status === "done"}
				>
					<img
						src={source.iconUrl}
						alt=""
						class="pill-icon"
					/>
					<span class="pill-name">{source.displayName}</span>
					{#if source.status === "searching"}
						<span class="pill-spinner"></span>
					{:else if source.resultsCount !== undefined}
						<span class="pill-count">{source.resultsCount}</span>
					{/if}
				</div>
			{/each}
		</div>
	{/if}
{:else}
	<!-- Completed: compact inline pills -->
	{#if sourceStatuses.length > 0}
		<div class="source-pills completed">
			{#each sourceStatuses as source}
				<div class="source-pill done">
					<img
						src={source.iconUrl}
						alt=""
						class="pill-icon"
					/>
					<span class="pill-name">{source.displayName}</span>
					<span class="pill-count">{source.resultsCount || 0}</span>
				</div>
			{/each}
		</div>
	{/if}
{/if}

<style>
	.search-status {
		display: flex;
		align-items: center;
		gap: 8px;
		margin-bottom: 10px;
	}

	.status-dot {
		width: 7px;
		height: 7px;
		background: #3b82f6;
		border-radius: 50%;
		animation: pulse 1.5s ease-in-out infinite;
		flex-shrink: 0;
	}

	@keyframes pulse {
		0%, 100% { opacity: 1; transform: scale(1); }
		50% { opacity: 0.5; transform: scale(0.85); }
	}

	.status-text {
		font-size: 13px;
		color: #64748b;
	}

	.source-pills {
		display: flex;
		flex-wrap: wrap;
		gap: 6px;
		margin-bottom: 12px;
	}

	.source-pills.completed {
		margin-bottom: 0;
	}

	.source-pill {
		display: inline-flex;
		align-items: center;
		gap: 5px;
		padding: 4px 10px 4px 6px;
		border-radius: 9999px;
		border: 1px solid #e2e8f0;
		background: #f1f5f9;
		color: #64748b;
		font-size: 12px;
	}

	.source-pill.searching {
		background: #eff6ff;
		border-color: #bfdbfe;
		color: #2563eb;
	}

	.source-pill.done {
		background: #f8fafc;
		border-color: #e2e8f0;
		color: #475569;
	}

	.pill-icon {
		width: 14px;
		height: 14px;
		object-fit: contain;
		border-radius: 2px;
		flex-shrink: 0;
	}

	.pill-name {
		white-space: nowrap;
		font-size: 12px;
	}

	.pill-spinner {
		width: 10px;
		height: 10px;
		border: 1.5px solid #bfdbfe;
		border-top-color: #3b82f6;
		border-radius: 50%;
		animation: spin 0.8s linear infinite;
		flex-shrink: 0;
	}

	@keyframes spin {
		to { transform: rotate(360deg); }
	}

	.pill-count {
		display: inline-flex;
		align-items: center;
		justify-content: center;
		min-width: 16px;
		height: 16px;
		padding: 0 4px;
		background: #e2e8f0;
		border-radius: 4px;
		font-size: 10px;
		font-weight: 600;
		color: #64748b;
	}
</style>
