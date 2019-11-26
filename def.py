import RoboPiLib as RPL
import setup
def run_function():
    RPL.servoWrite(1,1400)
def stop_function():
        RPL.servoWrite(1,0)
x = 1
sensor_pin = 16
RPL.pinMode(sensor_pin,RPL.INPUT)
while x == 1:
    reading = RPL.digitalRead(sensor_pin)
    if reading == 0:
        run_function()
    elif reading == 1:
        stop_function()
