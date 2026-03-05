import re

FILLER_WORDS = {
    "explain", "describe", "tell", "give", "show",
    "what", "is", "are", "the", "a", "an",
    "please", "can", "you", "me", "about",
    "this", "that", "in", "on", "of", "to",
    "for", "with", "how", "lets", "let",
    "learn", "teach", "understand", "discuss",
    "talk", "regarding", "basically", "actually",
    "kind", "like", "so", "okay", "ok"
}

def clean_query(text):
    text = text.lower()
    
    # remove punctuation
    text = re.sub(r"[^\w\s]", "", text)

    words = text.split()
    filtered = [w for w in words if w not in FILLER_WORDS]

    return " ".join(filtered)
