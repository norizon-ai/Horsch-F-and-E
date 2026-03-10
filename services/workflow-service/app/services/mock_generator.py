"""
Dev/test mock data generator -- not imported in production.

Generates realistic German business meeting data for development
and testing purposes only. Production code should not depend on
this module at import time.
"""

from typing import List, Optional, Dict, Any
from datetime import datetime, timedelta
import random

from app.models import (
    Speaker,
    ActionItem,
    Protocol,
    CustomSection,
)


class MockGenerator:
    """Generates mock data for the workflow API."""

    # German names for realistic mock data
    FIRST_NAMES = [
        "Max", "Anna", "Thomas", "Maria", "Klaus", "Sabine",
        "Martin", "Julia", "Stefan", "Lisa", "Michael", "Sarah"
    ]

    LAST_NAMES = [
        "Mustermann", "Schmidt", "Weber", "Bauer", "Fischer",
        "Müller", "Schneider", "Hoffmann", "Wagner", "Braun"
    ]

    DEPARTMENTS = [
        "Engineering", "Product", "IT-Abteilung", "Marketing",
        "Sales", "HR", "Finance", "Operations", "Support"
    ]

    # Template-specific mock content
    TEMPLATE_MOCK_CONTENT: Dict[str, Dict[str, Any]] = {
        "CLIENT_UPDATE": {
            "title": "ACME GmbH - Quartals-Update Q1 2026",
            "tldr": "Gutes Meeting mit dem ACME-Team. Projekt liegt im Zeitplan, ERP-Integration zu 80% abgeschlossen. Kunde zufrieden mit Fortschritt, aber besorgt wegen Timeline für Phase 2. Nächster Meilenstein: API-Dokumentation bis 15.02.",
            "decisions": [
                "ERP-Integration wird vor UI-Redesign priorisiert",
                "Wöchentliche Status-Updates per E-Mail statt bi-weekly Calls",
                "Pilotphase startet am 01.03.2026"
            ],
            "action_items": [
                ("API-Dokumentation finalisieren", 14),
                ("Stakeholder-Update senden", 3),
                ("Pilotphase-Zeitplan erstellen", 7),
            ],
            "next_steps": [
                "Nächstes Meeting: Montag, 10:00 Uhr",
                "Pilotphase-Kickoff planen",
            ],
            "custom_sections": [
                {
                    "id": "status_updates",
                    "label": "Status Updates",
                    "type": "list",
                    "content": [
                        "ERP-Integration: 80% abgeschlossen, API-Endpoints fertig",
                        "UI-Redesign: Mockups erstellt, Feedback ausstehend",
                        "Performance: Ladezeiten um 40% reduziert",
                        "Testing: 85% Code-Coverage erreicht"
                    ]
                },
                {
                    "id": "key_insights",
                    "label": "Key Insights",
                    "type": "list",
                    "content": [
                        "Kunde priorisiert Stabilität über neue Features",
                        "Budget für Q2 bereits genehmigt",
                        "IT-Abteilung des Kunden unterstützt aktiv",
                        "Konkurrenzdruck erhöht Dringlichkeit"
                    ]
                },
                {
                    "id": "client_sentiment",
                    "label": "Client Sentiment",
                    "type": "text",
                    "content": "Kunde ist insgesamt zufrieden mit dem Projektfortschritt. Besondere Anerkennung für die schnelle Reaktionszeit des Support-Teams. Leichte Bedenken bezüglich der Timeline für Phase 2, aber Vertrauen in das Team. Interesse an langfristiger Partnerschaft signalisiert."
                }
            ]
        },
        "CLIENT_TECHNICAL": {
            "title": "TechCorp - SAP Integration Review",
            "tldr": "Technisches Review der SAP-Schnittstelle mit IT-Team von TechCorp. Authentifizierung über OAuth 2.0 bestätigt. Datenformat-Mapping für Stammdaten definiert. Offene Frage: Legacy-System-Migration und Datenmigrationsstrategie.",
            "decisions": [
                "OAuth 2.0 für Authentifizierung",
                "JSON-Format für Datenaustausch",
                "Batch-Import für Stammdaten",
            ],
            "action_items": [
                ("API-Spezifikation erstellen", 7),
                ("Testumgebung einrichten", 14),
                ("Datenmigrations-Konzept erstellen", 10),
            ],
            "next_steps": [
                "Technical Deep-Dive: Mittwoch, 14:00 Uhr",
                "Sandbox-Zugang für Tests bereitstellen",
            ],
            "custom_sections": [
                {
                    "id": "technical_requirements",
                    "label": "Technical Requirements",
                    "type": "list",
                    "content": [
                        "REST API mit OAuth 2.0 Authentication",
                        "JSON-basierter Datenaustausch (UTF-8)",
                        "Rate Limiting: max. 1000 Requests/Minute",
                        "Webhook-Support für Real-time Updates",
                        "TLS 1.3 Verschlüsselung mandatory"
                    ]
                },
                {
                    "id": "system_landscape",
                    "label": "System Landscape",
                    "type": "list",
                    "content": [
                        "SAP S/4HANA (On-Premise, Version 2023)",
                        "Legacy ERP: SAP R/3 (wird migriert)",
                        "Middleware: MuleSoft Anypoint",
                        "Database: Oracle 19c",
                        "Identity Provider: Azure AD"
                    ]
                },
                {
                    "id": "constraints",
                    "label": "Constraints",
                    "type": "list",
                    "content": [
                        "Wartungsfenster: Samstag 02:00-06:00 Uhr",
                        "Keine Änderungen während Monatsabschluss",
                        "Max. 5GB pro Batch-Upload",
                        "Compliance: ISO 27001 erforderlich"
                    ]
                },
                {
                    "id": "data_integrations",
                    "label": "Data Integrations",
                    "type": "list",
                    "content": [
                        "Stammdaten: Kunden, Lieferanten, Materialien",
                        "Bewegungsdaten: Bestellungen, Lieferscheine",
                        "Finanzdaten: Rechnungen, Zahlungen (read-only)",
                        "Sync-Intervall: 15 Minuten für kritische Daten"
                    ]
                }
            ]
        },
        "PROSPECT_SALES": {
            "title": "NeueKunde AG - Produkt-Demo",
            "tldr": "Erstes Demo-Meeting mit NeueKunde AG (200 MA, Maschinenbau). Interesse an Wissensdokumentation nach Pensionierungswelle. Hauptproblem: Undokumentiertes Expertenwissen. Interesse hoch, nächster Schritt: Pilot-Workshop.",
            "decisions": [
                "Pilot-Workshop für Februar geplant",
                "Fokus auf Produktions-Know-how",
            ],
            "action_items": [
                ("Angebot für Pilot-Workshop senden", 3),
                ("Use-Case-Dokumentation vorbereiten", 5),
                ("Referenzkundenanruf organisieren", 7),
            ],
            "next_steps": [
                "Follow-up Call: Freitag, 11:00 Uhr",
                "Entscheidung bis Ende Februar erwartet",
            ],
            "custom_sections": [
                {
                    "id": "company_context",
                    "label": "Company Context",
                    "type": "text",
                    "content": "NeueKunde AG ist ein mittelständischer Maschinenbauer mit 200 Mitarbeitern in Bayern. Spezialisiert auf Sondermaschinen für die Automobilindustrie. 40% der Belegschaft geht in den nächsten 5 Jahren in Rente. Aktuell keine strukturierte Wissensdokumentation."
                },
                {
                    "id": "pain_points",
                    "label": "Pain Points",
                    "type": "list",
                    "content": [
                        "Kritisches Expertenwissen nur in den Köpfen der Mitarbeiter",
                        "Einarbeitung neuer Mitarbeiter dauert 12-18 Monate",
                        "Kein zentrales System für technische Dokumentation",
                        "Wiederkehrende Fehler durch fehlendes Wissensmanagement",
                        "Hohe Abhängigkeit von einzelnen Schlüsselpersonen"
                    ]
                },
                {
                    "id": "interest_level",
                    "label": "Interest Level",
                    "type": "text",
                    "content": "Sehr hohes Interesse (8/10). Geschäftsführung hat das Thema zur strategischen Priorität erklärt. Budget ist grundsätzlich vorhanden. Entscheidung wird vom Geschäftsführer und Produktionsleiter gemeinsam getroffen."
                },
                {
                    "id": "objections",
                    "label": "Objections & Concerns",
                    "type": "list",
                    "content": [
                        "Bedenken bzgl. Akzeptanz bei älteren Mitarbeitern",
                        "Frage nach Datensicherheit (sensible Produktionsdaten)",
                        "Zeitaufwand für die Wissenserfassung",
                        "Integration mit bestehendem ERP-System"
                    ]
                }
            ]
        },
        "PARTNER": {
            "title": "Systemhaus Müller - Kooperationsgespräch",
            "tldr": "Erste Gespräche mit Systemhaus Müller über mögliche Partnerschaft. Interesse an Reseller-Modell für ihre mittelständischen Kunden. Gemeinsame Zielgruppe identifiziert. Nächster Schritt: Partnervertrag prüfen.",
            "decisions": [
                "Reseller-Rabatt: 20% auf Listenpreis",
                "Gemeinsamer Pilot bei Bestandskunde geplant",
            ],
            "action_items": [
                ("Partnervertragsentwurf senden", 7),
                ("Sales-Training für Partner-Team planen", 14),
                ("Co-Marketing-Möglichkeiten prüfen", 10),
            ],
            "next_steps": [
                "Vertragsverhandlung: KW 8",
                "Partner-Kickoff: Q2 2026",
            ],
            "custom_sections": [
                {
                    "id": "discussion_topics",
                    "label": "Discussion Topics",
                    "type": "list",
                    "content": [
                        "Partnerschaftsmodell: Reseller vs. Referral",
                        "Preisgestaltung und Rabattstruktur",
                        "Support-Verantwortlichkeiten (1st/2nd Level)",
                        "Marketing-Zusammenarbeit und Lead-Sharing",
                        "Schulung des Partner-Vertriebsteams"
                    ]
                },
                {
                    "id": "mutual_value",
                    "label": "Mutual Value",
                    "type": "list",
                    "content": [
                        "Für uns: Zugang zu 50+ Bestandskunden im Mittelstand",
                        "Für uns: Regionale Präsenz und Vertrauensvorsprung",
                        "Für Partner: Erweiterung des Portfolios um KI-Lösung",
                        "Für Partner: Wiederkehrende Umsätze durch SaaS-Modell",
                        "Gemeinsam: Stärkere Position gegenüber Enterprise-Anbietern"
                    ]
                },
                {
                    "id": "partner_concerns",
                    "label": "Partner Concerns",
                    "type": "list",
                    "content": [
                        "Technische Komplexität für eigenes Team",
                        "Aufwand für Produktschulung",
                        "Kannibalisierung bestehender Services",
                        "Mindestabnahmemengen im Vertrag"
                    ]
                }
            ]
        },
        "COACH_MENTOR": {
            "title": "AktivSenioren - Mentor Session mit Herrn Dr. Bauer",
            "tldr": "Mentoring-Session zu Vertriebsstrategie. Feedback: Fokus auf konkrete ROI-Berechnung für Kunden. Empfehlung: Branchen-spezifische Case Studies entwickeln. Warnung vor zu schneller Expansion.",
            "decisions": [
                "ROI-Kalkulator als Vertriebstool entwickeln",
                "Maschinenbau als Primärbranche fokussieren",
            ],
            "action_items": [
                ("ROI-Kalkulator-Konzept erstellen", 14),
                ("2-3 Case Studies ausarbeiten", 21),
                ("Pitch-Deck überarbeiten", 7),
            ],
            "next_steps": [
                "Nächste Mentor-Session: 15.03.2026",
                "Pitch-Deck zur Review senden",
            ],
            "custom_sections": [
                {
                    "id": "topics_discussed",
                    "label": "Topics Discussed",
                    "type": "list",
                    "content": [
                        "Vertriebsstrategie für Mittelstand",
                        "Preispositionierung und Value-Argumentation",
                        "Skalierung des Teams",
                        "Fundraising-Timing und -Strategie"
                    ]
                },
                {
                    "id": "feedback_received",
                    "label": "Feedback Received",
                    "type": "list",
                    "content": [
                        "Pitch ist zu technisch, mehr Business-Value zeigen",
                        "ROI-Berechnung fehlt - Kunden brauchen harte Zahlen",
                        "Referenzkunden sind wichtiger als Features",
                        "Team wächst zu schnell für aktuelle Umsatzbasis"
                    ]
                },
                {
                    "id": "recommendations",
                    "label": "Recommendations",
                    "type": "list",
                    "content": [
                        "ROI-Kalkulator entwickeln (Zeitersparnis, Fehlerreduktion)",
                        "3 detaillierte Case Studies mit messbaren Ergebnissen",
                        "Branchenfokus: erst Maschinenbau, dann IT-Dienstleister",
                        "Netzwerk nutzen: Intro zu 2-3 potenziellen Kunden",
                        "Fundraising erst nach 10 zahlenden Kunden"
                    ]
                }
            ]
        },
        "NETWORKING": {
            "title": "DLD Conference - Kontakt mit Dr. Sarah Klein",
            "tldr": "Interessanter Kontakt auf der DLD: Dr. Sarah Klein, CDO bei Industriekonzern. Interesse an AI-gestützter Wissensdokumentation. Potenzielle Enterprise-Kundin. Follow-up vereinbart.",
            "decisions": [],
            "action_items": [
                ("LinkedIn-Verbindung senden", 1),
                ("Intro-Meeting anfragen", 3),
                ("Company Research durchführen", 2),
            ],
            "next_steps": [
                "Intro-Call ansetzen",
                "Enterprise-Offering vorbereiten",
            ],
            "custom_sections": [
                {
                    "id": "contact_background",
                    "label": "Contact Background",
                    "type": "text",
                    "content": "Dr. Sarah Klein, Chief Digital Officer bei Müller Industrie AG (DAX-Konzern, 15.000 Mitarbeiter). Zuvor McKinsey Digital, dann VP Digital Transformation bei Siemens. Promotion in Wirtschaftsinformatik, TU München. Fokus auf KI-Implementierung in der Industrie."
                },
                {
                    "id": "current_work",
                    "label": "Current Work & Challenges",
                    "type": "list",
                    "content": [
                        "Leitet Digitalisierungsprogramm mit €50M Budget",
                        "Aktuell: KI-Strategie für Wissensmanagement",
                        "Problem: Wissenssilos zwischen Standorten",
                        "Sucht nach skalierbarer Lösung für 8 Werke"
                    ]
                },
                {
                    "id": "mutual_opportunities",
                    "label": "Mutual Opportunities",
                    "type": "list",
                    "content": [
                        "Potenzial: Enterprise-Pilot mit einer Abteilung",
                        "Referenz: Große Marke als Leuchtturmprojekt",
                        "Intro: Kann zu anderen CDOs im Netzwerk vorstellen",
                        "Feedback: Produktfeedback aus Enterprise-Perspektive"
                    ]
                },
                {
                    "id": "follow_up_notes",
                    "label": "Follow-up Notes",
                    "type": "text",
                    "content": "Visitenkarte erhalten. Sie hat explizit um ein Demo-Meeting gebeten. Termin idealerweise in den nächsten 2 Wochen, bevor ihr Q2-Planning beginnt. Interesse speziell an der Integration mit SharePoint und SAP."
                }
            ]
        },
        "TEAM_SYNC": {
            "title": "Team Sync - KW05 2026",
            "tldr": "Wöchentliches Team-Sync. Frontend: Meeting-Workflow zu 70% fertig. Backend: API-Mocks implementiert. Blocker: Design-Entscheidung für Export-Flow. Entscheidung: Export-Dialog nächste Woche fertigstellen.",
            "decisions": [
                "Export-Dialog-Design bis Freitag finalisieren",
                "Code-Review-Prozess einführen",
            ],
            "action_items": [
                ("Export-Flow Design fertigstellen", 5),
                ("Code-Review Guidelines dokumentieren", 7),
                ("Sprint-Retro vorbereiten", 3),
            ],
            "next_steps": [
                "Nächstes Sync: Montag, 10:00 Uhr",
                "Sprint Review: Freitag, 14:00 Uhr",
            ],
            "custom_sections": [
                {
                    "id": "updates_by_person",
                    "label": "Updates by Person",
                    "type": "list",
                    "content": [
                        "Lisa (Frontend): Meeting-Workflow 70%, Template-Selector fertig",
                        "Max (Backend): API-Mocks implementiert, SSE-Streaming funktioniert",
                        "Anna (Design): Export-Dialog Wireframes in Review",
                        "Thomas (DevOps): CI/CD Pipeline optimiert, Deploy-Zeit -40%"
                    ]
                },
                {
                    "id": "blockers",
                    "label": "Blockers",
                    "type": "list",
                    "content": [
                        "Export-Flow: Warten auf finale Design-Entscheidung",
                        "Confluence API: Rate-Limiting-Issues bei großen Dokumenten",
                        "Testing: Fehlende Testdaten für Edge-Cases"
                    ]
                },
                {
                    "id": "sprint_progress",
                    "label": "Sprint Progress",
                    "type": "text",
                    "content": "Sprint ist zu 65% abgeschlossen (Tag 8 von 10). 12 von 18 Story Points erledigt. Velocity liegt im Rahmen des Durchschnitts. Risiko: Export-Feature könnte in nächsten Sprint rutschen."
                }
            ]
        },
        "TEAM_DESIGN": {
            "title": "Feature Design - Chat Export Funktion",
            "tldr": "Design-Session für Chat-Export. Entschieden: PDF und Confluence als Export-Ziele. User-Flow: Template auswählen, Vorschau, Export. Offen: Handling großer Dateien. Edge Case: Multi-Speaker-Calls.",
            "decisions": [
                "PDF und Confluence als erste Export-Ziele",
                "Zweistufiger Export-Flow mit Vorschau",
                "Template-Auswahl vor Export",
            ],
            "action_items": [
                ("Wireframes erstellen", 5),
                ("User-Flow dokumentieren", 3),
                ("Edge-Cases definieren", 7),
            ],
            "next_steps": [
                "Design-Review: Mittwoch",
                "Implementation Start: KW 7",
            ],
            "custom_sections": [
                {
                    "id": "problem_statement",
                    "label": "Problem Statement",
                    "type": "text",
                    "content": "Nutzer möchten Meeting-Protokolle einfach exportieren und teilen. Aktuell ist nur Copy-Paste möglich, was Formatierung zerstört. Ziel: One-Click-Export in verschiedene Formate mit Beibehaltung der Struktur."
                },
                {
                    "id": "user_flow",
                    "label": "User Flow",
                    "type": "list",
                    "content": [
                        "1. Nutzer klickt 'Export' Button im Protokoll",
                        "2. Modal öffnet sich mit Format-Auswahl (PDF/Confluence)",
                        "3. Bei Confluence: Space und Parent-Page auswählen",
                        "4. Vorschau des formatierten Dokuments",
                        "5. Bestätigung und Export",
                        "6. Erfolgsmeldung mit Link zum Dokument"
                    ]
                },
                {
                    "id": "design_decisions",
                    "label": "Design Decisions",
                    "type": "list",
                    "content": [
                        "Modal statt neuer Seite (schneller, weniger Kontext-Wechsel)",
                        "Vorschau ist optional, aber standardmäßig eingeklappt",
                        "Letzter Export-Ort wird gespeichert (Convenience)",
                        "PDF-Export läuft client-seitig (kein Server-Roundtrip)",
                        "Confluence-Export zeigt Fortschrittsbalken"
                    ]
                },
                {
                    "id": "edge_cases",
                    "label": "Edge Cases",
                    "type": "list",
                    "content": [
                        "Sehr lange Protokolle (>50 Seiten): Pagination in PDF",
                        "Protokoll mit Bildern/Attachments: Separate Behandlung",
                        "Offline-Modus: Export nur lokal als PDF möglich",
                        "Confluence-Timeout: Retry-Mechanismus mit Feedback",
                        "Fehlende Berechtigungen: Klare Fehlermeldung + Hilfelink"
                    ]
                }
            ]
        },
    }

    def generate_speakers(self, count: int = 3) -> List[Speaker]:
        """Generate mock speakers with German names."""
        speakers = []
        used_names = set()

        for i in range(count):
            # Generate unique name
            while True:
                first = random.choice(self.FIRST_NAMES)
                last = random.choice(self.LAST_NAMES)
                full_name = f"{first} {last}"
                if full_name not in used_names:
                    used_names.add(full_name)
                    break

            speaker = Speaker(
                id=f"speaker-{i + 1}",
                detectedName=f"Sprecher {i + 1}",
                confirmedName="",
                sampleAudioUrl=f"/audio/sample-speaker-{i + 1}.mp3",
                speakingTime=random.randint(120, 400),
                transcriptSnippet=self._generate_snippet(),
                confidence=random.uniform(0.75, 0.98),
                isExternal=i == count - 1 if count > 2 else False,
                waveformData=self._generate_waveform(),
            )
            speakers.append(speaker)

        return speakers

    def _generate_snippet(self) -> str:
        """Generate a short transcript snippet."""
        snippets = [
            "Guten Morgen, vielen Dank dass ihr alle dabei seid...",
            "Ich habe die neuesten Zahlen mitgebracht und...",
            "Die API-Schnittstelle ist zu 80% fertig...",
            "Bezüglich der Performance-Tests haben wir...",
            "Das sollten wir auf jeden Fall priorisieren...",
            "Ich setze mich heute noch mit dem Kunden zusammen...",
        ]
        return random.choice(snippets)

    def _generate_waveform(self, length: int = 50) -> List[float]:
        """Generate mock waveform data."""
        return [random.uniform(0.1, 1.0) for _ in range(length)]

    def _get_attendee_names(self, speakers: Optional[List[Speaker]]) -> List[str]:
        """Get attendee names from speakers or generate new ones."""
        import logging
        logger = logging.getLogger(__name__)

        if speakers:
            attendees = []
            logger.info(f"_get_attendee_names: Processing {len(speakers)} speakers")
            for i, speaker in enumerate(speakers):
                # Handle both dict and Speaker object formats
                if isinstance(speaker, dict):
                    confirmed_name = speaker.get("confirmedName")
                    detected_name = speaker.get("detectedName")
                    logger.info(f"  Speaker {i} (dict): confirmed='{confirmed_name}', detected='{detected_name}'")
                else:
                    confirmed_name = speaker.confirmed_name
                    detected_name = speaker.detected_name
                    logger.info(f"  Speaker {i} (object): confirmed='{confirmed_name}', detected='{detected_name}'")

                # CRITICAL FIX: Check for confirmed_name and strip whitespace
                # Empty strings, None, or whitespace-only strings should fall through to detected_name
                confirmed_name_cleaned = confirmed_name.strip() if confirmed_name else ""

                if confirmed_name_cleaned:
                    logger.info(f"    → Using confirmed name: '{confirmed_name_cleaned}'")
                    attendees.append(confirmed_name_cleaned)
                elif detected_name:
                    logger.info(f"    → Using detected name: '{detected_name}' (confirmed name was empty or None)")
                    attendees.append(detected_name)
                else:
                    first = random.choice(self.FIRST_NAMES)
                    last = random.choice(self.LAST_NAMES)
                    generated_name = f"{first} {last}"
                    logger.info(f"    → Generated random name: '{generated_name}' (no confirmed or detected name)")
                    attendees.append(generated_name)
            logger.info(f"_get_attendee_names: Returning attendees: {attendees}")
            return attendees
        else:
            # Generate 3 random names
            used = set()
            names = []
            for _ in range(3):
                while True:
                    first = random.choice(self.FIRST_NAMES)
                    last = random.choice(self.LAST_NAMES)
                    name = f"{first} {last}"
                    if name not in used:
                        used.add(name)
                        names.append(name)
                        break
            return names

    def generate_protocol(
        self,
        speakers: Optional[List[Speaker]] = None,
        template_id: Optional[str] = None
    ) -> Protocol:
        """Generate a complete mock protocol, optionally using template-specific content."""
        attendees = self._get_attendee_names(speakers)
        today = datetime.now()

        # Use template-specific content if available
        if template_id and template_id in self.TEMPLATE_MOCK_CONTENT:
            mock_content = self.TEMPLATE_MOCK_CONTENT[template_id]

            action_items = []
            for i, (text, days_offset) in enumerate(mock_content.get("action_items", [])):
                due_date = (today + timedelta(days=days_offset)).strftime("%Y-%m-%d")
                action_items.append(ActionItem(
                    id=f"action-{i + 1}",
                    text=text,
                    assignee=attendees[i % len(attendees)],
                    dueDate=due_date,
                    completed=False,
                ))

            # Build custom sections from template
            custom_sections = None
            if "custom_sections" in mock_content:
                custom_sections = [
                    CustomSection(
                        id=section["id"],
                        label=section["label"],
                        type=section["type"],
                        content=section["content"]
                    )
                    for section in mock_content["custom_sections"]
                ]

            return Protocol(
                title=mock_content["title"],
                date=today.strftime("%Y-%m-%d"),
                attendees=attendees,
                executiveSummary=mock_content["tldr"],
                actionItems=action_items,
                fullTranscript=self._generate_transcript_for_template(attendees, template_id),
                decisions=mock_content.get("decisions", []),
                nextSteps=mock_content.get("next_steps", []),
                templateId=template_id,
                customSections=custom_sections,
            )

        # Default protocol generation
        return Protocol(
            title="Projektbesprechung Q1 2026",
            date=today.strftime("%Y-%m-%d"),
            attendees=attendees,
            executiveSummary=self._generate_summary(),
            actionItems=self._generate_action_items(attendees),
            fullTranscript=self._generate_transcript(attendees),
            decisions=[
                "ERP-Integration hat höchste Priorität",
                "Release-Termin bleibt wie geplant",
                "Wöchentliche Status-Updates per E-Mail"
            ],
            nextSteps=[
                "Nächstes Meeting: Freitag, 14:00 Uhr",
                "Kundentermin zur API-Klärung vereinbaren",
                "Stakeholder-Präsentation vorbereiten"
            ],
            templateId=template_id,
        )

    def _generate_transcript_for_template(
        self,
        attendees: List[str],
        template_id: str
    ) -> str:
        """Generate template-specific transcript content."""
        template_transcripts = {
            "CLIENT_UPDATE": [
                "Guten Morgen! Vielen Dank, dass Sie sich Zeit für unser Quartals-Update nehmen.",
                "Sehr gerne. Wir sind gespannt auf den aktuellen Stand des Projekts.",
                "Die ERP-Integration ist zu etwa 80% abgeschlossen. Wir liegen gut im Zeitplan.",
                "Das klingt sehr gut. Wie sieht es mit Phase 2 aus?",
                "Phase 2 beginnt planmäßig am 1. März. Die Pilotphase ist bereits vorbereitet.",
                "Perfekt. Wir sollten die wöchentlichen Updates auf E-Mail umstellen.",
            ],
            "CLIENT_TECHNICAL": [
                "Heute geht es um die technischen Details der SAP-Integration.",
                "Genau. Wir haben uns für OAuth 2.0 als Authentifizierungsmethode entschieden.",
                "Das Datenformat-Mapping für die Stammdaten ist definiert.",
                "Was ist mit der Legacy-System-Migration?",
                "Das ist noch offen. Wir brauchen ein Datenmigrations-Konzept.",
                "Die Testumgebung wird in den nächsten zwei Wochen eingerichtet.",
            ],
            "PROSPECT_SALES": [
                "Willkommen bei unserer Produktdemo! Erzählen Sie uns von Ihren Herausforderungen.",
                "Wir haben eine Pensionierungswelle. Viel Expertenwissen geht verloren.",
                "Genau dafür ist Norizon konzipiert. Lassen Sie mich zeigen...",
                "Das sieht interessant aus. Wie schnell können wir das einführen?",
                "Ein Pilot-Workshop wäre der beste erste Schritt. Etwa Februar?",
                "Ja, das passt. Schicken Sie uns bitte ein Angebot.",
            ],
            "TEAM_SYNC": [
                "Guten Morgen zusammen. Lasst uns die Updates durchgehen.",
                "Frontend: Der Meeting-Workflow ist zu 70% fertig.",
                "Backend: Die API-Mocks sind implementiert und getestet.",
                "Es gibt einen Blocker: Wir brauchen eine Design-Entscheidung für den Export.",
                "Okay, das priorisieren wir. Bis Freitag finalisieren.",
                "Alles klar. Sonst noch etwas?",
            ],
            "TEAM_DESIGN": [
                "Heute designen wir die Chat-Export-Funktion.",
                "Welche Export-Ziele sollen wir unterstützen?",
                "PDF und Confluence als erste Priorität.",
                "Der User-Flow sollte zweistufig sein: Erst Template, dann Vorschau.",
                "Wie gehen wir mit großen Dateien um?",
                "Das ist ein Edge Case, den wir noch definieren müssen.",
            ],
        }

        statements = template_transcripts.get(template_id, template_transcripts["TEAM_SYNC"])
        timestamps = ["00:00:15", "00:01:02", "00:02:18", "00:03:45", "00:04:52", "00:06:10"]

        lines = []
        for i, (ts, stmt) in enumerate(zip(timestamps, statements)):
            speaker = attendees[i % len(attendees)]
            lines.append(f"[{ts}] {speaker}: {stmt}")

        return "\n\n".join(lines)

    def _generate_summary(self) -> str:
        """Generate executive summary."""
        return """Die Projektbesprechung fokussierte sich auf den aktuellen Fortschritt des Q1-Releases und die Priorisierung der ausstehenden Features. Das Team hat sich auf einen realistischen Zeitplan geeinigt und klare Verantwortlichkeiten definiert.

Hauptthemen waren die Integration der neuen Schnittstelle zum ERP-System sowie die Optimierung der Benutzeroberfläche basierend auf dem Kundenfeedback der letzten Wochen."""

    def _generate_action_items(self, attendees: List[str]) -> List[ActionItem]:
        """Generate mock action items."""
        today = datetime.now()
        items = [
            ("API-Dokumentation aktualisieren", 14),
            ("Performance-Tests durchführen", 9),
            ("Stakeholder-Meeting vorbereiten", 7),
            ("Kundenfeedback analysieren", 5),
        ]

        action_items = []
        for i, (text, days_offset) in enumerate(items[:min(len(items), len(attendees))]):
            due_date = (today + timedelta(days=days_offset)).strftime("%Y-%m-%d")
            action_items.append(ActionItem(
                id=f"action-{i + 1}",
                text=text,
                assignee=attendees[i % len(attendees)],
                dueDate=due_date,
                completed=False,
            ))

        return action_items

    def _generate_transcript(self, attendees: List[str]) -> str:
        """Generate mock transcript."""
        lines = []
        timestamps = ["00:00:15", "00:00:32", "00:01:15", "00:02:03", "00:02:18", "00:03:45", "00:04:22"]
        statements = [
            "Guten Morgen zusammen. Vielen Dank, dass ihr alle dabei seid. Heute möchten wir den aktuellen Stand des Q1-Releases besprechen.",
            "Ja, ich habe die neuesten Zahlen mitgebracht. Wir liegen gut im Zeitplan, aber es gibt noch einige offene Punkte bei der ERP-Integration.",
            "Die API-Schnittstelle ist zu 80% fertig. Wir brauchen noch Klärung zu den Authentifizierungsanforderungen vom Kunden.",
            "Das sollten wir priorisieren. Kannst du das mit dem Kunden klären?",
            "Natürlich, ich setze mich heute noch mit ihnen zusammen.",
            "Bezüglich der Performance-Tests - wir haben erste Ergebnisse, die vielversprechend aussehen. Die Ladezeiten sind um 40% gesunken.",
            "Sehr gut. Dann sollten wir das auch in der nächsten Stakeholder-Präsentation hervorheben.",
        ]

        for i, (ts, stmt) in enumerate(zip(timestamps, statements)):
            speaker = attendees[i % len(attendees)]
            lines.append(f"[{ts}] {speaker}: {stmt}")

        return "\n\n".join(lines)

