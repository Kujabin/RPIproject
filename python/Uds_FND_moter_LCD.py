#LCD로 거리 표현, 자동문 기능 3cm되면 모터 열림(180도), 2초후 다시 닫힘(180도) 
import RPi.GPIO as GPIO                   
import time   
import I2C_driver                            

# Trig=11 초음파 신호 전송핀 번호 지정 및 출력지정
# Echo=12 초음파 수신하는 수신 핀 번호 지정 및 입력지정
def main():
    PinTrig=11
    PinEcho=12
    mylcd = I2C_driver.lcd()
    GPIO.setmode(GPIO.BOARD)  
    GPIO.setwarnings(False)
    GPIO.setup(PinTrig, GPIO.OUT)           
    GPIO.setup(PinEcho, GPIO.IN)                    

    startTime=0
    stopTime=0
    while True:
        GPIO.output(PinTrig, False)    
        time.sleep(2)

        print ('Calculating Distance. 1 nanosec pulse')
        GPIO.output(PinTrig, True)          
        time.sleep(0.00001)            
        GPIO.output(PinTrig, False)         

        while GPIO.input(PinEcho) == 0:   
            startTime = time.time()
        while GPIO.input(PinEcho) == 1:   
            stopTime = time.time()

        Time_interval= stopTime - startTime     
        Distance = Time_interval * 17000
        Distance = int(round(Distance, 2))

        print ('Distance => ', Distance, 'cm')
        mylcd.lcd_display_string("Distance: "+str(Distance)+"cm", 1,0)

        
    GPIO.cleanup()

if __name__ == '__main__':
    main()