<script lang="ts">
	import type { Source } from "$lib/types";
	import { groupSourcesByUrl } from "$lib/utils/sourceGrouping";
	import { sanitizeSnippet } from "$lib/utils/sanitizeSnippet";
	import { t } from "svelte-i18n";
	import { Card, CardContent } from "$lib/components/ui/card";
	import { Badge } from "$lib/components/ui/badge";
	import { Button } from "$lib/components/ui/button";
	import { slide } from "svelte/transition";

	export let sources: Source[] = [];
	export let messageId = "";
	export let expanded = false;

	$: groupedSources = groupSourcesByUrl(sources);
	$: uniqueCount = groupedSources.length;
	$: totalSections = sources.length;

	let expandedSources = new Set<string>();

	function toggleSource(id: string) {
		const next = new Set(expandedSources);
		if (next.has(id)) {
			next.delete(id);
		} else {
			next.add(id);
		}
		expandedSources = next;
	}

	function toggleExpanded() {
		expanded = !expanded;
	}

	function getSourceIconUrl(sourceType: string | undefined): string {
		switch (sourceType) {
			case "sharepoint":
				return "/icons/sharepoint.svg";
			case "confluence":
				return "/icons/confluence.svg";
			case "wiki":
				return "/icons/intranet.svg";
			case "jira":
				return "/icons/jira.svg";
			case "web":
				return "/icons/web.svg";
			case "elasticsearch":
				return "/icons/elasticsearch.svg";
			default:
				return "/icons/elasticsearch.svg";
		}
	}

	function getSourceLabel(sourceType: string | undefined): string {
		switch (sourceType) {
			case "sharepoint":
				return $t("sources.types.sharepoint");
			case "confluence":
				return $t("sources.types.confluence");
			case "wiki":
				return $t("sources.types.wiki");
			case "web":
				return $t("sources.types.web");
			case "jira":
				return $t("sources.types.jira");
			case "elasticsearch":
				return $t("sources.types.elasticsearch");
			default:
				return $t("sources.types.document");
		}
	}
</script>

<Card class="mt-4 shadow-none overflow-hidden">
	<!-- Collapsible trigger -->
	<button
		class="flex items-center justify-between w-full px-3.5 py-2.5 bg-nora-slate-50 hover:bg-nora-slate-100 cursor-pointer border-none font-[inherit] text-left transition-colors duration-100"
		on:click={toggleExpanded}
	>
		<div
			class="text-xs font-semibold text-nora-slate-600 flex items-center gap-1.5"
		>
			<svg
				class="w-3.5 h-3.5"
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
			{uniqueCount}
			{$t("sources.title")}
			{#if totalSections > uniqueCount}
				<span class="text-[11px] text-nora-slate-400 font-normal ml-1"
					>({totalSections} {$t("sources.sections")})</span
				>
			{/if}
		</div>
		<svg
			class="w-3.5 h-3.5 text-nora-slate-400 transition-transform duration-200 {expanded
				? ''
				: '-rotate-90'}"
			viewBox="0 0 24 24"
			fill="none"
			stroke="currentColor"
			stroke-width="2"
		>
			<polyline points="6 9 12 15 18 9" />
		</svg>
	</button>

	<!-- Collapsible content -->
	{#if expanded}
		<div transition:slide={{ duration: 200 }}>
			<CardContent class="p-3 grid gap-2">
				{#each groupedSources as source, index}
					<Card
						class="shadow-none hover:border-nora-blue-300 hover:bg-nora-blue-50 transition-all duration-150"
						id="source-{messageId}-{index + 1}"
					>
						<CardContent class="p-3 flex flex-col gap-2">
							<!-- Header -->
							<div class="flex items-start gap-3">
								<div
									class="w-8 h-8 rounded-md flex items-center justify-center shrink-0 overflow-hidden"
								>
									<img
										src={getSourceIconUrl(
											source.sourceType,
										)}
										alt={getSourceLabel(source.sourceType)}
										class="w-8 h-8 object-contain"
									/>
								</div>
								<div
									class="flex-1 min-w-0 flex flex-wrap items-center gap-2"
								>
									<a
										href={source.url || "#"}
										target="_blank"
										rel="noopener noreferrer"
										class="text-sm font-semibold text-nora-slate-900 leading-tight no-underline hover:underline {!source.url
											? 'cursor-default hover:no-underline'
											: ''}"
									>
										{source.title}
									</a>
									{#if source.sectionCount > 1}
										<Badge
											variant="outline"
											class="bg-nora-orange-100 text-nora-orange-600 border-nora-orange-200 text-[10px] font-semibold px-1.5 py-0"
											>{source.sectionCount}
											{$t("sources.sections")}</Badge
										>
									{/if}
								</div>
							</div>

							<!-- Primary snippet -->
							{#if source.sections[0]?.snippet}
								<div
									class="source-snippet text-[13px] text-nora-slate-500 leading-normal line-clamp-3"
								>
									{@html sanitizeSnippet(
										source.sections[0].snippet,
									)}
								</div>
							{/if}

							<!-- Meta -->
							<div
								class="text-[11px] text-nora-slate-400 flex items-center gap-2"
							>
								<span class="flex items-center gap-1"
									>{getSourceLabel(source.sourceType)}</span
								>
								{#if source.lastUpdated}
									<span>Updated {source.lastUpdated}</span>
								{/if}
							</div>

							<!-- Expandable additional sections -->
							{#if source.sectionCount > 1}
								<Button
									variant="outline"
									size="sm"
									class="w-full text-xs font-medium text-nora-slate-600 gap-1.5 [&_svg]:size-3.5"
									on:click={() => toggleSource(source.id)}
								>
									{#if expandedSources.has(source.id)}
										<svg
											viewBox="0 0 24 24"
											fill="none"
											stroke="currentColor"
											stroke-width="2"
										>
											<polyline
												points="18 15 12 9 6 15"
											/>
										</svg>
										{$t("sources.hide_sections", {
											values: {
												count: source.sectionCount - 1,
											},
										})}
									{:else}
										<svg
											viewBox="0 0 24 24"
											fill="none"
											stroke="currentColor"
											stroke-width="2"
										>
											<polyline points="6 9 12 15 18 9" />
										</svg>
										{$t("sources.show_sections", {
											values: {
												count: source.sectionCount - 1,
											},
										})}
									{/if}
								</Button>

								{#if expandedSources.has(source.id)}
									<div
										class="mt-1 pt-2 border-t border-nora-slate-100 grid gap-2"
										transition:slide={{ duration: 200 }}
									>
										{#each source.sections.slice(1) as section}
											<div
												class="source-snippet p-2.5 bg-nora-slate-50 rounded-md text-[13px] text-nora-slate-600 leading-normal"
											>
												{@html sanitizeSnippet(
													section.snippet,
												)}
											</div>
										{/each}
									</div>
								{/if}
							{/if}
						</CardContent>
					</Card>
				{/each}
			</CardContent>
		</div>
	{/if}
</Card>
