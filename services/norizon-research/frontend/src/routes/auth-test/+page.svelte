<script lang="ts">
	import { authStore, currentUser, isAuthenticated, authLoading } from '$lib/stores/authStore';
	import { AuthenticatedAPI } from '$lib/api/workflowAuthApi';
	import { onMount } from 'svelte';

	let testResult = '';
	let backendUser: any = null;
	let history: any = null;
	let loading = false;
	let error = '';

	onMount(() => {
		authStore.initialize();
	});

	async function testBackendAuth() {
		loading = true;
		error = '';
		testResult = '';
		backendUser = null;

		try {
			const result = await AuthenticatedAPI.testAuth();
			testResult = JSON.stringify(result, null, 2);
		} catch (err) {
			error = err instanceof Error ? err.message : 'Auth test failed';
			console.error('❌ Auth test error:', err);
		} finally {
			loading = false;
		}
	}

	async function fetchCurrentUser() {
		loading = true;
		error = '';
		backendUser = null;

		try {
			const user = await AuthenticatedAPI.getCurrentUser();
			backendUser = user;
		} catch (err) {
			error = err instanceof Error ? err.message : 'Failed to fetch user';
			console.error('❌ User fetch error:', err);
		} finally {
			loading = false;
		}
	}

	async function fetchHistory() {
		loading = true;
		error = '';
		history = null;

		try {
			const result = await AuthenticatedAPI.getHistory();
			history = result;
		} catch (err) {
			error = err instanceof Error ? err.message : 'Failed to fetch history';
			console.error('❌ History fetch error:', err);
		} finally {
			loading = false;
		}
	}

	async function getToken() {
		const token = await authStore.getAccessToken();
		if (token) {
			alert('Token (first 50 chars): ' + token.substring(0, 50) + '...');
		} else {
			alert('No token available');
		}
	}
</script>

<div class="container">
	<h1>Auth0 Authentication Test</h1>

	<div class="section">
		<h2>Auth0 Client Status</h2>
		{#if $authLoading}
			<p class="loading">Loading authentication state...</p>
		{:else if $isAuthenticated}
			<div class="success-box">
				<p><strong>✅ Authenticated</strong></p>
				<p>User: {$currentUser?.email || 'Unknown'}</p>
				<p>Name: {$currentUser?.name || 'Unknown'}</p>
				<button onclick={() => authStore.logout()} class="btn-secondary">
					Logout
				</button>
			</div>
		{:else}
			<div class="warning-box">
				<p>❌ Not authenticated</p>
				<button onclick={() => authStore.login()} class="btn-primary">
					Login with Auth0
				</button>
			</div>
		{/if}
	</div>

	{#if $isAuthenticated}
		<div class="section">
			<h2>Token Management</h2>
			<button onclick={getToken} class="btn-secondary">
				View Access Token
			</button>
		</div>

		<div class="section">
			<h2>Backend API Tests</h2>
			<div class="button-group">
				<button onclick={testBackendAuth} disabled={loading} class="btn-primary">
					Test Auth Endpoint
				</button>
				<button onclick={fetchCurrentUser} disabled={loading} class="btn-primary">
					Get Current User
				</button>
				<button onclick={fetchHistory} disabled={loading} class="btn-primary">
					Fetch History
				</button>
			</div>

			{#if loading}
				<p class="loading">Loading...</p>
			{/if}

			{#if error}
				<div class="error-box">
					<strong>Error:</strong> {error}
				</div>
			{/if}

			{#if testResult}
				<div class="result-box">
					<h3>Auth Test Result:</h3>
					<pre>{testResult}</pre>
				</div>
			{/if}

			{#if backendUser}
				<div class="result-box">
					<h3>Backend User Info:</h3>
					<pre>{JSON.stringify(backendUser, null, 2)}</pre>
				</div>
			{/if}

			{#if history}
				<div class="result-box">
					<h3>History:</h3>
					<pre>{JSON.stringify(history, null, 2)}</pre>
				</div>
			{/if}
		</div>
	{/if}
</div>

<style>
	.container {
		max-width: 800px;
		margin: 0 auto;
		padding: 40px 20px;
	}

	h1 {
		font-size: 32px;
		font-weight: 600;
		color: #1f2937;
		margin-bottom: 32px;
	}

	h2 {
		font-size: 20px;
		font-weight: 600;
		color: #374151;
		margin-bottom: 16px;
	}

	h3 {
		font-size: 16px;
		font-weight: 600;
		color: #4b5563;
		margin-bottom: 8px;
	}

	.section {
		background: white;
		border: 1px solid #e5e7eb;
		border-radius: 8px;
		padding: 24px;
		margin-bottom: 24px;
	}

	.success-box {
		background: #dcfce7;
		border: 1px solid #86efac;
		border-radius: 8px;
		padding: 16px;
	}

	.warning-box {
		background: #fef3c7;
		border: 1px solid #fcd34d;
		border-radius: 8px;
		padding: 16px;
	}

	.error-box {
		background: #fee2e2;
		border: 1px solid #fca5a5;
		border-radius: 8px;
		padding: 16px;
		color: #991b1b;
		margin-top: 16px;
	}

	.result-box {
		background: #f3f4f6;
		border: 1px solid #d1d5db;
		border-radius: 8px;
		padding: 16px;
		margin-top: 16px;
	}

	.button-group {
		display: flex;
		gap: 12px;
		flex-wrap: wrap;
	}

	.btn-primary {
		background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
		color: white;
		border: none;
		padding: 10px 20px;
		border-radius: 8px;
		font-size: 14px;
		font-weight: 500;
		cursor: pointer;
		transition: transform 0.2s;
	}

	.btn-primary:hover:not(:disabled) {
		transform: translateY(-1px);
	}

	.btn-primary:disabled {
		opacity: 0.5;
		cursor: not-allowed;
	}

	.btn-secondary {
		background: white;
		color: #667eea;
		border: 1px solid #667eea;
		padding: 10px 20px;
		border-radius: 8px;
		font-size: 14px;
		font-weight: 500;
		cursor: pointer;
		transition: all 0.2s;
	}

	.btn-secondary:hover {
		background: #667eea;
		color: white;
	}

	.loading {
		color: #6b7280;
		font-style: italic;
	}

	pre {
		background: #1f2937;
		color: #e5e7eb;
		padding: 12px;
		border-radius: 6px;
		overflow-x: auto;
		font-size: 12px;
		line-height: 1.5;
	}

	p {
		margin: 8px 0;
	}
</style>
