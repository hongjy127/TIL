#include <TimerOne.h>

#include <Led.h>

Led led(13);

void flash() {
    led.toggle();
}

void setup() {
    Timer1.initialize(500000);
    Timer1.attachInterrupt(flash);
}

void loop() {

}