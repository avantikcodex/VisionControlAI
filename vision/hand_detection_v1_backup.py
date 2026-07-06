import cv2
import mediapipe as mp
import time
from gestures.mouse_controller import move_mouse

vision_active = False

cap = cv2.VideoCapture(0)

mp_hands = mp.solutions.hands

hands = mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=1,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
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

            for id, lm in enumerate(hand_landmarks.landmark):

                cx = int(lm.x * w)
                cy = int(lm.y * h)

                lm_list.append((cx, cy))

            if len(lm_list) != 0:

                fingers = []

                # Thumb
                if lm_list[tip_ids[0]][0] > lm_list[tip_ids[0] - 1][0]:
                    fingers.append(1)
                else:
                    fingers.append(0)

                # Other Fingers
                for id in range(1, 5):

                    if lm_list[tip_ids[id]][1] < lm_list[tip_ids[id] - 2][1]:
                        fingers.append(1)
                    else:
                        fingers.append(0)

                finger_count = fingers.count(1)

                # Gesture Recognition
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

                # Activation System
                if gesture_name == "OPEN PALM":
                    vision_active = True

                elif gesture_name == "FIST":
                    vision_active = False

                # Mouse Control
                if vision_active and len(lm_list) > 8:

                    index_x = lm_list[8][0]
                    index_y = lm_list[8][1]

                    move_mouse(
                        index_x,
                        index_y,
                        w,
                        h
                    )

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
        f"Gesture: {gesture_name}",
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