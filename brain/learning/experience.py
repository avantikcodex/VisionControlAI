class ExperienceManager:

    def __init__(self):

        self.memory = []

    def store(self, question, answer):

        self.memory.append({

            "question": question,

            "answer": answer

        })

        print("[Experience] Stored")