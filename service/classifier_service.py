"""
classifier_service.py
Healthcare Intent Classification Service

Pipeline:

1. Extract USER utterances
2. Normalize
3. Emergency Check
4. Candidate Detection
5. Aggregate Evidence
6. Intent Resolution
7. Confidence Calculation
8. Human Review
"""

from typing import List, Dict, Any
from .text_normalizer import TextNormalizer
from .candidate_detector import CandidateDetector
from .intent_resolver import IntentResolver
from .confidence_engine import ConfidenceEngine


class ClassifierService:

    def __init__(self):

        self.normalizer = TextNormalizer()
        self.detector = CandidateDetector()
        self.resolver = IntentResolver()
        self.confidence_engine = ConfidenceEngine()

    # ==================================================
    # MAIN ENTRY
    # ==================================================

    def classify(
        self,
        transcript: List[Dict[str, str]]
    ) -> Dict[str, Any]:
        
        # print("Transcript", transcript, "\n", "\n" )

        # ------------------------------------------
        # STEP 1
        # USER UTTERANCES
        # ------------------------------------------

        user_utterances = [

            msg["content"]

            for msg in transcript

            if (
                msg.get(
                    "role",
                    ""
                ).lower() == "user"

                and

                msg.get(
                    "content",
                    ""
                ).strip()
            )
        ]
        
        # print("user_utterances: ", user_utterances, "\n")

        if not user_utterances:

            return self._build_result(
                primary_intent="No User Request (Silent Call)",
                secondaries=[],
                confidence=0.99,
                needs_human_review=False,
                reasoning={
                    "resolution_rule":
                        "no_user_utterances",
                    "evidence": []
                }
            )

        # ------------------------------------------
        # STEP 2
        # NORMALIZE
        # ------------------------------------------

        normalized_utterances = [

            self.normalizer.normalize(
                utt
            )

            for utt in user_utterances
        ]

        all_normalized = " ".join(
            normalized_utterances
        )
        
        print("normalized_utterances", normalized_utterances, "\n")

        # ------------------------------------------
        # STEP 3
        # DETECT PER UTTERANCE
        # ------------------------------------------

        intent_hits = {}

        for utterance in normalized_utterances:

            detected = self.detector.detect(
                utterance
            )

            for (
                intent_name,
                evidence
            ) in detected.items():

                if intent_name not in intent_hits:

                    intent_hits[
                        intent_name
                    ] = {

                        "score": 0,

                        "keywords": [],

                        "phrases": [],

                        "patterns": [],

                        "negative_patterns": [],

                        "utterances": []
                    }

                target = intent_hits[
                    intent_name
                ]

                target["score"] += (
                    evidence["score"]
                )

                target[
                    "keywords"
                ].extend(
                    evidence["keywords"]
                )

                target[
                    "phrases"
                ].extend(
                    evidence["phrases"]
                )

                target[
                    "patterns"
                ].extend(
                    evidence["patterns"]
                )

                target[
                    "negative_patterns"
                ].extend(
                    evidence[
                        "negative_patterns"
                    ]
                )

                target[
                    "utterances"
                ].append(
                    utterance
                )
        for i in intent_hits:     
            print("intent_hits: ", i, "\n", "\n")
        
        # for idx, utterance in enumerate(normalized_utterances, start=1):

        #     print("\n" + "=" * 80)
        #     print(f"UTTERANCE #{idx}")
        #     print(f"TEXT: {utterance}")

        #     detected = self.detector.detect(utterance)

        #     if not detected:
        #         print("INTENTS: NONE")
        #     else:

        #         print("INTENTS DETECTED:")

        #         for intent_name, evidence in detected.items():

        #             print(f"\n  Intent: {intent_name}")
        #             print(f"  Score : {evidence['score']}")

        #             print(
        #                 f"  Keywords: {evidence['keywords']}"
        #             )

        #             print(
        #                 f"  Phrases : {evidence['phrases']}"
        #             )

        #             print(
        #                 f"  Patterns: {evidence['patterns']}"
        #             )

        #             print(
        #                 f"  Negatives: {evidence['negative_patterns']}"
        #             )

        #     # Existing logic
        #     for intent_name, evidence in detected.items():

        #         if intent_name not in intent_hits:

        #             intent_hits[intent_name] = {
        #                 "score": 0,
        #                 "keywords": [],
        #                 "phrases": [],
        #                 "patterns": [],
        #                 "negative_patterns": [],
        #                 "utterances": []
        #             }

        #         target = intent_hits[intent_name]

        #         target["score"] += evidence["score"]

        #         target["keywords"].extend(
        #             evidence["keywords"]
        #         )

        #         target["phrases"].extend(
        #             evidence["phrases"]
        #         )

        #         target["patterns"].extend(
        #             evidence["patterns"]
        #         )

        #         target["negative_patterns"].extend(
        #             evidence["negative_patterns"]
        #         )

        #         target["utterances"].append(
        #             utterance
        #         )

        print("\n")
        print("=" * 120)
        print("CONVERSATION WITH INTENT ANALYSIS")
        print("=" * 120)

        user_idx = 0

        for idx, msg in enumerate(transcript, start=1):

            role = msg.get("role", "").lower()

            print("\n" + "=" * 80)

            if role == "agent":

                print(f"[{idx}] AGENT")
                print(msg["content"])

            elif role == "user":

                user_idx += 1

                original = msg["content"]

                normalized = self.normalizer.normalize(
                    original
                )

                print(f"[{idx}] USER")
                print(f"ORIGINAL  : {original}")
                print(f"NORMALIZED: {normalized}")

                detected = self.detector.detect(
                    normalized
                )

                if not detected:

                    print("INTENTS: NONE")

                else:

                    print("INTENTS DETECTED:")

                    for intent_name, evidence in detected.items():

                        print(
                            f"\n  Intent: {intent_name}"
                        )

                        print(
                            f"  Score: {evidence['score']}"
                        )

                        print(
                            f"  Keywords: {evidence['keywords']}"
                        )

                        print(
                            f"  Phrases: {evidence['phrases']}"
                        )

                        print(
                            f"  Patterns: {evidence['patterns']}"
                        )

                        print(
                            f"  Negatives: {evidence['negative_patterns']}"
                        )


        # ------------------------------------------
        # STEP 4
        # NO CANDIDATES
        # ------------------------------------------

        if not intent_hits:

            return self._build_result(
                primary_intent="General Inquiry",
                secondaries=[],
                confidence=0.10,
                needs_human_review=True,
                reasoning={
                    "resolution_rule":
                        "fallback_general",
                    "evidence": []
                }
            )

        # ------------------------------------------
        # DEDUPE
        # ------------------------------------------

        for info in intent_hits.values():

            info["keywords"] = list(
                dict.fromkeys(
                    info["keywords"]
                )
            )

            info["phrases"] = list(
                dict.fromkeys(
                    info["phrases"]
                )
            )

            info["patterns"] = list(
                dict.fromkeys(
                    info["patterns"]
                )
            )

            info[
                "negative_patterns"
            ] = list(
                dict.fromkeys(
                    info[
                        "negative_patterns"
                    ]
                )
            )

        # ------------------------------------------
        # STEP 5
        # EMERGENCY OVERRIDE
        # ------------------------------------------

        if (
            "Emergency Request"
            in intent_hits
        ):

            return self._build_result(
                primary_intent="Emergency Request",

                secondaries=[],

                confidence=0.99,

                needs_human_review=False,

                reasoning={

                    "resolution_rule":
                        "emergency_override",

                    "evidence":
                        intent_hits[
                            "Emergency Request"
                        ]
                }
            )

        # ------------------------------------------
        # STEP 6
        # RESOLUTION
        # ------------------------------------------

        resolution = (
            self.resolver.resolve(
                intent_hits,
                all_normalized
            )
        )

        primary = (
            resolution["primary"]
        )

        secondaries = (
            resolution["secondaries"]
        )

        rule = (
            resolution[
                "resolution_rule"
            ]
        )

        if not primary:

            primary = (
                "General Inquiry"
            )

            secondaries = []

            rule = (
                "fallback_general"
            )

        # ------------------------------------------
        # STEP 7
        # CONFIDENCE
        # ------------------------------------------

        primary_info = (
            intent_hits.get(
                primary,
                {}
            )
        )

        confidence = (
            self.confidence_engine.compute(

                primary_intent=primary,

                candidate_info=primary_info,

                secondary_count=len(secondaries)
            )
        )

        # ------------------------------------------
        # STEP 8
        # HUMAN REVIEW
        # ------------------------------------------

        needs_review = (
            self._requires_human_review(
                confidence,
                len(intent_hits),
                primary
            )
        )

        # ------------------------------------------
        # FINAL RESULT
        # ------------------------------------------

        return self._build_result(

            primary_intent=primary,

            secondaries=secondaries,

            confidence=confidence,

            needs_human_review=needs_review,

            reasoning={

                "resolution_rule":
                    rule,

                "evidence":
                    primary_info,

                "candidate_count":
                    len(intent_hits)
            }
        )

    # ==================================================
    # REVIEW LOGIC
    # ==================================================

    def _requires_human_review(

        self,

        confidence: float,

        candidate_count: int,

        primary_intent: str

    ) -> bool:

        if (
            primary_intent
            ==
            "Emergency Request"
        ):
            return False

        if confidence < 0.70:
            return True

        if candidate_count >= 4:
            return True

        return False

    # ==================================================
    # RESULT BUILDER
    # ==================================================

    def _build_result(

        self,

        primary_intent: str,

        secondaries: List[str],

        confidence: float,

        needs_human_review: bool,

        reasoning: Dict[str, Any]

    ) -> Dict[str, Any]:
        
        print("\n", "Final Intent: ", primary_intent, "\n", "\n")
    

        return {

            "primary_intent":
                primary_intent,

            "secondary_intents":
                secondaries,

            "confidence":
                confidence,

            "needs_human_review":
                needs_human_review,

            "reasoning":
                reasoning
        }
