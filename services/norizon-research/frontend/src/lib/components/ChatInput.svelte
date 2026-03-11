<script lang="ts">
	import { t } from "svelte-i18n";

	let {
		disabled = false,
		onSubmit = undefined as ((query: string) => void) | undefined,
		onsubmit: onsubmitProp = undefined as ((query: string) => void) | undefined,
	} = $props();

	let input = $state("");
	let textarea: HTMLTextAreaElement | undefined = $state(undefined);

	let placeholder = $derived($t("search.placeholder") || "Frag Nora...");
	let hasContent = $derived(input.trim().length > 0);

	function handleSubmit() {
		const trimmed = input.trim();
		if (trimmed && !disabled) {
			onSubmit?.(trimmed);
			onsubmitProp?.(trimmed);
			input = "";
			if (textarea) {
				textarea.style.height = "auto";
			}
		}
	}

	function handleKeydown(e: KeyboardEvent) {
		if (e.key === "Enter" && !e.shiftKey) {
			e.preventDefault();
			handleSubmit();
		}
	}

	function autoResize() {
		if (textarea) {
			textarea.style.height = "auto";
			textarea.style.height = Math.min(textarea.scrollHeight, 200) + "px";
		}
	}
</script>

<div
	class="input-wrapper"
	class:disabled
>
	<textarea
		bind:this={textarea}
		bind:value={input}
		oninput={autoResize}
		onkeydown={handleKeydown}
		{placeholder}
		{disabled}
		rows="1"
		class="input-field"
	></textarea>
	<button
		type="button"
		onclick={handleSubmit}
		disabled={!hasContent || disabled}
		class="send-btn"
		class:active={hasContent && !disabled}
		title={$t("common.send") || "Senden"}
		aria-label="Send"
	>
		<svg
			viewBox="0 0 24 24"
			fill="none"
			stroke="currentColor"
			stroke-width="2.5"
			stroke-linecap="round"
			stroke-linejoin="round"
		>
			<line x1="12" y1="19" x2="12" y2="5" />
			<polyline points="5 12 12 5 19 12" />
		</svg>
	</button>
</div>

<style>
	.input-wrapper {
		display: flex;
		align-items: center;
		min-height: 52px;
		padding: 8px 8px 8px 16px;
		background: #ffffff;
		border: 1.5px solid #e5e7eb;
		border-radius: 24px;
		box-shadow: 0 2px 8px rgba(0, 0, 0, 0.04);
		transition:
			border-color 0.2s ease,
			box-shadow 0.2s ease;
	}

	.input-wrapper:focus-within {
		border-color: #d1d5db;
		box-shadow: 0 2px 12px rgba(0, 0, 0, 0.06);
	}

	.input-wrapper.disabled {
		opacity: 0.65;
	}

	.input-field {
		flex: 1;
		border: none;
		background: transparent;
		font-size: 17px;
		font-family: inherit;
		resize: none;
		outline: none;
		min-height: 24px;
		max-height: 200px;
		line-height: 1.6;
		color: #0f172a;
		padding: 0;
		overflow-y: auto;
	}

	.input-field::placeholder {
		color: #9ca3af;
	}

	.input-field:disabled {
		cursor: not-allowed;
	}

	.send-btn {
		flex-shrink: 0;
		width: 36px;
		height: 36px;
		border-radius: 50%;
		border: none;
		cursor: pointer;
		display: flex;
		align-items: center;
		justify-content: center;
		transition:
			background-color 0.15s ease,
			color 0.15s ease;
		margin-left: 8px;
		background: #e5e7eb;
		color: #9ca3af;
	}

	.send-btn.active {
		background: #0f172a;
		color: #ffffff;
	}

	.send-btn.active:hover {
		background: #1e293b;
	}

	.send-btn:disabled {
		cursor: not-allowed;
	}

	.send-btn svg {
		width: 16px;
		height: 16px;
	}
</style>
