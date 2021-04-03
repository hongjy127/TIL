const int led_pin = 9;

void setup() {
    pinMode(led_pin, OUTPUT);
    digitalWrite(led_pin, LOW);
}

void loop() {
    int pwm_val;

    for(pwm_val = 0; pwm_val<256; pwm_val +=5) {
        analogWrite(led_pin, pwm_val);
        delay(100);
    }

    digitalWrite(led_pin, LOW);
    delay(2000);
}