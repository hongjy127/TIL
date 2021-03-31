# Python

## 설치

- jupyter notebook

conda 설치하면 알아서 jupyter notebook 설치

cmd > `jupyter notebook`



- 실행권한

#!usr/bin/python

chmod a+x test.py

LF로 바꿔주기

./test.py하면 실행됨



- OpenCV 설치

**윈도우**

`pip install opencv-python`

**라즈베리파이에 설치**(OpenCV version 4.5)

```
sudo apt-get install -y libjpeg-dev libtiff5-dev libjasper-dev libpng12-dev
sudo apt-get install -y libavcodec-dev libavformat-dev libswscale-dev libxvidcore-dev libx264-dev libxine2-dev
sudo apt-get install -y libv4l-dev v4l-utils
sudo apt-get install -y libgstreamer1.0-dev libgstreamer-plugins-base1.0-dev
sudo apt-get install -y libgtk2.0-dev
sudo apt-get install -y mesa-utils libgl1-mesa-dri libgtkgl2.0-dev libgtkglext1-dev
sudo apt-get install -y libatlas-base-dev gfortran libeigen3-dev

pip install opencv-python
```



Haar Cascade

C:\Users\hongj\Anaconda3\envs\iot-ex\Lib\site-packages\cv2\data



- NumPy, Matplotlib 설치

`pip install numpy matplotlib`



- 파일 넘기기

  - pc -> raspberrypi 파일 넘기기

    vscode: 소스 끌어다놓기

    samba

  - raspberrypi -> pc 파일 넘기기

    samba



**raspberrypi에서 클래스 사용**

```
$ cd ~
$ mkdir PYTHON_LIB
// 여기에 samba 이용해서 파일 옮기기
```

환경변수 잡기

.profile > 맨 마지막줄에 `export PYTHONPATH=/home/pi/PYTHON_LIB` 추가

```
$ source .profile
$ echo $PYTHONPATH
확인하기
```



## Numpy

np.array()

.dtype

.shape

np.arange()

np.linspace()

np.zeros(n)

np.zeros((m,n))

np.ones(n)

np.ones((m,n))

np.eye(n)

np.astype(타입)

### 인덱싱과 슬라이싱





## OpenCV

### camera

import cv2

cv2.imread(filenamd [,flags])

cv2.imwrite



cv2.VideoCapture()





### graphic





### processing





### facedetect





### streaming





## PiCamera

메뉴 > Raspberry Pi Configuration > Interfaces > Camera-Enable



raspistill / raspivid

```
// 동작 확인
$ raspistill -v -o test.jpg
-t	ms 단위 촬영 시간
-tl 촬영 간격
-w -h	폭, 높이
-br	밝기
-hf / -vf

$ raspivid -o video.h264
```



```
$ nano camera.sh

#!/bin/bash
DATE=$(date+"%Y-%m-%d_%H%M")
raspistill -o /home/pi/picamera/$DATE.jpg
// 촬영 날짜를 이미지 이름으로 저장

$ chmod +x camera.sh
$ ./camera.sh
```

cron: 명령을 반복 실행 할 때

```
$ sudo crontab -e

* * * * * /home/pi/work/camera.sh 2> /home/pi/work/err.log
// 매 분마다 camera.sh 실행
```



### python-picamera

라이브러리는 디폴트로 설치되어있음

만약 설치해야하면

```
$ sudo apt-get install python-picamera
```

```python
from picamera import PiCamera

camera = PiCamera()
# close 필요 -- with문과 같이 사용

.rotation = 180
.vflip=True

.resolution

.capture

.start_preview()
.stop_preview()

.start_recoding()
.stop_recoding()
```

텍스트 설정



## pyAudio

### 윈도우

```
$ conda install pyaudio
```

### 라즈베리파이

```
$ pip install pyaudio
$ sudo apt-get install libportaudio2
```

```
$ python select_mic.py 2> /dev/null
표준 출력만 나옴
```





### pydub

#### 윈도우 설치

