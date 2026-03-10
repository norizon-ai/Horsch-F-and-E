# Fine-Tuning Guide

This document explains how to use the QA testing framework to systematically improve prompts and retrieval configuration.

---

## Step-by-Step Fine-Tuning Workflow

### Step 1: Establish Baseline Metrics

Run the full evaluation suite to get current performance numbers.

```bash
# Start the system
docker-compose up -d

# Run baseline evaluation
python -m pytest tests/evaluation/ -v --tb=short
```

Or use the evaluation module directly:

```python
from tests.evaluation import GoldenDataset, RetrievalEvaluator

dataset = GoldenDataset()
print(f"Loaded {len(dataset)} questions")
print(f"Categories: {dataset.categories()}")

evaluator = RetrievalEvaluator()
# ... run searches and evaluate
```

**Baseline metrics to capture:**
- Retrieval: P@10, R@10, MRR, NDCG@10
- Answer quality: Faithfulness, Relevance, Completeness (from LLM-judge)
- Confidence calibration: ECE score
- Latency: p50, p95 response times

---

### Step 2: Find Optimal Retrieval Configuration

Compare BM25 vs Vector vs Hybrid search to find best weights.

```python
from tests.evaluation import SearchMethodComparison, ParameterSweep, GoldenDataset

dataset = GoldenDataset()
questions = dataset.get_by_category("troubleshooting")

# Compare predefined configurations
comparison = SearchMethodComparison()
report = await comparison.compare_all_standard_configs(questions)
print(comparison.format_comparison_report(report))

# Fine-grained weight sweep
sweep = ParameterSweep()
optimal_vector, optimal_bm25, score = await sweep.find_optimal_weights(
    questions,
    optimize_for="mrr",
    steps=10
)
print(f"Optimal: {optimal_vector*100}% vector, {optimal_bm25*100}% BM25 (MRR={score:.3f})")
```

**Apply optimal weights to `agents.yaml`:**

```yaml
agents:
  confluence_docs:
    backend:
      hybrid_enabled: true
      vector_weight: 0.4    # Update based on sweep results
      bm25_weight: 0.6      # Update based on sweep results
      search_fields:
        - "title^3"
        - "content"
```

---

### Step 3: Identify Weak Question Categories

Find which question types perform poorly.

```python
from tests.evaluation import GoldenDataset, RetrievalEvaluator

dataset = GoldenDataset()
evaluator = RetrievalEvaluator()

for category in dataset.categories():
    questions = dataset.get_by_category(category)
    # ... run evaluation
    print(f"{category}: MRR={mrr:.3f}, P@10={p10:.3f}")
```

**Common findings and fixes:**

| Weak Category | Likely Issue | Config Change |
|---------------|--------------|---------------|
| Cross-domain | Single-agent search | Enable multi-agent in supervisor |
| Troubleshooting | Keyword mismatch | Increase `bm25_weight` |
| Compliance/Standards | Semantic concepts | Increase `vector_weight` |
| Project details | Specific IDs | Add `id_field` to search_fields |

---

### Step 4: Fine-Tune Prompts

Use the Answer Evaluator to identify prompt issues.

```python
from tests.evaluation import AnswerEvaluator

evaluator = AnswerEvaluator(llm_provider, language="de")

for q in dataset.sample(10):
    result = await evaluator.evaluate(q.question, system_answer, sources)

    if result.scores.factual_accuracy < 4:
        print(f"Low factual accuracy: {q.id}")
        print(f"  Hallucinations: {result.hallucinations}")
```

**Prompt files to modify based on issues:**

| Issue | Prompt File | Section to Modify |
|-------|-------------|-------------------|
| Hallucinations | `prompts/retriever.yaml` | `generate_answer` - stricter grounding |
| Incomplete answers | `prompts/supervisor.yaml` | `generate_report` - completeness checks |
| Wrong sources | `prompts/elasticsearch_agent.yaml` | `search_strategy` - query planning |
| Low confidence calibration | `prompts/retriever.yaml` | `estimate_confidence` |

