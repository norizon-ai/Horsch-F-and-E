"""Audio preprocessing via FFmpeg."""

import logging
import subprocess
from pathlib import Path

logger = logging.getLogger(__name__)


def preprocess_audio(input_path: str, output_dir: str) -> str:
    """
    Convert any audio/video file to 16kHz mono WAV for Whisper.

    Args:
        input_path: Path to the source audio/video file.
        output_dir: Directory to write the converted WAV.

    Returns:
        Path to the converted WAV file.

    Raises:
        RuntimeError: If FFmpeg fails.
    """
    input_file = Path(input_path)
    output_file = Path(output_dir) / f"{input_file.stem}.wav"
    output_file.parent.mkdir(parents=True, exist_ok=True)

    cmd = [
        "ffmpeg",
        "-i", str(input_file),
        "-ar", "16000",      # 16kHz sample rate
        "-ac", "1",           # mono
        "-c:a", "pcm_s16le",  # 16-bit PCM
        "-y",                 # overwrite
        str(output_file),
    ]

    logger.info(f"Preprocessing audio: {input_file.name} -> {output_file.name}")

    result = subprocess.run(
        cmd,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        timeout=120,
    )

    if result.returncode != 0:
        stderr = result.stderr.decode(errors="replace")
        raise RuntimeError(f"FFmpeg preprocessing failed: {stderr[:500]}")

    logger.info(f"Audio preprocessed: {output_file} ({output_file.stat().st_size} bytes)")
    return str(output_file)
