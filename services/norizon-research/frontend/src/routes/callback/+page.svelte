<script lang="ts">
	import { onMount } from 'svelte';
	import { goto } from '$app/navigation';
	import { authStore, authLoading } from '$lib/stores/authStore';
	import { chatStore, currentSessionId } from '$lib/stores/chatStore';

	let processing = true;

	onMount(async () => {
		try {
			console.log('📍 Callback page: Starting auth processing');

			// Wait for auth initialization to complete
			await new Promise<void>((resolve) => {
				let unsubscribe: () => void;
				unsubscribe = authStore.subscribe((state) => {
					console.log('📍 Auth state:', {
						isLoading: state.isLoading,
						isAuthenticated: state.isAuthenticated,
						error: state.error
					});
					if (!state.isLoading) {
						unsubscribe();
						resolve();
					}
				});
			});

			// Check if authentication was successful
			const isAuth = await authStore.checkAuth();
			console.log('📍 Callback page: isAuth =', isAuth);

			if (isAuth) {
				console.log('✅ Auth successful, creating session and redirecting to chat');
				// Create a new chat session and redirect
				const sessionId = chatStore.createSession();
				currentSessionId.set(sessionId);
				goto(`/chat/${sessionId}`);
			} else {
				console.log('❌ Auth failed, redirecting to landing');
				// Redirect to landing if auth failed
				goto('/');
			}
		} catch (err) {
			console.error('❌ Callback error:', err);
			// Redirect to landing on error
			goto('/');
		} finally {
			processing = false;
		}
	});
</script>

<svelte:head>
	<title>Authenticating...</title>
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
		border: 3px solid var(--slate-200);
		border-top-color: var(--orange-500);
		border-radius: 50%;
		animation: spin 0.8s linear infinite;
	}

	@keyframes spin {
		to { transform: rotate(360deg); }
	}
</style>

