<script lang="ts">
	import { onDestroy } from "svelte";

	export let src: string | undefined = undefined;
	export let compact = false;

	let audio: HTMLAudioElement;
	let isPlaying = false;
	let currentTime = 0;
	let duration = 0;

	function togglePlay() {
		if (!audio) return;

		if (isPlaying) {
			audio.pause();
		} else {
			audio.play();
		}
	}

	function handleTimeUpdate() {
		currentTime = audio.currentTime;
	}

	function handleLoadedMetadata() {
		duration = audio.duration;
	}

	function handlePlay() {
		isPlaying = true;
	}

	function handlePause() {
		isPlaying = false;
	}

	function handleEnded() {
		isPlaying = false;
		currentTime = 0;
	}

	function formatTime(seconds: number): string {
		const mins = Math.floor(seconds / 60);
		const secs = Math.floor(seconds % 60);
		return `${mins}:${secs.toString().padStart(2, "0")}`;
	}

	function handleSeek(e: MouseEvent) {
		const bar = e.currentTarget as HTMLDivElement;
		const rect = bar.getBoundingClientRect();
		const percent = (e.clientX - rect.left) / rect.width;
		audio.currentTime = percent * duration;
	}

	onDestroy(() => {
		if (audio) {
			audio.pause();
		}
	});
</script>

{#if src}
	<div class="audio-player" class:compact>
		<audio
			bind:this={audio}
			{src}
			on:timeupdate={handleTimeUpdate}
			on:loadedmetadata={handleLoadedMetadata}
			on:play={handlePlay}
			on:pause={handlePause}
			on:ended={handleEnded}
		>
			<track kind="captions" />
		</audio>

		<button
			class="play-btn"
			on:click={togglePlay}
			aria-label={isPlaying ? "Pause" : "Play"}
		>
			{#if isPlaying}
				<svg viewBox="0 0 24 24" fill="currentColor">
					<rect x="6" y="4" width="4" height="16" rx="1" />
					<rect x="14" y="4" width="4" height="16" rx="1" />
				</svg>
			{:else}
				<svg viewBox="0 0 24 24" fill="currentColor">
					<polygon points="5 3 19 12 5 21 5 3" />
				</svg>
			{/if}
		</button>

		{#if !compact}
			<div class="progress-section">
				<div
					class="progress-bar"
					role="slider"
					tabindex="0"
					aria-label="Audio progress"
					aria-valuemin={0}
					aria-valuemax={duration}
					aria-valuenow={currentTime}
					on:click={handleSeek}
					on:keydown={(e) => {
						if (e.key === "ArrowRight") audio.currentTime += 5;
						if (e.key === "ArrowLeft") audio.currentTime -= 5;
					}}
				>
					<div class="progress-track">
						<div
							class="progress-fill"
							style="width: {duration > 0
								? (currentTime / duration) * 100
								: 0}%"
						></div>
					</div>
				</div>
				<div class="time-display">
					<span>{formatTime(currentTime)}</span>
					<span>/</span>
					<span>{formatTime(duration)}</span>
				</div>
			</div>
		{/if}
	</div>
{:else}
	<div class="audio-player disabled" class:compact>
		<button class="play-btn" disabled aria-label="No audio">
			<svg viewBox="0 0 24 24" fill="currentColor">
				<polygon points="5 3 19 12 5 21 5 3" />
			</svg>
		</button>
		{#if !compact}
			<span class="no-audio">Keine Audiodatei</span>
		{/if}
	</div>
{/if}

<style>
	.audio-player {
		display: flex;
		align-items: center;
		gap: 12px;
		padding: 8px 12px;
		background: var(--slate-50, #f8fafc);
		border-radius: 8px;
	}

	.audio-player.compact {
		padding: 0;
		background: transparent;
		gap: 0;
	}

	.audio-player.disabled {
		opacity: 0.5;
	}

	.play-btn {
		width: 44px;
		height: 44px;
		display: flex;
		align-items: center;
		justify-content: center;
		background: var(--blue-500, #3b82f6);
		color: white;
		border: none;
		border-radius: 50%;
		cursor: pointer;
		transition: all 0.15s ease;
		flex-shrink: 0;
	}

	.compact .play-btn {
		width: 36px;
		height: 36px;
	}

	.play-btn:hover:not(:disabled) {
		background: var(--blue-600, #2563eb);
		transform: scale(1.05);
	}

	.play-btn:disabled {
		background: var(--slate-300, #cbd5e1);
		cursor: not-allowed;
	}

	.play-btn svg {
		width: 18px;
		height: 18px;
	}

	.compact .play-btn svg {
		width: 16px;
		height: 16px;
	}

	.progress-section {
		flex: 1;
		display: flex;
		flex-direction: column;
		gap: 4px;
	}

	.progress-bar {
		cursor: pointer;
		padding: 4px 0;
	}

	.progress-track {
		height: 4px;
		background: var(--slate-200, #e2e8f0);
		border-radius: 2px;
		overflow: hidden;
	}

	.progress-fill {
		height: 100%;
		background: var(--blue-500, #3b82f6);
		border-radius: 2px;
		transition: width 0.1s linear;
	}

	.time-display {
		display: flex;
		gap: 4px;
		font-size: 11px;
		color: var(--slate-500, #64748b);
		font-variant-numeric: tabular-nums;
	}

	.no-audio {
		font-size: 13px;
		color: var(--slate-400, #94a3b8);
	}
</style>
