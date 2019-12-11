import RoboPiLib as RPL
import setup
portan_read = RPL.analogRead(5)
bowan_read = RPL.analogRead(7)
starboardan_read = RPL.analogRead(6)

def conditions():
    if portan_read and starboardan_read <= 350:
        RPL.servoWrite(1,1550)
        RPL.servoWrite(0,1450)
    elif portan_read and starboardan_read >= 350:
        RPL.servoWrite(1,1550)
        RPL.servoWrite(0,1450)
    elif portan_read >= 350 and starboardan_read < 350:
        RPL.servoWrite(1,1550)
        RPL.servoWrite(0,1550)
    elif starboardan_read >= 350 and portan_read < 350:
        RPL.servoWrite(1,1450)
        RPL.servoWrite(0,1450)
    print portan_read
conditions()
