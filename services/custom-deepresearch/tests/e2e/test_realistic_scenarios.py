"""
End-to-end realistic scenario tests for Nora Search (DeepSearch).

Based on TechMech Solutions GmbH usage patterns.
Tests real-world scenarios across all 8 Confluence spaces.

Run with: pytest tests/e2e/test_realistic_scenarios.py -v --timeout=180
Set DEEPSEARCH_URL environment variable for custom endpoint.
"""

import asyncio
import os
from dataclasses import dataclass, field
from typing import AsyncGenerator, Optional

import httpx
import pytest

# Mark all tests as e2e and async
pytestmark = [pytest.mark.e2e, pytest.mark.asyncio]


@dataclass
class RealisticScenario:
    """A realistic test scenario based on TechMech Solutions usage."""

    name: str
    query: str
    description: str
    expected_spaces: list[str]
    expected_pages: list[str] = field(default_factory=list)
    min_sources: int = 1
    min_confidence: float = 0.5
    requires_comparison: bool = False
    requires_cross_domain: bool = False
    max_response_time_ms: int = 30000  # 30 seconds default


# TechMech Solutions realistic scenarios based on 8 Confluence spaces
TECHMECH_SCENARIOS = [
    # === ONBOARDING & HR ===
    RealisticScenario(
        name="new_employee_onboarding",
        query="Ich bin neu bei TechMech Solutions. Wie läuft die Einarbeitung ab?",
        description="New employee asking about onboarding process",
        expected_spaces=["HR"],
        expected_pages=["Einarbeitungsplan neue Mitarbeiter", "IT-Equipment Checkliste"],
        min_sources=2,
        min_confidence=0.6,
    ),
    RealisticScenario(
        name="safety_training",
        query="Welche Sicherheitsunterweisungen brauche ich für die Werkstatt?",
        description="Employee asking about required safety training",
        expected_spaces=["HR"],
        expected_pages=["Sicherheitsunterweisung Werkstatt", "PSA-Anforderungen"],
        min_confidence=0.7,
    ),

    # === TROUBLESHOOTING (SRV) ===
    RealisticScenario(
        name="robot_vibration_issue",
        query="Unsere Roboterzelle vibriert stark. Was kann die Ursache sein?",
        description="Technician troubleshooting robot cell vibration",
        expected_spaces=["SRV"],
        expected_pages=["Vibrationen Roboterzelle - Troubleshooting Guide"],
        min_confidence=0.7,
    ),
    RealisticScenario(
        name="plc_not_starting",
        query="Die SPS startet nicht. Welche Schritte soll ich durchführen?",
        description="Technician troubleshooting PLC startup issue",
        expected_spaces=["SRV"],
        expected_pages=["SPS startet nicht - Checkliste"],
        min_confidence=0.7,
    ),
    RealisticScenario(
        name="pneumatic_leak",
        query="Wir haben einen Druckabfall im Pneumatiksystem. Wie finde ich die Leckage?",
        description="Technician finding pneumatic system leak",
        expected_spaces=["SRV"],
        expected_pages=["Druckabfall Pneumatiksystem - Leckagesuche"],
        min_confidence=0.7,
    ),

    # === ENGINEERING (ENG) ===
    RealisticScenario(
        name="robot_specs_comparison",
        query="Was sind die Unterschiede zwischen RC-3000 und RC-5000?",
        description="Engineer comparing robot cell series",
        expected_spaces=["ENG"],
        expected_pages=["RC-3000 Technische Spezifikationen", "RC-5000 Konstruktionszeichnungen"],
        requires_comparison=True,
        min_sources=2,
    ),
    RealisticScenario(
        name="gripper_selection",
        query="Welche Greifersysteme gibt es für die RC-5000 Heavy Duty?",
        description="Engineer selecting gripper systems",
        expected_spaces=["ENG"],
        expected_pages=["RC-5000 Greifersysteme - Übersicht"],
        min_confidence=0.7,
    ),
    RealisticScenario(
        name="sensor_calibration",
        query="Wie kalibriere ich einen DMS-100 Drehmomentsensor?",
        description="Technician calibrating torque sensor",
        expected_spaces=["ENG"],
        expected_pages=["DMS-100 Kalibrieranleitung"],
        min_confidence=0.7,
    ),

    # === PROJECT DETAILS (PRJ) ===
    RealisticScenario(
        name="autotech_project_status",
        query="Was ist der aktuelle Stand beim AutoTech AG Projekt?",
        description="Project manager checking project status",
        expected_spaces=["PRJ"],
        expected_pages=["PRJ-2025-018 - AutoTech AG Montageanlage"],
        min_sources=2,
    ),
    RealisticScenario(
        name="lessons_learned_electrowerk",
        query="Welche Lessons Learned gab es beim ElectroWerk Prüfstation Projekt?",
        description="Engineer reviewing past project learnings",
        expected_spaces=["PRJ"],
        expected_pages=["PRJ-2024-067 - ElectroWerk Prüfstation", "Lessons Learned Workshop Protokoll"],
        min_confidence=0.6,
    ),
    RealisticScenario(
        name="cleanroom_requirements",
        query="Welche Reinraumanforderungen gelten für das MediPack Projekt?",
        description="Engineer checking cleanroom requirements",
        expected_spaces=["PRJ"],
        expected_pages=["PRJ-2025-022 - MediPack Solutions Verpackungslinie", "Anforderungen Reinraumumgebung"],
        min_confidence=0.7,
    ),

    # === COMPLIANCE (CMP) ===
    RealisticScenario(
        name="ce_marking_requirements",
        query="Was muss ich bei der CE-Kennzeichnung beachten?",
        description="Engineer checking CE marking requirements",
        expected_spaces=["CMP"],
        expected_pages=["CE-Kennzeichnung", "Maschinenrichtlinie 200642EG"],
        min_sources=2,
    ),
    RealisticScenario(
        name="risk_assessment_iso12100",
        query="Wie führe ich eine Risikobeurteilung nach ISO 12100 durch?",
        description="Safety engineer performing risk assessment",
        expected_spaces=["CMP"],
        expected_pages=["Risikobeurteilung - Methodik nach ISO 12100", "Gefährdungsanalyse Methodik"],
        min_confidence=0.7,
    ),
    RealisticScenario(
        name="food_industry_compliance",
        query="Welche Hygiene-Anforderungen gelten für Lebensmittelanlagen?",
        description="Engineer checking food industry compliance",
        expected_spaces=["CMP"],
        expected_pages=["EHEDG Hygienic Design Prinzipien", "FDA Regulations für Food Contact"],
        min_sources=2,
    ),

    # === QUALITY (QM) ===
    RealisticScenario(
        name="8d_report_process",
        query="Wie erstelle ich einen 8D-Report bei einer Kundenreklamation?",
        description="Quality engineer creating 8D report",
        expected_spaces=["QM"],
        expected_pages=["8D-Reports und Reklamationen"],
        min_confidence=0.7,
    ),
    RealisticScenario(
        name="incoming_inspection",
        query="Welche Prüfungen sind bei der Wareneingangskontrolle durchzuführen?",
        description="Quality technician checking incoming inspection",
        expected_spaces=["QM"],
        expected_pages=["AWA-001 Mechanische Komponenten prüfen", "AWA-002 Elektrische Komponenten prüfen"],
        min_sources=2,
    ),

    # === IT/SOFTWARE ===
    RealisticScenario(
        name="tia_portal_guidelines",
        query="Welche Programmierrichtlinien gelten für Siemens TIA Portal?",
        description="PLC programmer checking coding guidelines",
        expected_spaces=["IT"],
        expected_pages=["Siemens TIA Portal", "TIA Portal Projektvorlagen"],
        min_confidence=0.7,
    ),
    RealisticScenario(
        name="network_configuration",
        query="Wie ist das IP-Adressschema für Standardanlagen organisiert?",
        description="IT engineer checking network configuration",
        expected_spaces=["IT"],
        expected_pages=["IP-Adressvergabe Schema", "Netzwerkplan Standardanlage"],
        min_confidence=0.7,
    ),

    # === CROSS-DOMAIN (Multiple Spaces) ===
    RealisticScenario(
        name="supplier_approval_pneumatics",
        query="Welche Lieferanten sind für Pneumatikkomponenten zugelassen und wie werden sie bewertet?",
        description="Procurement checking approved suppliers",
        expected_spaces=["ENG", "QM"],
        expected_pages=["Festo Pneumatikkomponenten", "Approved Vendor List", "Lieferantenbewertung Q4-2024"],
        requires_cross_domain=True,
        min_sources=2,
    ),
    RealisticScenario(
        name="foodproc_compliance_full",
        query="Welche technischen und Compliance-Anforderungen gelten für das FoodProc Palettierroboter Projekt?",
        description="Project manager checking full project requirements",
        expected_spaces=["PRJ", "CMP", "ENG"],
        expected_pages=["PRJ-2025-031 - FoodProc GmbH", "EHEDG Hygienic Design Prinzipien"],
        requires_cross_domain=True,
        min_sources=3,
        max_response_time_ms=60000,  # Complex query needs more time
    ),
]


