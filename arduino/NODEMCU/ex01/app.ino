// 버튼을 눌렀을 때
// led가 blink 되게 하고
// 한 번 더 눌렀을 때
// led가 꺼지게

#include <MiniCom.h>
#include <Led.h>
#include <Button.h>

Button btn(D5); // 5: GPI05
Led led(D6);    // 6: GPI06
MiniCom com;
bool state = false; // true: blink 모드, false: off 모드
int timer_id = -1;

void check() {
    if(!state) {
        timer_id = com.setInterval(500, [](){
            com.print(0, "Blink mode");
            led.toggle();
        });
        state = true;
    } else {
        led.off();
        state = false;
        com.print(0, "Off mode");
        // 타이머를 꺼야 함.
        SimpleTimer &timer = com.getTimer();
        timer.deleteTimer(timer_id);
    }
}

void setup() {
	com.init();
    btn.setCallback(check);
    com.print(0, "Off mode");

}

void loop() {
    btn.check();
	com.run();
}
