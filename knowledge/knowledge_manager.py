from knowledge.app_repository import find_app
from knowledge.website_repository import find_website
from knowledge.intent_repository import find_intent


class KnowledgeManager:

    def app(self, name):

        return find_app(name)

    def website(self, name):

        return find_website(name)

    def intent(self, command):

        return find_intent(command)