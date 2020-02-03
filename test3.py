import RoboPiLib as RPL
import setup
x = 1
L = 1 #Left Motor
R = 0 # Right Motor
LS = 16 #Left Sensor
RS = 17 #Right Sensor
RPL.pinMode(LS,RPL.INPUT)
RPL.pinMode(RS,RPL.INPUT)

def left(): #only left motor controls
if readingL == READING:
RPL.servoWrite(L, SPEED)
elif readingL == 1:
RPL.servoWrite(L, SPEED)

def right(): #only right motor controls
if readingR == READING:
RPL.servoWrite(R, SPEED)
elif readingR == 1:
RPL.servoWrite(R, SPEED)

def both(): #instructions for when both motors are set off
RPL.servoWrite(L, SPEED)
RPL.servoWrite(R, SPEED)

def none():  #instructions for what to do when no motors are set off
RPL.servoWrite(L, SPEED)
RPL.servoWrite(R, SPEED)

while x == 1:
readingL = RPL.digitalRead(LS)
readingR = RPL.digitalRead(RS)
if readingL == READING and readingR == READING:
both()
elif readingL == READING and readingR == READING:
none()
else:
left()
right()
