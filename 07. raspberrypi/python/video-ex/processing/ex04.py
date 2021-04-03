# 모자이크
import cv2
import numpy as np

src = cv2.imread('data/image.jpg', cv2.IMREAD_GRAYSCALE)
dst = np.zeros(src.shape, dtype = src.dtype)

N = 100
height, width = src.shape
# height, width, _ = src.shape

h = height // N
w = width // N

for i in range(N):
    for j in range(N):
        y = i*h
        x = j*w
        roi = src[y:y+h, x:x+w]
        # print(cv2.mean(roi))
        dst[y:y+h, x:x+w] = cv2.mean(roi)[0]
        # dst[y:y+h, x:x+w] = cv2.mean(roi)[0:3] # 컬러

cv2.imshow('dst', dst)
cv2.waitKey()
cv2.destroyAllWindows()