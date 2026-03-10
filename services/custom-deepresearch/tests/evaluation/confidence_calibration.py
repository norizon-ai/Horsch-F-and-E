"""
Confidence Calibration for Nora Search (DeepSearch) QA Evaluation.

Measures how well the system's confidence scores correlate with actual answer quality.
A well-calibrated system should have:
- 70% confident answers correct ~70% of the time
- 90% confident answers correct ~90% of the time

Poorly calibrated systems are either:
- Overconfident: High confidence for incorrect answers
- Underconfident: Low confidence for correct answers
"""

import math
from dataclasses import dataclass, field
from typing import Optional

import numpy as np


@dataclass
class CalibrationDataPoint:
    """A single data point for calibration analysis."""

    question_id: str
    confidence_score: float  # System's confidence (0-1)
    is_correct: bool  # Ground truth: was the answer correct?
    quality_score: Optional[float] = None  # Optional: quality score from evaluation


@dataclass
class CalibrationBin:
    """Statistics for a confidence bin."""

    bin_start: float
    bin_end: float
    count: int
    avg_confidence: float
    accuracy: float  # Proportion of correct answers in this bin
    expected_accuracy: float  # What accuracy should be based on confidence

    @property
    def calibration_error(self) -> float:
        """Difference between actual and expected accuracy."""
        return abs(self.accuracy - self.expected_accuracy)


@dataclass
class CalibrationReport:
    """Full calibration analysis report."""

    total_samples: int
    bins: list[CalibrationBin]
    ece: float  # Expected Calibration Error
    mce: float  # Maximum Calibration Error
    reliability_diagram: list[tuple[float, float, float]]  # (confidence, accuracy, count)
    overconfidence_rate: float  # Proportion of overconfident predictions
    underconfidence_rate: float  # Proportion of underconfident predictions
    optimal_threshold: float  # Confidence threshold maximizing F1

    @property
    def is_well_calibrated(self) -> bool:
        """Check if system is reasonably well-calibrated (ECE < 0.1)."""
        return self.ece < 0.1

    @property
    def calibration_quality(self) -> str:
        """Qualitative assessment of calibration."""
        if self.ece < 0.05:
            return "excellent"
        elif self.ece < 0.10:
            return "good"
        elif self.ece < 0.15:
            return "acceptable"
        elif self.ece < 0.25:
            return "poor"
        else:
            return "very_poor"


