<script lang="ts">
	import { locale, t } from "svelte-i18n";

	let {
		onshare = undefined as (() => void) | undefined,
		onmenu = undefined as (() => void) | undefined,
	} = $props();

	let currentLocale = $state("de");

	const unsubLocale = locale.subscribe((value) => {
		if (value) currentLocale = value;
	});

	function setLocale(newLocale: string) {
		locale.set(newLocale);
		currentLocale = newLocale;
		if (typeof localStorage !== "undefined") {
			localStorage.setItem("locale", newLocale);
		}
	}
</script>

<header class="chat-header">
	<div class="header-controls">
		<div class="lang-segmented">
			<button
				class="lang-option"
				class:active={currentLocale === "de"}
				onclick={() => setLocale("de")}
				title="Deutsch"
			>
				DE
			</button>
			<button
				class="lang-option"
				class:active={currentLocale === "en"}
				onclick={() => setLocale("en")}
				title="English"
			>
				EN
			</button>
		</div>

		<button
			class="share-btn"
			title={$t("common.share")}
			onclick={() => onshare?.()}
		>
			<svg
				viewBox="0 0 24 24"
				fill="none"
				stroke="currentColor"
				stroke-width="2"
				stroke-linecap="round"
				stroke-linejoin="round"
			>
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
		height: 56px;
		padding: 0 24px;
		border-bottom: 1px solid #f3f4f6;
		background: transparent;
		display: flex;
		align-items: center;
		justify-content: flex-end;
		flex-shrink: 0;
	}

	.header-controls {
		display: flex;
		align-items: center;
		gap: 8px;
	}

	.lang-segmented {
		display: flex;
		background: #f1f5f9;
		border-radius: 20px;
		padding: 3px;
		gap: 2px;
	}

	.lang-option {
		padding: 6px 14px;
		background: transparent;
		border: none;
		border-radius: 16px;
		font-size: 13px;
		font-weight: 600;
		color: #64748b;
		cursor: pointer;
		transition: background 0.15s ease, color 0.15s ease;
		line-height: 1;
	}

	.lang-option:hover:not(.active) {
		color: #334155;
	}

	.lang-option.active {
		background: #0f172a;
		color: #ffffff;
	}

	.share-btn {
		width: 38px;
		height: 38px;
		padding: 0;
		background: transparent;
		border: none;
		border-radius: 8px;
		cursor: pointer;
		color: #94a3b8;
		transition: background 0.15s ease, color 0.15s ease;
		display: flex;
		align-items: center;
		justify-content: center;
	}

	.share-btn:hover {
		background: #f1f5f9;
		color: #475569;
	}

	.share-btn svg {
		width: 18px;
		height: 18px;
	}
</style>
