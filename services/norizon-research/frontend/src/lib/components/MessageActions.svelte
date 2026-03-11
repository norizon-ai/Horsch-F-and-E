<script lang="ts">
	import { t } from "svelte-i18n";
	import { Button } from "$lib/components/ui/button";
	import { Separator } from "$lib/components/ui/separator";

	let {
		showExport = true,
		showRegenerate = true,
		showFeedback = true,
		onCopy = undefined as (() => void) | undefined,
		onRegenerate = undefined as (() => void) | undefined,
		onExportPdf = undefined as (() => void) | undefined,
		onExportWord = undefined as (() => void) | undefined,
		onThumbsUp = undefined as (() => void) | undefined,
		onThumbsDown = undefined as (() => void) | undefined,
		oncopy = undefined as (() => void) | undefined,
		onexportPdf = undefined as (() => void) | undefined,
	} = $props();

	let copied = $state(false);

	async function handleCopy() {
		onCopy?.();
		oncopy?.();
		copied = true;
		setTimeout(() => {
			copied = false;
		}, 2000);
	}
</script>

<div class="flex items-center gap-1 mt-3">
	<Button
		variant="ghost"
		size="sm"
		class="text-xs text-nora-slate-500 h-8 px-2.5 gap-1 [&_svg]:size-3.5"
		onclick={handleCopy}
	>
		{#if copied}
			<svg
				viewBox="0 0 24 24"
				fill="none"
				stroke="currentColor"
				stroke-width="2"
			>
				<polyline points="20 6 9 17 4 12" />
			</svg>
		{:else}
			<svg
				viewBox="0 0 24 24"
				fill="none"
				stroke="currentColor"
				stroke-width="2"
			>
				<rect x="9" y="9" width="13" height="13" rx="2" ry="2" />
				<path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1" />
			</svg>
		{/if}
		{copied ? $t("actions.copied") : $t("common.copy")}
	</Button>

	{#if showExport}
		<Button
			variant="ghost"
			size="sm"
			class="text-xs text-nora-slate-500 h-8 px-2.5 gap-1 [&_svg]:size-3.5"
			onclick={() => { onExportPdf?.(); onexportPdf?.(); }}
		>
			<svg
				viewBox="0 0 24 24"
				fill="none"
				stroke="currentColor"
				stroke-width="2"
			>
				<path d="M4 12v8a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2v-8" />
				<polyline points="16 6 12 2 8 6" />
				<line x1="12" y1="2" x2="12" y2="15" />
			</svg>
			{$t("actions.export")}
		</Button>
	{/if}

	{#if showRegenerate}
		<Separator orientation="vertical" class="h-4 mx-1" />
		<Button
			variant="ghost"
			size="sm"
			class="text-xs text-nora-slate-500 h-8 px-2.5 gap-1 [&_svg]:size-3.5"
			onclick={() => onRegenerate?.()}
		>
			<svg
				viewBox="0 0 24 24"
				fill="none"
				stroke="currentColor"
				stroke-width="2"
			>
				<polyline points="1 4 1 10 7 10" />
				<path d="M3.51 15a9 9 0 1 0 2.13-9.36L1 10" />
			</svg>
			{$t("common.regenerate")}
		</Button>
	{/if}

	{#if showFeedback}
		<Separator orientation="vertical" class="h-4 mx-1" />
		<Button
			variant="ghost"
			size="sm"
			class="text-xs text-nora-slate-500 h-8 px-2.5 [&_svg]:size-3.5"
			onclick={() => onThumbsUp?.()}
		>
			<svg
				viewBox="0 0 24 24"
				fill="none"
				stroke="currentColor"
				stroke-width="2"
			>
				<path
					d="M14 9V5a3 3 0 0 0-3-3l-4 9v11h11.28a2 2 0 0 0 2-1.7l1.38-9a2 2 0 0 0-2-2.3zM7 22H4a2 2 0 0 1-2-2v-7a2 2 0 0 1 2-2h3"
				/>
			</svg>
		</Button>

		<Button
			variant="ghost"
			size="sm"
			class="text-xs text-nora-slate-500 h-8 px-2.5 [&_svg]:size-3.5"
			onclick={() => onThumbsDown?.()}
		>
			<svg
				viewBox="0 0 24 24"
				fill="none"
				stroke="currentColor"
				stroke-width="2"
			>
				<path
					d="M10 15v4a3 3 0 0 0 3 3l4-9V2H5.72a2 2 0 0 0-2 1.7l-1.38 9a2 2 0 0 0 2 2.3zm7-13h2.67A2.31 2.31 0 0 1 22 4v7a2.31 2.31 0 0 1-2.33 2H17"
				/>
			</svg>
		</Button>
	{/if}
</div>