class TestRealisticScenarios:
    """E2E tests based on TechMech Solutions GmbH realistic usage patterns."""

    @pytest.fixture
    async def client(self) -> AsyncGenerator[httpx.AsyncClient, None]:
        """HTTP client for E2E tests with extended timeout."""
        base_url = os.environ.get("DEEPSEARCH_URL", "http://localhost:8000")
        async with httpx.AsyncClient(base_url=base_url, timeout=180.0) as client:
            yield client

    async def _run_search(
        self, client: httpx.AsyncClient, query: str
    ) -> dict:
        """Execute sync search and return result."""
        response = await client.post(
            "/api/v1/search/sync",
            json={"query": query},
        )
        assert response.status_code == 200, f"Search failed: {response.text}"
        return response.json()

    def _check_scenario_result(
        self, result: dict, scenario: RealisticScenario
    ) -> list[str]:
        """
        Check if result meets scenario expectations.

        Returns list of failed checks (empty if all pass).
        """
        failures = []

        # Check status
        if result.get("status") != "completed":
            failures.append(f"Status not completed: {result.get('status')}")
            return failures

        # Check confidence
        confidence = result.get("confidence_score", 0)
        if confidence < scenario.min_confidence:
            failures.append(
                f"Confidence {confidence:.2f} < min {scenario.min_confidence}"
            )

        # Check response time
        time_ms = result.get("processing_time_ms", 0)
        if time_ms > scenario.max_response_time_ms:
            failures.append(
                f"Response time {time_ms}ms > max {scenario.max_response_time_ms}ms"
            )

        # Check if answer exists
        final_report = result.get("final_report", "")
        if len(final_report) < 50:
            failures.append(f"Final report too short: {len(final_report)} chars")

        # Check sources count (if available)
        sources = result.get("sources", [])
        if len(sources) < scenario.min_sources:
            failures.append(
                f"Sources {len(sources)} < min {scenario.min_sources}"
            )

        return failures

    # === INDIVIDUAL SCENARIO TESTS ===

    @pytest.mark.parametrize(
        "scenario",
        [s for s in TECHMECH_SCENARIOS if not s.requires_cross_domain],
        ids=[s.name for s in TECHMECH_SCENARIOS if not s.requires_cross_domain],
    )
    async def test_single_domain_scenario(
        self, client: httpx.AsyncClient, scenario: RealisticScenario
    ):
        """Test single-domain scenarios."""
        result = await self._run_search(client, scenario.query)
        failures = self._check_scenario_result(result, scenario)

        if failures:
            pytest.fail(
                f"Scenario '{scenario.name}' failed:\n" + "\n".join(failures)
            )

    @pytest.mark.parametrize(
        "scenario",
        [s for s in TECHMECH_SCENARIOS if s.requires_cross_domain],
        ids=[s.name for s in TECHMECH_SCENARIOS if s.requires_cross_domain],
    )
    async def test_cross_domain_scenario(
        self, client: httpx.AsyncClient, scenario: RealisticScenario
    ):
        """Test cross-domain scenarios requiring multiple spaces."""
        result = await self._run_search(client, scenario.query)
        failures = self._check_scenario_result(result, scenario)

        if failures:
            pytest.fail(
                f"Cross-domain scenario '{scenario.name}' failed:\n"
                + "\n".join(failures)
            )


