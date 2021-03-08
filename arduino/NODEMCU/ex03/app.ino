#include <ESP8266WiFi.h>
#include <MiniCom.h>

// 5G 지원 x
const char *ssid = "KT_GiGA_2G_Wave2_05BE";
const char *password = "hf52ch1863";

MiniCom com(115200);

void wifi_connect() {
    // WiFi: 전역객체
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
    com.init();
    wifi_connect();
}

void loop() {
    
}
