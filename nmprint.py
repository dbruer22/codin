import RoboPiLib as RPL
import setup
import time
fire_count = 0
pin = [17]
motors = [0,1]
for number in pin:
  RPL.pinMode(number,RPL.INPUT)

def execut():
  global fire_count
  fire_count += 1
  print('The motor has pulsed %s times' % (fire_count))
  RPL.servoWrite(0,1590)
  RPL.servoWrite(1,1410)
  time.sleep(1)
  RPL.servoWrite(0,1500)
  RPL.servoWrite(1,1500)

while True:
  time.sleep(0.05)
  for x in pin:
    if RPL.digitalRead(x) == 0:
      execut()
