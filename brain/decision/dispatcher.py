from automation.automation_engine import AutomationEngine


class Dispatcher:

    def __init__(self):

        self.automation = AutomationEngine()

    def dispatch(self, decision):

        if decision is None:

            print("[Dispatcher] No decision")

            return False

        action = getattr(
            decision,
            "action",
            None
        )

        target = getattr(
            decision,
            "target",
            None
        )

        if not action:

            print("[Dispatcher] No action")

            return False

        print(
            f"[Dispatcher] Action : {action}"
        )

        # -----------------------------------------------------
        # SAFETY CHECK
        # -----------------------------------------------------

        confidence = getattr(
            decision,
            "confidence",
            0
        )

        need_confirmation = getattr(
            decision,
            "need_confirmation",
            False
        )

        risk = getattr(
            decision,
            "risk",
            "LOW"
        )

        print(
            f"[Dispatcher] Confidence : {confidence}"
        )

        print(
            f"[Dispatcher] Risk : {risk}"
        )

        if need_confirmation:

            print(
                "[Dispatcher] Confirmation required"
            )

            return False

        # -----------------------------------------------------
        # AUTOMATION
        # -----------------------------------------------------

        result = self.automation.execute(
            action,
            target
        )

        if result:

            print(
                "[Dispatcher] Automation successful"
            )

        else:

            print(
                "[Dispatcher] Automation failed"
            )

        return result