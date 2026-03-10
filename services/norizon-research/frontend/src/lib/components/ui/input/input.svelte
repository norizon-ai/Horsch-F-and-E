<script lang="ts">
	import { cn } from "$lib/utils/cn.js";
	export let value = "";
	export let type = "text";
	let className = "";
	export { className as class };
</script>

<input
	class={cn(
		"border-input bg-background ring-offset-background placeholder:text-muted-foreground focus-visible:ring-ring flex h-10 w-full rounded-md border px-3 py-2 text-base file:border-0 file:bg-transparent file:text-sm file:font-medium focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-offset-2 disabled:cursor-not-allowed disabled:opacity-50 md:text-sm",
		className,
	)}
	{type}
	bind:value
	{...$$restProps}
/>
