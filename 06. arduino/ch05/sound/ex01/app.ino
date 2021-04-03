#include <MiniCom.h>

MiniCom com;
// 저항을 조절해서 Led2가 꺼지는 순간으로 만들기 (약 520)

void check() {
    int level = analogRead(A0);
    com.print_i(0, "Sound: ", level);
}

void setup() {
    com.init();
    com.setInterval(500, check);
}

void loop() {
    com.run();
}