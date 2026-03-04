import re

# Common filler words in teaching speech
FILLER_WORDS = {
    "explain", "describe", "tell", "give", "show",
    "what", "is", "are", "the", "a", "an",
    "please", "can", "you", "me", "about",
    "this", "that", "in", "on", "of", "to",
    "for", "with", "how", "lets", "let",
    "learn", "teach", "understand", "discuss",
    "talk", "regarding", "basically", "actually"
}

def clean_text(text):
    """
    Step 1: Lowercase
    Step 2: Remove punctuation
    Step 3: Remove extra spaces
    """
    text = text.lower()
    text = re.sub(r"[^\w\s]", "", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


def extract_keywords(text):
    """
    Remove filler words and keep meaningful tokens
    """
    words = text.split()
    keywords = [word for word in words if word not in FILLER_WORDS]
    return keywords


def build_query(text):
    cleaned = clean_text(text)
    keywords = extract_keywords(cleaned)
    query = " ".join(keywords)
    return query
