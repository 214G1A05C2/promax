# ==========================================================
# INTENT PRIORITY
# ==========================================================

INTENT_PRIORITY = [

    "Emergency Request",

    "Cancel Appointment",

    "Reschedule Appointment",

    "Modify Appointment",

    "Schedule Appointment",

    "Appointment Confirmation/Inquiry",

    "Medication Refill Request",

    "Billing/Insurance Question",

    "Front Desk Request",

    "General Inquiry"
]


# ==========================================================
# MAIN INTENTS
# ==========================================================

MAIN_INTENT_PATTERNS = {

    "Schedule Appointment": {

        "strong": [

            r"\bschedule appointment\b",
            r"\bbook appointment\b",
            r"\bmake appointment\b",
            r"\bneed appointment\b",
            r"\bwant appointment\b",
            r"\bnew appointment\b",
            r"\bbook a visit\b",
            r"\bsee a doctor\b",
            r"\bsee a provider\b",
            r"\bneed consultation\b",
            r"\bfollow up appointment\b",
            r"\bannual physical\b",
            r"\bcheckup\b"
            r"\bschedule an appointment\b",
            r"\bschedule appointment\b",
            r"\bwanna schedule\b",
            r"\bwant to schedule\b",
            r"\bneed an appointment\b",
            r"\bi just wanna schedule\b",
            r"\bbook me\b",
        ],

        "weak": [

            r"\bappointment\b",
            r"\bvisit\b",
            r"\bconsultation\b",
            r"\bdoctor\b",
            r"\bprovider\b"
        ]
    },


    "Reschedule Appointment": {

        "strong": [

            r"\breschedule\b",
            r"\bmove appointment\b",
            r"\bchange appointment date\b",
            r"\bchange appointment time\b",
            r"\bdifferent date\b",
            r"\bdifferent time\b",
            r"\bneed another day\b",
            r"\bneed another time\b",
            r"\bmove it to tomorrow\b",
            r"\bmove it to next week\b"
        ],

        "weak": [

            r"\bschedule conflict\b",
            r"\bbusy that day\b",
            r"\bbusy at that time\b"
        ]
    },


    "Cancel Appointment": {

        "strong": [

            r"\bcancel appointment\b",
            r"\bcancel my appointment\b",
            r"\bcancel visit\b",
            r"\bcancel booking\b",
            r"\bi need to cancel\b",
            r"\bi want to cancel\b",
            r"\bremove appointment\b",
            r"\btake me off schedule\b"
        ],

        "weak": [

            r"\bi cannot attend\b",
            r"\bi can't attend\b",
            r"\bi won't attend\b",
            r"\bnot attending\b"
        ]
    },


    "Modify Appointment": {

        "strong": [

            r"\bchange provider\b",
            r"\bchange doctor\b",
            r"\bchange location\b",
            r"\bchange clinic\b",
            r"\bchange insurance\b",
            r"\bupdate insurance\b",
            r"\bupdate phone number\b",
            r"\bupdate email\b",
            r"\bupdate address\b",
            r"\bmodify appointment\b"
        ],

        "weak": [

            r"\bchange information\b",
            r"\bupdate information\b",
            r"\bmodify details\b"
        ]
    },


    "Medication Refill Request": {

        "strong": [

            r"\brefill prescription\b",
            r"\brefill medication\b",
            r"\bneed refill\b",
            r"\bprescription renewal\b",
            r"\bout of medication\b",
            r"\brunning out of medication\b"
        ],

        "weak": [

            r"\bprescription\b",
            r"\bmedication\b",
            r"\bmedicine\b"
        ]
    },


    "Billing/Insurance Question": {

        "strong": [

            r"\binsurance verification\b",
            r"\bverify insurance\b",
            r"\bcheck insurance\b",
            r"\binsurance coverage\b",
            r"\bwhat is my copay\b",
            r"\bwhat is my deductible\b",
            r"\bdo you accept insurance\b",
            r"\bbilling question\b",
            r"\bbilling issue\b",
            r"\bpayment question\b"
        ],

        "weak": [

            r"\binsurance\b",
            r"\bcigna\b",
            r"\baetna\b",
            r"\bblue cross\b",
            r"\bmember id\b",
            r"\bcoverage\b",
            r"\bcopay\b",
            r"\bdeductible\b",
            r"\bbalance\b"
        ]
    },


    "Appointment Confirmation/Inquiry": {

        "strong": [

            r"\bwhen is my appointment\b",
            r"\bwhat time is my appointment\b",
            r"\bdo i have an appointment\b",
            r"\bam i scheduled\b",
            r"\bconfirm appointment\b",
            r"\bcheck appointment\b",
            r"\bappointment details\b"
        ],

        "weak": [

            r"\bappointment status\b",
            r"\bbooking status\b"
        ]
    },


    "Front Desk Request": {

        "strong": [

            r"\bspeak to receptionist\b",
            r"\bspeak to front desk\b",
            r"\btransfer me\b",
            r"\bconnect me to office\b",
            r"\breal person\b",
            r"\bhuman agent\b",
            r"\bmedical records\b",
            r"\bleave message\b"
        ],

        "weak": [

            r"\breceptionist\b",
            r"\bfront desk\b",
            r"\boffice\b"
        ]
    },


    "General Inquiry": {

        "strong": [

            r"\bgeneral question\b",
            r"\bi have a question\b",
            r"\bneed information\b",
            r"\blooking for information\b",
            r"\bclinic hours\b",
            r"\boffice hours\b",
            r"\bclinic address\b"
        ],

        "weak": [

            r"\bquestion\b",
            r"\binformation\b"
        ]
    }
}


