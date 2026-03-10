# Implementing Clarifying Questions

This document outlines three approaches for implementing a clarifying question system that asks users for more information when queries are ambiguous (e.g., "Troubleshoot robot" -> "Which robot do you want to troubleshoot?").

---

## Current Architecture (No Clarification)

```
User: "Troubleshoot robot"
         |
         v
    API Layer
    /api/v1/search
         |
         v
    Supervisor Agent  <- LLM decides which agent to use
         |               (no option to ask for clarification)
         v
    Docs Agent       <- Searches with vague query
         |
         v
    Generic Results  <- Results may not match user's intent
```

**Problem:** Ambiguous queries proceed directly to search without knowing:
- Which robot model?
- What type of issue?
- Which specific symptoms?

---

## Approach 1: Query Analyzer Preprocessor

Add a dedicated preprocessing step that analyzes query clarity before routing.

### Architecture

```
User: "Troubleshoot robot"
         |
         v
    Query Analyzer Processor  <- NEW COMPONENT
    - Ambiguity Detection
    - Entity Extraction
    - Missing Info Identification
    - Question Generation
         |
    +----+----+
    |         |
    v         v
  CLEAR    AMBIGUOUS
  (>0.8)   (<0.8)
    |         |
    v         v
Supervisor  Return Clarifying Question:
Agent       "Which robot model?"
            Options: KUKA KR 6, KR 16, FANUC M-20iA
```

### Prompt Template

```yaml
# prompts/query_analyzer.yaml

analyze_query: |
  You are a query clarity analyzer for an industrial knowledge system.

  QUERY: {query}
  CONVERSATION_HISTORY: {history}
  AVAILABLE_AGENTS: {agent_descriptions}
  KNOWN_ENTITIES: {entity_catalog}

  Analyze if this query contains enough information to provide a useful answer.

  Consider:
  1. Is a specific product/system/component mentioned?
  2. Is the problem clearly described?
  3. Are there ambiguous references ("it", "the robot", "that error")?
  4. Could this query match multiple very different topics?

  RESPOND IN JSON:
  {
    "is_clear": true/false,
    "confidence": 0.0-1.0,
    "reasoning": "Brief explanation",
    "missing_info": ["category1", "category2"],
    "clarifying_question": "Question to ask if not clear",
    "options": ["Option 1", "Option 2", "Option 3"]
  }
```

### Pros & Cons

| Pros | Cons |
|------|------|
| Clean separation of concerns | Additional LLM call (latency + cost) |
| Easy to test in isolation | New component to maintain |
| Can be toggled on/off per deployment | May over-ask if threshold too sensitive |
| Detailed ambiguity analysis | Requires entity catalog for best results |

---

## Approach 2: Supervisor Enhancement

Extend the existing supervisor to include clarification as a routing option.

### Implementation

```python
# /deepsearch/supervisor/agent.py

CLARIFICATION_FUNCTION = {
    "name": "request_clarification",
    "description": """
        Ask the user for more information when the query is too vague
        to provide a useful answer. Use this when:
        - No specific product/system/component is mentioned
        - The problem description is unclear
        - The query could match multiple very different topics
    """,
    "parameters": {
        "type": "object",
        "properties": {
            "question": {
                "type": "string",
                "description": "The clarifying question to ask the user"
            },
            "options": {
                "type": "array",
                "items": {"type": "string"},
                "description": "Optional list of choices (2-4 options)"
            }
        },
        "required": ["question"]
    }
}
```

### Pros & Cons

| Pros | Cons |
|------|------|
| Minimal code changes | Mixes routing and clarification logic |
| No additional LLM call | Harder to tune clarification behavior |
| Leverages existing decision-making | LLM may inconsistently decide to clarify |
| Natural conversation flow | Less detailed ambiguity analysis |

---

## Approach 3: Entity-Aware Disambiguation

Combine pattern matching with domain knowledge for smart clarification.

### Entity Catalog Structure

```python
# /deepsearch/knowledge/entity_catalog.py

class EntityCatalog:
    """Domain-specific entity knowledge base."""

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
        """Detect which entity type the query is asking about."""
        # Pattern matching logic
```

### Pros & Cons

| Pros | Cons |
|------|------|
| Fast (no LLM call for detection) | Requires maintaining entity catalog |
| Deterministic behavior | Pattern-based = may miss edge cases |
| Customer-aware options | More complex implementation |
| Can work offline | Needs updates as products change |

---

## Recommendation

### Start with Approach 2, evolve to Approach 3

**Phase 1: Supervisor Enhancement**
- Add `request_clarification` function to supervisor
- Update supervisor prompt with clarification guidelines
- Minimal code changes, quick to implement

**Phase 2: Add Entity Catalog**
- Build entity catalog from customer configurations
- Use catalog to provide smart options
- Supervisor still decides when to clarify

**Phase 3: Full Entity-Aware System**
- Pattern-based pre-filtering
- Deterministic disambiguation for known patterns
- LLM fallback for novel queries

---

## API Changes Required

```python
# /deepsearch/api/models.py

class ClarificationOption(BaseModel):
    label: str           # Display text: "KUKA KR 16"
    value: str           # Internal ID: "kuka_kr16"
    description: str = None

class ClarificationRequest(BaseModel):
    question: str
    options: List[ClarificationOption]
    entity_type: str = None
    allow_freetext: bool = True

class SearchResponse(BaseModel):
    status: Literal["complete", "in_progress", "needs_clarification", "error"]
    needs_clarification: bool = False
    clarification: ClarificationRequest = None
    # ... existing fields
```

---

## Related Documentation

- [Architecture](../../ARCHITECTURE.md) - System design overview
- [API Reference](../API_REFERENCE.md) - Endpoint documentation
