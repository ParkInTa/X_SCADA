import RPi.GPIO as gpio
import time

def setup():
    gpio.setmode(gpio.BCM) 
    gpio.setup(24,gpio.IN)
    gpio.setup(18,gpio.OUT)
def loop():
    count = 0
    while True:
        try:
            value = gpio.input(24)
            if value == True:
                count += 1
                print(count)
                if count % 2 == 0:
                    gpio.output(18,False)
                else:
                    gpio.output(18,True)
            time.sleep(0.1)
        except KeyboardInterrupt:
            gpio.cleanup()
        
if __name__ == "__main__":      # 메인
    setup()
    loop()