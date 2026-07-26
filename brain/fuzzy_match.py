from rapidfuzz import process


def fuzzy_search(query, choices, score_cutoff=60):
    """
    Finds the closest matching string.
    """

    if not choices:
        return None

    result = process.extractOne(
        query,
        choices,
        score_cutoff=score_cutoff
    )

    if result:
        return result[0]

    return None