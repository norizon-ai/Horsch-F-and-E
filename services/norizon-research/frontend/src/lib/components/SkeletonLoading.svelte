<script lang="ts">
	export let showSources = true;
</script>

<div class="skeleton-wrapper">
	<!-- Summary block skeleton -->
	<div class="skeleton-group">
		<div
			class="skeleton"
			style="width:35%;height:20px;margin-bottom:14px"
		></div>
		<div
			class="skeleton"
			style="width:100%;height:14px;margin-bottom:10px"
		></div>
		<div
			class="skeleton"
			style="width:95%;height:14px;margin-bottom:10px"
		></div>
		<div
			class="skeleton"
			style="width:85%;height:14px;margin-bottom:10px"
		></div>
	</div>

	<!-- Key results skeleton -->
	<div class="skeleton-group">
		<div
			class="skeleton"
			style="width:28%;height:20px;margin-bottom:14px"
		></div>
		{#each [92, 88, 78] as width}
			<div class="skeleton-row">
				<div class="skeleton skeleton-dot"></div>
				<div class="skeleton" style="width:{width}%;height:14px"></div>
			</div>
		{/each}
	</div>

	<!-- Sources skeleton -->
	{#if showSources}
		<div class="skeleton-card">
			<div class="skeleton-card-header">
				<div
					class="skeleton"
					style="width:14px;height:14px;border-radius:4px"
				></div>
				<div class="skeleton" style="width:60px;height:14px"></div>
			</div>
			<div class="skeleton-card-body">
				{#each [1, 2, 3] as _}
					<div class="skeleton-source-row">
						<div
							class="skeleton"
							style="width:32px;height:32px;border-radius:8px;flex-shrink:0"
						></div>
						<div style="flex:1">
							<div
								class="skeleton"
								style="width:75%;height:14px;margin-bottom:6px"
							></div>
							<div
								class="skeleton"
								style="width:45%;height:10px"
							></div>
						</div>
					</div>
				{/each}
			</div>
		</div>
	{/if}
</div>

<style>
	.skeleton-wrapper {
		margin-top: 16px;
	}
	.skeleton-group {
		margin-bottom: 24px;
	}
	.skeleton {
		background: linear-gradient(
			90deg,
			#e2e8f0 25%,
			#f1f5f9 50%,
			#e2e8f0 75%
		);
		background-size: 200% 100%;
		animation: shimmer 1.5s infinite;
		border-radius: 6px;
	}
	.skeleton-dot {
		width: 6px !important;
		height: 6px !important;
		border-radius: 50% !important;
		flex-shrink: 0;
	}
	.skeleton-row {
		display: flex;
		align-items: center;
		gap: 12px;
		margin-bottom: 10px;
	}
	.skeleton-card {
		border: 1px solid #e2e8f0;
		border-radius: 12px;
		overflow: hidden;
		margin-top: 24px;
	}
	.skeleton-card-header {
		display: flex;
		align-items: center;
		gap: 8px;
		padding: 10px 14px;
		background: #f8fafc;
		border-bottom: 1px solid #e2e8f0;
	}
	.skeleton-card-body {
		padding: 12px;
		display: flex;
		flex-direction: column;
		gap: 8px;
	}
	.skeleton-source-row {
		display: flex;
		align-items: center;
		gap: 12px;
		padding: 12px;
		border: 1px solid #f1f5f9;
		border-radius: 8px;
	}
	@keyframes shimmer {
		0% {
			background-position: 200% 0;
		}
		100% {
			background-position: -200% 0;
		}
	}
</style>
