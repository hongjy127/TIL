# Arduino



## 설치 / 환경설정

[Arduino - Home](https://www.arduino.cc/)



- arduino_debug.14j.ini

  C:\Program Files (x86)\Arduino

  arduino_debug.14j.ini 에

  -DDEBUG=false 추가

  (-Xms128M

  -Xmx512M

  -Dfile.encoding=UTF8

  -Djava.net.preferIPv4Stack=true

  -DDEBUG=false)

  

- 보드, 포트 설정

  툴>보드>

  툴>포트>

  

- 주의사항

  C:\Users\hongj\Documents\Arduino 에 저장됨

  하드웨어 변경시 usb 포트 꼭 분리

  소프트웨어 변경 시 연결되어도 가능

  컴파일 > 업로드 : 업로드에는 컴파일 포함, 에러가 나는걸 확인하기 위해 컴파일 먼저

  

- vscode

  vscode > 확장팩 > Arduino

  프로젝트 만들기

  F1>arduino:initialize

  시리얼포트 정해주기

  한 디렉토리에는 .ino 파일 하나만 존재해야함 -> arduino.json 에서 sketch 변경 -> 내가 컴파일할 작업(연습때마다 프로젝트를 하나씩 만들어 줄 수 없기 때문에)



## 문법



\# include <Arduino.h>

상수 정의 (OUTPUT, HIGH 등)



클래스



라이브러리화

C:\\Users\\hongj\\Documents\\Arduino\\libraries

여기에 .h , .cpp 파일 저장



led



Tact 스위치



void (*callback)();  // 콜백 함수(함수에 대한 포인터)

함수에 대한 포인터: 리턴타입(*함수)(매개변수)

class Button {

protected:

  void (*callback)(); 

public:

  void setCallback(void (*callback)());

}

void Button::setCallback(void (*callback)()) {

  this->callback = callback;

}





c++은 새로운 타입을 정할 수 있음

typedef void(*button_callback_t)();





int의 크기 : pc 4바이트

arduino

int : 2바이트, -32,000 ~ +32,000

long : 4바이트, -20억 ~ +20억

unsigned : 부호가 없음

unsigned long : 0 ~ +40억





Timer1

[GitHub - PaulStoffregen/TimerOne: TimerOne Library with optimization and expanded hardware support](https://github.com/PaulStoffregen/TimerOne)

Timer2

아두이노앱에서 툴>라이브러리관리>라이브러리 검색 후 설치

vscode에서 F1>arduino: Library Manager



Timer : 하드웨어 타이머

한개밖에 운영하지 못함 -> 두 개 이상 사용하려면 소프트웨어 타이머 사용

소프트웨어 타이머(다양한 라이브러리가 존재)

SimpleTimer : 소프트웨어 타이머





Serial : pc와 통신하는 객체





I2C : LCD의 주소



https://mikeyancey.com/hamcalc/lcd_characters.php

http://maxpromer.github.io/LCD-Character-Creator/



문자열 클래스

String









MQTT 사용

MQTT 설치

방화벽>인바운드 규칙 확인