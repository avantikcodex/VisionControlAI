from brain.extractor.entity_patterns import PROFILE_PATTERNS


def extract_profile(sentence):

    result = {}

    for key, patterns in PROFILE_PATTERNS.items():

        for pattern in patterns:

            match = pattern.search(sentence)

            if match:

                result[key] = match.group(1).strip()

    return result