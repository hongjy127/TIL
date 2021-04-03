const int sw_pin = 3;
const int led_pin = 8;
volatile boolean led_st = LOW;
volatile unsigned long t1, t2;

void flash(void) {
    // 채터링: 200ms 이내에 눌려진건 무시
    t2 = millis();

    if((t2-t1) < 200) return;
    else t1 = t2;

    led_st = !led_st;
    digitalWrite(led_pin, led_st);
}

void setup() {
    pinMode(sw_pin, INPUT_PULLUP);
    attachInterrupt(digitalPinToInterrupt(sw_pin), flash, FALLING);

    pinMode(led_pin, OUTPUT);
    digitalWrite(led_pin, led_st);
    t1 = millis();
}

void loop() {}