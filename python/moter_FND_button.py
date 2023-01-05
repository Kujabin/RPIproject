import RPi.GPIO as GPIO 
import time 

def main():
    duty_ratio= 0
    MaxDuty= 12
    PWMpin= 12
    GPIO.setmode(GPIO.BOARD) 
    GPIO.setup(PWMpin, GPIO.OUT) 
    GPIO.setwarnings(False)

    seg = [31,32,33,35,36,37,38,40]
    #      a,b ,c ,d ,e ,f ,g ,dp
    GPIO.setup(seg, GPIO.OUT, initial=GPIO.LOW)
    #      a,b,c,d,e,f,g,dp

    

    Servo = GPIO.PWM(PWMpin, 50)

    Servo.start(0)

    fnd = [(0,0,0,0,0,0,1,1),
    (1,0,0,1,1,1,1,1),
    (0,0,1,0,0,1,0,1),
    (0,0,0,0,1,1,0,1),
    (1,0,0,1,1,0,0,1),
    (0,1,0,0,1,0,0,1),
    (0,1,0,0,0,0,0,1),
    (0,0,0,1,1,1,1,1),
    (0,0,0,0,0,0,0,1),
    (0,0,0,0,1,0,0,1)]
        
        
    while 1 :
        moter_button = int(input('0 ~ 9 중 숫자를 입력해주세요. : '))
        print(moter_button)

        if moter_button == 0 :
            fnd[0]
            GPIO.output(fnd[0], GPIO.HIGH)
            Servo.ChangeDutyCycle(duty_ratio)
            time.sleep(1)
        elif moter_button == 1 :
            fnd[1]
            GPIO.output(fnd[1], GPIO.HIGH)
            Servo.ChangeDutyCycle(duty_ratio)
            time.sleep(1)
        else :
            GPIO.cleanup()
            print('Everythings cleanup')

        Servo.stop()
        
    if __name__ == '__main__':
        main()




        