[ffmpeg 설치](https://www.ffmpeg.org/download.html#build-windows)

C:\ffmpeg 에 다운

C:\ffmpeg\bin을 PATH에 추가

```
$ pip install pydub
$ pip install ffmpeg-python
```

#### 리눅스 설치 

```
$ sudo apt install ffmpeg
```

```
$ pip install pydub
$ pip install ffmpeg-python
```



### sounddevice

https://python-sounddevice.readthedocs.io/en/0.4.1/#

녹음파일을 쉽게 준비

```
$ pip install sounddevice
$ pip install soundfile

설치되었는지 확인
$ python -m sounddevice
```



## Object Detection

### 설치환경

#### 윈도우

[3.1.0 버전 다운](https://github.com/protocolbuffers/protobuf/releases/tag/v3.1.0) -> c:\workspace\protoc-3.1.0-win32

**PATH 환경 변수 추가** -> c:\workspace\protoc-3.1.0-win32\bin

```
$ pip install tensorflow
$ pip install tf_slim
$ pip install IPython
$ pip install matplotlib pillow
```

```
$ pip install cython
$ pip install "git+https://github.com/philferriere/cocoapi.git#egg=pycocotools&subdirectory=PythonAPI"
$ pip install pycocotools
```

**c:\workspace\tf 에서 설치**

```
git clone https://github.com/tensorflow/models
```

 **PYTHONPATH 환경변수 등록**

c:\python_lib

c:\workspace\tf\models\research

c:\workspace\tf\models\research\slim

**Object Detection API 설치**

research\object_detection\packages\tf2\setup.py를 research\setup.py로 복사

c:\workspace\tf\models\research

```
// 명령창
$ protoc object_detection/protos/*.proto --python_out=.
```

```
$ python setup.py build
$ pip install .
```

#### 라즈베리파이

**mjpeg-streamer 설치**

```
$ sudo apt-get update
$ sudo apt-get upgrade
$ sudo apt-get install libjpeg8-dev imagemagick libv4l-dev
$ sudo ln -s /usr/include/linux/videodev2.h/usr/include/linux/videodev.h
$ sudo apt-get install cmake
$ git clone https://github.com/jacksonliam/mjpg-streamer.git
$ cd mjpg-streamer/mjpg-streamer-experimental
$ make
$ sudo make install
```

실행

```
mjpg_streamer -i "input_raspicam.so -vf" -o "output_http.so -p 8090 -w /usr/local/share/mjpg-streamer/www/"
```

 정지영상

http://ip주소:포트번호?action=snapshot

http://172.30.1.57:8090/?action=snapshot

동영상

http://ip주소:포트번호?action=stream

http://172.30.1.57:8090/?action=stream



**motion 설치**

```
$ sudo apt-get install motion
```

```
$ sudo nano /etc/motion/motion.conf

'daemon': on
'framerate': 10
'Stream_port': 8081
'Stream_quality': 100
'Stream_localhost': off
'webcontrol_localhost': off
'quality': 640
'height': 480 'post_capture': 5
```

```
$ sudo nano /etc/default/motion

'start_motion_daemon': yes
```

실행

```
$ sudo service motion restart
$ sudo motion
```

http://hongpi:8081/



**Motion JPEG**

.bashrc 파일에서

export PATH=.:$PATH:/home/pi/.local/bin 추가

(.은 현재 디렉토리, :는 환경변수 구분)

`source ~/.bashrc` 실행

(.profile은 로그인 쉘 - 로그인 해서 들어온 쉘만 적용, 로그인을 다시 해야 적용

.bashrc는 모든 쉘에서 적용, 새로운 터미널 열면 즉시 반영)



```
$ pip install django
$ where is django-admin	// 어디있는지 확인(안나오면 환경변수 적용 안된거)
$ django-admin startproject mysite
$ mv mysite iot
$ cd iot
$ python manage.py startapp mjpeg
```

python manage.py runserver 0.0.0.0:8000



**tensorflow 설치**

```
$ sudo apt-get update
$ sudo apt-get upgrade

$ sudo apt install gfortran libopenblas-dev liblapack-dev libhdf5-dev
$ sudo pip install --upgrade numpy

// 그냥 설치하면 tensorflow 1버전 설치됨
$ wget https://github.com/lhelontra/tensorflow-on-arm/releases/download/v2.2.0/tensorflow-2.2.0-cp37-none-linux_armv7l.whl
$ sudo pip install tensorflow-2.2.0-cp37-none-linux_armv7l.whl

$ python

>>> import tensorflow as tf
>>> tf.__version__
```



**블루투스**

```
$ sudo apt-get install bluetooth blueman bluez
$ sudo reboot
$ sudo apt-get install python-bluetooth
$ pip install pybluez
```

블루투스 페어링(처음에 주소 복사할 때만 사용)

```
$ hciconfig 	// 블루투스 주소 확인
$ sudo bluetoothctl	// 명령어로 페어링
[bluetooth]# scan on	// 장치 목록 보여줌
[bluetooth]# scan off	// 장치 찾으면 중지

[bluetooth]# default-agent
[bluetooth]# pair 주소

// 페어링 되면 
[bluetooth]# trust 주소
[bluetooth]# exit
```

