class MemoryReinforcement:

    def __init__(self):

        self.memory = {}

    def reinforce(self, item):

        if item not in self.memory:

            self.memory[item] = 1

        else:

            self.memory[item] += 1

    def score(self, item):

        return self.memory.get(item, 0)

    def strongest(self):

        if not self.memory:

            return None

        return max(
            self.memory,
            key=self.memory.get
        )

    def all(self):

        return self.memory