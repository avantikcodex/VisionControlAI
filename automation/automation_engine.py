from automation.app_controller import AppController
from automation.browser_controller import BrowserController
from automation.keyboard_controller import KeyboardController
from automation.mouse_controller import MouseController


class AutomationEngine:

    def __init__(self):

        self.app = AppController()
        self.browser = BrowserController()
        self.keyboard = KeyboardController()
        self.mouse = MouseController()

    def execute(self, action, target=None):

        if not action:
            print("[Automation] No action specified")
            return False

        action = str(action).upper().strip()

        print(
            f"[Automation] Action : {action}"
        )

        try:

            # -------------------------------------------------
            # APPLICATION
            # -------------------------------------------------

            if action == "OPEN_APPLICATION":

                return self.app.open(target)

            # -------------------------------------------------
            # WEBSITE
            # -------------------------------------------------

            elif action == "OPEN_WEBSITE":

                return self.browser.open(target)

            # -------------------------------------------------
            # KEYBOARD
            # -------------------------------------------------

            elif action == "TYPE_TEXT":

                return self.keyboard.type_text(target)

            elif action == "PRESS_KEY":

                return self.keyboard.press(target)

            elif action == "ENTER":

                return self.keyboard.enter()

            elif action == "ESCAPE":

                return self.keyboard.escape()

            elif action == "BACKSPACE":

                return self.keyboard.backspace()

            elif action == "DELETE":

                return self.keyboard.delete()

            elif action == "COPY":

                return self.keyboard.copy()

            elif action == "PASTE":

                return self.keyboard.paste()

            elif action == "CUT":

                return self.keyboard.cut()

            elif action == "SELECT_ALL":

                return self.keyboard.select_all()

            elif action == "UNDO":

                return self.keyboard.undo()

            elif action == "REDO":

                return self.keyboard.redo()

            elif action == "SAVE":

                return self.keyboard.save()

            elif action == "SWITCH_WINDOW":

                return self.keyboard.switch_window()

            elif action == "SHOW_DESKTOP":

                return self.keyboard.show_desktop()

            # -------------------------------------------------
            # MOUSE
            # -------------------------------------------------

            elif action == "MOUSE_MOVE":

                if not isinstance(target, (list, tuple)):
                    print("[Automation] Mouse coordinates required")
                    return False

                if len(target) < 2:
                    print("[Automation] Mouse coordinates required")
                    return False

                return self.mouse.move(
                    target[0],
                    target[1]
                )

            elif action == "MOUSE_CLICK":

                if isinstance(target, (list, tuple)):

                    if len(target) >= 2:

                        return self.mouse.click(
                            target[0],
                            target[1]
                        )

                return self.mouse.click()

            elif action == "MOUSE_RIGHT_CLICK":

                if isinstance(target, (list, tuple)):

                    if len(target) >= 2:

                        return self.mouse.right_click(
                            target[0],
                            target[1]
                        )

                return self.mouse.right_click()

            elif action == "MOUSE_DOUBLE_CLICK":

                if isinstance(target, (list, tuple)):

                    if len(target) >= 2:

                        return self.mouse.double_click(
                            target[0],
                            target[1]
                        )

                return self.mouse.double_click()

            elif action == "MOUSE_MIDDLE_CLICK":

                if isinstance(target, (list, tuple)):

                    if len(target) >= 2:

                        return self.mouse.middle_click(
                            target[0],
                            target[1]
                        )

                return self.mouse.middle_click()

            elif action == "SCROLL_UP":

                amount = target if target is not None else 5

                return self.mouse.scroll_up(amount)

            elif action == "SCROLL_DOWN":

                amount = target if target is not None else 5

                return self.mouse.scroll_down(amount)

            # -------------------------------------------------
            # UNKNOWN
            # -------------------------------------------------

            else:

                print(
                    f"[Automation] Unknown action : {action}"
                )

                return False

        except Exception as error:

            print(
                f"[Automation] Execution failed : {error}"
            )

            return False