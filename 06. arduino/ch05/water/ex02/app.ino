#include <MiniCom.h>

MiniCom com;
int buzzer = 8;

void check() {
    int d_value = analogRead(A0);
    double a_value = (float)d_value * 5.0 / 1024.0 ;
    com.print_i(0, "D: ", d_value);
    com.print_d(1, "A: ", a_value);

    if(d_value > 400) {
        digitalWrite(buzzer, HIGH);
        // 통신을 통해 알람 발송...
        
    } else {
        digitalWrite(buzzer, LOW);
    }   
}

void setup() {
    com.init();
    com.setInterval(1000, check);
    pinMode(8, OUTPUT);
}

void loop() {
    com.run();
}