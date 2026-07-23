import cv2
import mediapipe as mp
import time
from gestures.mouse_controller import move_mouse, left_click, right_click
vision_active = False

stable_gesture = "UNKNOWN"
last_gesture = "UNKNOWN"
gesture_start_time = time.time()

cap = cv2.VideoCapture(0)

mp_hands = mp.solutions.hands

hands = mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=2,
    min_detection_confidence=0.45,
    min_tracking_confidence=0.45
)

mp_draw = mp.solutions.drawing_utils

tip_ids = [4, 8, 12, 16, 20]

prev_time = 0

while True:

    success, frame = cap.read()

    if not success:
        break

    frame = cv2.resize(frame, (640, 480))
    frame = cv2.flip(frame, 1)

    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    results = hands.process(rgb_frame)

    finger_count = 0
    gesture_name = "UNKNOWN"

    if results.multi_hand_landmarks:

        for hand_landmarks in results.multi_hand_landmarks:

            mp_draw.draw_landmarks(
                frame,
                hand_landmarks,
                mp_hands.HAND_CONNECTIONS
            )

            lm_list = []

            h, w, c = frame.shape

            for landmark_id, lm in enumerate(hand_landmarks.landmark):

                cx = int(lm.x * w)
                cy = int(lm.y * h)

                lm_list.append((cx, cy))

            if len(lm_list) != 0:

                fingers = []

                if lm_list[4][0] > lm_list[3][0]:
                    fingers.append(1)
                else:
                    fingers.append(0)

                for finger_id in range(1, 5):

                    if lm_list[tip_ids[finger_id]][1] < lm_list[tip_ids[finger_id] - 2][1]:
                        fingers.append(1)
                    else:
                        fingers.append(0)

                finger_count = fingers.count(1)

                if finger_count == 0:
                    gesture_name = "FIST"
                elif finger_count == 1:
                    gesture_name = "ONE"
                elif finger_count == 2:
                    gesture_name = "VICTORY"
                elif finger_count == 3:
                    gesture_name = "THREE"
                elif finger_count == 4:
                    gesture_name = "FOUR"
                elif finger_count == 5:
                    gesture_name = "OPEN PALM"

                current_time = time.time()

                if gesture_name != last_gesture:
                    last_gesture = gesture_name
                    gesture_start_time = current_time

                if current_time - gesture_start_time > 0.8:

                    stable_gesture = gesture_name

                    if stable_gesture == "OPEN PALM":
                        vision_active = True

                    elif stable_gesture == "FIST":
                        vision_active = False

                if vision_active and len(lm_list) > 8:

                    index_x = lm_list[8][0]
                    index_y = lm_list[8][1]

                    move_mouse(
                        index_x,
                        index_y,
                        w,
                        h
                    )

                if vision_active and stable_gesture == "VICTORY":
                    print("LEFT CLICK DETECTED")
                    left_click()
                if vision_active and stable_gesture == "THREE": 
                    print("RIGHT CLICK DETECTED")
                    right_click()

    current_time = time.time()

    fps = 1 / (current_time - prev_time) if prev_time else 0

    prev_time = current_time

    status_text = "ACTIVE" if vision_active else "PAUSED"

    cv2.putText(
        frame,
        f"FPS: {int(fps)}",
        (10, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 255, 0),
        2
    )

    cv2.putText(
        frame,
        f"Fingers: {finger_count}",
        (10, 80),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 255, 0),
        2
    )

    cv2.putText(
        frame,
        f"Gesture: {stable_gesture}",
        (10, 120),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 255, 255),
        2
    )

    cv2.putText(
        frame,
        f"STATUS: {status_text}",
        (10, 160),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 255, 0) if vision_active else (0, 0, 255),
        2
    )

    cv2.imshow("VisionControlAI Mouse Control", frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()