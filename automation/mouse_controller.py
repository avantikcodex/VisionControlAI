import time

import pyautogui


class MouseController:

    def __init__(self):

        pyautogui.PAUSE = 0.05

    # ---------------------------------------------------------
    # MOVE
    # ---------------------------------------------------------

    def move(self, x, y, duration=0.2):

        try:

            x = int(x)
            y = int(y)
            duration = float(duration)

            if duration < 0:
                duration = 0

            pyautogui.moveTo(
                x,
                y,
                duration=duration
            )

            print(
                f"[Mouse] Moved : ({x}, {y})"
            )

            return True

        except Exception as error:

            print(
                f"[Mouse] Move failed : {error}"
            )

            return False

    # ---------------------------------------------------------
    # CLICK
    # ---------------------------------------------------------

    def click(self, x=None, y=None):

        try:

            if x is not None and y is not None:

                self.move(x, y)

            pyautogui.click()

            print("[Mouse] Left Click")

            return True

        except Exception as error:

            print(
                f"[Mouse] Click failed : {error}"
            )

            return False

    def right_click(self, x=None, y=None):

        try:

            if x is not None and y is not None:

                self.move(x, y)

            pyautogui.rightClick()

            print("[Mouse] Right Click")

            return True

        except Exception as error:

            print(
                f"[Mouse] Right click failed : {error}"
            )

            return False

    def double_click(self, x=None, y=None):

        try:

            if x is not None and y is not None:

                self.move(x, y)

            pyautogui.doubleClick()

            print("[Mouse] Double Click")

            return True

        except Exception as error:

            print(
                f"[Mouse] Double click failed : {error}"
            )

            return False

    def middle_click(self, x=None, y=None):

        try:

            if x is not None and y is not None:

                self.move(x, y)

            pyautogui.click(button="middle")

            print("[Mouse] Middle Click")

            return True

        except Exception as error:

            print(
                f"[Mouse] Middle click failed : {error}"
            )

            return False

    # ---------------------------------------------------------
    # BUTTON CONTROL
    # ---------------------------------------------------------

    def mouse_down(self, button="left"):

        try:

            pyautogui.mouseDown(button=button)

            print(
                f"[Mouse] Button Down : {button}"
            )

            return True

        except Exception as error:

            print(
                f"[Mouse] Mouse down failed : {error}"
            )

            return False

    def mouse_up(self, button="left"):

        try:

            pyautogui.mouseUp(button=button)

            print(
                f"[Mouse] Button Up : {button}"
            )

            return True

        except Exception as error:

            print(
                f"[Mouse] Mouse up failed : {error}"
            )

            return False

    # ---------------------------------------------------------
    # SCROLL
    # ---------------------------------------------------------

    def scroll_up(self, amount=5):

        try:

            amount = int(amount)

            if amount < 0:
                amount = abs(amount)

            pyautogui.scroll(amount)

            print(
                f"[Mouse] Scroll Up : {amount}"
            )

            return True

        except Exception as error:

            print(
                f"[Mouse] Scroll up failed : {error}"
            )

            return False

    def scroll_down(self, amount=5):

        try:

            amount = int(amount)

            if amount < 0:
                amount = abs(amount)

            pyautogui.scroll(-amount)

            print(
                f"[Mouse] Scroll Down : {amount}"
            )

            return True

        except Exception as error:

            print(
                f"[Mouse] Scroll down failed : {error}"
            )

            return False

    # ---------------------------------------------------------
    # POSITION
    # ---------------------------------------------------------

    def position(self):

        try:

            point = pyautogui.position()

            print(
                f"[Mouse] Position : ({point.x}, {point.y})"
            )

            return point.x, point.y

        except Exception as error:

            print(
                f"[Mouse] Position failed : {error}"
            )

            return None

    # ---------------------------------------------------------
    # SCREEN SIZE
    # ---------------------------------------------------------

    def screen_size(self):

        try:

            width, height = pyautogui.size()

            print(
                f"[Mouse] Screen : {width}x{height}"
            )

            return width, height

        except Exception as error:

            print(
                f"[Mouse] Screen size failed : {error}"
            )

            return None

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
                f"[Mouse] Waited : {seconds} seconds"
            )

            return True

        except Exception as error:

            print(
                f"[Mouse] Wait failed : {error}"
            )

            return False