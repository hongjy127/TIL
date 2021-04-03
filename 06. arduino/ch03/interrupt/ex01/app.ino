const int sw_pin = 3;
const int led_pin = 8;
volatile boolean led_st = LOW;

void flash(void) {
    led_st = !led_st;
    digitalWrite(led_pin, led_st);
}

void setup() {
    pinMode(sw_pin, INPUT_PULLUP);
    attachInterrupt(digitalPinToInterrupt(sw_pin), flash, FALLING);

    pinMode(led_pin, OUTPUT);
    digitalWrite(led_pin, led_st);
}

void loop() {}