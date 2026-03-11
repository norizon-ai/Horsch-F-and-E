<script lang="ts">
	import { cn } from "$lib/utils/cn.js";
	let { class: className = "", children, id = undefined, ...restProps } = $props();
</script>

<div
	class={cn(
		"bg-card text-card-foreground rounded-lg border shadow-sm",
		className,
	)}
	{id}
	{...restProps}
>
	{@render children?.()}
</div>
