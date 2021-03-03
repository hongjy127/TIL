#include <SimpleTimer.h>

SimpleTimer timer;
const int var_pin = A0;
int analog_val;

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

    // delay(2000);
}

void setup() {
    Serial.begin(9600);
    timer.setInterval(100, check);
}

void loop() {
    timer.run();
}