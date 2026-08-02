STOP_WORDS = {

    "a",
    "an",
    "the",

    "please",
    "could",
    "can",
    "would",
    "will",

    "you",
    "your",
    "me",
    "my",
    "mine",

    "for",
    "to",
    "of",
    "on",
    "at",
    "in",
    "into",
    "from",
    "with",
    "by",

    "is",
    "are",
    "am",
    "was",
    "were",
    "be",

    "hey",
    "hi",
    "hello",

    "kindly",
    "just",

    "do",
    "does",
    "did"
}


def remove_stop_words(tokens):

    cleaned = []

    for token in tokens:

        if token not in STOP_WORDS:

            cleaned.append(token)

    return cleaned