**Example prompt modification:**

```yaml
# BEFORE (too permissive)
generate_answer: |
  Generate an answer based on the sources.

# AFTER (stricter grounding)
generate_answer: |
  Generate an answer ONLY using information from the provided sources.

  STRICT RULES:
  - Every claim MUST have a citation [1], [2], etc.
  - If sources don't contain the answer, say "Die Quellen enthalten keine Information zu..."
  - Do NOT add information from general knowledge
```

---

### Step 5: Run Hallucination Detection

Check if answers contain fabricated information.

```python
from tests.evaluation import HallucinationDetector

detector = HallucinationDetector(llm_provider)

known_entities = {"RC-3000", "RC-5000", "DMS-100", "AutoTech AG", ...}

report = await detector.full_analysis(
    answer=system_answer,
    sources=retrieved_sources,
    known_entities=known_entities,
)

print(f"Hallucination rate: {report.hallucination_rate*100:.1f}%")
```

**If hallucination rate > 10%, modify:**
- `prompts/retriever.yaml` - stricter source grounding
- `prompts/supervisor.yaml` - add verification step
- `quality_threshold` in `config.py` - increase for more iterations

---

### Step 6: Validate Confidence Calibration

Check if confidence scores correlate with actual correctness.

```python
from tests.evaluation import ConfidenceCalibrator

calibrator = ConfidenceCalibrator(n_bins=10)
report = calibrator.analyze(data_points)
print(calibrator.format_report(report))
```

**Calibration fixes:**

| Issue | ECE | Fix |
|-------|-----|-----|
| Overconfident | > 0.15 | Lower base confidence in `estimate_confidence` prompt |
| Underconfident | > 0.15 | Raise confidence for multi-source answers |
| Well-calibrated | < 0.10 | No changes needed |

---

### Step 7: A/B Test Prompt Changes

Test prompt modifications before deploying.

```python
results_a = await run_evaluation(config_a, dataset.sample(20))
results_b = await run_evaluation(config_b, dataset.sample(20))

print(f"Config A - MRR: {results_a['mrr']:.3f}, Faithfulness: {results_a['faithfulness']:.2f}")
print(f"Config B - MRR: {results_b['mrr']:.3f}, Faithfulness: {results_b['faithfulness']:.2f}")
```

---

### Step 8: Iterate and Track Progress

Keep a changelog of changes and their impact.

```markdown
## Optimization Log

### 2025-01-21: Baseline
- MRR: 0.65, P@10: 0.45, Faithfulness: 3.8/5
- ECE: 0.18 (overconfident)

### 2025-01-22: Increased vector_weight to 0.6
- MRR: 0.72 (+0.07), P@10: 0.52 (+0.07)
- Better semantic matching for compliance questions

### 2025-01-23: Stricter grounding in retriever.yaml
- Faithfulness: 4.2/5 (+0.4)
- Hallucination rate: 8% -> 3%
```

---

## Configuration Files Reference

| File | Purpose | Key Settings |
|------|---------|--------------|
| `agents.yaml` | Agent & retrieval config | `vector_weight`, `bm25_weight`, `search_fields` |
| `prompts/supervisor.yaml` | Orchestration prompts | Report generation, quality assessment |
| `prompts/elasticsearch_agent.yaml` | Search strategy | Query planning, result synthesis |
| `prompts/retriever.yaml` | Answer generation | Grounding rules, confidence estimation |
| `deepsearch/config.py` | Global settings | `max_iterations`, `quality_threshold` |

### Environment Variables (override any setting)

```bash
export DR_LLM_TEMPERATURE=0.1        # Lower = more deterministic
export DR_MAX_ITERATIONS=5           # More search iterations
export DR_QUALITY_THRESHOLD=0.8      # Higher = stricter early stopping
export DR_CONFIDENCE_THRESHOLD=0.7   # Minimum confidence to report
```

---

## Related Documentation

- [Testing Guide](testing.md) - QA testing strategy
- [Architecture](../../ARCHITECTURE.md) - System design
