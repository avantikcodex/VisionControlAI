import pyautogui

pyautogui.FAILSAFE = True

screen_width, screen_height = pyautogui.size()

def move_mouse(x, y, frame_width, frame_height):

    screen_x = int((x / frame_width) * screen_width)
    screen_y = int((y / frame_height) * screen_height)

    pyautogui.moveTo(screen_x, screen_y)