"""
confidence_engine.py

Deterministic confidence scoring.

No AI.
No ML.

Confidence is based on:

- Candidate score
- Keywords
- Phrases
- Regex matches
- Negative patterns
- Ambiguity
"""

from typing import Dict, Any


class ConfidenceEngine:

    def __init__(self):
        pass

    def compute(
        self,
        primary_intent: str,
        candidate_info: Dict[str, Any],
        secondary_count: int
    ) -> float:

        if not primary_intent:
            return 0.0

        score = candidate_info.get(
            "score",
            0
        )

        keywords = candidate_info.get(
            "keywords",
            []
        )

        phrases = candidate_info.get(
            "phrases",
            []
        )

        patterns = candidate_info.get(
            "patterns",
            []
        )

        negatives = candidate_info.get(
            "negative_patterns",
            []
        )

        confidence = 0.40

        # ---------------------------------
        # Detector score contribution
        # ---------------------------------

        confidence += min(
            score * 0.03,
            0.30
        )

        # ---------------------------------
        # Keywords
        # ---------------------------------

        confidence += min(
            len(keywords) * 0.02,
            0.10
        )

        # ---------------------------------
        # Phrases
        # ---------------------------------

        confidence += min(
            len(phrases) * 0.05,
            0.15
        )

        # ---------------------------------
        # Regex
        # ---------------------------------

        confidence += min(
            len(patterns) * 0.06,
            0.20
        )

        # ---------------------------------
        # Negative Patterns
        # ---------------------------------

        confidence -= min(
            len(negatives) * 0.10,
            0.30
        )

        # ---------------------------------
        # Ambiguity Penalty
        # ---------------------------------

        if secondary_count >= 1:

            confidence -= min(
                secondary_count * 0.04,
                0.20
            )

        # ---------------------------------
        # Strong Evidence Bonus
        # ---------------------------------

        if (
            score >= 12
            and
            len(patterns) >= 2
        ):

            confidence += 0.10

        # ---------------------------------
        # Clamp
        # ---------------------------------

        confidence = max(
            0.0,
            min(
                confidence,
                0.99
            )
        )

        return round(
            confidence,
            2
        )
