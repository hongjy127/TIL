#include <MqttCom.h>
#include <DHT.h>
#include <PWMLed.h>
#include <ArduinoJson.h>

const char *ssid = "KT_GiGA_2G_Wave2_05BE";
const char *password = "hf52ch1863";
const char *server = "172.30.1.35";
const char *sub_topic = "test/led"; // 아두이노는 토픽 하나만 지정 가능, #, + 지원 안됨 -> JSON 사용

MqttCom com(ssid, password);
DHT dht11(D5, DHT11);
PWMLed led(D6);

// 외부에서 장치 제어
// LED PWM 제어
void subscribe(char* topic, uint8_t* payload, unsigned int length) {
    char buf[128];
    memcpy(buf, payload, length);   // 메모리 내용 복사
    buf[length] = '\0';

    // JSON 문자열 -> 객체로 변환
    StaticJsonDocument<128> doc;
    auto error = deserializeJson(doc, buf);
    if(error) {
        Serial.println("deserializeJson() error");
        Serial.println(error.c_str());
        return;
    }

    const char *device = doc["device"];
    int value = doc["value"].as<int>();

    Serial.println(topic);
    Serial.println(buf);

    // atoi: 문자열 --> 정수로 변환
    // atof: 문자열 --> double로 변환
    // int value = atoi(buf);
    led.setValue(value);
}

// 주기적으로 센서의 데이터 수집
void publish() {
    double temp = dht11.readTemperature();
    double humi = dht11.readHumidity();
    com.print_d(0, "Temp.: ", temp);
    com.print_d(1, "Humi.: ", humi);

    // double을 publish하지 못함 --> 문자열로 바꿈
    String value = "";
    value += temp;
    com.publish("user1/home/livingroom/temp", value.c_str());
    value = "";
    value += humi;
    com.publish("user1/home/livingroom/humi", value.c_str());
}

void setup() {
    // com.init(server);
    com.init(server, sub_topic, subscribe);
    com.setInterval(2000, publish);
}

void loop() {
    com.run();
}