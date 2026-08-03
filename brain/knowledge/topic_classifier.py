AI = {
    "ai",
    "artificial intelligence",
    "machine learning",
    "deep learning",
    "neural network",
    "chatgpt",
    "llm"
}

PROGRAMMING = {
    "python",
    "java",
    "javascript",
    "c",
    "c++",
    "coding",
    "programming",
    "code",
    "algorithm"
}

SCIENCE = {
    "physics",
    "chemistry",
    "biology",
    "science",
    "atom",
    "molecule",
    "energy"
}

MATHEMATICS = {
    "math",
    "mathematics",
    "algebra",
    "geometry",
    "calculus",
    "equation"
}

HISTORY = {
    "history",
    "independence",
    "world war",
    "freedom",
    "king",
    "emperor"
}

POLITICS = {
    "politics",
    "government",
    "prime minister",
    "president",
    "constitution",
    "parliament"
}

GEOGRAPHY = {
    "country",
    "capital",
    "river",
    "mountain",
    "continent",
    "earth"
}


def check_keywords(sentence, words, keywords):
    """
    Matches both single-word and multi-word keywords.
    """

    for keyword in keywords:

        # Multi-word phrase
        if " " in keyword:

            if keyword in sentence:
                return True

        # Single word
        else:

            if keyword in words:
                return True

    return False


def classify_topic(sentence):

    sentence = sentence.lower().strip()

    words = sentence.split()

    if check_keywords(sentence, words, AI):
        return "AI"

    if check_keywords(sentence, words, PROGRAMMING):
        return "PROGRAMMING"

    if check_keywords(sentence, words, SCIENCE):
        return "SCIENCE"

    if check_keywords(sentence, words, MATHEMATICS):
        return "MATHEMATICS"

    if check_keywords(sentence, words, HISTORY):
        return "HISTORY"

    if check_keywords(sentence, words, POLITICS):
        return "POLITICS"

    if check_keywords(sentence, words, GEOGRAPHY):
        return "GEOGRAPHY"

    return "GENERAL"