// 2개의 색상은 255로 고정
// 나머지 1개의 색상은 0.2초 간격으로 그라데이션 효과 줌
// 0 -> 5 -> 10 -> ... -> 255 -> 0 -> 5
// 버튼을 누른 경우
// 그라데이션 효과주는 색상 변경
// r -> g -> b

#include <Button.h>
#include <ColorLed.h>
#include <SimpleTimer.h>

Button btn(3);
ColorLed cled(9, 10, 11);
SimpleTimer timer;

int color = 0;
int value = 0;

void gradation() {
    value = (value + 5) % 255;
    switch(color) {
        case 0:
            cled.rgb(value, 255, 255);
            break;
        case 1:
            cled.rgb(255, value, 255);
            break;
        case 2:
            cled.rgb(255, 255, value);
            break;
    }
}

void changeColor() {
    color = (color + 1) % 3;
    value = 0;
}

void setup() {
    timer.setInterval(200, gradation);
    btn.attachInterrupt(changeColor, FALLING);
}

void loop() {
    timer.run();
}