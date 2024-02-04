import cv2
import mediapipe as mp
hand_detect1 = mp.solutions.hands
hand_detect = hand_detect1.Hands()

draw_utits = mp.solutions.drawing_utils
cap = cv2.VideoCapture(0)
fingerTips = [4, 8, 12, 16, 20]
while True:
    _, frame = cap.read()
    f_h, f_w, _= frame.shape
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    output = hand_detect.process(rgb_frame)
    hands = output.multi_hand_landmarks
    lmlist = []
    fingers = []
    if hands:
        for hand in hands:
            draw_utits.draw_landmarks(frame, hand, hand_detect1.HAND_CONNECTIONS)
            landmarks = hand.landmark
            for id, landmark in enumerate(landmarks):
                x = int(landmark.x*f_w)
                y = int(landmark.y*f_h)
                lmlist.append([id, x, y])

    if len(lmlist) != 0:
        if lmlist[fingerTips[0]][1]< lmlist[fingerTips[0]-1][1]:
            fingers.append(1)
        else:
            fingers.append(0)

        for id in range(1, 5):
            if lmlist[fingerTips[id]][2] < lmlist[fingerTips[id]-2][2]:
                fingers.append(1)
            else:
                fingers.append(0)

        total = fingers.count(1)
        print(total)
        cv2.putText(frame, f'finger_count{total}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 5)
    cv2.imshow("frame", frame)
    cv2.waitKey(1)



