import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

LED_BLUE = 11
LED_RED = 16
LED_GREEN = 18
while 1 :

    GPIO.setup(LED_BLUE, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(LED_RED, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(LED_GREEN, GPIO.OUT, initial=GPIO.LOW)


    GPIO.output(LED_BLUE, GPIO.HIGH)
    time.sleep(2)
    #LED 끄기
    GPIO.output(LED_BLUE, GPIO.LOW)
    time.sleep(2)

 
    GPIO.output(LED_RED, GPIO.HIGH)
    time.sleep(2)
    #LED 끄기
    GPIO.output(LED_RED, GPIO.LOW)
    time.sleep(2)


    
    GPIO.output(LED_GREEN, GPIO.HIGH)
    time.sleep(2)
    #LED 끄기
    GPIO.output(LED_GREEN, GPIO.LOW)
    time.sleep(2)