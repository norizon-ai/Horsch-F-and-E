<script lang="ts">
	import { cn } from "$lib/utils/cn.js";
	let { orientation = "horizontal", class: className = "", ...restProps } = $props();
</script>

<div
	role="separator"
	class={cn(
		"bg-border shrink-0",
		orientation === "horizontal" ? "h-[1px] w-full" : "min-h-full w-[1px]",
		className,
	)}
	{...restProps}
></div>
