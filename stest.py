import RoboPiLib as RPL
import setup
import time

pul_pin = 1
dir_pin = 2

direction = 1
speed = 5000

RPL.pinMode(pul_pin,RPL.PWM)
RPL.pinMode(dir_pin,RPL.OUTPUT)

RPL.digitalWrite(dir_pin,direction)
RPL.pwmWrite(pul,speed,speed*2)

time.sleep(.5)

RPL.pinMode(pul_pin,0,0)
