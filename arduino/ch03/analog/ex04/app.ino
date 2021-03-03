#include <PWMLed.h>

PWMLed led(9);

void setup() {}

void loop() {
    int pwm_val;

    for(pwm_val = 0; pwm_val<256; pwm_val +=5) {
        led.setValue(pwm_val);
        delay(100);
    }

    led.off();
    delay(2000);
}