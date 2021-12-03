import RPi.GPIO as gpio
import time

# 한줄 주석
'''
여러줄 주석
'''

def setup(): #함수(메쏘드) 정의
    gpio.setmode(gpio.BCM) # 핀타입
    gpio.setup(18,gpio.OUT)

def loop():
    try:
        while (True):
            gpio.output(18, True)
            time.sleep(0.5)
            gpio.output(18, False)
            time.sleep(0.5)
    except KeyboardInterrupt:
            print("Error!")
            gpio.cleanup()

if __name__ == "__main__":      # 메인
    setup()
    loop()