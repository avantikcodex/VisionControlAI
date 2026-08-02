from knowledge.knowledge_manager import KnowledgeManager

km = KnowledgeManager()

ACTION_WORDS = {
    "open",
    "launch",
    "start",
    "run",
    "play",
    "browse",
    "search",
    "watch"
}


def extract_entity(tokens):

    # Remove action words
    filtered = []

    for token in tokens:

        if token not in ACTION_WORDS:

            filtered.append(token)

    sentence = " ".join(filtered)

    # ---------- Applications ----------

    app = km.app(sentence)

    if app:

        return {

            "type": "APPLICATION",

            "value": app

        }

    # ---------- Websites ----------

    website = km.website(sentence)

    if website:

        return {

            "type": "WEBSITE",

            "value": website

        }

    return None