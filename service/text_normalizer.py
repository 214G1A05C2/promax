"""
text_normalizer.py

Healthcare transcript normalization.

Deterministic.
No AI.
No embeddings.
"""

import re


CONTRACTIONS = {
    "i'm": "i am",
    "you're": "you are",
    "he's": "he is",
    "she's": "she is",
    "it's": "it is",
    "we're": "we are",
    "they're": "they are",

    "i've": "i have",
    "you've": "you have",
    "we've": "we have",
    "they've": "they have",

    "i'd": "i would",
    "you'd": "you would",
    "he'd": "he would",
    "she'd": "she would",
    "we'd": "we would",
    "they'd": "they would",

    "i'll": "i will",
    "you'll": "you will",
    "he'll": "he will",
    "she'll": "she will",
    "we'll": "we will",
    "they'll": "they will",

    "can't": "cannot",
    "won't": "will not",

    "don't": "do not",
    "doesn't": "does not",
    "didn't": "did not",

    "shouldn't": "should not",
    "couldn't": "could not",
    "wouldn't": "would not",

    "isn't": "is not",
    "aren't": "are not",
    "wasn't": "was not",
    "weren't": "were not",

    "hasn't": "has not",
    "haven't": "have not",
    "hadn't": "had not",

    "let's": "let us",

    "that's": "that is",
    "what's": "what is",
    "who's": "who is",
    "where's": "where is",
    "when's": "when is",
    "how's": "how is",

    "there's": "there is",
    "here's": "here is",
}


HEALTHCARE_NORMALISATIONS = {

    # Appointment

    "appt": "appointment",
    "appt.": "appointment",
    "apt": "appointment",
    "apointment": "appointment",
    "apointmnt": "appointment",
    "appoinment": "appointment",
    "apptment": "appointment",

    # Medication

    "med": "medication",
    "meds": "medication",

    # Prescription

    "rx": "prescription",
    "presc": "prescription",

    # Refill

    "refil": "refill",
    "refilll": "refill",

    # Cancel

    "cancle": "cancel",
    "cancl": "cancel",
    "cncl": "cancel",

    # Schedule

    "resched": "reschedule",

    "sched": "schedule",
    "schedul": "schedule",

    # Insurance

    "ins": "insurance",
    "insurence": "insurance",

    # Front Desk

    "frnt desk": "front desk",
    "f desk": "front desk",

    # Emergency misspellings only

    "emerg": "emergency",
    "emrgncy": "emergency",

    # Breathing misspellings only

    "brething": "breathing",
}


class TextNormalizer:

    @staticmethod
    def normalize(text: str) -> str:

        if not isinstance(text, str):
            return ""

        text = text.lower().strip()

        text = TextNormalizer._expand_contractions(
            text
        )

        text = TextNormalizer._normalize_healthcare(
            text
        )

        # Replace punctuation with spaces
        text = re.sub(
            r"[^\w\s]",
            " ",
            text
        )

        # Collapse spaces
        text = re.sub(
            r"\s+",
            " ",
            text
        ).strip()

        return text

    @staticmethod
    def _expand_contractions(
        text: str
    ) -> str:

        words = text.split()

        expanded = []

        for word in words:

            if word in CONTRACTIONS:

                expanded.append(
                    CONTRACTIONS[word]
                )

            else:

                expanded.append(
                    word
                )

        return " ".join(expanded)

    @staticmethod
    def _normalize_healthcare(
        text: str
    ) -> str:

        for abbr, full in (
            HEALTHCARE_NORMALISATIONS.items()
        ):

            text = re.sub(
                rf"\b{re.escape(abbr)}\b",
                full,
                text
            )

        return text
