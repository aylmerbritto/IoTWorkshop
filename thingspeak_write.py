import requests
import http.client as hp
import urllib
import time
import random
import RPi.GPIO as GPIO
import time
 
#GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BCM)
 
#set GPIO Pins
GPIO_TRIGGER = 2
GPIO_ECHO = 3

 
#set GPIO direction (IN / OUT)
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)

sleep = 15
key = 'F9MIAWHX33MY9B3F'

def ultrasonic():
    # set Trigger to HIGH
    GPIO.output(GPIO_TRIGGER, True)
 
    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)
 
    StartTime = time.time()
    StopTime = time.time()
 
    # save StartTime
    while GPIO.input(GPIO_ECHO) == 0:
        StartTime = time.time()
 
    # save time of arrival
    while GPIO.input(GPIO_ECHO) == 1:
        StopTime = time.time()
 
    # time difference between start and arrival
    TimeElapsed = StopTime - StartTime
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    distance = (TimeElapsed * 34300) / 2
 
    return distance

def update_distance():
    while True:
        dist = ultrasonic()
        print(dist)
        params = urllib.parse.urlencode({'field1': dist, 'key':key }) 
        headers = {"Content-typZZe": "application/x-www-form-urlencoded","Accept": "text/plain"}
        conn = hp.HTTPConnection("api.thingspeak.com:80")
        try:
            conn.request("POST", "/update", params, headers)
            response = conn.getresponse()
            print (dist)
            print (response.status, response.reason)
            data = response.read()
            conn.close()
        except:
            print( "connection failed")
        break

if __name__ == "__main__":
        while True:
                update_distance()
                time.sleep(sleep)
