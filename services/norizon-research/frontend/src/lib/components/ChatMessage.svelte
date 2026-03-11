<script lang="ts">
	import type { Message } from "$types";
	import { marked } from "marked";

	let {
		message,
		showExportOptions = false,
		onExportPDF = undefined,
		onExportWord = undefined,
		onExportSharepoint = undefined,
	}: {
		message: Message;
		showExportOptions?: boolean;
		onExportPDF?: (() => void) | undefined;
		onExportWord?: (() => void) | undefined;
		onExportSharepoint?: (() => void) | undefined;
	} = $props();

	// Configure marked for safe rendering
	marked.setOptions({
		breaks: true,
		gfm: true,
	});

	let renderedContent = $derived(marked(message.content || ""));
	let isUser = $derived(message.role === "user");
</script>

<div class="chat-message w-full py-6 px-4">
	<div class="max-w-5xl mx-auto">
		<div
			class="flex items-start gap-4 {isUser
				? 'flex-row-reverse'
				: 'flex-row'}"
		>
			<!-- Avatar -->
			<div class="flex-shrink-0 pt-1">
				{#if isUser}
					<div
						class="w-8 h-8 rounded-full bg-gray-200 flex items-center justify-center shadow-sm"
					>
						<svg
							class="w-4 h-4 text-gray-600"
							fill="currentColor"
							viewBox="0 0 20 20"
						>
							<path
								fill-rule="evenodd"
								d="M10 9a3 3 0 100-6 3 3 0 000 6zm-7 9a7 7 0 1114 0H3z"
								clip-rule="evenodd"
							/>
						</svg>
					</div>
				{:else}
					<div
						class="w-8 h-8 rounded-lg bg-white border border-gray-200 p-1.5 shadow-sm flex items-center justify-center"
					>
						<img
							src="/favicon.png"
							alt="Nora"
							class="w-full h-full object-contain"
						/>
					</div>
				{/if}
			</div>

			<!-- Message Content -->
			<div class={isUser ? "max-w-[85%]" : "flex-1 min-w-0"}>
				<!-- Role Label -->
				<div
					class="text-sm font-semibold text-gray-900 mb-2 {isUser
						? 'text-right'
						: 'text-left'}"
				>
					{isUser ? "You" : "Nora"}
				</div>

				<!-- Sources (moved to top) -->
				{#if message.sources && message.sources.length > 0 && !isUser}
					<div class="mb-4 pl-2">
						<div
							class="text-xs font-semibold text-gray-500 uppercase tracking-wide mb-2"
						>
							Sources
						</div>
						<div class="flex flex-wrap gap-2">
							{#each message.sources as source, idx}
								<a
									href={source.url}
									target="_blank"
									rel="noopener noreferrer"
									class="inline-flex items-center px-2.5 py-1.5 text-xs bg-white/80 backdrop-blur-sm hover:bg-white text-gray-700 hover:text-norizon-blue rounded-lg border border-gray-200 hover:border-norizon-blue transition-all shadow-sm"
									title={source.title}
								>
									<svg
										class="w-3 h-3 mr-1.5 flex-shrink-0"
										fill="none"
										stroke="currentColor"
										viewBox="0 0 24 24"
									>
										<path
											stroke-linecap="round"
											stroke-linejoin="round"
											stroke-width="2"
											d="M13.828 10.172a4 4 0 00-5.656 0l-4 4a4 4 0 105.656 5.656l1.102-1.101m-.758-4.899a4 4 0 005.656 0l4-4a4 4 0 00-5.656-5.656l-1.1 1.1"
										/>
									</svg>
									<span class="font-medium">[{idx + 1}]</span>
									<span class="ml-1 max-w-[180px] truncate"
										>{source.title}</span
									>
								</a>
							{/each}
						</div>
					</div>
				{/if}

				<!-- Message Body -->
				<div
					class="rounded-2xl px-5 py-4 {isUser
						? 'bg-gray-100 text-gray-900 shadow-sm inline-block border border-gray-200'
						: 'bg-white/80 backdrop-blur-sm text-gray-800 shadow-sm border border-gray-200'}"
				>
					{#if message.isStreaming}
						<div class="flex items-center space-x-2 py-2">
							<div
								class="typing-dot w-2 h-2 bg-current rounded-full animate-bounce"
							></div>
							<div
								class="typing-dot w-2 h-2 bg-current rounded-full animate-bounce"
								style="animation-delay: 0.2s"
							></div>
							<div
								class="typing-dot w-2 h-2 bg-current rounded-full animate-bounce"
								style="animation-delay: 0.4s"
							></div>
						</div>
					{:else}
						<div
							class="prose {isUser
								? 'prose-slate'
								: 'prose-slate'} max-w-none prose-headings:font-semibold"
						>
							{@html renderedContent}
						</div>
					{/if}
				</div>

				<!-- Timestamp -->
				<div
					class="text-xs text-gray-400 mt-2 {isUser
						? 'text-right'
						: 'text-left'} pl-2"
				>
					{new Date(message.timestamp).toLocaleTimeString("en-US", {
						hour: "2-digit",
						minute: "2-digit",
					})}
				</div>

				<!-- Export Options (for assistant messages only) -->
				{#if !isUser && !message.isStreaming && showExportOptions}
					<div class="mt-4 pl-2">
						<div
							class="flex flex-wrap items-center gap-3 p-4 bg-gray-50 rounded-xl border border-gray-200"
						>
							<span class="text-sm font-medium text-gray-700"
								>Share it with your colleagues:</span
							>
							<div class="flex gap-2">
								<button
									onclick={() => onExportPDF?.()}
									class="flex items-center gap-2 px-3 py-2 bg-white hover:bg-norizon-blue hover:text-white rounded-lg transition-all text-sm font-medium text-gray-700 border border-gray-200 hover:border-norizon-blue shadow-sm"
								>
									<svg
										class="w-4 h-4"
										fill="none"
										stroke="currentColor"
										viewBox="0 0 24 24"
									>
										<path
											stroke-linecap="round"
											stroke-linejoin="round"
											stroke-width="2"
											d="M7 21h10a2 2 0 002-2V9.414a1 1 0 00-.293-.707l-5.414-5.414A1 1 0 0012.586 3H7a2 2 0 00-2 2v14a2 2 0 002 2z"
										/>
									</svg>
									PDF
								</button>
								<button
									onclick={() => onExportWord?.()}
									class="flex items-center gap-2 px-3 py-2 bg-white hover:bg-norizon-orange hover:text-white rounded-lg transition-all text-sm font-medium text-gray-700 border border-gray-200 hover:border-norizon-orange shadow-sm"
								>
									<svg
										class="w-4 h-4"
										fill="none"
										stroke="currentColor"
										viewBox="0 0 24 24"
									>
										<path
											stroke-linecap="round"
											stroke-linejoin="round"
											stroke-width="2"
											d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"
										/>
									</svg>
									Word
								</button>
								<button
									onclick={() => onExportSharepoint?.()}
									class="flex items-center gap-2 px-3 py-2 bg-white hover:bg-green-600 hover:text-white rounded-lg transition-all text-sm font-medium text-gray-700 border border-gray-200 hover:border-green-600 shadow-sm"
								>
									<svg
										class="w-4 h-4"
										fill="none"
										stroke="currentColor"
										viewBox="0 0 24 24"
									>
										<path
											stroke-linecap="round"
											stroke-linejoin="round"
											stroke-width="2"
											d="M8.684 13.342C8.886 12.938 9 12.482 9 12c0-.482-.114-.938-.316-1.342m0 2.684a3 3 0 110-2.684m0 2.684l6.632 3.316m-6.632-6l6.632-3.316m0 0a3 3 0 105.367-2.684 3 3 0 00-5.367 2.684zm0 9.316a3 3 0 105.368 2.684 3 3 0 00-5.368-2.684z"
										/>
									</svg>
									SharePoint
								</button>
							</div>
						</div>
					</div>
				{/if}
			</div>
		</div>
	</div>
</div>

<style>
	/* Enhanced prose styling */
	:global(.prose) {
		@apply text-[15px] leading-relaxed;
	}

	:global(.prose h1) {
		@apply text-2xl font-bold mt-6 mb-3 pb-2 border-b;
	}

	:global(.prose h2) {
		@apply text-xl font-semibold mt-5 mb-2;
	}

	:global(.prose h3) {
		@apply text-lg font-semibold mt-4 mb-2;
	}

	:global(.prose h4) {
		@apply text-base font-semibold mt-3 mb-1.5;
	}

	:global(.prose h5) {
		@apply text-sm font-semibold mt-3 mb-1.5;
	}

	:global(.prose h6) {
		@apply text-xs font-semibold mt-2 mb-1 uppercase tracking-wide;
	}

	:global(.prose p) {
		@apply mb-3 leading-7;
	}

	:global(.prose ul),
	:global(.prose ol) {
		@apply my-3 ml-5 space-y-1.5;
	}

	:global(.prose li) {
		@apply leading-7;
	}

	:global(.prose strong) {
		@apply font-semibold;
	}

	:global(.prose em) {
		@apply italic;
	}

	:global(.prose a) {
		@apply underline decoration-1 underline-offset-2 transition-colors;
	}

	/* Non-inverted prose (assistant messages) */
	:global(.prose-slate) {
		@apply text-gray-800;
	}

	:global(.prose-slate h1),
	:global(.prose-slate h2),
	:global(.prose-slate h3),
	:global(.prose-slate h4),
	:global(.prose-slate h5),
	:global(.prose-slate h6) {
		@apply text-gray-900;
	}

	:global(.prose-slate h1) {
		@apply border-gray-200;
	}

	:global(.prose-slate strong) {
		@apply text-gray-900;
	}

	:global(.prose-slate a) {
		@apply text-norizon-blue hover:text-norizon-orange;
	}

	:global(.prose-slate code) {
		@apply text-sm bg-gray-100 px-1.5 py-0.5 rounded font-mono text-norizon-blue border border-gray-200;
	}

	:global(.prose-slate pre) {
		@apply bg-gray-900 text-gray-100 p-4 rounded-lg my-4 overflow-x-auto shadow-inner;
	}

	:global(.prose-slate pre code) {
		@apply bg-transparent text-gray-100 p-0 border-0;
	}

	:global(.prose-slate blockquote) {
		@apply border-l-4 border-norizon-orange pl-4 italic text-gray-700 my-4 bg-gray-50 py-2;
	}

	:global(.prose-slate table) {
		@apply w-full my-4 border-collapse;
	}

	:global(.prose-slate th) {
		@apply bg-gray-100 font-semibold text-left p-2.5 border border-gray-300;
	}

	:global(.prose-slate td) {
		@apply p-2.5 border border-gray-300;
	}

	:global(.prose-slate hr) {
		@apply my-6 border-gray-200;
	}

	/* Inverted prose (user messages) */
	:global(.prose-invert) {
		@apply text-white;
	}

	:global(.prose-invert h1),
	:global(.prose-invert h2),
	:global(.prose-invert h3),
	:global(.prose-invert h4),
	:global(.prose-invert h5),
	:global(.prose-invert h6) {
		@apply text-white;
	}

	:global(.prose-invert h1) {
		@apply border-white/30;
	}

	:global(.prose-invert strong) {
		@apply text-white font-semibold;
	}

	:global(.prose-invert a) {
		@apply text-white/90 hover:text-white;
	}

	:global(.prose-invert code) {
		@apply bg-white/20 text-white border-white/30;
	}

	:global(.prose-invert pre) {
		@apply bg-black/30 text-white;
	}

	:global(.prose-invert pre code) {
		@apply bg-transparent;
	}

	:global(.prose-invert blockquote) {
		@apply border-white/50 text-white/90 bg-white/10;
	}

	:global(.prose-invert table) {
		@apply border-white/30;
	}

	:global(.prose-invert th) {
		@apply bg-white/20 border-white/30 text-white;
	}

	:global(.prose-invert td) {
		@apply border-white/30;
	}

	:global(.prose-invert hr) {
		@apply border-white/30;
	}

	@keyframes bounce {
		0%,
		100% {
			transform: translateY(0);
		}
		50% {
			transform: translateY(-4px);
		}
	}

	.animate-bounce {
		animation: bounce 1s ease-in-out infinite;
	}
</style>
