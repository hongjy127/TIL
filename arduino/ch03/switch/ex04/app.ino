#include <Led.h>
#include <Button.h>

Led led(8);
Button btn(4);

// 함수의 이름은 함수의 시작 주소
void work() {
    led.toggle();
}

void setup() {
    btn.setCallback(work);
}

void loop() {
    btn.check();
}