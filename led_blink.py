import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(2,GPIO.OUT)
while True:
	GPIO.output(2,GPIO.HIGH)
	time.sleep(1)
	GPIO.output(2,GPIO.LOW)
	time.sleep(1)
