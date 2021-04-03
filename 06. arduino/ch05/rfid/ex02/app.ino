#include <SPI.h>
#include <MFRC522.h>
#include <EEPROM.h>
#include <Servo.h>
#include <Led.h>

// RFID 태그 값 하나를 EEPROM에 기록

#define RST_PIN 9
#define SS_PIN 10

byte uid[4];
MFRC522 mfrc(SS_PIN, RST_PIN);
Led led(8);

void read_uid() {
    for(int i=0; i<4; i++) {
        uid[i] = EEPROM.read(100+i);
        Serial.print(uid[i]);
        Serial.print(" ");
    }
    Serial.println();
}

bool check_uid(byte *target) {
    for(int i=0; i<4; i++) {
        if(uid[i] != target[i]) {   // ID가 틀린경우 false 리턴
            return false;
        }
    }
    // ID가 일치하는 경우 true 리턴
    return true;
}

void setup() {
    Serial.begin(9600);
    SPI.begin();
    mfrc.PCD_Init();
    read_uid();
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

    // 이번에 읽은 RFID 태그가 EEPROM에 저장된 값과 일치하는지 조사
    // 일치하면 서보모터로 문을 열어주고,
    // 일치하지 않으면 긴 beep 경고음 출력
    if(check_uid(mfrc.uid.uidByte)) {   // 일치하는 경우
        
        Serial.println("ID Matched!");
    } else {    // 일치하지 않는 경우
        led.on();
        delay(1000);
        led.off();
        Serial.println("ID Missmatched!");
    }
    Serial.println();    
}