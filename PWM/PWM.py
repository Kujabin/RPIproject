import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
LED = 12

def main():
    # Duty 1-100
    Duty= 100
    GPIO.setup(LED, GPIO.OUT)

    PWMLED= GPIO.PWM(LED, 60)
    PWMLED.start(0)

    while True:        
        PWMLED.ChangeDutyCycle(Duty)

if __name__ == '__main__':
    main()