class TestEdgeCases:
    """Test edge cases and error handling."""

    @pytest.fixture
    async def client(self) -> AsyncGenerator[httpx.AsyncClient, None]:
        """HTTP client for E2E tests."""
        base_url = os.environ.get("DEEPSEARCH_URL", "http://localhost:8000")
        async with httpx.AsyncClient(base_url=base_url, timeout=60.0) as client:
            yield client

    async def test_out_of_domain_query(self, client: httpx.AsyncClient):
        """System should handle queries outside knowledge base gracefully."""
        result = await client.post(
            "/api/v1/search/sync",
            json={"query": "Wie ist das Wetter in München heute?"},
        )
        assert result.status_code == 200
        data = result.json()

        # Should complete but with low confidence
        assert data["status"] == "completed"
        # Out of domain should have lower confidence
        assert data.get("confidence_score", 1.0) < 0.8

    async def test_ambiguous_query(self, client: httpx.AsyncClient):
        """System should handle ambiguous queries."""
        result = await client.post(
            "/api/v1/search/sync",
            json={"query": "Problem"},
        )
        assert result.status_code == 200
        data = result.json()
        # Should still complete
        assert data["status"] == "completed"

    async def test_mixed_language_query(self, client: httpx.AsyncClient):
        """System should handle mixed language queries."""
        result = await client.post(
            "/api/v1/search/sync",
            json={"query": "How do I calibrate the DMS-100 sensor?"},
        )
        assert result.status_code == 200
        data = result.json()
        assert data["status"] == "completed"

    async def test_very_specific_query(self, client: httpx.AsyncClient):
        """System should handle very specific technical queries."""
        result = await client.post(
            "/api/v1/search/sync",
            json={"query": "Temperaturbeständigkeit der Komponenten für FoodProc bei -20°C bis +60°C"},
        )
        assert result.status_code == 200
        data = result.json()
        assert data["status"] == "completed"

    async def test_project_code_query(self, client: httpx.AsyncClient):
        """System should handle queries with project codes."""
        result = await client.post(
            "/api/v1/search/sync",
            json={"query": "Details zu Projekt PRJ-2025-018"},
        )
        assert result.status_code == 200
        data = result.json()
        assert data["status"] == "completed"


