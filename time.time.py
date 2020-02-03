import RoboPiLib as RPL
import setup
import time
x = 1
while x ==1:
    RPL.servoWrite(1, 1400)
    time.sleep(2)
    RPL.servoWrite(1, 0)
    time.sleep(2)
    RPL.servoWrite(0, 1400)
    time.sleep(3)
    RPL.servoWrite(0, 0)
    time.sleep(3)
     
