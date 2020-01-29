import RoboPiLib
import RoboPiLib_pwm as RPL
import setup

pul_pin = 1       #Your pin #
dir_pin = 2       #Your pin #

direction = 0     #can be 0 or 1
speed = 5000      #smaller = faster

RPL.pinMode(pul_pin,RPL.PWM)
RPL.pinMode(dir_pin,RPL.OUTPUT)

RPL.digitalWrite(dir_pin,direction) #sets the motor to forwards or backwards
RPL.pwmWrite(pul_pin,speed,speed*2) #moves the motor
