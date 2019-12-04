import RoboPiLib as RPL
import setup
RPL.pinMode(7, RPL.INPUT)

values = []

#for i in range(0,100):
 #  values.append(RPL.analogRead(7))
  # basic = ((sum(values) / 100) * -1) + 100
   #print basic

x = 1
sensor_pin = 16
RPL.pinMode(sensor_pin,RPL.INPUT)
while x == 1:
    an_reading = RPL.analogRead(sensor_pin)
    dig_reading = RPL.digitalRead(sensor_pin)
    print dig_reading
    #RPL.servoWrite(1, )
    #print reading
    if dig_reading == 1:
        RPL.servoWrite(1,1750 - (an_reading / 3))
        RPL.servoWrite(0,1250 + (an_reading / 3))
    elif dig_reading == 0:
        RPL.servoWrite(1,0)
        RPL.servoWrite(0,0)

    #if reading < 150:
        #RPL.servoWrite(1,1600)
    #elif reading >= 150:
        #RPL.servoWrite(1,0)
