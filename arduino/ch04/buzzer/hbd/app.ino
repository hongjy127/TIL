#include <Wire.h>
#include <LiquidCrystal_I2C.h>
#include <Melody.h>
#include "pitches.h"
#include "hbd.h"

// 하트
uint8_t name_1[8] = {
    0x00,
    0x0A,
    0x15,
    0x11,
    0x0A,
    0x04,
    0x00,
    0x00
};

// 아이스크림
uint8_t name_2[8] = {
    0x0E,
    0x1F,
    0x1F,
    0x0E,
    0x1F,
    0x0E,
    0x04,
    0x04
};

// 축하1
uint8_t name_3[8] = {
    0x02,
    0x07,
    0x0F,
    0x0F,
    0x1F,
    0x1F,
    0x1C,
    0x00 
};

// 축하2
uint8_t name_4[8] = {
    0x09,
    0x02,
    0x10,
    0x1A,
    0x19,
    0x10,
    0x00,
    0x00
};

// 닐라
uint8_t name_5[8] = {
    0x11,
    0x11,
    0x1D,
    0x0F,
    0x01,
    0x0F,
    0x08,
    0x0F
};

uint8_t name_6[8] = {
    0x02,
    0x1E,
    0x06,
    0x1F,
    0x12,
    0x1E,
    0x02,
    0x00
};




LiquidCrystal_I2C myLCD(0x27, 16, 2);
int length = sizeof(notes) / sizeof(int);
Melody melody(8, notes, durations, length);


void setup() {
    melody.play();

    myLCD.begin();
    myLCD.createChar(0, name_1);
    myLCD.createChar(1, name_2);
    myLCD.createChar(2, name_3);
    myLCD.createChar(3, name_4);
    myLCD.createChar(4, name_5);
    myLCD.createChar(5, name_6);
}

void loop() {
    melody.run();

    myLCD.setCursor(0, 0);
    myLCD.print("Happy Birthday ");
    myLCD.write(0);

    myLCD.setCursor(0,1);
    // 아이스크림
    myLCD.write(1);
    myLCD.print("Icecream");
    // 닐라
    myLCD.write(4);
    myLCD.write(5);
    myLCD.print(" ");
    //축하
    myLCD.write(2);
    myLCD.write(3);
    myLCD.write(2);
    myLCD.write(3);

}