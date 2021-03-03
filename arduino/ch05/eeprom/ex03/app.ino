#include <EEPROM.h>

String password = "";

void setup() {
    Serial.begin(9600);
    // EEPROM에서 읽어서 password 복원
    for(int i=0; i<1023; i++) {
        char ch = EEPROM.read(i);
        if(ch == '\0') {
            break;
        }
        password += ch;
    }

    Serial.println("password: " + password);

}

void loop() {

}