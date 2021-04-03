#include <ESP8266WiFi.h>
#include <MiniCom.h>

// 5G 지원 x
const char *ssid = "KT_GiGA_2G_Wave2_05BE";
const char *password = "hf52ch1863";

MiniCom com(115200);
WiFiServer server(80);  // 서버 소켓, 80: 포트번호

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
    com.init();
    WiFi.mode(WIFI_STA); // STAND ALONE 모드
    wifi_connect();
    server.begin();
}

void loop() {
    WiFiClient client = server.available(); // accept() 작업
    if(!client) {   // 접속이 없으면 바로 리턴
        return;
    }

    // wait until the client sends some data
    Serial.println("new Client");

    // 여기서부터는 어플리케이션의 프로토콜에 따라 바꿔줌
    while(!client.available()) {
        delay(1);
    }

    // Read the first line of the request
    String request = client.readStringUntil('\r');
    Serial.println(request);
    client.flush();

    // Return the response
    client.println("HTTP/1.1 200 OK");
    client.println("Content-Type: text/html");  // 응답 header
    client.println(""); // 헤더와 body 구분 역할
    client.println("<!DOCTYPE HTML>");  // 응답 body
    client.println("<html>");
    client.print("HELLO WORLD!");
    client.println("</html>");
    delay(1);
    Serial.println("Client disconnected");
    Serial.println("");

}
