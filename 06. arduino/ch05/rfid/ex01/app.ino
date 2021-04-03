#include <SPI.h>
#include <MFRC522.h>
#include <EEPROM.h>
#include <Led.h>

// RFID 태그 값 하나를 EEPROM에 기록

#define RST_PIN 9
#define SS_PIN 10

MFRC522 mfrc(SS_PIN, RST_PIN);
Led led(8);

void setup() {
    Serial.begin(9600);
    SPI.begin();
    mfrc.PCD_Init();
}

// EEPROM 100번지에 uid 저장
void write_uid(byte *uid) {
    for(int i = 0; i<4; i++) {
        EEPROM.write(100+i, uid[i]);
    }
}

void loop() {
    if( !mfrc.PICC_IsNewCardPresent() || !mfrc.PICC_ReadCardSerial() ) {
        delay(500);
        return;
    }

    led.on();
    delay(100);
    led.off();

    Serial.print("Card UID: ");

    // 태그의 ID출력하는 반복문, 태그의 ID사이즈(4)까지
    for(byte i=0; i<4; i++) {
        Serial.print(mfrc.uid.uidByte[i]);
        Serial.print(" ");
    }

    // EEPROM에 UID 저장
    write_uid(mfrc.uid.uidByte);
    Serial.println();
    
}