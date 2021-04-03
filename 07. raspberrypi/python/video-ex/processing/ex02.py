import cv2
import numpy as np

img = cv2.imread('data/image.jpg', cv2.IMREAD_GRAYSCALE)
img[120, 200] = 0
# print(img[100:110, 200:210])    # ROI(Region of Interest) 접근
cropImage = img[100:110, 200:210]   # 원본 데이터 공유
# cropImage = img[100:110, 200:210].copy() # 복사본을 생성
print(cropImage)

# img[100:400, 200:300] = 0   # ROI 접근
cropImage[:,:] = 100    # 이렇게 하면 img도 바뀜(참조를 가짐)
print(cropImage)

cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()