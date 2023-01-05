import Rpi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
setwarnings(False)
# raspberry pi pinnum
# LED ?
LED = 8         

def main():
    # 2.보드에 연결된 주변 장치 핀 번호 설정
	# GPIO.setup(핀번호, 핀상태(input/output), 초기상태)
    GPIO.setup(LED, GPIO.OUT, initial=GPIO.LOW)

	# 3.주변 장치 입력/출력 모드 상태 설정
	# GPIO.output(핀번호, 출력상태)
    GPIO.output(LED, GPIO.HIGH)

	# 4. 상황에 따른 동작 응용
	while True:        
        # GPIO.output(LED, GPIO.HIGH)
        # time.sleep(1)

if __name__ == '__main__':
	main()
