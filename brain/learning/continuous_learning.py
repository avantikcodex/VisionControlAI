class ContinuousLearning:

    def __init__(self):

        self.cycles = 0

    def update(self):

        self.cycles += 1

        print(
            f"[Continuous Learning] Cycle {self.cycles}"
        )

    def total_cycles(self):

        return self.cycles