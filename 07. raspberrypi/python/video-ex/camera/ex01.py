import cv2

# 경로는 현재 워킹디렉토리 기준
image_file = 'data/image.jpg'
img = cv2.imread(image_file)
img2 = cv2.imread(image_file, cv2.IMREAD_GRAYSCALE)

print(img.shape, img2.shape)
print(img.dtype, img2.dtype)

cv2.imshow('Lena color', img)
cv2.imshow('Lena grayscale', img2)

cv2.waitKey(0)          # 키 입력 대기, 인자는 시간(ms), 0이면 무한 대기
cv2.destroyAllWindows() # 출력한 모든 창 닫기