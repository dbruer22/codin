import RoboPiLib as RPL
RPL.RoboPiInit("/dev/ttyAMA0",115200)

import sys, tty, termios, signal

######################
## Motor Establishment
######################

motorL = 0
motorR = 1

motorR_forward = 1500
motorR_backward = 1000
motorL_forward = 1000
motorL_backward = 2000

try:
  RPL.pinMode(motorL,RPL.SERVO)
  RPL.servoWrite(motorL,1500)
  RPL.pinMode(motorR,RPL.SERVO)
  RPL.servoWrite(motorR,1500)
except:
  pass

######################
## Individual commands
######################

def forward():
  RPL.servoWrite(motorR,motorL_forward)
  RPL.servoWrite(motorL,motorR_forward)

def reverse():
  RPL.servoWrite(motorL,motorL_backward)
  RPL.servoWrite(motorR,motorR_forward)

def print_speed():
  print '--FORWARD: Left Motor: ', motorL_forward, ' Right Motor: ', motorR_forward, '\r'
  print '  BACKWARD: Left Motor: ', motorR_backward, ' Right Motor: ', motorL_backward, '\r'

def forwardSpeedChanges(change, mn = 1400, mx = 1600):
  global motorR_forward
  global motorL_forward
  motorR_forward += change
  motorL_forward += change
  motorL_forward = max(min(motorL_forward, mx), mn)
  motorR_forward = max(min(motorR_forward, mx), mn)
  print_speed()

def forwardSpeedChangeReset():
    global motorR_forward
    global motorL_forward
    motorR_forward = 1000
    print_speed()

def print_motor():
    print motorR

def motorchange(change, mn = 0, mx = 5):
  global motorR
  motorR = change

  print_motor()

def stopAll():
  try:
    RPL.servoWrite(motorL,400)
    RPL.servoWrite(motorR,motorR_forward)
  except:
    print "error except"
    pass


fd = sys.stdin.fileno() # I don't know what this does
old_settings = termios.tcgetattr(fd) # this records the existing console settings that are later changed with the tty.setraw... line so that they can be replaced when the loop ends

######################################
## Other motor commands should go here
######################################

def interrupted(signum, frame): # this is the method called at the end of the alarm
  stopAll()

signal.signal(signal.SIGALRM, interrupted) # this calls the 'interrupted' method when the alarm goes off
tty.setraw(sys.stdin.fileno()) # this sets the style of the input

print "Ready To Drive! Press * to quit.\r"
## the SHORT_TIMEOUT needs to be greater than the press delay on your keyboard
## on your computer, set the delay to 250 ms with `xset r rate 250 20`
SHORT_TIMEOUT = 0.255 # number of seconds your want for timeout
while True:
  signal.setitimer(signal.ITIMER_REAL,SHORT_TIMEOUT) # this sets the alarm
  ch = sys.stdin.read(1) # this reads one character of input without requiring an enter keypress
  signal.setitimer(signal.ITIMER_REAL,0) # this turns off the alarm
  if ch == '*': # pressing the asterisk key kills the process
    termios.tcsetattr(fd, termios.TCSADRAIN, old_settings) # this resets the console settings
    break # this ends the loop
  else:
    global motorR_forward
    if ch == 'a':
      while ch == 'a':
          forwardSpeedChanges(200)
          forward()
          break
      motorR_forward = 0
    elif ch == "r":
      motorR_forward = 0
    elif ch == "d":
     while ch == 'd':
         forwardSpeedChanges(-200)
         forward()
         break
     motorR_forward = 0

    elif ch == "1":
      motorchange(1)
    elif ch == "2":
      motorchange(2)
    elif ch == "3":
      motorchange(3)
    elif ch == "4":
      motorchange(4)
    else:
      stopAll()
