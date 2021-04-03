#include <MiniCom.h>

MiniCom com;

void check() {
    Serial.println("check called");
}

void setup() {
    com.init();
    com.setInterval(100, check);
}

void loop() {
    com.run();
}