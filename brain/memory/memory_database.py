import json
import os


class MemoryDatabase:

    def load(self, path):

        if not os.path.exists(path):

            return {}

        with open(path, "r", encoding="utf-8") as file:

            return json.load(file)

    def save(self, path, data):

        with open(path, "w", encoding="utf-8") as file:

            json.dump(data, file, indent=4)