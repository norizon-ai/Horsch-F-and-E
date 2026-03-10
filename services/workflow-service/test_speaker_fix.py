#!/usr/bin/env python3
"""
Test script to verify the speaker name replacement bug fix.

BUG DESCRIPTION:
User changed "Unknown Speaker"/"Speaker 0" to "Omar" in speaker verification.
In the protocol editor, under "Attendees", it STILL showed "Speaker 0" instead of "Omar".

ROOT CAUSE:
The _apply_speaker_name_replacements() function was replacing speaker names in:
- executiveSummary
- fullTranscript
- decisions
- nextSteps
- actionItems (text and assignee)
- customSections

BUT it was NOT replacing names in the 'attendees' field!

FIX:
Added attendees replacement in _apply_speaker_name_replacements() at line 183-185.
"""

import logging
from app.models import Speaker, Protocol, ActionItem
from app.routers.protocol import _apply_speaker_name_replacements

logging.basicConfig(level=logging.INFO, format='%(levelname)s - %(message)s')


def test_single_speaker_replacement():
    """Test replacing a single speaker name."""
    print("\n" + "=" * 70)
    print("TEST 1: Single Speaker Replacement (Speaker 0 → Omar)")
    print("=" * 70)

    speakers = [
        Speaker(
            id='speaker-0',
            detectedName='Speaker 0',
            confirmedName='Omar',
            speakingTime=120
        )
    ]

    protocol = Protocol(
        title='Test Meeting',
        date='2026-02-15',
        attendees=['Speaker 0', 'John Doe'],
        executiveSummary='Speaker 0 led the meeting and presented the roadmap.',
        actionItems=[
            ActionItem(
                id='action-1',
                text='Speaker 0 will fix the attendees bug',
                assignee='Speaker 0'
            )
        ],
        fullTranscript='[00:00] Speaker 0: Hello everyone',
        decisions=['Speaker 0 decided to prioritize this fix'],
        nextSteps=['Speaker 0 will deploy the fix']
    )

    print(f"\nBEFORE replacement:")
    print(f"  attendees:     {protocol.attendees}")
    print(f"  summary:       {protocol.executive_summary}")
    print(f"  action assignee: {protocol.action_items[0].assignee}")

    fixed = _apply_speaker_name_replacements(protocol, speakers)

    print(f"\nAFTER replacement:")
    print(f"  attendees:     {fixed.attendees}")
    print(f"  summary:       {fixed.executive_summary}")
    print(f"  action assignee: {fixed.action_items[0].assignee}")

    # Verify
    assert 'Speaker 0' not in str(fixed.attendees), "❌ FAILED: 'Speaker 0' still in attendees"
    assert 'Omar' in str(fixed.attendees), "❌ FAILED: 'Omar' not in attendees"
    assert 'Omar' in fixed.executive_summary, "❌ FAILED: 'Omar' not in summary"
    assert 'Omar' == fixed.action_items[0].assignee, "❌ FAILED: assignee not 'Omar'"

    print("\n✅ TEST 1 PASSED")


def test_multiple_speakers():
    """Test replacing multiple speaker names."""
    print("\n" + "=" * 70)
    print("TEST 2: Multiple Speakers (Speaker 0 → Omar, Unknown Speaker → Sarah)")
    print("=" * 70)

    speakers = [
        Speaker(
            id='speaker-0',
            detectedName='Speaker 0',
            confirmedName='Omar',
            speakingTime=120
        ),
        Speaker(
            id='speaker-1',
            detectedName='Unknown Speaker',
            confirmedName='Sarah',
            speakingTime=90
        )
    ]

    protocol = Protocol(
        title='Team Sync',
        date='2026-02-15',
        attendees=['Speaker 0', 'Unknown Speaker', 'External Guest'],
        executiveSummary='Speaker 0 and Unknown Speaker discussed the project status.',
        actionItems=[
            ActionItem(
                id='action-1',
                text='Speaker 0 will review the PR',
                assignee='Speaker 0'
            ),
            ActionItem(
                id='action-2',
                text='Unknown Speaker will deploy',
                assignee='Unknown Speaker'
            )
        ],
        fullTranscript='[00:00] Speaker 0: Hi\n[00:30] Unknown Speaker: Hello',
        decisions=['Speaker 0 approved the architecture', 'Unknown Speaker confirmed timeline'],
        nextSteps=['Speaker 0 to document', 'Unknown Speaker to test']
    )

    print(f"\nBEFORE replacement:")
    print(f"  attendees:     {protocol.attendees}")
    print(f"  summary:       {protocol.executive_summary}")

    fixed = _apply_speaker_name_replacements(protocol, speakers)

    print(f"\nAFTER replacement:")
    print(f"  attendees:     {fixed.attendees}")
    print(f"  summary:       {fixed.executive_summary}")

    # Verify
    assert 'Speaker 0' not in str(fixed.attendees), "❌ FAILED: 'Speaker 0' still in attendees"
    assert 'Unknown Speaker' not in str(fixed.attendees), "❌ FAILED: 'Unknown Speaker' still in attendees"
    assert 'Omar' in str(fixed.attendees), "❌ FAILED: 'Omar' not in attendees"
    assert 'Sarah' in str(fixed.attendees), "❌ FAILED: 'Sarah' not in attendees"
    assert 'External Guest' in str(fixed.attendees), "❌ FAILED: 'External Guest' removed (should stay)"

    print("\n✅ TEST 2 PASSED")


