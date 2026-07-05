vision_active = False

def process_gesture(gesture_name):

    global vision_active

    if gesture_name == "OPEN PALM":
        vision_active = True

    elif gesture_name == "FIST":
        vision_active = False

    return vision_active