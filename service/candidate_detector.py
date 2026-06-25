"""
candidate_detector.py

Deterministic intent candidate detection.

Returns rich candidate information instead of simple intent names.

No AI.
No embeddings.
Pure rules.
"""

import re

from typing import Dict, Any
from .intents import INTENT_DEFINITIONS, IntentDef


class CandidateDetector:
    """
    Detect candidate intents and preserve evidence.

    Output Example:

    {
        "Schedule Appointment": {
            "score": 8,
            "keywords": ["schedule"],
            "phrases": ["i need to schedule an appointment"],
            "patterns": ["regex_here"]
        }
    }
    """

    
    KEYWORD_SCORE = 1
    PHRASE_SCORE = 4
    REGEX_SCORE = 5
    NEGATIVE_PENALTY = 2

    def __init__(self):
        self.intent_defs = INTENT_DEFINITIONS

    def detect(self, normalized_text: str) -> Dict[str, Dict[str, Any]]:

        if not normalized_text.strip():
            return {}

        results = {}

        for intent_name, definition in self.intent_defs.items():

            if intent_name == "No User Request (Silent Call)":
                continue

            evidence = self._collect_matches(
                normalized_text,
                definition
            )

            if evidence["score"] > 0:

                results[intent_name] = evidence

        return results

    def _collect_matches(
        self,
        text: str,
        definition: IntentDef
    ) -> Dict[str, Any]:

        score = 0

        matched_keywords = []
        matched_phrases = []
        matched_patterns = []
        matched_negative_patterns = []

        # ------------------------------
        # Keywords
        # ------------------------------

        for kw in definition.get("keywords", []):

            if re.search(
                rf"\b{re.escape(kw)}\b",
                text
            ):

                matched_keywords.append(kw)
                score += self.KEYWORD_SCORE

        # ------------------------------
        # Phrases
        # ------------------------------

        for phrase in definition.get("phrases", []):

            if phrase in text:

                matched_phrases.append(phrase)
                score += self.PHRASE_SCORE

        # ------------------------------
        # Regex Patterns
        # ------------------------------

        for pattern in definition.get(
            "regex_patterns",
            []
        ):

            if re.search(pattern, text):

                matched_patterns.append(pattern)
                score += self.REGEX_SCORE

        # ------------------------------
        # Negative Patterns
        # ------------------------------

        for negative in definition.get(
            "negative_patterns",
            []
        ):

            if re.search(negative, text):

                matched_negative_patterns.append(
                    negative
                )

                score -= self.NEGATIVE_PENALTY

        score = max(score, 0)

        return {
            "score": score,
            "keywords": list(
                dict.fromkeys(
                    matched_keywords
                )
            ),
            "phrases": list(
                dict.fromkeys(
                    matched_phrases
                )
            ),
            "patterns": list(
                dict.fromkeys(
                    matched_patterns
                )
            ),
            "negative_patterns": list(
                dict.fromkeys(
                    matched_negative_patterns
                )
            )
        }
