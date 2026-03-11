<script lang="ts">
	import "../app.css";
	import { onMount } from "svelte";
	import { authStore } from "$lib/stores/authStore";
	import "$lib/i18n";
	import { isLoading as i18nLoading } from "svelte-i18n";

	let { children } = $props();

	onMount(() => {
		authStore.initialize();
	});
</script>

{#if $i18nLoading}
	<div class="loading-i18n">
		<div class="spinner"></div>
	</div>
{:else}
	{@render children()}
{/if}

<style>
	.loading-i18n {
		display: flex;
		align-items: center;
		justify-content: center;
		min-height: 100vh;
	}

	.spinner {
		width: 24px;
		height: 24px;
		border: 2px solid #e2e8f0;
		border-top-color: #3b82f6;
		border-radius: 50%;
		animation: spin 0.8s linear infinite;
	}

	@keyframes spin {
		to {
			transform: rotate(360deg);
		}
	}
</style>
