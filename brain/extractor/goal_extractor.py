from brain.extractor.entity_patterns import GOAL_PATTERNS


def extract_goal(sentence):

    result = {}

    for key, patterns in GOAL_PATTERNS.items():

        for pattern in patterns:

            match = pattern.search(sentence)

            if match:

                result[key] = match.group(1).strip()

    return result