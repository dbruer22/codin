import RoboPiLib as RPL
import setup
x = 1
sensor_pin = 16
RPL.pinMode(sensor_pin,RPL.INPUT)
import runner as r
while x == 1:
    reading = RPL.digitalRead(sensor_pin)
    if reading == 0:
        r.go()
    elif reading == 1:
        r.stop()
