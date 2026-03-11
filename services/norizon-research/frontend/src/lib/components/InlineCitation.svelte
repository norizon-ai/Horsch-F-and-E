<script lang="ts">
	import type { Source } from "$lib/types";
	import { Badge } from "$lib/components/ui/badge";

	let {
		index,
		source,
		excerpt = undefined as string | undefined,
	}: { index: number; source: Source; excerpt?: string } = $props();

	let showTooltip = $state(false);

	function getSourceIcon(sourceType: string | undefined): string {
		switch (sourceType) {
			case "sharepoint": return "folder";
			case "confluence": return "file";
			case "wiki": return "book";
			case "web": return "globe";
			default: return "file";
		}
	}

	function getSourceLabel(sourceType: string | undefined): string {
		switch (sourceType) {
			case "sharepoint": return "SharePoint";
			case "confluence": return "Confluence";
			case "wiki": return "Internal Wiki";
			case "web": return "Web";
			case "elasticsearch": return "Knowledge Base";
			default: return "Document";
		}
	}

	let iconType = $derived(getSourceIcon(source.sourceType));
	let sourceLabel = $derived(getSourceLabel(source.sourceType));
</script>

<span
	class="citation-wrapper"
	role="button"
	tabindex="0"
	onmouseenter={() => (showTooltip = true)}
	onmouseleave={() => (showTooltip = false)}
	onfocus={() => (showTooltip = true)}
	onblur={() => (showTooltip = false)}
	onclick={() => source.url && window.open(source.url, "_blank")}
	onkeypress={(e) =>
		e.key === "Enter" && source.url && window.open(source.url, "_blank")}
>
	<Badge
		variant="secondary"
		class="inline-flex items-center justify-center w-[18px] h-[18px] !rounded bg-blue-100 text-blue-600 text-[11px] font-semibold cursor-pointer !p-0 !border-0 hover:bg-blue-500 hover:text-white transition-all duration-150"
	>
		{index}
	</Badge>
	{#if showTooltip}
		<div class="citation-tooltip">
			<div class="tooltip-source">
				<div class="tooltip-icon">
					{#if iconType === "folder"}
						<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
							<path d="M22 19a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h5l2 3h9a2 2 0 0 1 2 2z" />
						</svg>
					{:else if iconType === "book"}
						<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
							<path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z" />
							<path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z" />
						</svg>
					{:else if iconType === "globe"}
						<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
							<circle cx="12" cy="12" r="10" />
							<line x1="2" y1="12" x2="22" y2="12" />
							<path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z" />
						</svg>
					{:else}
						<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
							<path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z" />
							<polyline points="14 2 14 8 20 8" />
						</svg>
					{/if}
				</div>
				<div class="tooltip-details">
					<div class="tooltip-title">{source.title}</div>
					<div class="tooltip-meta">
						{sourceLabel}
						{#if source.lastUpdated}
							<span class="tooltip-dot">·</span>
							Updated {source.lastUpdated}
						{/if}
					</div>
				</div>
			</div>
			{#if excerpt || source.snippet}
				<div class="tooltip-excerpt">"{excerpt || source.snippet}"</div>
			{/if}
		</div>
	{/if}
</span>

<style>
	.citation-wrapper {
		display: inline-flex;
		position: relative;
		margin: 0 2px;
		vertical-align: middle;
		cursor: pointer;
	}

	.citation-tooltip {
		position: absolute;
		bottom: calc(100% + 8px);
		left: 50%;
		transform: translateX(-50%);
		width: 280px;
		background: #ffffff;
		border: 1px solid #e2e8f0;
		border-radius: 10px;
		box-shadow: 0 12px 32px rgba(15, 23, 42, 0.12);
		padding: 12px;
		z-index: 100;
		text-align: left;
	}

	.citation-tooltip::after {
		content: "";
		position: absolute;
		top: 100%;
		left: 50%;
		transform: translateX(-50%);
		border: 6px solid transparent;
		border-top-color: #ffffff;
	}

	.citation-tooltip::before {
		content: "";
		position: absolute;
		top: 100%;
		left: 50%;
		transform: translateX(-50%);
		border: 7px solid transparent;
		border-top-color: #e2e8f0;
	}

	.tooltip-source {
		display: flex;
		align-items: flex-start;
		gap: 10px;
	}

	.tooltip-icon {
		width: 32px;
		height: 32px;
		background: #f1f5f9;
		border-radius: 6px;
		display: flex;
		align-items: center;
		justify-content: center;
		flex-shrink: 0;
	}

	.tooltip-icon svg {
		width: 16px;
		height: 16px;
		color: #64748b;
	}

	.tooltip-details {
		flex: 1;
		min-width: 0;
	}

	.tooltip-title {
		font-size: 13px;
		font-weight: 600;
		color: #0f172a;
		margin-bottom: 2px;
		white-space: nowrap;
		overflow: hidden;
		text-overflow: ellipsis;
	}

	.tooltip-meta {
		font-size: 11px;
		color: #64748b;
	}

	.tooltip-dot {
		margin: 0 4px;
	}

	.tooltip-excerpt {
		margin-top: 8px;
		padding-top: 8px;
		border-top: 1px solid #f1f5f9;
		font-size: 12px;
		color: #475569;
		line-height: 1.5;
		font-style: italic;
	}
</style>
