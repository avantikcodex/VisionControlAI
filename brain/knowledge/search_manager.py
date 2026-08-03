def search(destination, query):

    if destination == "AI_KNOWLEDGE":

        return {
            "source": "AI Database",
            "answer": "Artificial Intelligence enables computers to perform tasks that normally require human intelligence."
        }

    if destination == "PROGRAMMING_KNOWLEDGE":

        return {
            "source": "Programming Database",
            "answer": "Python is one of the world's most popular programming languages."
        }

    if destination == "SCIENCE_KNOWLEDGE":

        return {
            "source": "Science Database",
            "answer": "Science studies the natural world using observation and experimentation."
        }

    if destination == "HISTORY_KNOWLEDGE":

        return {
            "source": "History Database",
            "answer": "History is the study of past events."
        }

    if destination == "POLITICS_KNOWLEDGE":

        return {
            "source": "Politics Database",
            "answer": "Politics is the process of governing a nation or society."
        }

    return {
        "source": "General Database",
        "answer": "I don't have enough information yet."
    }