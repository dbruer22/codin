import RoboPiLib as RPL
import setup
x = 1
sensor_pin = 16
RPL.pinMode(sensor_pin,RPL.INPUT)
sensorpin = 17
RPL.pinMode(sensorpin,RPL.INPUT)
while x == 1:
    reading = RPL.digitalRead(sensor_pin)
    reding = RPL.digitalRead(sensorpin)
    if reading == 0 or reding == 0:
        RPL.servoWrite(1, 1400)
    elif reading == 1 and reding == 1:
        RPL.servoWrite(1, 0)
