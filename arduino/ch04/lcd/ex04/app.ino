#include <LiquidCrystal_I2C.h>

byte name_h[8] = {
        B00100,
        B11111,
        B01110,
        B00100,
        B11111,
        B00100,
        B01010,
        B00100
};

byte name_j[8] = {
        B11101,
        B00101,
        B00111,
        B01101,
        B10011,
        B00110,
        B01001,
        B00110
};

byte name_y[8] = {
        B01001,
        B10111,
        B10101,
        B10111,
        B01001,
        B00001,
        B01000,
        B01111
};

LiquidCrystal_I2C myLCD(0x27, 16, 2);

void setup() {
    myLCD.begin();

    myLCD.createChar(0, name_h);
    myLCD.createChar(1, name_j);
    myLCD.createChar(2, name_y);
}

void loop() {
    myLCD.setCursor(0, 0);
    myLCD.print("Hello, Arduino!");

    myLCD.setCursor(0, 1);
    myLCD.print("My name is ");

    myLCD.write(0);
    myLCD.write(1);
    myLCD.write(2);
}