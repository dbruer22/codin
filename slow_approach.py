import RoboPiLib as RPL
import setup
import time

#values = []

#for i in range(0,100):
 #  values.append(RPL.analogRead(7))
  # basic = ((sum(values) / 100) * -1) + 100
   #print basic

x = 1
sensor_pin = 16
sensorpin = 7
RPL.pinMode(sensor_pin,RPL.INPUT)
while x == 1:
    an_reading = RPL.analogRead(sensorpin)
    dig_reading = RPL.digitalRead(sensor_pin)
    #print an_reading
    #RPL.servoWrite(1, )
    #print reading
    if dig_reading == 1:
        #if an_reading <= 250:
        #    RPL.servoWrite(1,1950 - ((an_reading / 1)))
        #    RPL.servoWrite(0,950 + ((an_reading / 1)))
        #elif an_reading >= 200 <= 300:
        #    RPL.servoWrite(1,1750 - (an_reading / 2))
        #    RPL.servoWrite(0,1250 + (an_reading / 2))
        #elif an_reading >= 250:
        RPL.servoWrite(1,1700 - ((an_reading / 3) - 55))
        RPL.servoWrite(0,1200 + ((an_reading / 3) + 55))
    elif dig_reading == 0:
        time.sleep(2)
        RPL.servoWrite(1,0)
        RPL.servoWrite(0,0)

    #if reading < 150:
        #RPL.servoWrite(1,1600)
    #elif reading >= 150:
        #RPL.servoWrite(1,0)
