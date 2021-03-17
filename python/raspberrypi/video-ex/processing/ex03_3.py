# ROI를 좌측 상단에 이미지가 나오게 하기
import cv2
import numpy as np

img = cv2.imread('data/image.jpg')
print(img.shape)
# 773
x = 100
width = 580
# 579
y = 50
height = 500

# cropImage = img[y:y+height, x:x+width]
# img[0:height, 0:width] = cropImage

pt1 = x, y
pt2 = x+width, y+height
cv2.rectangle(img, pt1, pt2, (0,255,0), 2)

cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()