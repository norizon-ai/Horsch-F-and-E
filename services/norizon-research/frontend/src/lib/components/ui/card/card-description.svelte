<script lang="ts">
	import { cn } from "$lib/utils/cn.js";
	let { class: className = "", children, ...restProps } = $props();
</script>

<p class={cn("text-sm text-muted-foreground", className)} {...restProps}>
	{@render children?.()}
</p>
