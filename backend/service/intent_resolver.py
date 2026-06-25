"""
intent_resolver.py

Healthcare business-rule resolver.

Uses:
1. Candidate score
2. Business rules
3. Intent priority

to select primary + secondary intents.
"""

from typing import Dict, Any, List
from .intents import INTENT_DEFINITIONS


class IntentResolver:

    RULE_BONUS = 5

    def __init__(self):

        self.priority_map = {
            name: defn.get("priority", 0)
            for name, defn in INTENT_DEFINITIONS.items()
        }

    def resolve(
        self,
        candidates: Dict[str, Dict[str, Any]],
        normalized_text: str
    ) -> Dict[str, Any]:

        if not candidates:

            return {
                "primary": None,
                "secondaries": [],
                "resolution_rule": "no_candidates"
            }

        # -----------------------------------------
        # Working score table
        # -----------------------------------------

        scores = {
            intent: info["score"]
            for intent, info in candidates.items()
        }
        
        
        # ==========================================
        # APPOINTMENT INTENT BOOST
        # ==========================================


        APPOINTMENT_BOOST = 100

        if "Schedule Appointment" in scores:
            scores["Schedule Appointment"] += APPOINTMENT_BOOST

        if "Appointment Confirmation/Inquiry" in scores:
            scores["Appointment Confirmation/Inquiry"] += 90

        if "Reschedule Appointment" in scores:
            scores["Reschedule Appointment"] += 80

        if "Modify Appointment" in scores:
            scores["Modify Appointment"] += 70

        if "Cancel Appointment" in scores:
            scores["Cancel Appointment"] += 60


        applied_rule = "score_based"

        # =========================================
        # Emergency Override
        # =========================================

        if "Emergency Request" in scores:

            return {
                "primary": "Emergency Request",
                "secondaries": sorted(
                    [
                        x
                        for x in scores.keys()
                        if x != "Emergency Request"
                    ]
                ),
                "resolution_rule": "emergency_override"
            }

        # =========================================
        # Rule Adjustments
        # =========================================

        self._boost(
            scores,
            "Cancel Appointment",
            "Schedule Appointment"
        )

        self._boost(
            scores,
            "Reschedule Appointment",
            "Schedule Appointment"
        )

        self._boost(
            scores,
            "Modify Appointment",
            "Schedule Appointment"
        )

        self._boost(
            scores,
            "Cancel Appointment",
            "Reschedule Appointment"
        )

        self._boost(
            scores,
            "Medication/Refill Request",
            "General Inquiry"
        )

        self._boost(
            scores,
            "Appointment Confirmation/Inquiry",
            "General Inquiry"
        )

        self._boost(
            scores,
            "Medication/Refill Request",
            "Billing/Insurance Question"
        )

        self._boost(
            scores,
            "Cancel Appointment",
            "Modify Appointment"
        )

        self._boost(
            scores,
            "Cancel Appointment",
            "Appointment Confirmation/Inquiry"
        )

        self._boost(
            scores,
            "Front Desk Request",
            "General Inquiry"
        )

        # =========================================
        # Front Desk Special Rule
        # =========================================

        if (
            "Front Desk Request" in scores
            and
            "Billing/Insurance Question" in scores
        ):

            if self._contains_any(
                normalized_text,
                [
                    "front desk",
                    "transfer me",
                    "talk to a person",
                    "speak to someone"
                ]
            ):

                scores["Front Desk Request"] += (
                    self.RULE_BONUS
                )

                applied_rule = (
                    "front_desk_over_billing"
                )

        # =========================================
        # Final Winner
        # =========================================

        best = max(
            scores.keys(),
            key=lambda intent: (
                scores[intent],
                self.priority_map.get(intent, 0)
            )
        )

        secondaries = sorted(
            [
                intent
                for intent in scores.keys()
                if intent != best
            ]
        )

        return {
            "primary": best,
            "secondaries": secondaries,
            "resolution_rule": applied_rule
        }

    # ---------------------------------------------
    # Helpers
    # ---------------------------------------------

    def _boost(
        self,
        scores: Dict[str, int],
        winner: str,
        loser: str
    ):

        if winner in scores and loser in scores:

            scores[winner] += self.RULE_BONUS

    def _contains_any(
        self,
        text: str,
        values: List[str]
    ) -> bool:

        for value in values:

            if value in text:
                return True

        return False
