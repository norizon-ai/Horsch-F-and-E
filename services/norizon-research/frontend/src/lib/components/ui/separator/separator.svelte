<script lang="ts">
	import { cn } from "$lib/utils/cn.js";
	export let orientation = "horizontal";
	let className = "";
	export { className as class };
</script>

<div
	role="separator"
	class={cn(
		"bg-border shrink-0",
		orientation === "horizontal" ? "h-[1px] w-full" : "min-h-full w-[1px]",
		className,
	)}
	{...$$restProps}
></div>
