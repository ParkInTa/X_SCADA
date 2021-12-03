import RPi.GPIO as gpio
import time

GPIO.setmode(GPIO.BCM)
count = 0

def handler(channel):
    global count    
    count += 1
    print(count)
    
if __name__=="__main__":

    GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.add_event_detect(24,GPIO.RISING,callback=handler, bouncetime=300)
    
    while True:
        time.sleep(1)
    