class ConfidenceCalibrator:
    """Analyze and test confidence score calibration."""

    def __init__(self, n_bins: int = 10) -> None:
        """
        Initialize the calibrator.

        Args:
            n_bins: Number of bins for calibration analysis (default 10).
        """
        self.n_bins = n_bins

    def compute_calibration_bins(
        self, data_points: list[CalibrationDataPoint]
    ) -> list[CalibrationBin]:
        """
        Compute calibration statistics for each confidence bin.

        Args:
            data_points: List of calibration data points.

        Returns:
            List of CalibrationBin objects.
        """
        bins = []
        bin_size = 1.0 / self.n_bins

        for i in range(self.n_bins):
            bin_start = i * bin_size
            bin_end = (i + 1) * bin_size

            # Get points in this bin
            points_in_bin = [
                p for p in data_points
                if bin_start <= p.confidence_score < bin_end
                or (i == self.n_bins - 1 and p.confidence_score == 1.0)
            ]

            if len(points_in_bin) == 0:
                bins.append(
                    CalibrationBin(
                        bin_start=bin_start,
                        bin_end=bin_end,
                        count=0,
                        avg_confidence=bin_start + bin_size / 2,
                        accuracy=0.0,
                        expected_accuracy=bin_start + bin_size / 2,
                    )
                )
            else:
                avg_conf = sum(p.confidence_score for p in points_in_bin) / len(points_in_bin)
                accuracy = sum(1 for p in points_in_bin if p.is_correct) / len(points_in_bin)

                bins.append(
                    CalibrationBin(
                        bin_start=bin_start,
                        bin_end=bin_end,
                        count=len(points_in_bin),
                        avg_confidence=avg_conf,
                        accuracy=accuracy,
                        expected_accuracy=avg_conf,  # Expected = confidence
                    )
                )

        return bins

    def compute_ece(
        self, bins: list[CalibrationBin], total_samples: int
    ) -> float:
        """
        Compute Expected Calibration Error.

        ECE = sum(|accuracy - confidence| * n_bin / n_total) for all bins

        Args:
            bins: List of calibration bins.
            total_samples: Total number of samples.

        Returns:
            ECE score (lower is better, 0 is perfect).
        """
        if total_samples == 0:
            return 0.0

        ece = 0.0
        for bin_ in bins:
            if bin_.count > 0:
                weight = bin_.count / total_samples
                ece += weight * bin_.calibration_error
        return ece

    def compute_mce(self, bins: list[CalibrationBin]) -> float:
        """
        Compute Maximum Calibration Error.

        MCE = max(|accuracy - confidence|) across all bins

        Args:
            bins: List of calibration bins.

        Returns:
            MCE score (lower is better).
        """
        if not bins:
            return 0.0

        max_error = 0.0
        for bin_ in bins:
            if bin_.count > 0:
                max_error = max(max_error, bin_.calibration_error)
        return max_error

    def compute_confidence_distribution(
        self, data_points: list[CalibrationDataPoint]
    ) -> tuple[float, float]:
        """
        Compute over/underconfidence rates.

        Args:
            data_points: List of calibration data points.

        Returns:
            Tuple of (overconfidence_rate, underconfidence_rate).
        """
        if not data_points:
            return 0.0, 0.0

        overconfident = 0
        underconfident = 0

        for p in data_points:
            if p.confidence_score > 0.5:
                # High confidence - should be correct
                if not p.is_correct:
                    overconfident += 1
            else:
                # Low confidence - might be wrong
                if p.is_correct:
                    underconfident += 1

        return overconfident / len(data_points), underconfident / len(data_points)

    def find_optimal_threshold(
        self, data_points: list[CalibrationDataPoint]
    ) -> float:
        """
        Find confidence threshold that maximizes F1 score.

        Args:
            data_points: List of calibration data points.

        Returns:
            Optimal confidence threshold.
        """
        if not data_points:
            return 0.5

        best_f1 = 0.0
        best_threshold = 0.5

        for threshold in [i / 20 for i in range(1, 20)]:
            # Predictions: confidence >= threshold means "accept as correct"
            tp = sum(1 for p in data_points if p.confidence_score >= threshold and p.is_correct)
            fp = sum(1 for p in data_points if p.confidence_score >= threshold and not p.is_correct)
            fn = sum(1 for p in data_points if p.confidence_score < threshold and p.is_correct)

            precision = tp / (tp + fp) if (tp + fp) > 0 else 0
            recall = tp / (tp + fn) if (tp + fn) > 0 else 0
            f1 = 2 * precision * recall / (precision + recall) if (precision + recall) > 0 else 0

            if f1 > best_f1:
                best_f1 = f1
                best_threshold = threshold

        return best_threshold

    def analyze(
        self, data_points: list[CalibrationDataPoint]
    ) -> CalibrationReport:
        """
        Perform full calibration analysis.

        Args:
            data_points: List of calibration data points.

        Returns:
            CalibrationReport with full analysis.
        """
        if not data_points:
            return CalibrationReport(
                total_samples=0,
                bins=[],
                ece=0.0,
                mce=0.0,
                reliability_diagram=[],
                overconfidence_rate=0.0,
                underconfidence_rate=0.0,
                optimal_threshold=0.5,
            )

        # Compute bins
        bins = self.compute_calibration_bins(data_points)

        # Compute metrics
        ece = self.compute_ece(bins, len(data_points))
        mce = self.compute_mce(bins)
        overconf, underconf = self.compute_confidence_distribution(data_points)
        optimal_threshold = self.find_optimal_threshold(data_points)

        # Build reliability diagram data
        reliability = [
            (b.avg_confidence, b.accuracy, b.count)
            for b in bins
            if b.count > 0
        ]

        return CalibrationReport(
            total_samples=len(data_points),
            bins=bins,
            ece=ece,
            mce=mce,
            reliability_diagram=reliability,
            overconfidence_rate=overconf,
            underconfidence_rate=underconf,
            optimal_threshold=optimal_threshold,
        )

    def format_report(self, report: CalibrationReport) -> str:
        """
        Format calibration report as readable text.

        Args:
            report: CalibrationReport to format.

        Returns:
            Formatted string report.
        """
        lines = ["=" * 60]
        lines.append("CONFIDENCE CALIBRATION REPORT")
        lines.append("=" * 60)
        lines.append("")

        lines.append(f"Total samples: {report.total_samples}")
        lines.append(f"Calibration quality: {report.calibration_quality.upper()}")
        lines.append("")

        lines.append("Calibration Metrics:")
        lines.append(f"  ECE (Expected Calibration Error): {report.ece:.4f}")
        lines.append(f"  MCE (Maximum Calibration Error): {report.mce:.4f}")
        lines.append(f"  Overconfidence rate: {report.overconfidence_rate*100:.1f}%")
        lines.append(f"  Underconfidence rate: {report.underconfidence_rate*100:.1f}%")
        lines.append(f"  Optimal threshold: {report.optimal_threshold:.2f}")
        lines.append("")

        lines.append("Reliability Diagram (Confidence -> Accuracy):")
        lines.append("-" * 50)
        lines.append(f"{'Confidence':>12} {'Accuracy':>12} {'Count':>8} {'Gap':>8}")
        lines.append("-" * 50)

        for conf, acc, count in report.reliability_diagram:
            gap = acc - conf
            gap_str = f"+{gap:.2f}" if gap >= 0 else f"{gap:.2f}"
            lines.append(f"{conf:>12.2f} {acc:>12.2f} {count:>8} {gap_str:>8}")

        lines.append("-" * 50)
        lines.append("")

        # Interpretation
        if report.is_well_calibrated:
            lines.append("ASSESSMENT: System is well-calibrated.")
        else:
            if report.overconfidence_rate > report.underconfidence_rate:
                lines.append("ASSESSMENT: System is OVERCONFIDENT.")
                lines.append("  High confidence scores don't reliably indicate correctness.")
            else:
                lines.append("ASSESSMENT: System is UNDERCONFIDENT.")
                lines.append("  System often gives low confidence for correct answers.")

        lines.append("")
        lines.append("=" * 60)

        return "\n".join(lines)

    def create_data_point(
        self,
        question_id: str,
        confidence: float,
        is_correct: bool,
        quality_score: Optional[float] = None,
    ) -> CalibrationDataPoint:
        """
        Create a calibration data point.

        Args:
            question_id: Identifier for the question.
            confidence: System's confidence score (0-1).
            is_correct: Whether the answer was correct.
            quality_score: Optional quality score from evaluation.

        Returns:
            CalibrationDataPoint instance.
        """
        return CalibrationDataPoint(
            question_id=question_id,
            confidence_score=confidence,
            is_correct=is_correct,
            quality_score=quality_score,
        )


def compute_brier_score(data_points: list[CalibrationDataPoint]) -> float:
    """
    Compute Brier score (mean squared error of confidence).

    Lower is better. 0 = perfect, 1 = worst possible.

    Args:
        data_points: List of calibration data points.

    Returns:
        Brier score.
    """
    if not data_points:
        return 0.0

    total = 0.0
    for p in data_points:
        actual = 1.0 if p.is_correct else 0.0
        total += (p.confidence_score - actual) ** 2

    return total / len(data_points)


def compute_log_loss(data_points: list[CalibrationDataPoint]) -> float:
    """
    Compute log loss (cross-entropy).

    Lower is better.

    Args:
        data_points: List of calibration data points.

    Returns:
        Log loss score.
    """
    if not data_points:
        return 0.0

    eps = 1e-15  # Prevent log(0)
    total = 0.0

    for p in data_points:
        conf = min(max(p.confidence_score, eps), 1 - eps)
        if p.is_correct:
            total -= math.log(conf)
        else:
            total -= math.log(1 - conf)

    return total / len(data_points)
