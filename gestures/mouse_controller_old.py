import pyautogui
import time

pyautogui.FAILSAFE = True

screen_width, screen_height = pyautogui.size()

last_click_time = 0
last_right_click_time = 0

def move_mouse(x, y, frame_width, frame_height):

    screen_x = int((x / frame_width) * screen_width)
    screen_y = int((y / frame_height) * screen_height)

    pyautogui.moveTo(screen_x, screen_y)

def left_click():

    global last_click_time

    current_time = time.time()

    if current_time - last_click_time > 1:

        pyautogui.click()

        last_click_time = current_time

def right_click():

    global last_right_click_time

    current_time = time.time()

    if current_time - last_right_click_time > 1:

        pyautogui.rightClick()

        last_right_click_time = current_time