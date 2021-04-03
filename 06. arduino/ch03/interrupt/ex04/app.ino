#include <Led.h>
#include <Button.h>

Led leds[4] {
    Led(8),
    Led(9),
    Led(10),
    Led(11)
};

Button btn(3);

int current = 0;

// 버튼을 누를 때마다 led 순차 점멸
void flash() {
    if(btn.debounce()){
        for(int i=0; i<4; i++) {
            if(i==current) {
                leds[i].on();
            } else {
                leds[i].off();
            }
        }
        current = (current+1) % 4;
    }
}

void setup() {
    btn.attachInterrupt(flash, FALLING);
}

void loop() {}