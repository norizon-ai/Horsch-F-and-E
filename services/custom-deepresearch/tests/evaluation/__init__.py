"""
Evaluation module for Nora Search (DeepSearch) QA testing.

This module provides comprehensive tools for evaluating RAG system quality:

- **Golden Dataset**: Benchmark questions based on TechMech Solutions Confluence
- **Answer Quality**: LLM-as-judge evaluation (factual accuracy, completeness, etc.)
- **Retrieval Metrics**: P@K, R@K, MRR, NDCG for search quality
- **Search Comparison**: BM25 vs Vector vs Hybrid comparison framework
- **Hallucination Detection**: Detect claims not grounded in sources
- **Citation Verification**: Verify inline citations are accurate
- **Confidence Calibration**: Test if confidence scores are reliable

Usage:
    from tests.evaluation import (
        GoldenDataset,
        RetrievalEvaluator,
        AnswerEvaluator,
        SearchMethodComparison,
        HallucinationDetector,
        CitationVerifier,
        ConfidenceCalibrator,
    )

    # Load golden dataset
    dataset = GoldenDataset()
    questions = dataset.get_by_category("troubleshooting")

    # Evaluate retrieval
    evaluator = RetrievalEvaluator()
    metrics = evaluator.evaluate_batch(results)
"""

from .golden_dataset import GoldenDataset, GoldenQuestion, load_golden_dataset
from .retrieval_metrics import (
    RetrievalEvaluator,
    RetrievalResult,
    MetricsReport,
    create_retrieval_result,
)
from .answer_evaluator import (
    AnswerEvaluator,
    EvaluationResult,
    EvaluationScores,
)
from .search_comparison import (
    SearchMethodComparison,
    SearchConfiguration,
    ComparisonReport,
    ParameterSweep,
    SEARCH_CONFIGURATIONS,
)
from .hallucination_detector import (
    HallucinationDetector,
    HallucinationReport,
    HallucinatedClaim,
)
from .citation_verifier import (
    CitationVerifier,
    CitationReport,
    Citation,
)
from .confidence_calibration import (
    ConfidenceCalibrator,
    CalibrationReport,
    CalibrationDataPoint,
    compute_brier_score,
    compute_log_loss,
)
from .rigorous_evaluator import (
    RigorousEvaluator,
    RigorousEvaluationReport,
    DimensionResult,
    Verdict,
)

__all__ = [
    # Golden Dataset
    "GoldenDataset",
    "GoldenQuestion",
    "load_golden_dataset",
    # Retrieval Metrics
    "RetrievalEvaluator",
    "RetrievalResult",
    "MetricsReport",
    "create_retrieval_result",
    # Answer Evaluation
    "AnswerEvaluator",
    "EvaluationResult",
    "EvaluationScores",
    # Search Comparison
    "SearchMethodComparison",
    "SearchConfiguration",
    "ComparisonReport",
    "ParameterSweep",
    "SEARCH_CONFIGURATIONS",
    # Hallucination Detection
    "HallucinationDetector",
    "HallucinationReport",
    "HallucinatedClaim",
    # Citation Verification
    "CitationVerifier",
    "CitationReport",
    "Citation",
    # Confidence Calibration
    "ConfidenceCalibrator",
    "CalibrationReport",
    "CalibrationDataPoint",
    "compute_brier_score",
    "compute_log_loss",
    # Rigorous Evaluation
    "RigorousEvaluator",
    "RigorousEvaluationReport",
    "DimensionResult",
    "Verdict",
]
