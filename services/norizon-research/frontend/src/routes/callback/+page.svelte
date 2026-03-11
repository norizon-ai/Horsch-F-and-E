<script lang="ts">
	import { onMount } from 'svelte';
	import { goto } from '$app/navigation';
	import { authStore, authLoading } from '$lib/stores/authStore';
	import { chatStore, currentSessionId } from '$lib/stores/chatStore';

	let processing = $state(true);

	onMount(async () => {
		try {
			await new Promise<void>((resolve) => {
				let unsubscribe: () => void;
				unsubscribe = authStore.subscribe((state) => {
					if (!state.isLoading) {
						unsubscribe();
						resolve();
					}
				});
			});

			const isAuth = await authStore.checkAuth();

			if (isAuth) {
				const sessionId = chatStore.createSession();
				currentSessionId.set(sessionId);
				goto(`/chat/${sessionId}`);
			} else {
				goto('/');
			}
		} catch (err) {
			console.error('Callback error:', err);
			goto('/');
		} finally {
			processing = false;
		}
	});
</script>

<svelte:head>
	<title>Authentifizierung...</title>
</svelte:head>

{#if processing}
	<div class="callback-container">
		<div class="spinner"></div>
	</div>
{/if}

<style>
	.callback-container {
		display: flex;
		align-items: center;
		justify-content: center;
		min-height: 100vh;
		background: white;
	}

	.spinner {
		width: 40px;
		height: 40px;
		border: 3px solid #e2e8f0;
		border-top-color: #f97316;
		border-radius: 50%;
		animation: spin 0.8s linear infinite;
	}

	@keyframes spin {
		to { transform: rotate(360deg); }
	}
</style>
