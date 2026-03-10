from typing import List, Dict, Optional, Callable, Set, Any

class EntitySanitizer:
    """
    Modular, extensible operator for post-processing recognized entities.
    Supports multiple sanitization strategies (deduplication, merging, filtering, etc.).
    Now supports applying multiple strategies in sequence and user-defined custom strategies.
    """
    def __init__(self, config: Optional[Dict] = None):
        self.config = config or {}
        # Accept either a single strategy (string) or a list of strategies
        strategies = self.config.get("strategies")
        if strategies is None:
            # Fallback to single strategy for backward compatibility
            single_strategy = self.config.get("strategy")
            if single_strategy:
                self.strategies = [single_strategy]
            else:
                self.strategies = ["deduplicate"]
        elif isinstance(strategies, str):
            self.strategies = [strategies]
        elif isinstance(strategies, list):
            self.strategies = [s for s in strategies if isinstance(s, str)]
        else:
            self.strategies = ["deduplicate"]
        self.confidence_threshold = self.config.get("confidence_threshold", 0.0)
        self.entity_priority = self.config.get("entity_priority", [])
        # Strategy registry: maps strategy names to methods
        self._strategies = {
            "deduplicate": self._deduplicate,
            "merge_overlaps": self._merge_overlaps,
            "filter_by_confidence": self._filter_by_confidence,
            "entity_priority": self._entity_priority,
        }
        # Register custom strategies if provided
        custom_strategies = self.config.get("custom_strategies", {})
        for name, func in custom_strategies.items():
            # Assume func is a callable or import path; for now, just store as placeholder
            self._strategies[name] = func

    def apply(self, text: str, entities: List[Dict]) -> List[Dict]:
        """
        Apply the selected sanitization strategies in order to the list of entities.
        """
        result = entities
        for strategy in self.strategies:
            strategy_func = self._strategies.get(strategy)
            if not strategy_func:
                continue  # Skip unknown strategies
            result = strategy_func(text, result)
        return result

    def _deduplicate(self, text: str, entities: List[Dict]) -> List[Dict]:
        seen = set()
        deduped = []
        for ent in entities:
            key = (ent.get("start"), ent.get("end"), ent.get("entity_type"))
            if key not in seen:
                deduped.append(ent)
                seen.add(key)
        return deduped

    def _filter_by_confidence(self, text: str, entities: List[Dict]) -> List[Dict]:
        threshold = self.confidence_threshold
        return [ent for ent in entities if ent.get("score", 1.0) >= threshold]

    def _entity_priority(self, text: str, entities: List[Dict]) -> List[Dict]:
        priority = {etype: i for i, etype in enumerate(self.entity_priority)}
        entities_sorted = sorted(
            entities,
            key=lambda ent: (
                ent["start"],
                -ent["end"],
                priority.get(ent["entity_type"], float('inf')),
                -ent.get("score", 1.0)
            )
        )
        result = []
        occupied: Set[int] = set()
        for ent in entities_sorted:
            span = set(range(ent["start"], ent["end"]))
            if not occupied.intersection(span):
                result.append(ent)
                occupied.update(span)
        return result

    def _merge_overlaps(self, text: str, entities: List[Dict]) -> List[Dict]:
        entities_sorted = sorted(
            entities,
            key=lambda ent: (ent["start"], -ent["end"], -ent.get("score", 1.0))
        )
        result = []
        occupied: Set[int] = set()
        for ent in entities_sorted:
            span = set(range(ent["start"], ent["end"]))
            if not occupied.intersection(span):
                result.append(ent)
                occupied.update(span)
        return result 