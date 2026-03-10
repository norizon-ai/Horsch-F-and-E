<script lang="ts">
	import { cn } from "$lib/utils/cn.js";
	let className = "";
	export { className as class };
</script>

<div class={cn("p-6", className)} {...$$restProps}>
	<slot />
</div>
