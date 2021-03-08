#include <DoorLock.h>
#include <SimpleTimer.h>
#include <Servo.h>

const byte ROWS = 4;
const byte COLS = 4;

const byte col_pins[COLS] = {9, 8, 7, 6};
const byte row_pins[ROWS] = {10, 11, 12, 13};

const char hex_keys[ROWS][COLS] = {
    {'0', '1', '2', '3'},
    {'4', '5', '6', '7'},
    {'8', '9', 'A', 'B'},
    {'C', 'D', 'E', 'F'}
};

Keypad myKeypad = Keypad(makeKeymap(hex_keys), row_pins, col_pins, ROWS, COLS);
int led_pin = 4;
Servo door;

DoorLock doorlock(led_pin, myKeypad);

void open_door() {
    doorlock.beep(200);
    door.write(90);
    delay(5000);
    door.write(0);
    doorlock.beep(200);
}

void setup() {
    door.attach(5);
    door.write(0);
}

void loop() {
    doorlock.check(open_door);
}