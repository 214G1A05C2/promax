"""
intents.py – Master intent definitions for healthcare call transcripts.
Deterministic, no AI.
Contains all keywords, phrases, regex patterns, negative patterns, and examples.
"""
from typing import Dict, List, Any, Pattern
import re

# Type alias for readability
IntentDef = Dict[str, Any]

INTENT_DEFINITIONS: Dict[str, IntentDef] = {
    # ------------------------------------------------------------
    # 1. CANCEL APPOINTMENT
    # ------------------------------------------------------------
    "Cancel Appointment": {

        "priority": 90,

        "keywords": [
            "cancel",
            "cancellation",
            "call off",
            "not coming",
            "cannot make it",
            "unable to attend"
        ],

        "phrases": [

            "cancel my appointment",
            "cancel the appointment",

            "i need to cancel my appointment",
            "i want to cancel my appointment",
            "please cancel my appointment",

            "i cannot make my appointment",
            "i can not make my appointment",

            "i am unable to attend",

            "i will not be coming",

            "take me off the schedule",

            "cancel my visit",

            "cancel my follow up",

            "cancel my checkup"
        ],

        "regex_patterns": [

            r"\bcancel\s+(?:my|the|this|that)?\s*(?:appointment|visit|checkup|follow\s*up)?\b",

            r"\b(?:i\s+(?:need|want|would\s+like|have)\s+to\s+cancel)\b",

            r"\b(?:cannot|can\s*not|can't|unable)\s+(?:make|attend|keep)\s+(?:my|the)?\s*(?:appointment|visit)?\b",

            r"\btake\s+me\s+off\s+the\s+schedule\b",

            r"\bi\s+will\s+not\s+be\s+coming\b"
        ],

        "negative_patterns": [

            r"\bdon'?t\s+cancel\b",

            r"\bdo\s+not\s+cancel\b",

            r"\bkeep\s+the\s+appointment\b",

            r"\bstill\s+coming\b"
        ]
    },
    # ------------------------------------------------------------
    # 2. NO USER REQUEST (Silent Call)
    # ------------------------------------------------------------
    "No User Request (Silent Call)": {
        "priority": 0,   # Lowest, only used when absolutely no user content
        "keywords": [],  # Not needed – detected via empty user transcript
        "phrases": [],
        "regex_patterns": [],
        "negative_patterns": [],
        "examples": [],
    },

    # ------------------------------------------------------------
    # 3. APPOINTMENT CONFIRMATION / INQUIRY
    # ------------------------------------------------------------
    "Appointment Confirmation/Inquiry": {

        "priority": 30,

        "keywords": [

            "confirm appointment",

            "appointment confirmation",

            "appointment status",

            "appointment time",

            "appointment date",

            "check appointment",

            "verify appointment"
        ],

        "phrases": [

            "confirm my appointment",

            "i want to confirm my appointment",

            "please confirm my appointment",

            "do i have an appointment",

            "when is my appointment",

            "what time is my appointment",

            "what day is my appointment",

            "is my appointment still scheduled",

            "is my appointment confirmed",

            "check my appointment",

            "verify my appointment",

            "look up my appointment",

            "can you check my appointment"
        ],

        "regex_patterns": [

            r"\bconfirm\s+(?:my|the)?\s*appointment\b",

            r"\bverify\s+(?:my|the)?\s*appointment\b",

            r"\bcheck\s+(?:my|the)?\s*appointment\b",

            r"\bdo\s+i\s+have\s+(?:an|a)?\s*appointment\b",

            r"\bwhen\s+is\s+my\s+appointment\b",

            r"\bwhat\s+time\s+is\s+my\s+appointment\b",

            r"\bwhat\s+day\s+is\s+my\s+appointment\b",

            r"\bis\s+my\s+appointment\s+still\s+scheduled\b",

            r"\bis\s+my\s+appointment\s+confirmed\b"
        ],

        "negative_patterns": [

            r"\bcancel\b",

            r"\breschedule\b"
        ]
    },
    # ------------------------------------------------------------
    # 4. SCHEDULE APPOINTMENT
    # ------------------------------------------------------------
    "Schedule Appointment": {

        "priority": 70,

        "keywords": [

            "book appointment",

            "new appointment",

            "schedule appointment",

            "make appointment",

            "need appointment",

            "want appointment"
        ],

        "phrases": [

            "i need an appointment",

            "i want an appointment",

            "i need to schedule an appointment",

            "i want to schedule an appointment",

            "can i schedule an appointment",

            "book an appointment",

            "make an appointment",

            "schedule a new appointment",

            "i would like an appointment",

            "i would like to come in",

            "i need to see a doctor",

            "i want to see a doctor"
        ],

        "regex_patterns": [

            r"\b(?:schedule|book|make|get)\s+(?:a|an)?\s*(?:new\s+)?(?:appointment|visit|consultation)\b",

            r"\bi\s+(?:need|want|would\s+like)\s+(?:an|a)?\s*appointment\b",

            r"\bi\s+(?:need|want|would\s+like)\s+to\s+(?:schedule|book|make)\b",

            r"\bcan\s+i\s+(?:schedule|book|make)\b",

            r"\bneed\s+to\s+see\s+(?:a\s+)?doctor\b"
        ],

        "negative_patterns": [

            r"\bcancel\b",

            r"\breschedule\b",

            r"\bmodify\b",

            r"\bchange\b"
        ]
    },
    # ------------------------------------------------------------
    # 5. BILLING / INSURANCE QUESTION
    # ------------------------------------------------------------
    "Billing/Insurance Question": {

        "priority": 50,

        "keywords": [

            "billing",

            "insurance",

            "copay",

            "deductible",

            "coverage",

            "claim",

            "invoice",

            "statement",

            "eob",

            "out of pocket"
        ],

        "phrases": [

            "billing question",

            "insurance question",

            "can you explain my bill",

            "does my insurance cover",

            "is this covered by insurance",

            "what is my copay",

            "what is my deductible",

            "check my insurance",

            "update my insurance",

            "how much does the appointment cost",

            "how much is the doctor fee",

            "what is the fee",

            "what is the charge",

            "billing department"
        ],

        "regex_patterns": [

            r"\bbilling\b",

            r"\binsurance\b",

            r"\bcopay\b",

            r"\bdeductible\b",

            r"\bcoverage\b",

            r"\bclaim\b",

            r"\bexplain\s+(?:my|the)\s+bill\b",

            r"\bdoes\s+my\s+insurance\s+cover\b",

            r"\bhow\s+much\s+(?:does|is)\s+(?:the|this|that)?\s*(?:appointment|visit|consultation|fee|charge|cost)\b",

            r"\bdoctor\s+(?:fee|charge)\b"
        ],

        "negative_patterns": []
    },
    # ------------------------------------------------------------
    # 6. FRONT DESK REQUEST
    # ------------------------------------------------------------
    "Front Desk Request": {

        "priority": 40,

        "keywords": [

            "front desk",

            "reception",

            "representative",

            "operator",

            "human",

            "real person",

            "live person",

            "agent"
        ],

        "phrases": [

            "front desk please",

            "can i speak to someone",

            "i need to talk to someone",

            "connect me to the front desk",

            "transfer me to the front desk",

            "transfer me to a person",

            "i want to speak to a real person",

            "i need a human",

            "can i talk to an agent",

            "connect me to reception"
        ],

        "regex_patterns": [

            r"\bfront\s*desk\b",

            r"\breception\b",

            r"\btransfer\s+me\b",

            r"\bconnect\s+me\b",

            r"\bput\s+me\s+through\b",

            r"\bspeak\s+(?:to|with)\s+(?:someone|a\s+person|a\s+human|an\s+agent)\b",

            r"\btalk\s+(?:to|with)\s+(?:someone|a\s+person|a\s+human)\b",

            r"\breal\s+person\b",

            r"\blive\s+person\b"
        ],

        "negative_patterns": []
    },
    # ------------------------------------------------------------
    # 7. GENERAL INQUIRY (catch-all for unclear but active speech)
    # ------------------------------------------------------------
    "General Inquiry": {

        "priority": 5,

        "keywords": [

            "question",

            "help",

            "information",

            "info"
        ],

        "phrases": [

            "i have a question",

            "can you help me",

            "i need help",

            "i need information",

            "i have a quick question",

            "i wanted to ask something"
        ],

        "regex_patterns": [

            r"\bi\s+have\s+a\s+question\b",

            r"\bcan\s+you\s+help\s+me\b",

            r"\bi\s+need\s+help\b",

            r"\bi\s+need\s+information\b"
        ],

        "negative_patterns": []
    },
    # ------------------------------------------------------------
    # 8. MEDICATION / REFILL REQUEST
    # ------------------------------------------------------------
    "Medication/Refill Request": {

        "priority": 60,

        "keywords": [

            "refill",

            "prescription",

            "medication",

            "medicine",

            "pharmacy",

            "drug",

            "rx"
        ],

        "phrases": [

            "i need a refill",

            "refill my prescription",

            "refill my medication",

            "i need my medication",

            "i need more medication",

            "i ran out of my medication",

            "i ran out of my medicine",

            "i need a prescription refill",

            "send my prescription to the pharmacy",

            "call in my prescription",

            "call in my refill",

            "renew my prescription",

            "i need a new prescription",

            "i need my meds",

            "send it to cvs",

            "send it to walgreens",

            "send it to the pharmacy"
        ],

        "regex_patterns": [

            r"\brefill\b",

            r"\bprescription\b",

            r"\bmedication\b",

            r"\bmedicine\b",

            r"\bpharmacy\b",

            r"\brx\b",

            r"\bi\s+need\s+(?:a\s+)?refill\b",

            r"\brefill\s+(?:my|the)\s+(?:prescription|medication)\b",

            r"\bran\s+out\s+of\s+(?:my\s+)?(?:medication|medicine|pills)\b",

            r"\bsend\s+(?:my|the)\s+prescription\s+to\b",

            r"\bcall\s+in\s+(?:my|the)\s+(?:prescription|refill)\b",

            r"\brenew\s+(?:my|the)\s+prescription\b"
        ],

        "negative_patterns": [

            r"\bappointment\b"
        ]
    },
    # ------------------------------------------------------------
    # 9. EMERGENCY REQUEST (always wins)
    # ------------------------------------------------------------
    "Emergency Request": {

        "priority": 100,

        "keywords": [

            "heart attack",

            "stroke",

            "cannot breathe",

            "can't breathe",

            "chest pain",

            "unconscious",

            "bleeding",

            "overdose",

            "suicidal",

            "ambulance",

            "911"
        ],

        "phrases": [

            "i cannot breathe",

            "i can't breathe",

            "i am having chest pain",

            "i think i am having a heart attack",

            "i think i am having a stroke",

            "i need an ambulance",

            "call 911",

            "i am bleeding",

            "i overdosed",

            "i am suicidal",

            "someone is unconscious",

            "i am choking",

            "help i cannot breathe"
        ],

        "regex_patterns": [

            r"\bchest\s+pain\b",

            r"\bheart\s+attack\b",

            r"\bstroke\b",

            r"\bcannot\s+breathe\b",

            r"\bcan'?t\s+breathe\b",

            r"\bunconscious\b",

            r"\boverdose\b",

            r"\bsuicidal\b",

            r"\bambulance\b",

            r"\bcall\s+911\b",

            r"\bbleeding\b",

            r"\bchoking\b",

            r"\bhelp\s+.*\s+breathe\b"
        ],

        "negative_patterns": []
    },
    # ------------------------------------------------------------
    # 10. GENERAL INFORMATION REQUEST (directions, hours, etc.)
    # ------------------------------------------------------------
    "General Information Request": {

        "priority": 10,

        "keywords": [

            "hours",

            "location",

            "address",

            "directions",

            "parking",

            "fax",

            "phone number",

            "office hours",

            "new patient"
        ],

        "phrases": [

            "what are your hours",

            "where are you located",

            "what is your address",

            "do you have parking",

            "i need directions",

            "how do i get there",

            "what is your phone number",

            "what is your fax number",

            "do you accept new patients",

            "what services do you offer",

            "are you open saturday",

            "what time do you close"
        ],

        "regex_patterns": [

            r"\bhours\b",

            r"\baddress\b",

            r"\blocation\b",

            r"\bdirections\b",

            r"\bparking\b",

            r"\bfax\b",

            r"\bphone\s+number\b",

            r"\bnew\s+patient\b",

            r"\bwhere\s+are\s+you\s+located\b",

            r"\bwhat\s+are\s+your\s+hours\b"
        ],

        "negative_patterns": []
    },
    # ------------------------------------------------------------
    # 11. MODIFY APPOINTMENT (change details, not cancel)
    # ------------------------------------------------------------
    "Modify Appointment": {

        "priority": 75,

        "keywords": [

            "modify",

            "update appointment",

            "change appointment",

            "adjust appointment"
        ],

        "phrases": [

            "modify my appointment",

            "update my appointment",

            "change my appointment details",

            "adjust my appointment",

            "update appointment information",

            "change provider",

            "change doctor"
        ],

        "regex_patterns": [

            r"\bmodify\s+(?:my|the)\s+appointment\b",

            r"\bupdate\s+(?:my|the)\s+appointment\b",

            r"\bchange\s+(?:appointment\s+)?details\b",

            r"\badjust\s+(?:my|the)\s+appointment\b",

            r"\bchange\s+(?:doctor|provider)\b"
        ],

        "negative_patterns": [

            r"\bcancel\b",

            r"\breschedule\b"
        ]
    },
    # ------------------------------------------------------------
    # 12. RESCHEDULE APPOINTMENT (different from modify – implies cancel+schedule)
    # ------------------------------------------------------------
    "Reschedule Appointment": {

        "priority": 80,

        "keywords": [

            "reschedule",

            "new date",

            "new time",

            "different day",

            "different time"
        ],

        "phrases": [

            "reschedule my appointment",

            "i need to reschedule",

            "i want to reschedule",

            "can we reschedule",

            "move my appointment",

            "change my appointment to another day",

            "pick a new date",

            "pick a new time"
        ],

        "regex_patterns": [

            r"\breschedule\b",

            r"\bcan\s+we\s+reschedule\b",

            r"\bi\s+(?:need|want|have)\s+to\s+reschedule\b",

            r"\bmove\s+my\s+appointment\b",

            r"\bnew\s+(?:date|time)\b",

            r"\bdifferent\s+(?:date|time|day)\b",

            r"\bchange\s+it\s+to\b",

            r"\bmove\s+it\s+to\b"
        ],

        "negative_patterns": [

            r"\bcancel\b"
        ]
    }
}