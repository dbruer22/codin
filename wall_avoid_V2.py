import RoboPiLib as RPL
import setup
portan_read = RPL.analogRead(5)
bowan_read = RPL.analogRead(7)
starboardan_read = RPL.analogRead(6)

def conditions():
    x = 1
    while x == 1:
        if portan_read <= 350 and starboardan_read <= 350:
            RPL.servoWrite(1,1400)
            RPL.servoWrite(0,1600)
        elif portan_read >= 350 and starboardan_read >= 350:
            RPL.servoWrite(1,1600)
            RPL.servoWrite(0,1400)
        elif portan_read >= 350 and starboardan_read <= 349:
            RPL.servoWrite(1,1400)
            RPL.servoWrite(0,1400)
        elif starboardan_read >= 350 and portan_read <= 349:
            RPL.servoWrite(1,1600)
            RPL.servoWrite(0,1600)
    #print portan_read
    #print starboardan_read
conditions()
