// 연습 문제
// 자동 점멸 이동
// 버튼을 누를 때마다 지연 시간에 변경을 줌
// 200 ms -> 400 ms -> 600 ms -> 800 ms -> 200 ms

#include <Led.h>
#include <Button.h>

Button btn(3);
Led leds[4] {
    Led(8),
    Led(9),
    Led(10),
    Led(11)
};

int current = 0;
int intervals[4] {200,400,600,800};
int intervalIx = 0;

void flash() {
    if(!btn.debounce()) return;
    intervalIx = (intervalIx+1) % 4;
}

void blink() {
    for(int i=0; i<4; i++) {
        if(i==current) {
            leds[i].on();
        } else {
            leds[i].off();
        }
    }
    current = (current+1) % 4;
}

void setup() {
    btn.attachInterrupt(flash, FALLING);
}

void loop() {
    blink();
    // delay(intervals[intervalIx]);
}