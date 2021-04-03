import cv2

# 기존 노트북 카메라가 0번
# cap = cv2.VideoCapture(1) # 1번 카메라
# cap = cv2.VideoCapture('http://172.30.1.49:4747/video')   # ip 카메라
# cap = cv2.VideoCapture('http://172.30.1.26:4747/video')
cap = cv2.VideoCapture('http://hongpi:8000/mjpeg/stream')
# cap = cv2.VideoCapture('data/vtest.avi')  # 동영상 파일

# cap.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
# cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)

frame_size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),
            int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
print('frame_size = ', frame_size)

while True:
    retval, frame = cap.read()  # 동영상 프레임 하나
    # retval: true(성공) / false(실패)
    if not retval: break

    # 이미지(frame) 처리 -- 주로 AI와 연계

    cv2.imshow('frame', frame)
    key = cv2.waitKey(1)   # 1000/25 --> 최대 40 fps
    # 종료버튼 안되니 꼭 넣어줘야함
    if key == 27: break     # 27: esc
if cap.isOpened():
    cap.release()

cv2.destroyAllWindows()