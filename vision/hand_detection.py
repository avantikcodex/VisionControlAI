import cv2
import mediapipe as mp
import time

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

    current_time = time.time()

    fps = 1 / (current_time - prev_time) if prev_time else 0

    prev_time = current_time

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
        f"FPS: {int(fps)}",
        (10, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 255, 0),
        2
    )

    cv2.imshow("VisionControlAI Finger Counter", frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()