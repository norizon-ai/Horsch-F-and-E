#!/usr/bin/env python3
"""
Integration test for speaker name mapping through the API.

This test simulates the complete user workflow:
1. Create job
2. Transcription completes (detected speaker names)
3. User updates speaker names in verification step
4. Generate protocol
5. Verify speaker names are correct in protocol
"""

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from app.services.job_manager import JobManager
from app.services.mock_generator import MockGenerator
from app.models import Speaker
import asyncio


async def test_api_workflow():
    """Simulate the complete API workflow."""
    print("=" * 80)
    print("INTEGRATION TEST: Speaker Name Mapping via API Workflow")
    print("=" * 80)

    mock_gen = MockGenerator()

    # Step 1: Create job (POST /jobs)
    print("\n[1/5] Creating job...")
    job = JobManager.create_job()
    print(f"  ✓ Job created: {job.id}")

    # Step 2: Upload file triggers transcription (POST /jobs/{job_id}/upload)
    # This is mocked - in reality, KStudio would process and send SSE events
    print("\n[2/5] Simulating transcription (SSE stream)...")

    # Simulate transcription completion (from transcribe.py:88-98)
    speakers = mock_gen.generate_speakers(count=2)
    protocol = mock_gen.generate_protocol(speakers=speakers)

    JobManager.set_speakers(job.id, speakers)
    job = JobManager.get_job(job.id)
    job.transcript = protocol.full_transcript
    job.status = "completed"
    job.current_step = 3
    job.touch()

    print(f"  ✓ Transcription complete")
    print(f"  ✓ Detected speakers: {[s.detected_name for s in speakers]}")
    print(f"  ✓ Transcript stored: {len(job.transcript)} chars")
    print(f"\n  Transcript preview:")
    for line in job.transcript.split('\n')[:3]:
        print(f"    {line}")

    # Step 3: Get speakers (GET /jobs/{job_id}/speakers)
    print("\n[3/5] Fetching speakers for verification...")
    job = JobManager.get_job(job.id)
    fetched_speakers = job.speakers
    print(f"  ✓ Retrieved {len(fetched_speakers)} speakers")
    for i, speaker in enumerate(fetched_speakers):
        print(f"    Speaker {i}: id={speaker.id}, detected='{speaker.detected_name}', confirmed='{speaker.confirmed_name}'")

    # Step 4: User updates speaker names (PUT /jobs/{job_id}/speakers)
    print("\n[4/5] User updating speaker names...")
    updated_speakers = []
    for i, speaker in enumerate(fetched_speakers):
        # Simulate user input
        confirmed_names = ["Omar Mustermann", "Alice Schmidt"]
        speaker.confirmed_name = confirmed_names[i]
        updated_speakers.append(speaker)
        print(f"    Speaker {i}: '{speaker.detected_name}' → '{speaker.confirmed_name}'")

    # Save updated speakers (PUT /jobs/{job_id}/speakers)
    JobManager.set_speakers(job.id, updated_speakers)
    print(f"  ✓ Speakers updated and saved")

    # Step 5: Generate protocol (POST /jobs/{job_id}/protocol)
    print("\n[5/5] Generating protocol with confirmed speaker names...")

    # Import the protocol generation function
    from app.routers.protocol import _apply_speaker_name_replacements

    # Get job with updated speakers
    job = JobManager.get_job(job.id)

    # Generate protocol (in mock mode, this would happen in protocol.py:66-82)
    new_protocol = mock_gen.generate_protocol(speakers=job.speakers)

    # Apply speaker name replacements (the fix!)
    final_protocol = _apply_speaker_name_replacements(new_protocol, job.speakers)

    # Store protocol
    JobManager.set_protocol(job.id, final_protocol)

    print(f"  ✓ Protocol generated")
    print(f"  ✓ Protocol title: {final_protocol.title}")
    print(f"  ✓ Protocol attendees: {final_protocol.attendees}")

    # Verification
    print("\n" + "=" * 80)
    print("VERIFICATION")
    print("=" * 80)

    # Check 1: Attendees should have confirmed names
    print("\n1. Checking attendees list...")
    expected_attendees = ["Omar Mustermann", "Alice Schmidt"]
    if final_protocol.attendees == expected_attendees:
        print(f"  ✓ PASS: Attendees are correct: {final_protocol.attendees}")
    else:
        print(f"  ✗ FAIL: Expected {expected_attendees}, got {final_protocol.attendees}")
        return False

    # Check 2: Transcript should contain confirmed names
    print("\n2. Checking transcript content...")
    transcript = final_protocol.full_transcript
    print(f"  Transcript length: {len(transcript)} chars")

    confirmed_names_present = all(name in transcript for name in expected_attendees)
    detected_names_absent = all(s.detected_name not in transcript for s in job.speakers)

    if confirmed_names_present:
        print(f"  ✓ PASS: All confirmed names found in transcript")
        for name in expected_attendees:
            print(f"    - '{name}' ✓")
    else:
        print(f"  ✗ FAIL: Not all confirmed names found in transcript")
        for name in expected_attendees:
            found = "✓" if name in transcript else "✗"
            print(f"    - '{name}' {found}")
        return False

    if detected_names_absent:
        print(f"  ✓ PASS: No detected names remain in transcript")
        for s in job.speakers:
            print(f"    - '{s.detected_name}' removed ✓")
    else:
        print(f"  ✗ FAIL: Some detected names still present in transcript")
        for s in job.speakers:
            found = "✗" if s.detected_name in transcript else "✓"
            print(f"    - '{s.detected_name}' {found}")
        return False

    # Check 3: Show full transcript
    print("\n3. Full transcript with confirmed names:")
    print("-" * 80)
    lines = transcript.split('\n')
    for line in lines[:10]:  # First 10 lines
        print(f"  {line}")
    if len(lines) > 10:
        remaining = len(lines) - 10
        print(f"  ... ({remaining} more lines)")

    # Check 4: Action items should have confirmed names
    print("\n4. Checking action items...")
    if final_protocol.action_items:
        all_good = True
        for item in final_protocol.action_items:
            if item.assignee:
                if item.assignee in expected_attendees:
                    print(f"  ✓ PASS: Action '{item.text[:50]}...' assigned to '{item.assignee}'")
                else:
                    print(f"  ✗ FAIL: Action '{item.text[:50]}...' has unexpected assignee '{item.assignee}'")
                    all_good = False
        if not all_good:
            return False
    else:
        print(f"  (No action items in protocol)")

    # Cleanup
    JobManager.delete_job(job.id)

    print("\n" + "=" * 80)
    print("✓ INTEGRATION TEST PASSED")
    print("=" * 80)
    print("\nSummary:")
    print("  - Job created successfully")
    print("  - Transcription completed with detected names")
    print("  - User updated speaker names")
    print("  - Protocol generated with confirmed names")
    print("  - All verifications passed")
    print("\nThe speaker name mapping fix is working correctly!")

    return True


if __name__ == "__main__":
    result = asyncio.run(test_api_workflow())
    sys.exit(0 if result else 1)
