import RoboPiLib as RPL
import setup
RPL.pinMode(7, RPL.INPUT)

values = []

#for i in range(0,100):
 #  values.append(RPL.analogRead(7))
  # basic = ((sum(values) / 100) * -1) + 100
   #print basic

x = 1
sensor_pin = 15
RPL.pinMode(sensor_pin,RPL.INPUT)
while x == 1:
    an_reading = RPL.analogRead(7)
    dig_reading = RPL.digitalRead(sensor_pin)
    #print dig_reading
    #RPL.servoWrite(1, )
    print an_reading
    if dig_reading == 1:
        if an_reading <= 170:
            RPL.servoWrite(1,1600)
            RPL.servoWrite(0,1400)
        elif an_reading <= 200:
            RPL.servoWrite(1,1550)
            RPL.servoWrite(0,1450)
        elif an_reading <= 250:
            RPL.servoWrite(1,1525)
            RPL.servoWrite(0,1475)
        elif an_reading <= 300:
            RPL.servoWrite(1,1510)
            RPL.servoWrite(0,1490)
    elif dig_reading == 0:
        RPL.servoWrite(1,0)
        RPL.servoWrite(0,0)

    #if reading < 150:
        #RPL.servoWrite(1,1600)
    #elif reading >= 150:
        #RPL.servoWrite(1,0)
