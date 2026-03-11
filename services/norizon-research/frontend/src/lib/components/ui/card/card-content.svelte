<script lang="ts">
	import { cn } from "$lib/utils/cn.js";
	let { class: className = "", children, ...restProps } = $props();
</script>

<div class={cn("p-6", className)} {...restProps}>
	{@render children?.()}
</div>
