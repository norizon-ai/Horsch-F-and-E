#!/usr/bin/env python3
"""
Verification script for backend implementation.
Tests all modified endpoints and functionality.
"""

import sys
import os

# Add app to path
sys.path.insert(0, os.path.dirname(__file__))

def test_imports():
    """Test that all imports work correctly."""
    print("Testing imports...")

    try:
        from app.routers import microsoft, jobs, protocol
        from app.services import microsoft_teams, job_manager, file_metadata
        from app import models
        print("✅ All imports successful")
        return True
    except ImportError as e:
        print(f"❌ Import failed: {e}")
        return False


def test_models():
    """Test Pydantic model validation."""
    print("\nTesting Pydantic models...")

    try:
        from app.models import JobStatus
        from app.routers.microsoft import ImportRecordingRequest

        # Test JobStatus with new fields (use field aliases for input)
        job_status = JobStatus(
            id="job-123",
            status="processing",
            currentStep=2,
            createdAt="2024-02-14T10:00:00",
            updatedAt="2024-02-14T10:05:00",
            fileUploaded=True,
            hasSpeakers=True,
            hasProtocol=False,
            recordingDate="2024-02-14T09:30:00",
            skipSpeakerVerification=True,
            teamsAttendees=[
                {"name": "Lisa Mueller", "email": "lisa@example.com"}
            ]
        )
        # Access via Python attribute names (snake_case)
        assert job_status.recording_date == "2024-02-14T09:30:00"
        assert job_status.skip_speaker_verification is True
        assert len(job_status.teams_attendees) == 1
        print("✅ JobStatus model validated")

        # Test ImportRecordingRequest with attendees
        import_request = ImportRecordingRequest(
            meeting_id="meeting-123",
            recording_id="rec-456",
            meeting_subject="Test Meeting",
            meeting_start="2024-02-14T10:00:00",
            attendees=[
                {"name": "Test User", "email": "test@example.com"}
            ]
        )
        assert len(import_request.attendees) == 1
        print("✅ ImportRecordingRequest model validated")

        return True
    except Exception as e:
        print(f"❌ Model validation failed: {e}")
        return False


def test_file_metadata():
    """Test file metadata extraction functions."""
    print("\nTesting file metadata extraction...")

    try:
        from app.services.file_metadata import (
            extract_recording_date,
            extract_file_duration
        )

        # Test with non-existent file (should return None or fallback)
        date = extract_recording_date("/tmp/nonexistent.mp4")
        # Should return None or ISO date string
        assert date is None or isinstance(date, str)
        print("✅ extract_recording_date handles missing files")

        duration = extract_file_duration("/tmp/nonexistent.mp4")
        assert duration is None
        print("✅ extract_file_duration handles missing files")

        return True
    except Exception as e:
        print(f"❌ File metadata test failed: {e}")
        return False


def test_job_manager():
    """Test JobManager with new fields."""
    print("\nTesting JobManager...")

    try:
        from app.services.job_manager import JobManager

        # Create job
        job = JobManager.create_job()
        assert job.recording_date is None
        assert job.teams_import is False
        assert job.teams_attendees == []
        print("✅ JobManager creates jobs with new fields")

        # Update job with new fields
        JobManager.update_job(
            job.id,
            recording_date="2024-02-14T10:00:00",
            teams_import=True,
            teams_attendees=[{"name": "Test"}]
        )

        updated_job = JobManager.get_job(job.id)
        assert updated_job.recording_date == "2024-02-14T10:00:00"
        assert updated_job.teams_import is True
        assert len(updated_job.teams_attendees) == 1
        print("✅ JobManager updates new fields correctly")

        # Cleanup
        JobManager.delete_job(job.id)

        return True
    except Exception as e:
        print(f"❌ JobManager test failed: {e}")
        return False


def test_protocol_speaker_mapping():
    """Test speaker ID mapping in protocol generation."""
    print("\nTesting protocol speaker mapping...")

    try:
        from app.routers.protocol import build_protocol_prompt

        # Test speaker mapping
        transcript = """
        Speaker 0: Hello everyone.
        Speaker 1: Hi there.
        Speaker 0: Let's start the meeting.
        """

        template = None
        speaker_names = ["Lisa Mueller", "Max Mustermann"]

        prompt = build_protocol_prompt(transcript, template, speaker_names)

        # Verify prompt contains speaker mapping
        assert "Speaker 0 → Lisa Mueller" in prompt
        assert "Speaker 1 → Max Mustermann" in prompt
        print("✅ Protocol prompt includes speaker mapping")

        return True
    except Exception as e:
        print(f"❌ Protocol speaker mapping test failed: {e}")
        return False


def test_microsoft_teams_service():
    """Test Microsoft Teams service structure."""
    print("\nTesting Microsoft Teams service...")

    try:
        from app.services.microsoft_teams import MicrosoftTeamsService

        service = MicrosoftTeamsService()
        assert hasattr(service, 'list_meetings')
        assert hasattr(service, 'get_attendee_details')
        print("✅ Microsoft Teams service has new methods")

        return True
    except Exception as e:
        print(f"❌ Microsoft Teams service test failed: {e}")
        return False


def main():
    """Run all verification tests."""
    print("=" * 60)
    print("Backend Implementation Verification")
    print("=" * 60)

    tests = [
        ("Imports", test_imports),
        ("Pydantic Models", test_models),
        ("File Metadata", test_file_metadata),
        ("JobManager", test_job_manager),
        ("Protocol Speaker Mapping", test_protocol_speaker_mapping),
        ("Microsoft Teams Service", test_microsoft_teams_service),
    ]

    results = []
    for name, test_func in tests:
        try:
            result = test_func()
            results.append((name, result))
        except Exception as e:
            print(f"\n❌ Test '{name}' crashed: {e}")
            results.append((name, False))

    # Summary
    print("\n" + "=" * 60)
    print("Test Results Summary")
    print("=" * 60)

    passed = sum(1 for _, result in results if result)
    total = len(results)

    for name, result in results:
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"{status}: {name}")

    print("\n" + "=" * 60)
    print(f"Total: {passed}/{total} tests passed")
    print("=" * 60)

    if passed == total:
        print("\n🎉 All tests passed! Implementation verified.")
        return 0
    else:
        print(f"\n⚠️  {total - passed} test(s) failed. Review errors above.")
        return 1


if __name__ == "__main__":
    sys.exit(main())
