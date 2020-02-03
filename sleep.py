import RoboPiLib as RPL
import setup
import time
x = 1
while x ==1:
    RPL.servoWrite(1, 1400)
    time.sleep(1)
    RPL.servoWrite(1, 0)
    time.sleep(1) 
