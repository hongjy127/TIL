from picamera import PiCamera
import numpy as np
import time
from video import Video

# numpy 배열에 저장하기
with PiCamera() as camera:
    # camera.resolution = (320, 240)
    camera.resolution = (640, 480)
    camera.framerate = 30
    time.sleep(2)   # 카메라 예열시간

    # output = np.empty((240, 320, 3), dtype=np.uint8)
    output = np.empty((480, 640, 3), dtype=np.uint8)
    # camera.capture(output, 'bgr') # 사진
    
    while True:
        start_time = time.time()
        camera.capture(output, 'bgr', use_video_port=True)   # 동영상처럼
        if not Video.show(output): break
        end_time = time.time()
        fps = 1/(end_time-start_time)
        print(f'fps: {fps}')