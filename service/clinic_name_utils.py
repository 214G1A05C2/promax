import html
import re


_LEADING_CLEANUP = re.compile(
    r"^(?:hello|hi|hey|good morning|good afternoon|good evening|welcome|thanks|thank you)\b[\s,.-]*",
    re.IGNORECASE,
)

_CALLING_CLEANUP = re.compile(r"thank you for calling\s+", re.IGNORECASE)

_GREETING_PATTERNS = (
    re.compile(r"(?:hello|hi|hey|good morning|good afternoon|good evening)\s*,?\s*thank you for calling\s+(?P<clinic>.+)", re.IGNORECASE),
    re.compile(r"thank you for calling\s+(?P<clinic>.+)", re.IGNORECASE),
    re.compile(r"for calling\s+(?P<clinic>.+)", re.IGNORECASE),
    re.compile(r"calling\s+(?P<clinic>.+)", re.IGNORECASE),
    re.compile(r"i am\s+.+?\s+from\s+(?P<clinic>.+)", re.IGNORECASE),
    re.compile(r"i'm\s+.+?\s+from\s+(?P<clinic>.+)", re.IGNORECASE),
    re.compile(r"welcome to\s+(?P<clinic>.+)", re.IGNORECASE),
)

_STOP_PHRASES = (
    "if this is a medical emergency",
    "this is a medical emergency",
    "if this is a life-threatening emergency",
    "this is a life-threatening emergency",
    "please hang up now and dial nine-one-one",
    "please hang up now and dial nine one one",
    "please hang up and call nine one one",
    "otherwise",
    "how can i help you today",
    "how can i help you",
    "what can i do for you today",
    "what can i do for you",
    "can i help you today",
    "can i help you",
    "this call may be recorded",
    "this call is being recorded",
    "for quality and training purposes",
    "i can also assist",
    "i can also help",
    "i'm happy to help you",
    "i am a virtual assistant",
    "take care",
)


def normalize_clinic_name(raw_name: str) -> str:
    if raw_name is None:
        return "Unknown Clinic"

    text = html.unescape(str(raw_name)).replace("\xa0", " ")
    text = re.sub(r"\s+", " ", text).strip(" ,;:-.")

    for pattern in _GREETING_PATTERNS:
        match = pattern.search(text)
        if match:
            text = match.group("clinic")
            break

    text = _LEADING_CLEANUP.sub("", text)
    text = _CALLING_CLEANUP.sub("", text)

    lower_text = text.lower()
    cut_index = len(text)
    for phrase in _STOP_PHRASES:
        phrase_index = lower_text.find(phrase)
        if phrase_index != -1 and phrase_index < cut_index:
            cut_index = phrase_index

    text = text[:cut_index].strip(" ,;:-.")
    text = re.sub(r"\s+", " ", text)

    if not text:
        return "Unknown Clinic"

    if text.lower() in {"our practice", "the practice", "clinic", "medical group"}:
        return "Unknown Clinic"

    return text