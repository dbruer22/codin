import RoboPiLib as RPL
import setup
import time
start - time.time()
myTime = 1
sensor_pin = 16
RPL.pinMode(sensor_pin,RPL.INPUT)
while myTime <= 20:
    for fire in sensor:
        time.sleep()
    myTime time.time() - start
    reading = RPL.digitalRead(sensor_pin)
    if myTime >= 20:
        print "good bye"
        exit()
    if reading == 0:
        RPL.servoWrite(1,1400)
        time.sleep(1)
        RPL.servoWrite(1,0)
        time.sleep(1)
        RPL.servoWrite(1,1400)
        time.sleep(1)
        RPL.servoWrite(1,0)
        time.sleep(1)
        RPL.servoWrite(1,1400)
        time.sleep(1)
        RPL.servoWrite(1,0)
    elif reading == 1:
        RPL.servoWrite(1,0)
