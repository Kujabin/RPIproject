import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

LED_BLUE = 11
LED_RED = 16
LED_GREEN = 18

GPIO.setup(LED_BLUE, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(LED_RED, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(LED_GREEN, GPIO.OUT, initial=GPIO.LOW)

while 1 :
    RGB_butten = input("R, G, B 중에 입력해주세요. : ")
    print(RGB_butten)

    if RGB_butten == "R" or RGB_butten == "r" :
        GPIO.output(LED_RED, GPIO.HIGH)
        #time.sleep(2)

    elif RGB_butten == "G" or RGB_butten == "g" :
        GPIO.output(LED_GREEN, GPIO.HIGH)

    elif RGB_butten == "B" or RGB_butten == "b" :
        GPIO.output(LED_BLUE, GPIO.HIGH)

    else :
        GPIO.output(LED_RED, GPIO.LOW)
        GPIO.output(LED_GREEN, GPIO.LOW)
        GPIO.output(LED_BLUE, GPIO.LOW)
