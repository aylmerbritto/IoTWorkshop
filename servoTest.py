import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

# Declaring Servo Pin
servoPin = 3

# Setting mode for servo pin
GPIO.setup(servoPin , GPIO.OUT)


# function for setting angle of the servo motor using PWM 
# for this initial frequency of PWM must be set to 50Hz
# Servos will set to 0 degrees if given a signal of .5 ms, 90 when given 1.5 ms, and 180 when given 2.5ms pulses

pwm = GPIO.PWM(servoPin , 50) # setting the 50 Hz frequency

pwm.start(2.5) # setting the initial imporCycle to be 0 (basically setting the pin low or 0 V )

# function to

pwm.start(7.5)
pwm.start(12.5)
pwm.start(2.5)
