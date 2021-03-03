#include <MiniCom.h>

MiniCom com;

void check() {
    int d_value = analogRead(A0);
    double a_value = (float)d_value * 5.0 / 1024.0 ;
    com.print_i(0, "D: ", d_value);
    com.print_d(1, "A: ", a_value);
}

void setup() {
    com.init();
    com.setInterval(1000, check);
}

void loop() {
    com.run();
}