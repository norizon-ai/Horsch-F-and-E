"""
Preprocessor chain for composing multiple preprocessors.

Allows sequential application of multiple preprocessors.
"""

from typing import Any, Dict, List

from .base import Preprocessor


class PreprocessorChain(Preprocessor):
    """
    Chain multiple preprocessors together.

    Applies preprocessors in order, passing the output of each
    to the next. Useful for combining stopword removal with
    stemming, keyword extraction, etc.
    """

    def __init__(self, preprocessors: List[Preprocessor]):
        """
        Initialize preprocessor chain.

        Args:
            preprocessors: List of preprocessors to apply in order
        """
        if not preprocessors:
            raise ValueError("PreprocessorChain requires at least one preprocessor")
        self._preprocessors = preprocessors

    @property
    def name(self) -> str:
        """Name combining all preprocessor names."""
        return "+".join(p.name for p in self._preprocessors)

    def get_config(self) -> Dict[str, Any]:
        return {
            "name": self.name,
            "chain": [p.get_config() for p in self._preprocessors],
        }

    def process(self, query: str) -> str:
        """Apply all preprocessors in sequence."""
        result = query
        for preprocessor in self._preprocessors:
            result = preprocessor.process(result)
        return result

    def __len__(self) -> int:
        """Number of preprocessors in chain."""
        return len(self._preprocessors)

    def __iter__(self):
        """Iterate over preprocessors."""
        return iter(self._preprocessors)

    def __getitem__(self, index: int) -> Preprocessor:
        """Get preprocessor by index."""
        return self._preprocessors[index]


def chain(*preprocessors: Preprocessor) -> PreprocessorChain:
    """
    Convenience function to create a preprocessor chain.

    Example:
        pipeline = chain(
            StopwordRemover(),
            KeywordExtractor(max_terms=8),
        )
        result = pipeline.process("what is the RC-3000 error code")
    """
    return PreprocessorChain(list(preprocessors))
