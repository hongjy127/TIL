import cv2
import numpy as np

img = cv2.imread('data/image.jpg')
img[120, 200] = [255,0,0]
print(img[100:110, 200:210])    # ROI(Region of Interest) 접근

img[100:400, 200:300] = 0   # ROI 접근

cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()