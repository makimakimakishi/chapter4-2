import time
import RPi.GPIO as GPIO
import sys
GPIO.setmode(GPIO.BCM)
GPIO.setup(2, GPIO.OUT)
servo = GPIO.PWM(2, 50)
servo.start(0.0)
bottom = 2.5  # -90deg : 0.5ms / 20ms = 2.5[%]
middle = 7.25 #   0deg : 1.45ms / 20ms = 7.25[%]
top = 12.0    #  90deg : 2.4ms / 20ms = 12.0[%]
param = sys.argv
set_degree =int(param[1]):
setservo(setdegree)

def setservo(setdegree)
    print(set_degree)
    s=95*set_degree
    v=s/1800
    c=v+7.25
    servo.ChangeDutyCycle(c)
    for i in range(5):
	servo.ChangeDutyCycle(bottom)
	time.sleep(1.0)

	servo.ChangeDutyCycle(c)
	time.sleep(1.0)
