"""
File metadata extraction utilities.

Extracts recording date and other metadata from audio/video files.
"""

import os
from datetime import datetime
from typing import Optional
import subprocess
import json


def extract_recording_date(file_path: str) -> Optional[str]:
    """
    Extract the recording date from file metadata.

    Supports common formats: MP4, MP3, WAV, M4A, WebM
    Uses ffprobe to extract metadata, falls back to file creation time.

    Args:
        file_path: Path to the media file

    Returns:
        ISO 8601 datetime string or None if extraction fails
    """
    if not os.path.exists(file_path):
        return None

    # Try ffprobe first (most accurate for media files)
    try:
        result = subprocess.run(
            [
                "ffprobe",
                "-v", "quiet",
                "-print_format", "json",
                "-show_format",
                file_path
            ],
            capture_output=True,
            text=True,
            timeout=10
        )

        if result.returncode == 0:
            metadata = json.loads(result.stdout)
            format_info = metadata.get("format", {})
            tags = format_info.get("tags", {})

            # Check various metadata fields for recording date
            # Different formats use different tag names
            date_fields = [
                "creation_time",  # MP4, M4A
                "date",  # General
                "DATE",  # Uppercase variant
                "encoded_date",  # Some encoders
                "IDIT",  # WAV files
            ]

            for field in date_fields:
                date_str = tags.get(field)
                if date_str:
                    # Parse and normalize to ISO 8601
                    try:
                        # Handle various date formats
                        if "T" in date_str:
                            # ISO format (2024-02-14T10:30:00.000000Z)
                            dt = datetime.fromisoformat(date_str.replace("Z", "+00:00"))
                        else:
                            # Try parsing as simple date
                            dt = datetime.strptime(date_str[:10], "%Y-%m-%d")

                        return dt.isoformat()
                    except (ValueError, AttributeError):
                        continue

    except (subprocess.TimeoutExpired, subprocess.SubprocessError, json.JSONDecodeError, FileNotFoundError):
        # ffprobe not available or failed - fall back to file stats
        pass

    # Fallback: use file creation/modification time
    try:
        stat = os.stat(file_path)
        # Use the earlier of creation time (if available) or modification time
        if hasattr(stat, 'st_birthtime'):
            # macOS/BSD
            timestamp = stat.st_birthtime
        else:
            # Linux/Windows - use modification time
            timestamp = stat.st_mtime

        dt = datetime.fromtimestamp(timestamp)
        return dt.isoformat()

    except (OSError, ValueError):
        # Last resort: current time
        return datetime.utcnow().isoformat()


def extract_file_duration(file_path: str) -> Optional[int]:
    """
    Extract duration in seconds from media file.

    Args:
        file_path: Path to the media file

    Returns:
        Duration in seconds or None if extraction fails
    """
    if not os.path.exists(file_path):
        return None

    try:
        result = subprocess.run(
            [
                "ffprobe",
                "-v", "quiet",
                "-print_format", "json",
                "-show_format",
                file_path
            ],
            capture_output=True,
            text=True,
            timeout=10
        )

        if result.returncode == 0:
            metadata = json.loads(result.stdout)
            format_info = metadata.get("format", {})
            duration_str = format_info.get("duration")

            if duration_str:
                return int(float(duration_str))

    except (subprocess.TimeoutExpired, subprocess.SubprocessError, json.JSONDecodeError, FileNotFoundError, ValueError):
        pass

    return None
