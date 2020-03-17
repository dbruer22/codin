import RoboPiLib as RPL
import setup

clockwise = 0
counter = 1

RPL.digitalWrite(2,clockwise)
RPL.servoWrite(2,20000)
