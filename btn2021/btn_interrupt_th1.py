# 버튼 인터럽트 쓰레드 방식
import RPi.GPIO as GPIO
import time
import threading # thread 사용

GPIO.setmode(GPIO.BCM)
handler1Flag = True
handler2Flag = True

def handler1(channel): # 메쏘드 정의
    print("인터럽트 발생 handler1")
    handler1Thread().start()

def handler2(channel):
    print("인터럽트 발생 handler2")
    handler2Thread().start()

class handler1Thread(threading.Thread): # 클래스 정의
    def run(self):
        while handler1Flag:
            print("handler1")
            time.sleep(1)

class handler2Thread(threading.Thread):
    def run(self):
        while handler2Flag:
            print("handler2")
            time.sleep(1)

# linux kernel epoll
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.add_event_detect(24, GPIO.RISING,
        callback=handler1, bouncetime=300)
GPIO.add_event_detect(23, GPIO.RISING,
        callback=handler2, bouncetime=300)

if __name__ == "__main__":
    while True:
        time.sleep(0.1)