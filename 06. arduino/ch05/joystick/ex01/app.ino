#include <MiniCom.h>
#include <Led.h>
#include <Button.h>

// 조이스틱의 x, y값을 읽어 LCD 출력
MiniCom com;
Led led(8);
Button btn(A2);

void check() {
    // 평상시 0, 최대 -255, +255 사이의 값을 가지도록 해석
    int x = analogRead(A1);
    int y = analogRead(A0);
    x = map(x, 0, 1023, -255, 255);
    y = map(y, 0, 1023, 255, -255);
    com.print_i(0, "X: ", x, "Y: ", y);
}

void blink() {
    // if(!btn.debounce()) return;
    led.toggle();
}

void setup() {
    com.init();
    com.setInterval(100, check);
    // btn.attachInterrupt(blink, FALLING);    // 하드웨어 지원 필요... uno: D2, D3만 가능
    btn.setCallback(blink);
}

void loop() {
    com.run();
    btn.check();
}