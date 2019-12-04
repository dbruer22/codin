import RoboPiLib as RPL
import setup
RPL.pinMode(7, RPL.INPUT)

values = []

#for i in range(0,100):
 #  values.append(RPL.analogRead(7))
  # basic = ((sum(values) / 100) * -1) + 100
   #print basic

x = 1
sensor_pin = 7
RPL.pinMode(sensor_pin,RPL.INPUT)
while x == 1:
    reading = RPL.analogRead(sensor_pin)
    #RPL.servoWrite(1, )
    #print reading
    RPL.servoWrite(1,1700 - (reading / 3))
    RPL.servoWrite(0,1700 - (reading / 3))
    #if reading < 150:
        #RPL.servoWrite(1,1600)
    #elif reading >= 150:
        #RPL.servoWrite(1,0)
