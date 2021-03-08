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

IP address, Saved Sessions

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

\\\IP주소 > 네트워크 드라이브 연결





## Raspberrypi

