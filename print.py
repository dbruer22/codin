import RoboPiLib as RPL
import setup
import time
x = 1
sensor_pin = 16
RPL.pinMode(sensor_pin,RPL.INPUT)
while x == 1:
    reading = RPL.digitalRead(sensor_pin)
    if reading == 0:
        RPL.servoWrite(1,1400)
        time.sleep(1)
    elif reading == 1:
        RPL.servoWrite(1,0)
print "%02d" % (RPL.digitalRead(sensor_pin))
