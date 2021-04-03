#include <Led.h>

Led led1(9);
Led led2(8);

int sw1 = 3;
int sw2 = 4;

void setup() {
    pinMode(sw1, INPUT);    // 풀다운
    pinMode(sw2, INPUT);    // 풀업
}

void loop() {
    int v1,v2;
 
    // 풀다운: 평소에 L, 누르면 H
    v1 = digitalRead(sw1);
    led1.setValue(v1);

    // 풀업: 평소에 H, 누르면 L 
    v2 = digitalRead(sw2);
    led2.setValue(!v2);
}