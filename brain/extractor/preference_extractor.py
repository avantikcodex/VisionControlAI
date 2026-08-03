from brain.extractor.entity_patterns import PREFERENCE_PATTERNS


def extract_preferences(sentence):

    result = {}

    for key, patterns in PREFERENCE_PATTERNS.items():

        for pattern in patterns:

            match = pattern.search(sentence)

            if match:

                result[key] = match.group(1).strip()

    return result