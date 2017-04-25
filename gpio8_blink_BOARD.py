import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(8, GPIO.OUT)


def blink():
    GPIO.output(8,GPIO.HIGH)
    time.sleep(3)
    GPIO.output(8,GPIO.LOW)
    time.sleep(3)

try:

    while True:
                blink()
                print(123)

except KeyboardInterrupt:
    pass

GPIO.cleanup()
