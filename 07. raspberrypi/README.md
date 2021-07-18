# Raspberrypi



## 설치

[Raspberry Pi OS – Raspberry Pi](https://www.raspberrypi.org/software/)

**원격 접속**

[Download PuTTY - a free SSH and telnet client for Windows](https://www.putty.org/)

[Download VNC Viewer for Windows | VNC® Connect (realvnc.com)](https://www.realvnc.com/en/connect/download/viewer/windows/)



**HDMI, 키보드, 마우스 없을 때**

SD카드 > 파일준비(라즈베리파이로 옮기면 없어짐)

- ssh
- wpa_aupplicant.conf

```
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1
country=GB
network={
ssid="무선네트워크SSID"
psk="패스워드"
}
```

(키보드, 마우스 연결 못하면 원격으로 접속해서 명령 입력)

**putty 접속**

IP address(접속할 서버 IP-라즈베리파이), Saved Sessions

(window10에서는 cmd창에서 접속 가능)

```
> ssh pi@172.30.1.57
```



**VNC 접속**

Username: pi, Password: 라즈베리파이 비밀번호



**라즈베리파이 초기화**

영어설정 그대로(한글폰트 다운받고 나중에 바꿔야 안깨짐)

 메뉴 > Preference > Raspverry Pi Configuration > SSH, VNC-Enable

(기본 설정 Hostname: pi, password: raspberry)

```
// 패키지 업데이트, 주기적으로 해주기
$ sudo apt update
$ sudo apt upgrade
```

```
// 무선 마우스 반응 속도
$ sudo nano /boot/cmdline.txt

// 라인 끝에
usbhid.mousepoll=0
```

```
$ sudo apt-get install fonts-unfonts-core
$ sudo apt-get install nabi im-config
$ sudo reboot
```

 메뉴 > Preference(설정) > Input Method(입력기) > hangul > OK > 재기동

메뉴 > Preference > Raspverry Pi Configuration

​	Locale, Timezone 바꾸기, Wifi Country는 바꾸면 안됨



**Samba**

```
$ sudo apt install samba samba-common-bin
```

```
$ sudo smbpasswd -a pi
// password는 라즈베리파이 비밀번호
```

```
$ sudo nano /etc/samba/smb.conf
// 나오는 창 맨 끝에 아래 입력
[pi]
   comment = pi shared folder
   path = /home/pi
   valid users = pi
   browseable = yes
   guest ok = no
   read only = no
   create mask = 0777
   
// 재시작
$ sudo service smbd restart
```

\\\라즈베리파이 IP주소 > id, pw > 네트워크 드라이브 연결



**Python3 설정**

확인

```
$ cd usr/bin
$ ls python*
$ ls pip*
```

기본은 python3로 만들기

```
$ sudo ln -sf python3.7 python
$ sudo ln -sf python3.7-config python3-config
$ sudo cp pip3 pip
```



**sudo: hongpi 호스트를 해석할 수 없습니다: 이름 혹은 서비스를 알 수 없습니다**

```
$ cd/etc
$ sudo nano hosts
```

\> 127.0.0.1, _없애기



**mosqutto 설치**

```
$ sudo apt install mosquitto mosquitto-clients
```

제어

```
$ sudo systemctl start|stop|restart|status mosquitto
```

 부팅시 자동 실행 설정

```
$ sudo systemctl enable mosquitto
```



**mosquitto.conf** 

```
$ cd /etc/mosquitto
$ sudo nano /mosquitto.conf
```

추가

```
bind_address 0.0.0.0
allow_anonymous true
```





## 리눅스 기초

- 현재 날짜

```
$ date
$ sudo date -s "2021-03-09- 09:00:00"
```

- hostname

```
$ hostname
```

- ls

```
$ ls
$ ls /etc
$ ls -l		// l: long format
$ ls -la	// a: all(hidden file도 보여주기)
```

- password

```
$ passwd
// 설정 들어가서 바꾸는게 더 편함
```

- /home/<사용자 id>

```
$ cd	// home으로 이동할 때 자주 사용
$ cd ~	// home 하위로 이동할 때 자주 사용
```

- print working directory

```
$ pwd
```

- directory

```
$ mkdir test	// make directory
$ rmdir test	// remove directory (모든 파일이 지워져있을 때 사용 가능)
$ rm test	// 파일, directory 다 지움
$ rm -rf test	// 서브 directory까지 물어보지말고 다 지워라
```

- touch: 파일접근시간을 현재시간으로 수정, 존재하지 않으면 새로 생성

```
$ touch test
```

- cat: 짧은 파일내용 확인

```
$ cat	// 입력한 내용을 출력, Ctrl+D로 끝냄
$ cat 파일명	// 파일을 출력
$ cat > a.txt	// 표준출력장치를 a.txt로 바꿔라
$ cat 파일명1 파일명2	// 여러 파일을 연속해서 출력
$ cat a.txt b.txt > c.txt	// 내용이 c.txt로 저장(기존내용 버림)
$ cat a.txt b.txt >> c.txt	// 기존 내용 뒤에 붙여서 저장
```

- head/tail

```
$ head .bashrc
$ head -5 bashrc
$ tail .bashrc
$ tail -5 bashrc
```

- copy/move

```
$ cp <복사할 대상> <복사할 위치>
$ mv <파일명> <이동할 위치>
$ mv <파일명> <새로운 파일명>	// 파일 이름 바꾸기
```

```
$ which python3	// 명령어의 위치를 찾아줌
```

- 권한
  - 소유자(owner), 그룹(group), 다른사람(other)에 대해서 지정
  - 읽기(r), 쓰기(w), 실행(x), 권한없음(-)으로 구성
  - ex) rw-r--r--

```
$ ln -s <원본> <파일명>	// 심벌릭 링크 만들기
$ ln -s /usr/bin/python3.7 python
```

```
$ cat group	// 그룹 보기
$ cat group | grep pi
```

- chmod: 파일 권한 변경

```
$ chmod <수정번호-8진수> <파일>
$ chmod g+w a.txt	// u:소유자(생략가능), g:그룹, o:other
					// a: all
					// +권한 추가, -권한 제거
```

- IO 리다이렉션
  - \>, \>>
  - 2>, 2>>: 에러 출력

- 아카이브/압축

```
$ tar -cvf a.tar a
$ tar -xvf a.tar

$ tar -zcvf a.tar.gz a
$ tar -zxvf a.tar.gz
```





## Raspberrypi

vscode 확장팩 > Remote - SSH

새로운 환경이라 확장팩 새로 설치해줘야함

(Code Runner)



라즈베리파이에 vscode 설치 > .deb ARM

메뉴 > 개발 > vscode 또는 터미널 > 디렉토리 > `$ code .`



원격창열기 > Connect to Host... > ssh pi@hongpi > .ssh/config > Linux > 비밀번호 > 원격 연결 성공!



**실행**

- 원래는 `$ python led_ex.py`

- 2

  `$ chmod a+x led_ex.py`

  파일 첫줄에 `#!/usr/bin/python` 넣기

  LF

  `$ ./led_ex.py`

- Code Runner로 실행



---



RPi.GPIO 모듈: 라즈베리파이에만 있음.



**SPI 통신**

메뉴 > Preference > Raspverry Pi Configuration > Interfaces > SPI-Enable

```
$ cd ~
$ mkdir libs
$ cd libs
$ git clone git://github.com/doceme/py-spidev
$ cd py-spidev
$ sudo python3 setup.py install
```



**GPIO-ZERO**

[gpiozero — Gpiozero 1.5.1 Documentation](https://gpiozero.readthedocs.io/en/stable/)

```
$ sudo apt update	// 혹시 업데이트 될까봐
$ sudo apt install python3-gpiozero
```

- 서보모터 지터링 방지

```
1. 라이브러리 설치

$ wget https://github.com/joan2937/pigpio/archive/master.zip
$ unzip master.zip
$ cd pigpio-master
$ make
$ sudo make install

2. 운영

사용전 서버 데몬 기동 필요
$ sudo pigpiod

정지
$ sudo killall pigpiod


3. 프로그램
import pigpio

SERVO = 21 
pi = pigpio.pi() 

pi.set_servo_pulsewidth(SERVO, 500)    # 서보모터 0도
pi.set_servo_pulsewidth(SERVO, 1500)     # 서보모터 90도
pi.set_servo_pulsewidth(SERVO, 2500)    # 서보모터 180도

cf) 각도를 입력으로 하는 경우

서보모터의 전체 각도를 다 사용하는 경우

f`(x) = 500+ 11.11x     --> 모터에 무리를 줄 수 있음

f`(x) = 600+ 10x    --> 약간의 여분을 주는 경우

-90 ~ 90도 각도 값으로 제어하는 경우 

pulse_width = 500 + 11.11*(value+90)
pi.set_servo_pulsewidth(SERVO, pulse_width)
```





---

라즈베리파이는 제어가 메인이 아님. 제어는 아두이노에서

라즈베리파이는 영상과 오디오 처리 위주
