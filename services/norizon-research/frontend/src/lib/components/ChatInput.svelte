<script lang="ts">
	import { t } from "svelte-i18n";
	import { createEventDispatcher } from "svelte";
	import { Button } from "$lib/components/ui/button";

	const dispatch = createEventDispatcher();

	export let disabled = false;
	export let onSubmit: ((query: string) => void) | undefined = undefined;

	let input = "";
	let textarea: HTMLTextAreaElement;

	$: placeholder = $t("search.placeholder");
	$: hasContent = input.trim().length > 0;

	function handleSubmit() {
		const trimmed = input.trim();
		if (trimmed && !disabled) {
			onSubmit?.(trimmed);
			dispatch("submit", trimmed);
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
			textarea.style.height = Math.min(textarea.scrollHeight, 120) + "px";
		}
	}
</script>

<div
	class="flex items-end gap-3 p-3 px-4 bg-white border border-gray-300 rounded-2xl shadow-md transition-[border-color,box-shadow] duration-150 focus-within:border-nora-orange-500 focus-within:ring-2 focus-within:ring-nora-orange-500/20 {disabled
		? 'opacity-70'
		: ''}"
>
	<textarea
		bind:this={textarea}
		bind:value={input}
		on:input={autoResize}
		on:keydown={handleKeydown}
		{placeholder}
		{disabled}
		rows="1"
		class="flex-1 border-0 bg-transparent text-[15px] font-[inherit] resize-none outline-none min-h-[24px] max-h-[120px] leading-normal text-nora-slate-900 placeholder:text-nora-slate-400 disabled:cursor-not-allowed"
	></textarea>
	<Button
		type="button"
		size="icon"
		on:click={handleSubmit}
		disabled={!hasContent || disabled}
		class="shrink-0 h-9 w-9 rounded-[10px] {hasContent && !disabled
			? 'bg-[#1e3a5f] text-white hover:bg-[#162d4a]'
			: 'bg-slate-100 text-slate-400'}"
		title={$t("common.send") || "Send"}
	>
		<svg
			class="h-[18px] w-[18px]"
			viewBox="0 0 24 24"
			fill="none"
			stroke="currentColor"
			stroke-width="2"
		>
			<line x1="22" y1="2" x2="11" y2="13" />
			<polygon points="22 2 15 22 11 13 2 9 22 2" />
		</svg>
	</Button>
</div>
