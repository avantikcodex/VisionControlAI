class AnswerGenerator:

    def generate(self, query, result):

        answer = result["answer"]

        source = result["source"]

        query_type = query["query_type"]

        # ------------------------
        # Explain
        # ------------------------

        if query_type == "EXPLAIN":

            return (
                f"{answer}\n\n"
                f"Source : {source}"
            )

        # ------------------------
        # Learn
        # ------------------------

        if query_type == "LEARN":

            return (
                f"I can help you learn this topic step by step.\n\n"
                f"{answer}"
            )

        # ------------------------
        # Search
        # ------------------------

        if query_type == "SEARCH":

            return (
                f"I searched my knowledge.\n\n"
                f"{answer}"
            )

        # ------------------------
        # Default
        # ------------------------

        return answer