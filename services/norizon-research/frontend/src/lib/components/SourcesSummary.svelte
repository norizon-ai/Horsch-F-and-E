<script lang="ts">
	import type { Source } from "$lib/types";
	import { groupSourcesByUrl } from "$lib/utils/sourceGrouping";
	import { sanitizeSnippet } from "$lib/utils/sanitizeSnippet";
	import { t } from "svelte-i18n";
	import { slide } from "svelte/transition";

	let {
		sources = [] as Source[],
		messageId = "",
		expanded = $bindable(false),
	} = $props();

	let groupedSources = $derived(groupSourcesByUrl(sources));
	let uniqueCount = $derived(groupedSources.length);
	let totalSections = $derived(sources.length);

	let expandedSources = $state(new Set<string>());

	function toggleSource(id: string) {
		const next = new Set(expandedSources);
		if (next.has(id)) {
			next.delete(id);
		} else {
			next.add(id);
		}
		expandedSources = next;
	}

	function getSourceIconUrl(sourceType: string | undefined): string {
		switch (sourceType) {
			case "sharepoint": return "/icons/sharepoint.svg";
			case "confluence": return "/icons/confluence.svg";
			case "wiki": return "/icons/intranet.svg";
			case "jira": return "/icons/jira.svg";
			case "web": return "/icons/web.svg";
			case "elasticsearch": return "/icons/elasticsearch.svg";
			default: return "/icons/elasticsearch.svg";
		}
	}

	function getSourceLabel(sourceType: string | undefined): string {
		switch (sourceType) {
			case "sharepoint": return $t("sources.types.sharepoint");
			case "confluence": return $t("sources.types.confluence");
			case "wiki": return $t("sources.types.wiki");
			case "web": return $t("sources.types.web");
			case "jira": return $t("sources.types.jira");
			case "elasticsearch": return $t("sources.types.elasticsearch");
			default: return $t("sources.types.document");
		}
	}
</script>

