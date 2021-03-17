import cv2

image_file = 'data/image.jpg'
img = cv2.imread(image_file)

cv2.imwrite('data/image.bmp', img)
cv2.imwrite('data/image.png', img)
cv2.imwrite('data/image2.png', img, [cv2.IMWRITE_PNG_COMPRESSION, 9])
cv2.imwrite('data/image2.jpg', img, [cv2.IMWRITE_JPEG_QUALITY, 90])