class TestLatencyBenchmarks:
    """Benchmark latency for different query types."""

    @pytest.fixture
    async def client(self) -> AsyncGenerator[httpx.AsyncClient, None]:
        """HTTP client for E2E tests."""
        base_url = os.environ.get("DEEPSEARCH_URL", "http://localhost:8000")
        async with httpx.AsyncClient(base_url=base_url, timeout=180.0) as client:
            yield client

    # Simple queries should be fast
    SIMPLE_LATENCY_TARGET_MS = 10000  # 10 seconds

    # Complex queries can take longer
    COMPLEX_LATENCY_TARGET_MS = 30000  # 30 seconds

    async def test_simple_query_latency(self, client: httpx.AsyncClient):
        """Simple factual query should complete within target latency."""
        result = await client.post(
            "/api/v1/search/sync",
            json={"query": "Welche Fehlercodes gibt es bei der RC-3000?"},
        )
        assert result.status_code == 200
        data = result.json()

        latency = data.get("processing_time_ms", 999999)
        assert latency < self.SIMPLE_LATENCY_TARGET_MS, (
            f"Simple query latency {latency}ms exceeded target {self.SIMPLE_LATENCY_TARGET_MS}ms"
        )

    async def test_complex_query_latency(self, client: httpx.AsyncClient):
        """Complex multi-source query should complete within target latency."""
        result = await client.post(
            "/api/v1/search/sync",
            json={
                "query": "Vergleiche die Konstruktionsstandards für RC-3000 und RC-5000 "
                "hinsichtlich Werkstoffauswahl und Lastberechnungen"
            },
        )
        assert result.status_code == 200
        data = result.json()

        latency = data.get("processing_time_ms", 999999)
        assert latency < self.COMPLEX_LATENCY_TARGET_MS, (
            f"Complex query latency {latency}ms exceeded target {self.COMPLEX_LATENCY_TARGET_MS}ms"
        )


class TestAgentRouting:
    """Test that supervisor routes to correct agents."""

    @pytest.fixture
    async def client(self) -> AsyncGenerator[httpx.AsyncClient, None]:
        """HTTP client for E2E tests."""
        base_url = os.environ.get("DEEPSEARCH_URL", "http://localhost:8000")
        async with httpx.AsyncClient(base_url=base_url, timeout=120.0) as client:
            yield client

    ROUTING_TEST_CASES = [
        # (query, expected_to_use_confluence)
        ("RC-3000 Technische Spezifikationen", True),
        ("Wie erstelle ich einen 8D-Report?", True),
        ("SPS startet nicht - was tun?", True),
        ("Welche Greifersysteme gibt es für RC-5000?", True),
        ("ISO 12100 Risikobeurteilung Methodik", True),
        ("AutoTech AG Projekt Status", True),
    ]

    @pytest.mark.parametrize(
        "query,expect_confluence",
        ROUTING_TEST_CASES,
        ids=[f"routing_{i}" for i in range(len(ROUTING_TEST_CASES))],
    )
    async def test_agent_routing(
        self, client: httpx.AsyncClient, query: str, expect_confluence: bool
    ):
        """Test that queries are routed to the correct agent."""
        result = await client.post(
            "/api/v1/search/sync",
            json={"query": query},
        )
        assert result.status_code == 200
        data = result.json()

        # Verify search completed
        assert data["status"] == "completed"

        # If we expect Confluence sources, check that sources exist
        if expect_confluence:
            sources = data.get("sources", [])
            # Should have found at least some sources from Confluence
            assert len(sources) > 0, f"Expected Confluence sources for: {query}"
