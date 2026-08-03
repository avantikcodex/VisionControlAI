class ResponseHandler:

    def build(self, request):

        decision = request.decision

        if decision is None:

            return "I couldn't understand."

        action = decision.action

        if action == "OPEN_APPLICATION":

            return f"Opening {decision.target['name']}."

        if action == "OPEN_WEBSITE":

            return f"Opening {decision.target['name']}."

        return "Done."