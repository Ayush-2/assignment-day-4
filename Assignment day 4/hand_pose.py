import cv2
import mediapipe as mp
#drawing utility
mp_drawing = mp.solutions.drawing_utils
# Hand pose
mp_hands = mp.solutions.hands

#model hand pose
model_hand_pose= mp_hands.Hands()

cap = cv2.VideoCapture(0)

while cap.isOpened():
    flag, frame = cap.read()
    if not flag:
        print("Could not access the camera.")
        break



    results=model_hand_pose.process(frame)
    if results.multi_hand_landmarks:
      for hand_landmarks in results.multi_hand_landmarks:
        mp_drawing.draw_landmarks(
            frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)




    cv2.imshow('Frame', frame)
    if cv2.waitKey(10) & 0xff == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()