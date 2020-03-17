import RoboPiLib as RPL
import setup

clockwise = 0
counter = 1

RPL.digitalWrite(2,counter)
RPL.servoWrite(2,20000)
