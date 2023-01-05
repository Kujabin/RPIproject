import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
import time

Switch= 10

GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering

def main():    
    GPIO.setup(Switch, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) 

    while True: 
        # GPIO.input(Switch)와 ?를 AND 연산으로 변경 가능
        if GPIO.input(Switch) == ?:
            print("Button was pushed!")
        else:
            print("Button was not pushed!")        
            time.sleep(1)

if __name__ == '__main__':
    	main()
