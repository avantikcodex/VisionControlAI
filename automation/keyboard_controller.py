import time

import pyautogui


class KeyboardController:

    def __init__(self):

        pyautogui.PAUSE = 0.05

    # ---------------------------------------------------------
    # BASIC KEYBOARD
    # ---------------------------------------------------------

    def type_text(self, text):

        if text is None:
            print("[Keyboard] No text specified")
            return False

        text = str(text)

        if not text:
            print("[Keyboard] Empty text")
            return False

        try:

            pyautogui.write(
                text,
                interval=0.02
            )

            print(f"[Keyboard] Typed : {text}")

            return True

        except Exception as error:

            print(
                f"[Keyboard] Failed to type : {error}"
            )

            return False

    def press(self, key):

        if key is None:
            return False

        key = str(key).lower().strip()

        if not key:
            return False

        try:

            pyautogui.press(key)

            print(f"[Keyboard] Pressed : {key}")

            return True

        except Exception as error:

            print(
                f"[Keyboard] Failed to press {key} : {error}"
            )

            return False

    # ---------------------------------------------------------
    # SHORTCUTS
    # ---------------------------------------------------------

    def hotkey(self, *keys):

        if not keys:
            print("[Keyboard] No shortcut specified")
            return False

        keys = tuple(
            str(key).lower().strip()
            for key in keys
        )

        try:

            # Press modifiers/keys in order
            for key in keys:
                pyautogui.keyDown(key)
                time.sleep(0.03)

            # Release in reverse order
            for key in reversed(keys):
                pyautogui.keyUp(key)
                time.sleep(0.03)

            print(
                f"[Keyboard] Shortcut : {' + '.join(keys)}"
            )

            return True

        except Exception as error:

            # Safety: release any keys that may still
            # be held down if an error occurs.
            for key in reversed(keys):
                try:
                    pyautogui.keyUp(key)
                except Exception:
                    pass

            print(
                f"[Keyboard] Shortcut failed : {error}"
            )

            return False

    # ---------------------------------------------------------
    # COMMON KEYS
    # ---------------------------------------------------------

    def enter(self):
        return self.press("enter")

    def escape(self):
        return self.press("esc")

    def backspace(self):
        return self.press("backspace")

    def delete(self):
        return self.press("delete")

    # ---------------------------------------------------------
    # EDITING
    # ---------------------------------------------------------

    def select_all(self):
        return self.hotkey("ctrl", "a")

    def copy(self):
        return self.hotkey("ctrl", "c")

    def paste(self):
        return self.hotkey("ctrl", "v")

    def cut(self):
        return self.hotkey("ctrl", "x")

    def undo(self):
        return self.hotkey("ctrl", "z")

    def redo(self):
        return self.hotkey("ctrl", "y")

    def save(self):
        return self.hotkey("ctrl", "s")

    # ---------------------------------------------------------
    # WINDOWS
    # ---------------------------------------------------------

    def switch_window(self):
        return self.hotkey("alt", "tab")

    def show_desktop(self):
        return self.hotkey("win", "d")

    # ---------------------------------------------------------
    # WAIT
    # ---------------------------------------------------------

    def wait(self, seconds=1):

        try:

            seconds = float(seconds)

            if seconds < 0:
                seconds = 0

            time.sleep(seconds)

            print(
                f"[Keyboard] Waited : {seconds} seconds"
            )

            return True

        except Exception as error:

            print(
                f"[Keyboard] Wait failed : {error}"
            )

            return False