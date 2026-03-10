<script lang="ts">
	import type { SearchProgress, AgentIteration } from "$lib/types";
	import { t } from "svelte-i18n";
	import { Badge } from "$lib/components/ui/badge";

	export let progress: SearchProgress;
	export let isComplete = false;

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
		if (
			name.startsWith("delegate_to_") ||
			name.startsWith("delegate to ")
		) {
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

	$: sourceStatuses =
		progress.agentIterations
			?.filter(
				(ai) =>
					ai.agentName !== "analyzing" &&
					ai.agentName !== "generating_report",
			)
			.map((ai) => ({
				name: ai.agentName,
				displayName:
					ai.displayName || getFallbackDisplayName(ai.agentName),
				iconUrl: ai.iconUrl || getFallbackIconUrl(ai.agentName),
				status: ai.status,
				resultsCount: ai.resultsCount,
				searchingLabel: ai.searchingLabel,
				itemLabel: ai.itemLabel,
			})) ?? [];

	$: isThinking =
		progress.phase === "analyzing" ||
		progress.agentIterations?.some(
			(ai) => ai.agentName === "analyzing" && ai.status === "thinking",
		);

	$: totalDocuments = sourceStatuses.reduce(
		(sum, s) => sum + (s.resultsCount || 0),
		0,
	);
	$: completedSources = sourceStatuses.filter(
		(s) => s.status === "done",
	).length;
	$: totalSources = sourceStatuses.length;

	$: statusMessage = (() => {
		if (isComplete) return "";
		if (progress.phase === "generating_report") return $t("search.writing");
		if (totalSources > 0 && completedSources < totalSources)
			return $t("search.gatheringSources");
		if (totalSources > 0 && completedSources === totalSources)
			return $t("search.analyzing");
		if (isThinking) return $t("search.thinking");
		return $t("search.starting");
	})();
</script>

{#if !isComplete}
	<!-- Active search state -->
	<div class="flex items-center gap-2 mb-3">
		<div
			class="w-2 h-2 bg-nora-blue-500 rounded-full animate-pulse shrink-0"
		></div>
		<span class="text-[13px] text-nora-slate-600">{statusMessage}</span>
	</div>

	{#if sourceStatuses.length > 0}
		<div class="flex flex-wrap gap-2 mb-4">
			{#each sourceStatuses as source}
				{#if source.status === "searching"}
					<Badge
						variant="outline"
						class="bg-nora-blue-50 text-nora-blue-700 border-nora-blue-200 rounded-xl gap-1.5 py-1 px-2.5"
					>
						<img
							src={source.iconUrl}
							alt=""
							class="w-3.5 h-3.5 object-contain rounded-sm shrink-0"
						/>
						<span class="whitespace-nowrap"
							>{source.displayName}</span
						>
						<span
							class="w-2.5 h-2.5 border-[1.5px] border-nora-blue-200 border-t-nora-blue-500 rounded-full animate-spin shrink-0"
						></span>
					</Badge>
				{:else}
					<Badge
						variant="outline"
						class="bg-nora-slate-100 text-nora-slate-600 border-nora-slate-200 rounded-xl gap-1.5 py-1 px-2.5"
					>
						<img
							src={source.iconUrl}
							alt=""
							class="w-3.5 h-3.5 object-contain rounded-sm shrink-0"
						/>
						<span class="whitespace-nowrap"
							>{source.displayName}</span
						>
						<Badge
							variant="secondary"
							class="!rounded-lg !px-1.5 !py-0 text-[10px] font-semibold min-w-[16px] text-center bg-nora-slate-200 text-nora-slate-600 !border-0"
							>{source.resultsCount || 0}</Badge
						>
					</Badge>
				{/if}
			{/each}
		</div>
	{/if}
{:else}
	<!-- Complete state: compact inline pills -->
	{#if sourceStatuses.length > 0}
		{#each sourceStatuses as source}
			<Badge
				variant="outline"
				class="bg-nora-slate-100 text-nora-slate-600 border-nora-slate-200 rounded-[10px] gap-[5px] py-[3px] px-2 text-[11px]"
			>
				<img
					src={source.iconUrl}
					alt=""
					class="w-3 h-3 object-contain rounded-sm"
				/>
				<span class="whitespace-nowrap">{source.displayName}</span>
				<Badge
					variant="secondary"
					class="!rounded-md !px-1 !py-0 text-[9px] font-semibold min-w-[14px] text-center bg-nora-slate-200 text-nora-slate-600 !border-0"
					>{source.resultsCount || 0}</Badge
				>
			</Badge>
		{/each}
	{/if}
{/if}
