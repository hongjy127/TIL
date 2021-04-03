#include <SimpleTimer.h>
#include <LiquidCrystal_I2C.h>

SimpleTimer timer;
const int var_pin = A0;

LiquidCrystal_I2C myLCD(0x27, 16, 2);

void check() {
    int digital_val;
    float ff;
    digital_val = analogRead(var_pin);
    ff = (float)digital_val / 1023. * 5.0;

    // LCD로 출력
    // 출력 모양
    // Volt: 4.3V
    // D. value: 805
    // 아두이노 문자열 클래스 : String
    // myLCD.clear();

    char msg[17];

    String buf = "Volt: ";  // String buf = "Volt: " + ff + "V"; --> error
    buf = buf + ff + "V";
    sprintf(msg, "%-16s", buf.c_str());
    // sprintf(msg, "Volt: %fV", ff);   이거는 안됨, sprintf는 float 지원 안함.
    myLCD.setCursor(0, 0);
    // myLCD.print(buf.c_str());
    myLCD.print(msg);

    // buf = "D. value: "; // String buf = "D. value: " + digital_val; --> error
    // buf = buf + digital_val;
    // sprintf(msg, "%16s", buf.c_str());
    sprintf(msg, "D. value: %4d", digital_val);
    myLCD.setCursor(0, 1);
    // myLCD.print(buf.c_str());
    myLCD.print(msg);
}

void setup() {
    Serial.begin(9600);
    myLCD.begin();
    timer.setInterval(100, check);
}

void loop() {
    timer.run();
}