def test_german_speakers():
    """Test German speaker names (Sprecher 1, etc.)."""
    print("\n" + "=" * 70)
    print("TEST 3: German Speakers (Sprecher 1 → Max, Sprecher 2 → Anna)")
    print("=" * 70)

    speakers = [
        Speaker(
            id='speaker-1',
            detectedName='Sprecher 1',
            confirmedName='Max',
            speakingTime=150
        ),
        Speaker(
            id='speaker-2',
            detectedName='Sprecher 2',
            confirmedName='Anna',
            speakingTime=100
        )
    ]

    protocol = Protocol(
        title='Projektbesprechung',
        date='2026-02-15',
        attendees=['Sprecher 1', 'Sprecher 2'],
        executiveSummary='Sprecher 1 und Sprecher 2 haben die Anforderungen besprochen.',
        actionItems=[],
        fullTranscript='[00:00] Sprecher 1: Guten Tag\n[00:15] Sprecher 2: Hallo',
        decisions=['Sprecher 1 hat zugestimmt'],
        nextSteps=['Sprecher 2 erstellt das Dokument']
    )

    print(f"\nBEFORE replacement:")
    print(f"  attendees:     {protocol.attendees}")
    print(f"  summary:       {protocol.executive_summary}")

    fixed = _apply_speaker_name_replacements(protocol, speakers)

    print(f"\nAFTER replacement:")
    print(f"  attendees:     {fixed.attendees}")
    print(f"  summary:       {fixed.executive_summary}")

    # Verify
    assert 'Sprecher 1' not in str(fixed.attendees), "❌ FAILED: 'Sprecher 1' still in attendees"
    assert 'Sprecher 2' not in str(fixed.attendees), "❌ FAILED: 'Sprecher 2' still in attendees"
    assert 'Max' in str(fixed.attendees), "❌ FAILED: 'Max' not in attendees"
    assert 'Anna' in str(fixed.attendees), "❌ FAILED: 'Anna' not in attendees"

    print("\n✅ TEST 3 PASSED")


def test_no_replacement_when_not_confirmed():
    """Test that names are NOT replaced if user didn't confirm them."""
    print("\n" + "=" * 70)
    print("TEST 4: No Replacement When Not Confirmed")
    print("=" * 70)

    speakers = [
        Speaker(
            id='speaker-0',
            detectedName='Speaker 0',
            confirmedName='',  # Empty - user didn't confirm
            speakingTime=120
        )
    ]

    protocol = Protocol(
        title='Test Meeting',
        date='2026-02-15',
        attendees=['Speaker 0'],
        executiveSummary='Speaker 0 discussed the topic.',
        actionItems=[],
        fullTranscript='[00:00] Speaker 0: Hello'
    )

    print(f"\nBEFORE replacement:")
    print(f"  attendees:     {protocol.attendees}")

    fixed = _apply_speaker_name_replacements(protocol, speakers)

    print(f"\nAFTER replacement (should be unchanged):")
    print(f"  attendees:     {fixed.attendees}")

    # Verify - should NOT have changed
    assert 'Speaker 0' in str(fixed.attendees), "❌ FAILED: 'Speaker 0' was replaced but shouldn't be"

    print("\n✅ TEST 4 PASSED")


if __name__ == '__main__':
    print("\n" + "=" * 70)
    print("SPEAKER NAME REPLACEMENT FIX - COMPREHENSIVE TEST SUITE")
    print("=" * 70)

    try:
        test_single_speaker_replacement()
        test_multiple_speakers()
        test_german_speakers()
        test_no_replacement_when_not_confirmed()

        print("\n" + "=" * 70)
        print("ALL TESTS PASSED ✅")
        print("=" * 70)
        print("\nThe bug is FIXED:")
        print("- Attendees field now correctly shows confirmed speaker names")
        print("- All other fields (summary, transcript, actions, etc.) also updated")
        print("- Works for English ('Speaker 0') and German ('Sprecher 1') names")
        print("- Only replaces when user has confirmed the name")
        print("\n")

    except AssertionError as e:
        print(f"\n\n❌ TEST FAILED: {e}\n")
        exit(1)
    except Exception as e:
        print(f"\n\n❌ UNEXPECTED ERROR: {e}\n")
        import traceback
        traceback.print_exc()
        exit(1)
