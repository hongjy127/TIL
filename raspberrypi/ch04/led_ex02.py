from gpiozero import LED
from signal import pause

red = LED(21)

red.blink(on_time=0.5, off_time=0.5, n=5) # 백그라운드 스레드를 이용해서 운영

pause() # 신호가 들어오면 실행, 메인 스레드 중지 상태
