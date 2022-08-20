
import machine
from machine import Pin, PWM 
import utime, time
from time import sleep

servo = PWM(Pin(0))
led = Pin(25, Pin.OUT)

servo.freq(50)

def servoAngle(degrees):
    if degrees > 180 : degrees = 180
    if degrees < 0 : degrees = 0
    newDuty = minDuty + (maxDuty - minDuty) * (degrees/180)
    servo.duty_u16(int(newDuty))
maxDuty = 8200
minDuty = 1700




while True:
    for degree in range(0,180,1):
        servoAngle(degree)
        sleep(0.02)
        print("increasing---" + str(degree))


    for degree in range(180, 0, -1):
        servoAngle(degree)
        sleep(0.02)
        print("decreasing--" + str(degree))