# ==========================================================
# SUB INTENT DETECTION
# ==========================================================

SUB_INTENT_PATTERNS = {

    "Billing/Insurance Question": [

        r"\binsurance\b",
        r"\bcigna\b",
        r"\baetna\b",
        r"\bmember id\b",
        r"\bcoverage\b",
        r"\bprimary insurance\b",
        r"\bsecondary insurance\b"
    ],

    "Appointment Confirmation/Inquiry": [

        r"\bconfirm\b",
        r"\bappointment details\b",
        r"\bwhat time\b",
        r"\bwhen is\b"
    ]
}


# ==========================================================
# WORKFLOW TAGS
# ==========================================================

WORKFLOW_TAG_PATTERNS = {

    "Existing Patient": [

        r"\bhave been there before\b",
        r"\bexisting patient\b",
        r"\breturning patient\b"
    ],

    "New Patient": [

        r"\bnew patient\b",
        r"\bfirst visit\b",
        r"\bfirst appointment\b"
    ],

    "Provider Preference": [

        r"\bprefer dr\b",
        r"\bprefer doctor\b",
        r"\bprefer provider\b",
        r"\bi prefer\b"
    ],

    "Follow Up Visit": [

        r"\bfollow up\b",
        r"\bfollow-up\b"
    ],

    "Insurance Verification": [

        r"\bmember id\b",
        r"\binsurance\b",
        r"\bcoverage\b",
        r"\bverify coverage\b"
    ],

    "Coverage Verification": [

        r"\bcoverage looks good\b",
        r"\bverify coverage\b",
        r"\binsurance verified\b"
    ],

    "Appointment Scheduled": [

        r"\bavailable\b",
        r"\bappointment booked\b",
        r"\bappointment scheduled\b"
    ]
}


# ==========================================================
# EMERGENCY
# ==========================================================

EMERGENCY_PATTERNS = [

    r"\bi can't breathe\b",
    r"\bi cant breathe\b",
    r"\bheart attack\b",
    r"\bstroke\b",
    r"\bsevere bleeding\b",
    r"\bunconscious\b",
    r"\bambulance\b",
    r"\bcall an ambulance\b",
    r"\bchest pain\b",
    r"\bsuicidal\b"
]


# ==========================================================
# SYMPTOMS
# ==========================================================

SYMPTOM_PATTERNS = [

    r"\bpain\b",
    r"\bheadache\b",
    r"\bfever\b",
    r"\bcough\b",
    r"\bnausea\b",
    r"\bvomiting\b",
    r"\bdizziness\b",
    r"\bfatigue\b",
    r"\bweakness\b",
    r"\brash\b",
    r"\bswelling\b",
    r"\bshortness of breath\b"
]