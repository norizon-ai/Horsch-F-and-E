<script lang="ts">
	import { cn } from "$lib/utils/cn.js";
	let className = "";
	export { className as class };
</script>

<div
	class={cn(
		"bg-card text-card-foreground rounded-lg border shadow-sm",
		className,
	)}
	{...$$restProps}
>
	<slot />
</div>
