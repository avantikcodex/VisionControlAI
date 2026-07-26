from launcher.search_app import search_application
from launcher.app_launcher import launch_application


class ApplicationSkill:

    name = "APPLICATION"

    def execute(self, command):

        app = search_application(command)

        if app:

            launch_application(app)

            return True

        return False