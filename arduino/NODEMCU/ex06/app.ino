#include <MqttCom.h>
#include <Led.h>

const char *ssid = "KT_GiGA_2G_Wave2_05BE";
const char *password = "hf52ch1863";
const char *server = "172.30.1.35";
const char *sub_topic = "test/led"; // 아두이노는 토픽 하나만 지정 가능, #, + 지원 안됨

MqttCom com(ssid, password);

// 외부에서 장치 제어
void subscribe(char* topic, uint8_t* payload, unsigned int length) {
    char buf[128];
    memcpy(buf, payload, length);   // 메모리 내용 복사
    buf[length] = '\0';

    Serial.println(topic);
    Serial.println(buf);
}

// 주기적으로 센서의 데이터 수집
void publish() {
    com.publish("test/greet", "hello world!");
}

void setup() {
    // com.init(server);
    com.init(server, sub_topic, subscribe);
    com.setInterval(2000, publish);
}

void loop() {
    com.run();
}