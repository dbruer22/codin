import RoboPiLib as RPL
import setup
portan_read = RPL.analogRead(5)
bowan_read = RPL.analogRead(7)
starboardan_read = RPL.analogRead(6)

def port_turn():
    RPL.servoWrite(1,1550)
    RPL.servoWrite(0,1550)

def star_turn():
    RPL.servoWrite(1,1450)
    RPL.servoWrite(0,1450)

def bow_move():
    RPL.servoWrite(1,1450)
    RPL.servoWrite(0,1550)

def stern_move():
    RPL.servoWrite(1,1550)
    RPL.servoWrite(0,1450)

def conditions():
    x = 1
    while x == 1:
        portan_read = RPL.analogRead(5)
        bowan_read = RPL.analogRead(7)
        starboardan_read = RPL.analogRead(6)
        if portan_read <= 350 and starboardan_read <= 350:
            stern_move()
        elif portan_read >= 350 and starboardan_read >= 350:
            bow_move()
        elif portan_read >= 350 and starboardan_read <= 349:
            star_turn()
        elif starboardan_read >= 350 and portan_read <= 349:
            port_turn()
        #print portan_read
        #print starboardan_read
conditions()
