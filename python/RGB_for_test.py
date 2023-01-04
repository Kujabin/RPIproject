import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

LED_BLUE = 11
LED_RED = 16
LED_GREEN = 18
RGB = [LED_RED, LED_GREEN, LED_BLUE]

while 1 :
    GPIO.setup(RGB, GPIO.OUT, initial = GPIO.LOW)
    for i in RGB :
        GPIO.output(i,GPIO.HIGH)
        time.sleep(1)
        GPIO.output(i,GPIO.LOW)
        time.sleep(1)