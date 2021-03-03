#include <PWMLed.h>

PWMLed led(9);

void setup() {

}

void loop() {
    int analog_val, pwm_val;
    analog_val = analogRead(A0);
    pwm_val = map(analog_val, 0, 1023, 255, 0);

    led.setValue(pwm_val);
}