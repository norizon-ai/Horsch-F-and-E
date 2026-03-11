<script lang="ts">
	import type { Source } from "$types";

	let {
		source,
		index = 0,
		checked = false,
		checking = false,
	}: {
		source: Source;
		index?: number;
		checked?: boolean;
		checking?: boolean;
	} = $props();

	let hasErrored = $state(false);

	let domain = $derived((() => {
		try {
			return new URL(source.url).hostname.replace("www.", "");
		} catch {
			return source.url;
		}
	})());

	let faviconUrl = $derived(
		`https://www.google.com/s2/favicons?domain=${domain}&sz=64`,
	);

	function handleFaviconError(event: Event) {
		if (hasErrored) return;
		hasErrored = true;
		const img = event.target as HTMLImageElement;
		img.src =
			'data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="%23666" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline></svg>';
	}
</script>

<div
	class="source-card"
	class:checking
	class:checked
>
	<!-- Header with Logo and Index -->
	<div class="flex items-start gap-3 mb-3">
		<div class="flex-shrink-0 relative">
			<div
				class="w-10 h-10 rounded-lg overflow-hidden bg-gray-100 flex items-center justify-center border border-gray-200"
			>
				<img
					src={faviconUrl}
					alt={domain}
					class="w-full h-full object-contain"
					onerror={handleFaviconError}
				/>
			</div>
			{#if checked}
				<span
					class="absolute -top-1 -right-1 inline-flex items-center justify-center w-5 h-5 text-white bg-green-500 rounded-full shadow-sm checkmark-appear"
				>
					<svg
						class="w-3 h-3"
						fill="none"
						stroke="currentColor"
						viewBox="0 0 24 24"
					>
						<path
							stroke-linecap="round"
							stroke-linejoin="round"
							stroke-width="3"
							d="M5 13l4 4L19 7"
						/>
					</svg>
				</span>
			{:else if checking}
				<span
					class="absolute -top-1 -right-1 inline-flex items-center justify-center w-5 h-5 text-white bg-blue-600 rounded-full shadow-sm"
				>
					<div class="w-2 h-2 bg-white rounded-full animate-pulse"></div>
				</span>
			{:else}
				<span
					class="absolute -top-1 -right-1 inline-flex items-center justify-center w-5 h-5 rounded-full text-xs font-bold text-white shadow-sm"
					style="background: #f97316; padding: 0;"
				>
					{index + 1}
				</span>
			{/if}
		</div>

		<div class="flex-1 min-w-0">
			<h3
				class="font-semibold text-gray-900 mb-1 line-clamp-2 hover:text-blue-600 transition-colors"
			>
				{source.title}
			</h3>
			<div class="flex items-center gap-2 text-xs text-gray-500">
				<span class="truncate">{domain}</span>
			</div>
		</div>
	</div>

	<!-- Snippet -->
	{#if source.snippet}
		<p class="text-sm text-gray-600 mb-3 line-clamp-3 leading-relaxed">
			{source.snippet}
		</p>
	{/if}

	<!-- Visit Link -->
	<a
		href={source.url}
		target="_blank"
		rel="noopener noreferrer"
		class="inline-flex items-center text-sm text-blue-600 hover:text-blue-700 font-medium transition-colors"
	>
		<svg
			class="w-4 h-4 mr-1.5"
			fill="none"
			stroke="currentColor"
			viewBox="0 0 24 24"
		>
			<path
				stroke-linecap="round"
				stroke-linejoin="round"
				stroke-width="2"
				d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14"
			/>
		</svg>
		Mehr lesen
	</a>
</div>

<style>
	.source-card {
		background: #ffffff;
		border: 1px solid #e2e8f0;
		border-radius: 12px;
		padding: 16px;
		transition: all 0.2s ease;
		cursor: pointer;
	}

	.source-card:hover {
		border-color: rgba(59, 130, 246, 0.3);
		box-shadow: 0 4px 16px rgba(0, 0, 0, 0.06);
	}

	.source-card.checking {
		border-color: #3b82f6;
		box-shadow: 0 0 0 0 rgba(59, 130, 246, 0.4);
		animation: pulse 2s cubic-bezier(0.4, 0, 0.6, 1) infinite;
	}

	.source-card.checked {
		border-color: #86efac;
		background: rgba(240, 253, 244, 0.3);
	}

	@keyframes pulse {
		0%, 100% { box-shadow: 0 0 0 0 rgba(59, 130, 246, 0.4); }
		50% { box-shadow: 0 0 0 8px rgba(59, 130, 246, 0); }
	}

	@keyframes checkmarkAppear {
		0% { transform: scale(0) rotate(-45deg); opacity: 0; }
		50% { transform: scale(1.2) rotate(5deg); }
		100% { transform: scale(1) rotate(0deg); opacity: 1; }
	}

	.checkmark-appear {
		animation: checkmarkAppear 0.4s ease-out;
	}

	.line-clamp-2 {
		display: -webkit-box;
		-webkit-line-clamp: 2;
		-webkit-box-orient: vertical;
		overflow: hidden;
	}

	.line-clamp-3 {
		display: -webkit-box;
		-webkit-line-clamp: 3;
		-webkit-box-orient: vertical;
		overflow: hidden;
	}
</style>
