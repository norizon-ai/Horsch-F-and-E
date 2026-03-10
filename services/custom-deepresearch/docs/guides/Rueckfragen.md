

## Ansatz 1: Preprocessor

Ein dedizierter Vorverarbeitungsschritt

```
Benutzer: "Roboter Fehlersuche"
         |
         v
    Anfrage-Analysator        <- NEUE KOMPONENTE
    - Mehrdeutigkeitserkennung
    - Entitätsextraktion
    - Fehlende Info identifizieren
    - Fragengenerierung
         |
    +----+----+
    |         |
    v         v
  KLAR    MEHRDEUTIG
  (bspw. >0.8)   (<0.8)
    |         |
    v         v
Supervisor  Rückfrage zurückgeben:
Agent       "Welches Robotermodell?"
            Optionen: KUKA KR 6, KR 16, FANUC M-20iA
```

### Prompt-Vorlage

```yaml
# prompts/query_analyzer.yaml

analyze_query: |
  Du bist ein Anfrage-Klarheitsanalysator für ein industrielles Wissenssystem.

  ANFRAGE: {query}
  GESPRÄCHSVERLAUF: {history}
  VERFÜGBARE_AGENTEN: {agent_descriptions}
  BEKANNTE_ENTITÄTEN: {entity_catalog}

  Analysiere, ob diese Anfrage genügend Informationen enthält, um eine nützliche Antwort zu geben.

  Berücksichtige:
  1. Wird ein spezifisches Produkt/System/Komponente genannt?
  2. Ist das Problem klar beschrieben?
  3. Gibt es mehrdeutige Verweise ("es", "der Roboter", "dieser Fehler")?
  4. Könnte diese Anfrage mehrere sehr unterschiedliche Themen betreffen?

  ANTWORTE IM JSON-FORMAT:
  {
    "is_clear": true/false,
    "confidence": 0.0-1.0,
    "reasoning": "Kurze Erklärung",
    "missing_info": ["Kategorie1", "Kategorie2"],
    "clarifying_question": "Frage, falls nicht klar",
    "options": ["Option 1", "Option 2", "Option 3"]
  }
```


## Ansatz 2: Supervisor

Erweiterung des bestehenden Supervisors um Rückfragen als Routing-Option.

### Implementierung

```python
# /deepsearch/supervisor/agent.py

CLARIFICATION_FUNCTION = {
    "name": "request_clarification",
    "description": """
        Den Benutzer um weitere Informationen bitten, wenn die Anfrage zu vage ist,
        um eine nützliche Antwort zu geben. Verwende dies wenn:
        - Kein spezifisches Produkt/System/Komponente genannt wird
        - Die Problembeschreibung unklar ist
        - Die Anfrage mehrere sehr unterschiedliche Themen betreffen könnte
    """,
    "parameters": {
        "type": "object",
        "properties": {
            "question": {
                "type": "string",
                "description": "Die Rückfrage an den Benutzer"
            },
            "options": {
                "type": "array",
                "items": {"type": "string"},
                "description": "Optionale Liste von Auswahlmöglichkeiten (2-4 Optionen)"
            }
        },
        "required": ["question"]
    }
}
```

## Zusätzlich Entitätsbewusste Disambiguierung


```python
# /deepsearch/knowledge/entity_catalog.py -> Z.B. dann direkt aus SAP data lake, cached daily

class EntityCatalog:
    """Domänenspezifische Entitäts-Wissensbasis."""

    ROBOTS = {
        "kuka": [
            Entity(id="kuka_kr6", name="KUKA KR 6", aliases=["kr6", "kr-6"]),
            Entity(id="kuka_kr16", name="KUKA KR 16", aliases=["kr16", "kr-16"]),
        ],
        "fanuc": [
            Entity(id="fanuc_m20", name="FANUC M-20iA", aliases=["m20", "m-20"]),
        ],
    }

    @classmethod
    def detect_entity_type(cls, query: str) -> Optional[str]:
        """Erkennt, nach welchem Entitätstyp die Anfrage fragt."""
        # Mustererkennungslogik
```

