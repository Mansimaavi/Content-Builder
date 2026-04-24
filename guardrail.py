AGRICULTURE_KEYWORDS = [
    "agriculture",
    "farming",
    "crop",
    "fertilizer",
    "irrigation",
    "soil",
    "harvest",
    "pesticide",
    "wheat",
    "rice",
]

def check_guardrail(query: str) -> bool:
    query = query.lower()

    for word in AGRICULTURE_KEYWORDS:
        if word in query:
            return False

    return True
