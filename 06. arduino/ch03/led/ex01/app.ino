// 아두이노에서는 전역변수를 사용함
const int pd_led_pin = 11;  // pull down
const int pu_led_pin = 7;  // pull up

void setup() {
  // put your setup code here, to run once:
  pinMode(pd_led_pin, OUTPUT);
  pinMode(pu_led_pin, OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
    digitalWrite(pd_led_pin, HIGH);
    digitalWrite(pu_led_pin, HIGH);
    delay(1000);

    digitalWrite(pd_led_pin, LOW);
    digitalWrite(pu_led_pin, LOW);
    delay(1000);
}