def recognize_gesture(finger_count):

    if finger_count == 0:
        return "FIST"

    elif finger_count == 1:
        return "ONE"

    elif finger_count == 2:
        return "VICTORY"

    elif finger_count == 3:
        return "THREE"

    elif finger_count == 4:
        return "FOUR"

    elif finger_count == 5:
        return "OPEN PALM"

    return "UNKNOWN"