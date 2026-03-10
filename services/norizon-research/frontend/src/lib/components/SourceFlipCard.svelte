<script lang="ts">
	export let sourceName = "";
	export let sourceUrl = "";

	$: domain = (() => {
		try {
			return new URL(sourceUrl).hostname.replace("www.", "");
		} catch {
			return sourceUrl;
		}
	})();

	$: faviconUrl = (() => {
		try {
			new URL(sourceUrl);
			return `https://logo.clearbit.com/${domain}`;
		} catch {
			return "";
		}
	})();

	function handleFaviconError(event: Event) {
		const img = event.target as HTMLImageElement;
		img.src = `https://www.google.com/s2/favicons?domain=${domain}&sz=64`;
	}
</script>

<div class="flip-card">
	<div class="flip-card-inner">
		<!-- Front -->
		<div class="flip-card-face flip-card-front">
			<div
				class="w-16 h-16 rounded-xl overflow-hidden bg-gray-100 flex items-center justify-center border-2 border-norizon-blue shadow-lg"
			>
				<img
					src={faviconUrl}
					alt={domain}
					class="w-full h-full object-contain p-2"
					on:error={handleFaviconError}
				/>
			</div>
		</div>
		<!-- Back -->
		<div class="flip-card-face flip-card-back">
			<div
				class="w-16 h-16 rounded-xl bg-gradient-to-br from-norizon-blue to-norizon-orange flex items-center justify-center shadow-lg"
			>
				<svg
					class="w-8 h-8 text-white"
					fill="none"
					stroke="currentColor"
					viewBox="0 0 24 24"
				>
					<path
						stroke-linecap="round"
						stroke-linejoin="round"
						stroke-width="2"
						d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"
					/>
				</svg>
			</div>
		</div>
	</div>
	<p
		class="text-xs text-center mt-2 text-gray-600 font-medium truncate max-w-[80px]"
	>
		{domain}
	</p>
</div>

<style>
	.flip-card {
		perspective: 1000px;
		display: inline-block;
	}

	.flip-card-inner {
		position: relative;
		width: 64px;
		height: 64px;
		transition: transform 0.8s;
		transform-style: preserve-3d;
		animation: flip 2s ease-in-out infinite;
	}

	.flip-card-face {
		position: absolute;
		width: 100%;
		height: 100%;
		backface-visibility: hidden;
		-webkit-backface-visibility: hidden;
	}

	.flip-card-front {
		transform: rotateY(0deg);
	}

	.flip-card-back {
		transform: rotateY(180deg);
	}

	@keyframes flip {
		0% {
			transform: rotateY(0deg);
		}
		50% {
			transform: rotateY(180deg);
		}
		100% {
			transform: rotateY(360deg);
		}
	}
</style>
