#include <ESP8266WiFi.h>
#include <PubSubClient.h>
#include <MiniCom.h>

// 5G 지원 x
const char *ssid = "KT_GiGA_2G_Wave2_05BE";
const char *password = "hf52ch1863";
// const char *ssid = "TECH2_2G";
// const char *password = "tech21234!";
const char *mqtt_server = "172.30.1.39";

MiniCom com(115200);
WiFiClient espClient;
PubSubClient client(espClient);
long lastMsg = 0;
char msg[50];
int value = 0;

void wifi_connect() {
    WiFi.begin(ssid, password);
    while(WiFi.status() != WL_CONNECTED ) {
        delay(500);
        Serial.print(".");
    }
    com.print(0, "WiFi connected", true);
    IPAddress ip = WiFi.localIP();
    String ipstr = ip.toString();
    com.print(1, ipstr.c_str(), true);
}

void setup() {
    pinMode(BUILTIN_LED, OUTPUT);
    Serial.begin(115200);
    wifi_connect();
    client.setServer(mqtt_server, 1883);
    client.setCallback(callback);   // 토픽 수신 시 호출할 함수 등록
}

void callback(char* topic, byte* payload, unsigned int length) {
    Serial.print("Message arrived[");
    Serial.print(topic);
    Serial.print("]");
    for(int i=0; i<length; i++) {
        Serial.print((char)payload[i]);
    }
    Serial.println();

    if((char)payload[0] == '1') {
        digitalWrite(BUILTIN_LED, LOW);
    } else {
        digitalWrite(BUILTIN_LED, HIGH);
    }
}

void reconnect() {
    while(!client.connected()) {
        Serial.print("Attempting MQTT connection...");
        if(!client.connect("ESP8266Client")) {  // 클라이언트 아이디
            Serial.println("connected");
            client.publish("outTopic", "hello world");
            client.subscribe("inTopic");
        } else {
            Serial.print("failed, rc=");
            Serial.print(client.state());
            Serial.println(" try again in 5 seconds");
            delay(5000);
        }
    }
}

void loop() {
    if(!client.connected()) {
        reconnect();
    }
    client.loop();

    long now = millis();
    if(now-lastMsg > 2000) {
        lastMsg = now;
        ++value;
        snprintf(msg, 75, "hello world #%1d", value);
        Serial.print("Publish message: ");
        Serial.println(msg);
        client.publish("outTopic", msg);
    }

}
