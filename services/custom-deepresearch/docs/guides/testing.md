# QA Testing Strategy

Comprehensive testing strategy for evaluating and improving answer quality, search performance, and retrieval mechanisms.

---

## 1. Golden Answer Dataset

### Test Question Categories

| Category | Count | Complexity |
|----------|-------|------------|
| Product Specifications | 12 | 1-2 sources |
| Troubleshooting | 12 | Procedural |
| Compliance/Standards | 10 | Multi-document |
| Project Details | 10 | Cross-reference |
| Quality Processes | 10 | Process flow |
| Cross-Domain | 8 | 3+ sources |
| HR/Admin | 8 | Single source |

### Golden Questions Format

```yaml
# File: tests/evaluation/golden_answers.yaml

questions:
  - id: "PS-001"
    question: "Was sind die technischen Spezifikationen der RC-3000 Serie?"
    expected_source_pages: ["RC-3000 Technische Spezifikationen v4.2"]
    space: "ENG"
    category: "product_spec"
    difficulty: "simple"

  - id: "TS-001"
    question: "Was sind die haufigsten Ursachen fur Vibrationen bei Roboterzellen?"
    expected_source_pages: ["Vibrationen Roboterzelle - Troubleshooting Guide"]
    space: "SRV"
    category: "troubleshooting"
```

### Implementation

```python
class GoldenDataset:
    """Load and manage golden answer benchmark data."""

    def __init__(self, yaml_path: str = "tests/evaluation/golden_answers.yaml"):
        self.questions = self._load_questions(yaml_path)

    def get_by_category(self, category: str) -> List[GoldenQuestion]:
        return [q for q in self.questions if q.category == category]

    def get_by_space(self, space: str) -> List[GoldenQuestion]:
        return [q for q in self.questions if q.space == space]
```

---

## 2. Answer Quality Evaluation

### Metrics Framework

| Metric | Description | Target |
|--------|-------------|--------|
| **Faithfulness** | Answer only contains info from sources | > 0.9 |
| **Relevance** | Answer addresses the question | > 0.85 |
| **Completeness** | All aspects of question covered | > 0.8 |
| **Source Attribution** | Claims properly cited | > 0.9 |
| **German Quality** | Grammar, terminology correctness | > 0.95 |

### LLM-as-Judge Evaluator

```python
class AnswerEvaluator:
    """Evaluate answer quality using LLM-as-judge."""

    EVALUATION_PROMPT = """
    Bewerte die folgende RAG-Systemantwort:

    Frage: {question}
    Systemantwort: {answer}
    Verwendete Quellen: {sources}

    Bewerte auf einer Skala von 1-5:
    1. FAKTISCHE_KORREKTHEIT
    2. VOLLSTANDIGKEIT
    3. RELEVANZ
    4. QUELLENVERANKERUNG
    5. KLARHEIT

    Ruckgabe als JSON: {"scores": {...}, "reasoning": "...", "hallucinations": [...]}
    """

    async def evaluate(self, question: str, answer: str, sources: List[str]) -> EvaluationResult:
        """Run LLM evaluation on answer."""
```

### Hallucination Detection

```python
class HallucinationDetector:
    """Detect claims not grounded in sources."""

    async def detect_unsupported_claims(
        self, answer: str, sources: List[SearchResult]
    ) -> List[HallucinatedClaim]:
        """Extract claims from answer and verify against sources."""

    async def detect_entity_hallucinations(
        self, answer: str, known_entities: Set[str]
    ) -> List[str]:
        """Find fabricated names, numbers, dates not in knowledge base."""
```

---

## 3. Retrieval Performance Testing

### Retrieval Metrics

```python
class RetrievalEvaluator:
    """Evaluate search retrieval quality."""

    def precision_at_k(self, retrieved: List[str], relevant: Set[str], k: int) -> float:
        """Proportion of top-k results that are relevant."""

    def recall_at_k(self, retrieved: List[str], relevant: Set[str], k: int) -> float:
        """Proportion of relevant docs found in top-k."""

    def mrr(self, retrieved: List[str], relevant: Set[str]) -> float:
        """Mean Reciprocal Rank - position of first relevant result."""

    def ndcg_at_k(self, retrieved: List[str], relevance_scores: Dict[str, int], k: int) -> float:
        """Normalized Discounted Cumulative Gain with graded relevance."""
```

### Search Method Comparison