<details class="sources-details" bind:open={expanded}>
	<summary class="sources-summary-trigger">
		<div class="summary-left">
			<svg
				class="summary-icon"
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
			<span class="summary-label">
				{uniqueCount}
				{$t("sources.title")}
				{#if totalSections > uniqueCount}
					<span class="summary-sections"
						>({totalSections} {$t("sources.sections")})</span
					>
				{/if}
			</span>
		</div>
		<svg
			class="chevron-icon"
			viewBox="0 0 24 24"
			fill="none"
			stroke="currentColor"
			stroke-width="2"
		>
			<polyline points="6 9 12 15 18 9" />
		</svg>
	</summary>

	<!-- Expanded content -->
	<div class="sources-content" transition:slide={{ duration: 200 }}>
		{#each groupedSources as source, index}
			<div
				class="source-item"
				id="source-{messageId}-{index + 1}"
			>
				<!-- Source header -->
				<div class="source-header">
					<div class="source-icon-wrap">
						<img
							src={getSourceIconUrl(source.sourceType)}
							alt={getSourceLabel(source.sourceType)}
							class="source-type-icon"
						/>
					</div>
					<div class="source-meta">
						<a
							href={source.url || "#"}
							target="_blank"
							rel="noopener noreferrer"
							class="source-title"
							class:no-link={!source.url}
						>
							{source.title}
						</a>
						<div class="source-sub">
							<span>{getSourceLabel(source.sourceType)}</span>
							{#if source.lastUpdated}
								<span>· {source.lastUpdated}</span>
							{/if}
							{#if source.sectionCount > 1}
								<span class="section-badge"
									>{source.sectionCount} {$t("sources.sections")}</span
								>
							{/if}
						</div>
					</div>
				</div>

				<!-- Primary snippet -->
				{#if source.sections[0]?.snippet}
					<div class="source-snippet">
						{@html sanitizeSnippet(source.sections[0].snippet)}
					</div>
				{/if}

				<!-- Additional sections toggle -->
				{#if source.sectionCount > 1}
					<button
						class="show-sections-btn"
						onclick={() => toggleSource(source.id)}
					>
						{#if expandedSources.has(source.id)}
							<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
								<polyline points="18 15 12 9 6 15" />
							</svg>
							{$t("sources.hide_sections", { values: { count: source.sectionCount - 1 } })}
						{:else}
							<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
								<polyline points="6 9 12 15 18 9" />
							</svg>
							{$t("sources.show_sections", { values: { count: source.sectionCount - 1 } })}
						{/if}
					</button>

					{#if expandedSources.has(source.id)}
						<div class="extra-sections" transition:slide={{ duration: 200 }}>
							{#each source.sections.slice(1) as section}
								<div class="extra-snippet">
									{@html sanitizeSnippet(section.snippet)}
								</div>
							{/each}
						</div>
					{/if}
				{/if}
			</div>
		{/each}
	</div>
</details>

<style>
	.sources-details {
		margin-top: 16px;
		border: 1px solid #e2e8f0;
		border-radius: 10px;
		overflow: hidden;
	}

	.sources-summary-trigger {
		display: flex;
		align-items: center;
		justify-content: space-between;
		padding: 10px 14px;
		background: #f8fafc;
		cursor: pointer;
		list-style: none;
		user-select: none;
		transition: background 0.1s ease;
	}

	.sources-summary-trigger::-webkit-details-marker {
		display: none;
	}

	.sources-summary-trigger:hover {
		background: #f1f5f9;
	}

	.summary-left {
		display: flex;
		align-items: center;
		gap: 6px;
	}

	.summary-icon {
		width: 14px;
		height: 14px;
		color: #64748b;
		flex-shrink: 0;
	}

	.summary-label {
		font-size: 12px;
		font-weight: 600;
		color: #475569;
	}

	.summary-sections {
		font-size: 11px;
		font-weight: 400;
		color: #94a3b8;
		margin-left: 4px;
	}

	.chevron-icon {
		width: 14px;
		height: 14px;
		color: #94a3b8;
		transition: transform 0.2s ease;
	}

	details[open] .chevron-icon {
		transform: rotate(180deg);
	}

	.sources-content {
		padding: 10px;
		display: flex;
		flex-direction: column;
		gap: 8px;
		border-top: 1px solid #e2e8f0;
	}

	.source-item {
		padding: 12px;
		border: 1px solid #f1f5f9;
		border-radius: 8px;
		background: #ffffff;
		transition: border-color 0.15s ease;
	}

	.source-item:hover {
		border-color: #bfdbfe;
	}

	.source-header {
		display: flex;
		align-items: flex-start;
		gap: 10px;
		margin-bottom: 8px;
	}

	.source-icon-wrap {
		width: 28px;
		height: 28px;
		flex-shrink: 0;
		border-radius: 6px;
		overflow: hidden;
		display: flex;
		align-items: center;
		justify-content: center;
	}

	.source-type-icon {
		width: 28px;
		height: 28px;
		object-fit: contain;
	}

	.source-meta {
		flex: 1;
		min-width: 0;
	}

	.source-title {
		font-size: 13px;
		font-weight: 600;
		color: #0f172a;
		text-decoration: none;
		display: block;
		line-height: 1.3;
		margin-bottom: 3px;
	}

	.source-title:hover {
		text-decoration: underline;
	}

	.source-title.no-link {
		cursor: default;
	}

	.source-title.no-link:hover {
		text-decoration: none;
	}

	.source-sub {
		font-size: 11px;
		color: #94a3b8;
		display: flex;
		align-items: center;
		flex-wrap: wrap;
		gap: 4px;
	}

	.section-badge {
		display: inline-block;
		padding: 1px 6px;
		background: #ffedd5;
		color: #c2410c;
		border-radius: 4px;
		font-size: 10px;
		font-weight: 600;
	}

	.source-snippet {
		font-size: 12px;
		color: #64748b;
		line-height: 1.5;
		display: -webkit-box;
		-webkit-line-clamp: 3;
		-webkit-box-orient: vertical;
		overflow: hidden;
	}

	.show-sections-btn {
		display: inline-flex;
		align-items: center;
		gap: 4px;
		margin-top: 8px;
		padding: 4px 8px;
		background: none;
		border: 1px solid #e2e8f0;
		border-radius: 6px;
		font-size: 12px;
		color: #64748b;
		cursor: pointer;
		transition: all 0.15s ease;
		font-family: inherit;
	}

	.show-sections-btn:hover {
		background: #f1f5f9;
		color: #334155;
	}

	.show-sections-btn svg {
		width: 12px;
		height: 12px;
	}

	.extra-sections {
		margin-top: 8px;
		padding-top: 8px;
		border-top: 1px solid #f1f5f9;
		display: flex;
		flex-direction: column;
		gap: 6px;
	}

	.extra-snippet {
		padding: 8px;
		background: #f8fafc;
		border-radius: 6px;
		font-size: 12px;
		color: #64748b;
		line-height: 1.5;
	}
</style>
