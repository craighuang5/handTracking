import cv2
import mediapipe as mp

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands   # mp_hands is a module holding all functionalities we will use
hand = mp_hands.Hands()         # hand object

while True:                     # continuously get frames from webcam
    success, frame = cap.read()
    if success:
        RGB_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        result = hand.process(RGB_frame)
        if result.multi_hand_landmarks:
            for hand_landmarks in result.multi_hand_landmarks:
                print(hand_landmarks)
                mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
        cv2.imshow("capture image", frame)
        if cv2.waitKey(1) == ord('q'):
            break
cv2.destroyAllWindows()