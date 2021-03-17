# ROI를 좌측 상단에 이미지가 나오게 하기
import cv2
import numpy as np

img = cv2.imread('data/image.jpg')
width = 1000
height = 1000

cropImage = img[400:400+height, 300:300+width]
img[0:height, 0:width] = cropImage

cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()