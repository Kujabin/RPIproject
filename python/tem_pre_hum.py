from Adafruit_BME280 import *
import RPi.GPIO as GPIO 
import time 
import I2C_driver

def main():
    fnd = [(0,0,0,0,0,0,1,1),
    (1,0,0,1,1,1,1,1),
    (0,0,1,0,0,1,0,1),
    (0,0,0,0,1,1,0,1),
    (1,0,0,1,1,0,0,1),
    (0,1,0,0,1,0,0,1),
    (0,1,0,0,0,0,0,1),
    (0,0,0,1,1,1,1,1),
    (0,0,0,0,0,0,0,1),
    (0,0,0,0,1,0,0,1),
    (0,1,1,0,1,1,0,0),
    (1,0,0,1,1,1,1,0),
    (0,0,0,0,0,0,0,0)]

seg = [31,32,33,35,36,37,38,40]

sensor = BME280(t_mode=BME280_OSAMPLE_8, p_mode=BME280_OSAMPLE_8, h_mode=BME280_OSAMPLE_8)

duty_ratio= 2
MaxDuty= 12
PWMpin= 12
PinTrig=16
PinEcho=18
GPIO.setmode(GPIO.BOARD) 
GPIO.setup(PinTrig, GPIO.OUT) 
GPIO.setup(PinEcho, GPIO.IN) 
GPIO.setup(PWMpin, GPIO.OUT) 
GPIO.setup(seg, GPIO.OUT, initial=GPIO.LOW)
Servo=GPIO.PWM(PWMpin, 50) 
Servo.start(0)
time.sleep(1)
startTime=0
stopTime=0
mylcd = I2C_driver.lcd()

degrees = sensor.read_temperature()#온도 측정 값
pascals = sensor.read_pressure()#압력 측정 값 단위 파스칼
hectopascals = pascals / 100#압력 측정 값 파스칼에서 헥토파스칼로 변경
humidity = sensor.read_humidity()#습도 측정 값

#print ('Temp      = {0:0.3f} deg C'.format(degrees)) #온도
#print ('Pressure  = {0:0.2f} hPa'.format(hectopascals)) #압력
#print ('Humidity  = {0:0.2f} %'.format(humidity)) #습도

print ('Temp      = {0:0.3f} deg C'.format(degrees), 'Humidity  = {0:0.2f} %'.format(humidity)) #온도

while True:
    Servo.ChangeDutyCycle(duty_ratio)
    GPIO.output(PinTrig, False) 
    time.sleep(2)

    while GPIO.input(PinEcho) == 0: 
            startTime = time.time()

    while GPIO.input(PinEcho) == 1: 
            stopTime = time.time()
    Time_interval= stopTime - startTime
        
    mylcd.lcd_display_string('온도 = {0:0.3f} deg C'.format(degrees), 1)
    mylcd.lcd_display_string('습도 = {0:0.2f} %'.format(humidity), 2)

    if degrees>23:
        duty_ratio = 10
        Servo.ChangeDutyCycle(duty_ratio)
        time.sleep(1)
        GPIO.output(seg, fnd[12])
        time.sleep(1)
        GPIO.output(seg, fnd[13])
        time.sleep(1)
        GPIO.output(seg, fnd[12])
        time.sleep(1)
        GPIO.output(seg, fnd[13])
        time.sleep(1)
        GPIO.output(seg, fnd[12])
        time.sleep(1)
        GPIO.output(seg, fnd[13])
        time.sleep(1)