import re


QUESTION_WORDS = {
    "what",
    "who",
    "when",
    "where",
    "why",
    "which",
    "whose",
    "how"
}


EXPLAIN_WORDS = {
    "explain",
    "describe",
    "define",
    "meaning"
}


TEACH_WORDS = {
    "teach",
    "learn",
    "study"
}


SEARCH_WORDS = {
    "find",
    "search",
    "look"
}


LANGUAGES = {
    "english",
    "hindi",
    "urdu",
    "marathi",
    "tamil",
    "telugu",
    "kannada",
    "malayalam"
}


class QueryProcessor:

    def process(self, sentence):

        sentence = sentence.lower().strip()

        sentence = re.sub(r"\s+", " ", sentence)

        return {
            "original": sentence,
            "query_type": self.detect_type(sentence),
            "language": self.detect_language(sentence)
        }

    def detect_type(self, sentence):

        words = sentence.split()

        for word in words:

            if word in QUESTION_WORDS:
                return "QUESTION"

            if word in EXPLAIN_WORDS:
                return "EXPLAIN"

            if word in TEACH_WORDS:
                return "LEARN"

            if word in SEARCH_WORDS:
                return "SEARCH"

        return "GENERAL"

    def detect_language(self, sentence):

        for language in LANGUAGES:

            if language in sentence:

                return language.title()

        return "English"