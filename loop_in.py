import RPi.GPIO as GPIO
import time

GPIO_PIN = 24
count=5

GPIO.setmode(GPIO.BCM)
GPIO.setup(GPIO_PIN, GPIO.IN)
while True:
        #if(GPIO.input(GPIO_PIN)==1):
        #count=count-1
        print(GPIO.input(GPIO_PIN))
        time.sleep(1)
print('end')

GPIO.cleanup()
