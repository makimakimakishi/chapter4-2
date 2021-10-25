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
set_degree =int(param[1])
wiringpi.wiringPiSetupGpio()
wiringpi.pinMode( servo_pin, 2 )
wiringpi.pwmSetMode(0)
wiringpi.pwmSetRange(1024)
wiringpi.pwmSetClock(375)
if(set_degree = -90):
    move_deg = int( 81 + 41 / 90 * set_degree )
    wiringpi.pwmWrite( 2,move_deg )

