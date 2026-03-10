<script lang="ts">
	import { createEventDispatcher } from 'svelte';
	import { locale, t } from 'svelte-i18n';
	import { authStore, currentUser, isAuthenticated } from '$lib/stores/authStore';

	const dispatch = createEventDispatcher<{
		share: void;
		settings: void;
	}>();

	let currentLocale = 'de';

	// Subscribe to locale changes
	locale.subscribe(value => {
		if (value) currentLocale = value;
	});

	function setLocale(newLocale: string) {
		locale.set(newLocale);
		currentLocale = newLocale;
		// Save preference to localStorage
		if (typeof localStorage !== 'undefined') {
			localStorage.setItem('locale', newLocale);
		}
	}

	function handleLogout() {
		authStore.logout();
	}
</script>

<header class="chat-header">
	<div class="chat-header-left">
		{#if $isAuthenticated && $currentUser}
			<div class="user-info">
				<div class="user-avatar">
					{($currentUser.email || '?').charAt(0).toUpperCase()}
				</div>
				<span class="user-email">{$currentUser.email}</span>
				<button class="logout-btn" on:click={handleLogout} title="Logout">
					<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
						<path d="M9 21H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h4"/>
						<polyline points="16 17 21 12 16 7"/>
						<line x1="21" y1="12" x2="9" y2="12"/>
					</svg>
					Logout
				</button>
			</div>
		{/if}
	</div>

	<div class="header-controls">
		<!-- Language segmented control -->
		<div class="lang-segmented">
			<button
				class="lang-option"
				class:active={currentLocale === 'de'}
				on:click={() => setLocale('de')}
				title="Deutsch"
			>
				DE
			</button>
			<button
				class="lang-option"
				class:active={currentLocale === 'en'}
				on:click={() => setLocale('en')}
				title="English"
			>
				EN
			</button>
		</div>

		<!-- Divider -->
		<div class="header-divider"></div>

		<!-- Share button -->
		<button
			class="header-btn"
			title={$t('common.share')}
			on:click={() => dispatch('share')}
		>
			<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
				<circle cx="18" cy="5" r="3" />
				<circle cx="6" cy="12" r="3" />
				<circle cx="18" cy="19" r="3" />
				<line x1="8.59" y1="13.51" x2="15.42" y2="17.49" />
				<line x1="15.41" y1="6.51" x2="8.59" y2="10.49" />
			</svg>
		</button>
	</div>
</header>

<style>
	.chat-header {
		padding: 12px 24px;
		border-bottom: 1px solid var(--slate-200, #e2e8f0);
		background: var(--white, #ffffff);
		display: flex;
		align-items: center;
		justify-content: space-between;
		min-height: 56px;
	}

	.chat-header-left {
		display: flex;
		align-items: center;
		gap: 12px;
		flex: 1;
	}

	.user-info {
		display: flex;
		align-items: center;
		gap: 12px;
	}

	.user-avatar {
		width: 32px;
		height: 32px;
		border-radius: 50%;
		background: linear-gradient(135deg, var(--orange-500) 0%, var(--orange-400) 100%);
		color: white;
		display: flex;
		align-items: center;
		justify-content: center;
		font-weight: 600;
		font-size: 14px;
	}

	.user-email {
		font-size: 14px;
		color: var(--slate-700);
		font-weight: 500;
	}

	.logout-btn {
		display: flex;
		align-items: center;
		gap: 6px;
		padding: 6px 12px;
		background: var(--slate-50);
		border: 1px solid var(--slate-200);
		border-radius: var(--radius-sm);
		font-size: 13px;
		font-weight: 500;
		color: var(--slate-600);
		cursor: pointer;
		transition: all 0.15s ease;
	}

	.logout-btn:hover {
		background: var(--slate-100);
		color: var(--slate-700);
		border-color: var(--slate-300);
	}

	.logout-btn svg {
		width: 16px;
		height: 16px;
	}

	/* Grouped controls container */
	.header-controls {
		display: flex;
		align-items: center;
		gap: 8px;
		background: var(--slate-50, #f8fafc);
		padding: 4px 6px;
		border-radius: var(--radius-md, 10px);
		border: 1px solid var(--slate-200, #e2e8f0);
	}

	/* Language segmented control */
	.lang-segmented {
		display: flex;
		background: var(--white, #ffffff);
		border-radius: 6px;
		padding: 2px;
	}

	.lang-option {
		padding: 5px 10px;
		background: transparent;
		border: none;
		border-radius: 4px;
		font-size: 12px;
		font-weight: 600;
		color: var(--slate-500, #64748b);
		cursor: pointer;
		transition: all 0.15s ease;
	}

	.lang-option:hover:not(.active) {
		color: var(--slate-700, #334155);
	}

	.lang-option.active {
		background: var(--deep-blue, #1e3a5f);
		color: var(--white, #ffffff);
	}

	/* Divider */
	.header-divider {
		width: 1px;
		height: 18px;
		background: var(--slate-200, #e2e8f0);
	}

	/* Icon button */
	.header-btn {
		padding: 6px;
		background: var(--white, #ffffff);
		border: none;
		border-radius: 6px;
		cursor: pointer;
		color: var(--slate-500, #64748b);
		transition: all 0.15s ease;
		display: flex;
		align-items: center;
		justify-content: center;
	}

	.header-btn:hover {
		background: var(--slate-100, #f1f5f9);
		color: var(--slate-700, #334155);
	}

	.header-btn svg {
		width: 18px;
		height: 18px;
	}
</style>
