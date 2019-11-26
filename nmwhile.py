import RoboPiLib as RPL
import setup
import time
start = time.time()
myTime = 1
sensor = [16, 17]
while myTime <= 20:
  for fire in sensor:
    time.sleep(0.05)
    myTime = time.time() - start
    #print(myTime, 'less than 20 seconds')
    if myTime >= 20:
      print('Over 20 seconds')
      print('Self destructing in...')
      print(3)
      time.sleep(1)
      print(2)
      time.sleep(1)
      print(1)
      time.sleep(1)
      exit()
    if RPL.digitalRead(fire) == 0:
      #print('Detection')
      RPL.servoWrite(0,1590)
      time.sleep(0.5)
      RPL.servoWrite(0,1500)
      time.sleep(0.5)
      RPL.servoWrite(0,1590)
      time.sleep(0.5)
      RPL.servoWrite(0,1500)
      time.sleep(0.5)
      RPL.servoWrite(0,1590)
      time.sleep(0.5)
      RPL.servoWrite(0,1500)
