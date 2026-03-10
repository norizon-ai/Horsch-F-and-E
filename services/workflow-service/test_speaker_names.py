#!/usr/bin/env python3
"""
Test script to verify speaker name replacement in protocol generation.

This script tests the complete flow:
1. Create job
2. Upload file (triggers transcription with detected names)
3. Update speaker names (user confirms names)
4. Generate protocol (should use confirmed names)
"""

import asyncio
import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from app.services.job_manager import JobManager
from app.services.mock_generator import MockGenerator
from app.routers.protocol import _apply_speaker_name_replacements
from app.models import Speaker, Protocol


def test_speaker_name_replacement():
    """Test speaker name replacement logic."""
    print("=" * 80)
    print("TEST: Speaker Name Replacement in Protocol")
    print("=" * 80)

    # Create mock generator
    mock_gen = MockGenerator()

    # Step 1: Generate initial speakers (as would happen during transcription)
    print("\n1. INITIAL TRANSCRIPTION - Detected Speakers:")
    print("-" * 80)
    speakers = mock_gen.generate_speakers(count=3)
    for i, speaker in enumerate(speakers):
        print(f"  Speaker {i}: id={speaker.id}, detected='{speaker.detected_name}', confirmed='{speaker.confirmed_name}'")

    # Step 2: Generate initial protocol with detected names
    print("\n2. INITIAL PROTOCOL GENERATION:")
    print("-" * 80)
    initial_protocol = mock_gen.generate_protocol(speakers=speakers)
    print(f"  Attendees: {initial_protocol.attendees}")
    print(f"  Transcript preview: {initial_protocol.full_transcript[:200]}...")

    # Step 3: User updates speaker names (speaker verification step)
    print("\n3. USER UPDATES SPEAKER NAMES:")
    print("-" * 80)
    speakers[0].confirmed_name = "Omar"
    speakers[1].confirmed_name = "Sarah"
    speakers[2].confirmed_name = "Michael"
    for i, speaker in enumerate(speakers):
        print(f"  Speaker {i}: detected='{speaker.detected_name}' → confirmed='{speaker.confirmed_name}'")

    # Step 4: Apply speaker name replacements
    print("\n4. APPLY SPEAKER NAME REPLACEMENTS:")
    print("-" * 80)
    updated_protocol = _apply_speaker_name_replacements(initial_protocol, speakers)
    print(f"  Updated Attendees: {updated_protocol.attendees}")
    print(f"  Updated Transcript preview: {updated_protocol.full_transcript[:400]}...")

    # Step 5: Verify replacements worked
    print("\n5. VERIFICATION:")
    print("-" * 80)
    transcript = updated_protocol.full_transcript

    # Check for confirmed names
    checks = [
        ("Omar" in transcript, "✓ 'Omar' found in transcript", "✗ 'Omar' NOT found in transcript"),
        ("Sarah" in transcript, "✓ 'Sarah' found in transcript", "✗ 'Sarah' NOT found in transcript"),
        ("Michael" in transcript, "✓ 'Michael' found in transcript", "✗ 'Michael' NOT found in transcript"),
    ]

    # Check for detected names (should NOT be present)
    for speaker in speakers:
        if speaker.detected_name and speaker.confirmed_name != speaker.detected_name:
            checks.append((
                speaker.detected_name not in transcript,
                f"✓ '{speaker.detected_name}' correctly removed",
                f"✗ '{speaker.detected_name}' still present (BUG!)"
            ))

    all_passed = True
    for condition, pass_msg, fail_msg in checks:
        if condition:
            print(f"  {pass_msg}")
        else:
            print(f"  {fail_msg}")
            all_passed = False

    # Full transcript for debugging
    print("\n6. FULL UPDATED TRANSCRIPT:")
    print("-" * 80)
    print(updated_protocol.full_transcript)

    print("\n" + "=" * 80)
    if all_passed:
        print("✓ ALL TESTS PASSED")
        print("=" * 80)
        return 0
    else:
        print("✗ SOME TESTS FAILED")
        print("=" * 80)
        return 1


