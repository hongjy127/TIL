import cv2
import sys

cascade_file = "haarcascade_frontalface_alt.xml"
cascade = cv2.CascadeClassifier(cascade_file)

image_file = "data/face1.jpg"
out_file = "data/face1-mosaic.jpg"

image = cv2.imread(image_file)
image_gs = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

face_list = cascade.detectMultiScale(image_gs, scaleFactor=1.1,
                                minNeighbors=1, minSize=(100,100))

if len(face_list) == 0:
    print("no face")
    quit()

mosaic_rate = 30
print(face_list)
color = (0,0,255)

for face in face_list:
    x,y,w,h = face
    face_img = image[y:y+h, x:x+w]
    face_img = cv2.resize(face_img, (w//mosaic_rate, h//mosaic_rate))
    face_img = cv2.resize(face_img, (w, h), interpolation=cv2.INTER_AREA)
    image[y:y+h, x:x+w] = face_img
    
cv2.imwrite(out_file, image)
cv2.imshow('face1-mosaic.jpg', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
