import cv2
eye_cascade = cv2.CascadeClassifier('haarcascade_eye (3).xml')
cap = cv2.VideoCapture(0)
while True:
    # Read the frame
    _, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Detect the faces
    eyes = eye_cascade.detectMultiScale(gray, 1.1, 4)
    # Draw the rectangle around face
    for (x, y, w, h) in eyes:
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 0), 5)
        # display
    cv2.imshow('img', img)
    # stop if escape key is pressed
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
    # Release the VideoCapture object
cap.release()
