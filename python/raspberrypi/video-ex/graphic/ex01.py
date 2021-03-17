import cv2
import numpy as np

# White 배경 색상
img = np.zeros(shape=(512,512,3), dtype=np.uint8) + 255
# img = np.ones(shape=(512,512,3), dtype=np.uint8) * 255
# img = np.full(shape=(512,512,3), (255,255,255), dtype=np.uint8)

pt1 = 100, 100
pt2 = 400, 400
cv2.rectangle(img, pt1, pt2, (0,255,0), 2)      # Green

cv2.line(img, (0,0), (500,0), (255,0,0), 5)     # Blue
# cv2.line(img, (0,0), (0,500), (0,0,255), 5)   # Red
# open cv에서는 color: (Blue, Green, Red)
# 다른 라이브러리는 (Red, Green, Blue)임

cv2.imshow('img', img)
cv2.waitKey()
cv2.destroyAllWindows()