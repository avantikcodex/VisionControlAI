import re


def tokenize(sentence):
    """
    Converts a sentence into clean lowercase tokens.
    """

    sentence = sentence.lower()

    # Remove punctuation
    sentence = re.sub(r"[^\w\s]", "", sentence)

    # Split into words
    tokens = sentence.split()

    return tokens