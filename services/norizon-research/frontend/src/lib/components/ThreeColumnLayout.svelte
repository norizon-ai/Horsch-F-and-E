<script lang="ts">
	import { goto } from "$app/navigation";
	import { onMount } from "svelte";
	import { showSources } from "$stores/chatStore";

	let {
		appTitle = "Nora",
		children,
		navCenter,
		navActions,
		sidebarHeader,
		leftSidebar,
		rightPanel,
	} = $props();

	let leftDrawerOpen = $state(false);
	let rightDrawerOpen = $state(false);
	let isMobile = $state(false);

	onMount(() => {
		const checkMobile = () => {
			isMobile = window.innerWidth < 1024;
		};
		checkMobile();
		window.addEventListener("resize", checkMobile);
		return () => window.removeEventListener("resize", checkMobile);
	});

	function handleHomeClick() {
		goto("/");
	}

	function toggleSources() {
		showSources.update((v) => !v);
	}

	$effect(() => {
		if (typeof document !== "undefined") {
			if (leftDrawerOpen || rightDrawerOpen) {
				document.body.style.overflow = "hidden";
			} else {
				document.body.style.overflow = "";
			}
		}
	});
</script>

<!-- Animated Background -->
<div class="fixed inset-0 -z-10 overflow-hidden bg-gradient-to-br from-white via-slate-50 to-blue-50/30">
	<div class="absolute inset-0 opacity-30">
		{#each Array(50) as _, i}
			<div
				class="absolute w-1 h-1 bg-blue-600 rounded-full animate-float"
				style="
					left: {Math.random() * 100}%;
					top: {Math.random() * 100}%;
					animation-delay: {Math.random() * 5}s;
					animation-duration: {15 + Math.random() * 10}s;
				"
			></div>
		{/each}
	</div>
</div>

<div class="h-screen flex flex-col bg-transparent">
	<!-- Top Navigation Bar -->
	<nav class="bg-white/80 backdrop-blur-md border-b border-gray-200/50 px-4 md:px-6 py-3 md:py-4 flex items-center justify-between shadow-sm">
		<div class="flex items-center space-x-2 md:space-x-4">
			{#if isMobile}
				<button
					onclick={() => (leftDrawerOpen = !leftDrawerOpen)}
					class="p-2 hover:bg-gray-100 rounded-lg transition-colors"
					title="Toggle Sessions"
				>
					<svg class="w-5 h-5 text-gray-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
						<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16" />
					</svg>
				</button>
			{/if}
			<button onclick={handleHomeClick} class="flex items-center space-x-3 md:space-x-4 hover:opacity-80 transition-opacity">
				<img src="/favicon.png" alt="Nora Logo" class="h-6 md:h-8 w-6 md:w-8 object-contain" />
				<span class="text-xl md:text-2xl font-bold" style="color: #1e3a8a;">{appTitle}</span>
			</button>
		</div>

		<div class="flex items-center space-x-2 md:space-x-4 text-sm md:text-base">
			{@render navCenter?.()}
		</div>

		<div class="flex items-center space-x-2 md:space-x-3">
			{@render navActions?.()}
		</div>
	</nav>

	<!-- 3-Column Layout -->
	<div class="flex-1 flex overflow-hidden relative">
		<!-- Left Sidebar: Sessions (Desktop) -->
		<aside class="hidden lg:flex lg:flex-col lg:w-72 bg-white/80 backdrop-blur-md border-r border-gray-200/50 overflow-y-auto">
			<div class="p-4">
				{@render sidebarHeader?.()}
				{@render leftSidebar?.()}
			</div>
		</aside>

		<!-- Left Sidebar: Mobile Drawer -->
		{#if leftDrawerOpen && isMobile}
			<div class="fixed inset-0 z-50">
				<div class="absolute inset-0 bg-black/50" onclick={() => (leftDrawerOpen = false)}></div>
				<aside class="absolute left-0 top-0 bottom-0 w-80 bg-white shadow-xl overflow-y-auto">
					<div class="p-4 border-b border-gray-200">
						<div class="flex items-center justify-between mb-4">
							<h2 class="text-lg font-semibold text-gray-900">Sessions</h2>
							<button onclick={() => (leftDrawerOpen = false)} class="p-2 hover:bg-gray-100 rounded-lg">
								<svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
									<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
								</svg>
							</button>
						</div>
					</div>
					<div class="p-4">
						{@render sidebarHeader?.()}
						{@render leftSidebar?.()}
					</div>
				</aside>
			</div>
		{/if}

		<!-- Main Content -->
		<main class="flex-1 overflow-hidden bg-transparent">
			{@render children?.()}
		</main>

		<!-- Right Panel: Sources (Desktop) -->
		{#if $showSources}
			<aside class="hidden lg:block lg:w-80 xl:w-96 bg-white border-l border-gray-200 overflow-y-auto">
				<div class="p-4 md:p-6">
					<h2 class="text-lg font-semibold text-gray-900 mb-4 flex items-center">
						<svg class="w-5 h-5 mr-2 text-orange-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
							<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" />
						</svg>
						Sources
					</h2>
					{@render rightPanel?.()}
				</div>
			</aside>
		{/if}

		<!-- Right Panel: Mobile Drawer -->
		{#if rightDrawerOpen && isMobile}
			<div class="fixed inset-0 z-50">
				<div class="absolute inset-0 bg-black/50" onclick={() => (rightDrawerOpen = false)}></div>
				<aside class="absolute right-0 top-0 bottom-0 w-full bg-white shadow-xl overflow-y-auto">
					<div class="p-4 border-b border-gray-200">
						<div class="flex items-center justify-between mb-4">
							<h2 class="text-lg font-semibold text-gray-900 flex items-center">
								<svg class="w-5 h-5 mr-2 text-orange-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
									<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" />
								</svg>
								Sources
							</h2>
							<button onclick={() => (rightDrawerOpen = false)} class="p-2 hover:bg-gray-100 rounded-lg">
								<svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
									<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
								</svg>
							</button>
						</div>
					</div>
					<div class="p-4">
						{@render rightPanel?.()}
					</div>
				</aside>
			</div>
		{/if}
	</div>

	<!-- Mobile Bottom Navigation -->
	{#if isMobile}
		<nav class="fixed bottom-0 left-0 right-0 bg-white border-t border-gray-200 shadow-lg z-40">
			<div class="flex justify-around items-center h-16">
				<button
					onclick={() => (leftDrawerOpen = !leftDrawerOpen)}
					class="flex flex-col items-center justify-center flex-1 h-full hover:bg-gray-50 transition-colors"
					class:text-blue-600={leftDrawerOpen}
					class:text-gray-600={!leftDrawerOpen}
				>
					<svg class="w-6 h-6 mb-1" fill="none" stroke="currentColor" viewBox="0 0 24 24">
						<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 10h.01M12 10h.01M16 10h.01M9 16H5a2 2 0 01-2-2V6a2 2 0 012-2h14a2 2 0 012 2v8a2 2 0 01-2 2h-5l-5 5v-5z" />
					</svg>
					<span class="text-xs font-medium">Sessions</span>
				</button>

				<button
					onclick={() => (rightDrawerOpen = !rightDrawerOpen)}
					class="flex flex-col items-center justify-center flex-1 h-full hover:bg-gray-50 transition-colors"
					class:text-orange-500={rightDrawerOpen}
					class:text-gray-600={!rightDrawerOpen}
				>
					<svg class="w-6 h-6 mb-1" fill="none" stroke="currentColor" viewBox="0 0 24 24">
						<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" />
					</svg>
					<span class="text-xs font-medium">Sources</span>
				</button>

				<button
					onclick={handleHomeClick}
					class="flex flex-col items-center justify-center flex-1 h-full hover:bg-gray-50 transition-colors text-gray-600"
				>
					<svg class="w-6 h-6 mb-1" fill="none" stroke="currentColor" viewBox="0 0 24 24">
						<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-6 0a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1m-6 0h6" />
					</svg>
					<span class="text-xs font-medium">Home</span>
				</button>
			</div>
		</nav>
	{/if}
</div>

<style>
	img { object-fit: contain; }

	@keyframes float {
		0%, 100% { transform: translateY(0px) translateX(0px); opacity: 0.3; }
		50% { transform: translateY(-20px) translateX(10px); opacity: 0.6; }
	}

	.animate-float {
		animation: float linear infinite;
	}
</style>
