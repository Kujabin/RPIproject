import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

#a = 37
#b = 35
#c = 33
#d = 31
#e = 29
#f = 27
#g = 23
#h = 21

seg = [37, 35, 33, 31, 29, 27, 23, 21 ] # GPIO pin
# A B C D E F G DP
fnd = [(1,1,1,1,1,1,0,0), #0
( 1,0,0,1,1,1,1,1), #1
( 0,0,1,0,0,1,0,1), #2
( 0,0,0,0,1,1,0,1), #3 
( 1,0,0,1,1,0,0,1), #4
( 0,1,0,0,1,0,0,1), #5
( 0,1,0,0,0,0,0,1), #6
( 0,0,0,1,1,1,1,1), #7
( 0,0,0,0,0,0,0,1), #8
( 0,0,0,0,1,0,0,1)] #9

for i in range (10) :
    GPIO.output(i,GPIO.HIGH)
