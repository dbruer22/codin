import RoboPiLib as RPL
import setup
import time
x = 1
sensor_pin = 16
sensorpin = 7
RPL.pinMode(sensor_pin,RPL.INPUT)
while x == 1:
    an_reading = RPL.analogRead(sensorpin)
    dig_reading = RPL.digitalRead(sensor_pin)
    if dig_reading == 1:
        RPL.servoWrite(1,1700 - ((an_reading / 3) - 55))
        RPL.servoWrite(0,1200 + ((an_reading / 3) + 55))
    elif dig_reading == 0:
        time.sleep(2)
        RPL.servoWrite(1,0)
        RPL.servoWrite(0,0)
