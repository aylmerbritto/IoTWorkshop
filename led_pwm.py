import RPi.GPIO as GPIO     # Importing RPi library to use the GPIO pins
from time import sleep  # Importing sleep from time library

led_pin = 2            # Initializing the GPIO pin 21 for LED

GPIO.setmode(GPIO.BCM)          # We are using the BCM pin numbering
GPIO.setup(led_pin, GPIO.OUT)   # Declaring pin 21 as output pin

pwm = GPIO.PWM(led_pin, 100)    # Created a PWM object
pwm.start(0)                    # Started PWM at 0% duty cycle

try:
    while True:                    # Loop will run forever
        for x in range(100):    # This Loop will run 100 times
            pwm.ChangeDutyCycle(x) # Change duty cycle
            sleep(0.01)         # Delay of 10mS
            
        for x in range(100,0,-1): # Loop will run 100 times; 100 to 0
            pwm.ChangeDutyCycle(x)
            sleep(0.01)

# If keyboard Interrupt (CTRL-C) is pressed
except KeyboardInterrupt:
        pwm.stop()      # Stop the PWM
        GPIO.cleanup()  # Make all the output pins LOW
