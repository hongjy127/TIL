import cv2
import sys
import time

cascade_file = "haarcascade_frontalface_default.xml"
face_calssifier = cv2.CascadeClassifier(cascade_file)

cap = cv2.VideoCapture(0)

if cap.isOpened():
    print(f'width: {cap.get(3)}, height: {cap.get(4)}')
else:
    print("No camera")

while True:
    start_time = time.time()
    ret, frame = cap.read()
    if ret:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faces = face_calssifier.detectMultiScale(gray, 1.3, 5)
        for (x,y,w,h) in faces:
            cropped_face = frame[y:y+h, x:x+w].copy()
            cropped_face = cv2.resize(cropped_face, dsize = (300, 300), interpolation=cv2.INTER_AREA)
            cv2.rectangle(frame, (x,y), (x+w, y+h), (0,0,255), 3)

            cv2.imshow('face', cropped_face)
        cv2.imshow('video', frame)

        if cv2.waitKey(1) == 27: break
    else:
        print('error')

    end_time = time.time()
    fps = int(1/(end_time-start_time))
    print('fps: ', fps)

cap.release()
cv2.destroyAllWindows()