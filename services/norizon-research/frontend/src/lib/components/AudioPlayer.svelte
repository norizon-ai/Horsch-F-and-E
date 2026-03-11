<script lang="ts">
	import { onDestroy } from "svelte";

	let {
		src = undefined as string | undefined,
		compact = false,
	}: { src?: string; compact?: boolean } = $props();

	let audio = $state<HTMLAudioElement | undefined>(undefined);
	let isPlaying = $state(false);
	let currentTime = $state(0);
	let duration = $state(0);

	function togglePlay() {
		if (!audio) return;
		if (isPlaying) {
			audio.pause();
		} else {
			audio.play();
		}
	}

	function handleTimeUpdate() {
		if (audio) currentTime = audio.currentTime;
	}

	function handleLoadedMetadata() {
		if (audio) duration = audio.duration;
	}

	function handlePlay() { isPlaying = true; }
	function handlePause() { isPlaying = false; }
	function handleEnded() { isPlaying = false; currentTime = 0; }

	function formatTime(seconds: number): string {
		const mins = Math.floor(seconds / 60);
		const secs = Math.floor(seconds % 60);
		return `${mins}:${secs.toString().padStart(2, "0")}`;
	}

	function handleSeek(e: MouseEvent) {
		const bar = e.currentTarget as HTMLDivElement;
		const rect = bar.getBoundingClientRect();
		const percent = (e.clientX - rect.left) / rect.width;
		if (audio) audio.currentTime = percent * duration;
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
			ontimeupdate={handleTimeUpdate}
			onloadedmetadata={handleLoadedMetadata}
			onplay={handlePlay}
			onpause={handlePause}
			onended={handleEnded}
		>
			<track kind="captions" />
		</audio>

		<button
			class="play-btn"
			onclick={togglePlay}
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
					onclick={handleSeek}
					onkeydown={(e) => {
						if (e.key === "ArrowRight" && audio) audio.currentTime += 5;
						if (e.key === "ArrowLeft" && audio) audio.currentTime -= 5;
					}}
				>
					<div class="progress-track">
						<div
							class="progress-fill"
							style="width: {duration > 0 ? (currentTime / duration) * 100 : 0}%"
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
		background: #f8fafc;
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
		background: #3b82f6;
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
		background: #2563eb;
		transform: scale(1.05);
	}

	.play-btn:disabled {
		background: #cbd5e1;
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
		background: #e2e8f0;
		border-radius: 2px;
		overflow: hidden;
	}

	.progress-fill {
		height: 100%;
		background: #3b82f6;
		border-radius: 2px;
		transition: width 0.1s linear;
	}

	.time-display {
		display: flex;
		gap: 4px;
		font-size: 11px;
		color: #64748b;
		font-variant-numeric: tabular-nums;
	}

	.no-audio {
		font-size: 13px;
		color: #94a3b8;
	}
</style>