def test_full_workflow():
    """Test the complete workflow with JobManager."""
    print("\n\n")
    print("=" * 80)
    print("TEST: Full Workflow with JobManager")
    print("=" * 80)

    mock_gen = MockGenerator()

    # Step 1: Create job
    print("\n1. CREATE JOB:")
    print("-" * 80)
    job = JobManager.create_job()
    print(f"  Job created: {job.id}")

    # Step 2: Simulate transcription (mock mode)
    print("\n2. TRANSCRIPTION (Mock Mode):")
    print("-" * 80)
    speakers = mock_gen.generate_speakers(count=2)
    protocol = mock_gen.generate_protocol(speakers=speakers)

    # Store in job (as would happen in transcribe.py)
    JobManager.set_speakers(job.id, speakers)
    job = JobManager.get_job(job.id)
    job.transcript = protocol.full_transcript
    job.touch()

    print(f"  Speakers detected: {[s.detected_name for s in speakers]}")
    print(f"  Transcript stored: {len(job.transcript)} chars")
    print(f"  Transcript preview: {job.transcript[:200]}...")

    # Step 3: User updates speaker names
    print("\n3. USER UPDATES SPEAKERS:")
    print("-" * 80)
    speakers[0].confirmed_name = "Alice"
    speakers[1].confirmed_name = "Bob"
    JobManager.set_speakers(job.id, speakers)
    print(f"  Updated speakers: {[(s.detected_name, '→', s.confirmed_name) for s in speakers]}")

    # Step 4: Generate protocol (should use confirmed names)
    print("\n4. GENERATE PROTOCOL:")
    print("-" * 80)
    job = JobManager.get_job(job.id)
    print(f"  Job speakers: {[(s.detected_name, s.confirmed_name) for s in job.speakers]}")

    # Regenerate protocol with speaker name replacements
    new_protocol = mock_gen.generate_protocol(speakers=job.speakers)
    updated_protocol = _apply_speaker_name_replacements(new_protocol, job.speakers)

    print(f"  Protocol attendees: {updated_protocol.attendees}")
    print(f"  Protocol transcript preview: {updated_protocol.full_transcript[:400]}...")

    # Step 5: Verify
    print("\n5. VERIFICATION:")
    print("-" * 80)
    transcript = updated_protocol.full_transcript

    checks = [
        ("Alice" in transcript, "✓ 'Alice' in protocol", "✗ 'Alice' NOT in protocol (BUG!)"),
        ("Bob" in transcript, "✓ 'Bob' in protocol", "✗ 'Bob' NOT in protocol (BUG!)"),
        (speakers[0].detected_name not in transcript or speakers[0].detected_name == "Alice",
         f"✓ '{speakers[0].detected_name}' removed/replaced",
         f"✗ '{speakers[0].detected_name}' still present (BUG!)"),
        (speakers[1].detected_name not in transcript or speakers[1].detected_name == "Bob",
         f"✓ '{speakers[1].detected_name}' removed/replaced",
         f"✗ '{speakers[1].detected_name}' still present (BUG!)"),
    ]

    all_passed = True
    for condition, pass_msg, fail_msg in checks:
        if condition:
            print(f"  {pass_msg}")
        else:
            print(f"  {fail_msg}")
            all_passed = False

    # Cleanup
    JobManager.delete_job(job.id)

    print("\n" + "=" * 80)
    if all_passed:
        print("✓ ALL TESTS PASSED")
        print("=" * 80)
        return 0
    else:
        print("✗ SOME TESTS FAILED")
        print("=" * 80)
        return 1


if __name__ == "__main__":
    # Run both tests
    result1 = test_speaker_name_replacement()
    result2 = test_full_workflow()

    sys.exit(max(result1, result2))
