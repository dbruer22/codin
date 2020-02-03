#runs it
import RoboPiLib as RPL
import setup

def go():
    RPL.servoWrite(1,1400)

def stop():
    RPL.servoWrite(1,0)
