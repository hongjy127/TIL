// int ENPin = 9;
// int in1Pin = 8;
// int in2Pin = 7;

int ENPin = 3;
int in1Pin = 5;
int in2Pin = 4;

void setup() {
    Serial.begin(9600);

    pinMode(ENPin, OUTPUT);
    pinMode(in1Pin, OUTPUT);
    pinMode(in2Pin, OUTPUT);
}

void loop() {
    Serial.println("Forward");
    analogWrite(ENPin, 255);
    digitalWrite(in1Pin, HIGH);
    digitalWrite(in2Pin, LOW);
    delay(1000);

    Serial.println("Stop");
    digitalWrite(in1Pin, LOW);
    digitalWrite(in2Pin, LOW);
    delay(1000);

    Serial.println("back");
    analogWrite(ENPin, 100);
    digitalWrite(in1Pin, LOW);
    digitalWrite(in2Pin, HIGH);
    delay(1000);

    Serial.println("Stop");
    digitalWrite(in1Pin, LOW);
    digitalWrite(in2Pin, LOW);
    delay(1000);
}