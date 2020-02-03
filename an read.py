import RoboPiLib as RPL
import setup
RPL.pinMode(7, RPL.INPUT)

values = []

for i in range(0,100):
   values.append(RPL.analogRead(7))
print sum(values) / 100
