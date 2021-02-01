import RoboPiLib as RPL
import setup
###EDIT THESE IF NEEDED
L = 0
R = 1
motors = [0,1] ###If extra motors add pin # here

def front():
  RPL.servoWrite(L,1600)
  RPL.servoWrite(R,1400)

def left():
  RPL.servoWrite(L,1500)
  RPL.servoWrite(R,1400)

def right():
  RPL.servoWrite(L,1600)
  RPL.servoWrite(R,1500)

def back():
  RPL.servoWrite(L,1400)
  RPL.servoWrite(R,1600)

def stop():
  for x in motors:
    RPL.servoWrite(x,1500)
    print("disabling pin # %s" % (x))
