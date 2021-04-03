// 버튼을 누른 후 5초동안만 아날로그 값 측정
// 이 기간동안 LED는 켜짐
// 5초 후 LED 꺼지고, 값은 측정되지 않음.
// 5초 이내에 버튼을 다시 누르면 정지

#include <SimpleTimer.h>
#include <Led.h>
#include <Button.h>

const int var_pin = A0;

SimpleTimer timer;
int timerId;
Led led(8);
Button btn(3);

void check() {
    int digital_val;
    float ff;

    digital_val = analogRead(var_pin);

    ff = (float)digital_val / 1023. * 5.0;

    Serial.print("Input Voltage(0~5 V) = ");
    Serial.println(ff);

    Serial.print("Digital Value(0~1023) = ");
    Serial.println(digital_val);
    Serial.println("---------------------");
}

void start() {
    if(!btn.debounce()) return;
    if(timerId == -1) {
        led.on();
        timerId = timer.setInterval(100, check);
        timer.setTimeout(5000, stop);
    } else {
        stop();
    }
}

void stop() {
    led.off();
    timer.deleteTimer(timerId); // timerId는 0보다 큰 값
    timerId = -1;
}

void setup() {
    Serial.begin(9600);
    btn.attachInterrupt(start, FALLING);
}

void loop() {
    timer.run();
}

