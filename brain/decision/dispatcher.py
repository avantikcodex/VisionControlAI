from launcher.app_launcher import launch_application
from browser.websites import open_website


class Dispatcher:

    def dispatch(self, decision):

        if decision.action == "OPEN_APPLICATION":

            return launch_application(decision.target)

        elif decision.action == "OPEN_WEBSITE":

            return open_website(decision.target)

        else:

            print("No dispatcher available for:", decision.action)

            return False