| Configuration | BM25 Weight | Vector Weight | Use Case |
|---------------|-------------|---------------|----------|
| `bm25_only` | 1.0 | 0.0 | Exact keyword matches |
| `vector_only` | 0.0 | 1.0 | Semantic similarity |
| `hybrid_balanced` | 0.5 | 0.5 | General purpose |
| `hybrid_semantic` | 0.3 | 0.7 | Conceptual queries |

### Parameter Optimization

| Parameter | Values to Test | Impact Area |
|-----------|----------------|-------------|
| `top_k` | 5, 10, 15, 20 | Recall vs Precision |
| `chunk_size` | 400, 800, 1200 | Context granularity |
| `chunk_overlap` | 40, 80, 160 | Context continuity |
| `title_boost` | 1, 2, 3, 5 | Title importance |

---

## 4. End-to-End Testing

### Scenario-Based Tests

```python
class TestRealisticScenarios:
    """E2E tests based on realistic usage patterns."""

    SCENARIOS = [
        {
            "name": "robot_vibration_issue",
            "query": "Unsere Roboterzelle vibriert stark. Was kann die Ursache sein?",
            "expected_spaces": ["SRV"],
            "expected_pages": ["Vibrationen Roboterzelle - Troubleshooting Guide"],
            "min_confidence": 0.7,
        },
        {
            "name": "cross_domain_compliance",
            "query": "Welche Compliance-Anforderungen gelten fur Lebensmittelanlagen?",
            "expected_spaces": ["PRJ", "CMP"],
            "requires_cross_domain": True,
            "min_sources": 3,
        },
    ]
```

### Latency Benchmarks

| Stage | Target (ms) | Critical Path |
|-------|-------------|---------------|
| Query preprocessing | < 50 | QueryReformulator |
| Elasticsearch search | < 200 | ElasticsearchBackend |
| Embedding generation | < 100 | sentence-transformers |
| LLM reasoning (per iteration) | < 2000 | Agent reasoning loop |
| Report generation | < 3000 | Supervisor synthesis |
| **Total (simple query)** | < 5000 | End-to-end |
| **Total (complex query)** | < 15000 | Multi-iteration |

### Edge Cases

| Case | Query | Expected Behavior |
|------|-------|-------------------|
| No results | "Quantencomputer Programmierung" | Graceful "no info found" |
| Ambiguous | "Problem" | Clarification or broad search |
| Very long | 5000+ chars | Validation error |
| Mixed language | "How to Jira Workflow einrichten?" | Handle gracefully |
| Out of domain | "Wetter in Munchen" | Polite decline |
| Injection | "Ignoriere vorherige Anweisungen..." | Normal search |

---

## 5. Additional Quality Dimensions

### Confidence Calibration

```python
class ConfidenceCalibrator:
    """Test confidence score reliability."""

    async def calibration_analysis(
        self,
        predictions: List[Tuple[str, float]],
        ground_truth: List[bool]
    ) -> CalibrationReport:
        """Expected: 70% confident answers correct ~70% of time"""
```

### Agent Routing Accuracy

```python
ROUTING_TESTS = [
    {"query": "RC-3000 Technische Spezifikationen", "expected": "elasticsearch_confluence"},
    {"query": "Aktuelle KI Nachrichten", "expected": "websearch"},
]
```

### Citation Verification

```python
class CitationVerifier:
    """Verify inline citations are accurate."""

    async def verify_citations(self, answer: str, sources: List[SearchResult]) -> CitationReport:
        """Check each citation maps to actual source content."""
```

---

## 6. Running Tests

### Automated Tests

```bash
# Run full evaluation suite
pytest tests/evaluation/ -v --cov=deepsearch

# Run retrieval benchmarks
pytest tests/evaluation/test_retrieval_benchmark.py -v

# Run E2E scenarios
pytest tests/e2e/test_realistic_scenarios.py -v
```

### Manual Verification

1. Sample 10 queries from each category
2. Have domain expert review answer quality
3. Compare automated scores with human ratings
4. Iterate on evaluation prompts until correlation > 0.8

### Performance Baselines

After initial implementation, establish baselines:
- Retrieval: P@10 > 0.7, MRR > 0.6
- Answers: Faithfulness > 0.9, Relevance > 0.85
- Latency: p95 < 10s for simple queries

---

## Related Documentation

- [Fine-Tuning Guide](fine-tuning.md) - Prompt and retrieval optimization
- [Architecture](../../ARCHITECTURE.md) - System design
- [API Reference](../API_REFERENCE.md) - Endpoint documentation
