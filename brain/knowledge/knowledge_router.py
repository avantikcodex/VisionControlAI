def route(query, topic):

    query_type = query["query_type"]

    # ---------- Learning ----------

    if query_type == "LEARN":

        return "LEARNING_ENGINE"

    # ---------- Search ----------

    if query_type == "SEARCH":

        return "SEARCH_ENGINE"

    # ---------- AI ----------

    if topic == "AI":

        return "AI_KNOWLEDGE"

    # ---------- Programming ----------

    if topic == "PROGRAMMING":

        return "PROGRAMMING_KNOWLEDGE"

    # ---------- Science ----------

    if topic == "SCIENCE":

        return "SCIENCE_KNOWLEDGE"

    # ---------- Mathematics ----------

    if topic == "MATHEMATICS":

        return "MATHEMATICS_KNOWLEDGE"

    # ---------- History ----------

    if topic == "HISTORY":

        return "HISTORY_KNOWLEDGE"

    # ---------- Politics ----------

    if topic == "POLITICS":

        return "POLITICS_KNOWLEDGE"

    # ---------- Geography ----------

    if topic == "GEOGRAPHY":

        return "GEOGRAPHY_KNOWLEDGE"

    return "GENERAL_KNOWLEDGE"