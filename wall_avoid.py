import RoboPiLib as RPL
import setup
import time
def wall_avoid_varibles():
    x = 1
    RPL.pinMode(16,RPL.INPUT)
    an_reading = RPL.analogRead(7)
    bow_read = RPL.digitalRead(16)
    starboard_read = RPL.digitalRead(15)
    port_read = RPL.digitalRead(14)
    port_side = 0
    starboard_side = 1
    global bow_read, starboard_read, port_read, an_reading, x, port_side, starboard_side
wall_avoid_varibles()

def port_move():
    wall_avoid_varibles()
    RPL.servoWrite(starboard_side,1450)
    RPL.servoWrite(port_side,1550)
def starboard_move():
    wall_avoid_varibles()
    RPL.servoWrite(starboard_side,1550)
    RPL.servoWrite(port_side,1450)
def stern_move():
    wall_avoid_varibles()
    RPL.servoWrite(starboard_side,1550)
    RPL.servoWrite(port_side,1450)
def bow_move():
    wall_avoid_varibles()
    RPL.servoWrite(1,1700 - ((an_reading / 3) - 55))
    RPL.servoWrite(0,1200 + ((an_reading / 3) + 55))
def conditions():
    wall_avoid_varibles()
    if bow_read == 0 and starboard_read == 0 and port_read == 1:
        port_move()
    elif bow_read == 1 and starboard_read == 0 and port_read == 1:
        port_move()
    elif bow_read == 0 and starboard_read == 1 and port_read == 0:
        starboard_move()
    elif bow_read == 1 and starboard_read == 1 and port_read == 0:
        starboard_move()
    elif bow_read == 0 and starboard_read == 1 and port_read == 1:
        bow_move()
    elif bow_read == 0 and starboard_read == 0 and port_read == 0:
        bow_move()
    else:
        stern_move()
conditions()
    #elif bow_read == 0 and starboard_read == 1 and port_read == 0:
    #    bow_move()
    #elif bow_read == 0 and starboard_read == 0 and port_read == 1:
    #    bow_move()

def starboard_conditions():
    if bow_read == 0 and starboard_read == 1 and port_read == 0:
        starboard_move()
    elif bow_read == 1 and starboard_read == 1 and port_read == 0:
        starboard_move()

#while x == 1:
#    if bow_read or starboard_read or port_read == 1:
#        RPL.servoWrite(1,1700 - ((an_reading / 3) - 55))
#        RPL.servoWrite(0,1200 + ((an_reading / 3) + 55))
#    elif dig_reading or RPL.digitalRead(15) or RPL.digitalRead(14) == 0:
#        if RPL.digitalRead(15) == 1:
#            RPL.servoWrite(1,1450)
#            RPL.servoWrite(0,1550)
#        elif RPL.digitalRead(15) == 0:
#            RPL.servoWrite(1,1470)
#            RPL.servoWrite(0,1530)
#        elif RPL.digitalRead(14) == 1:
#            RPL.servoWrite(1,1550)
#            RPL.servoWrite(0,1450)
#        elif RPL.digitalRead(14) == 0:
#            RPL.servoWrite(1,1550)
#            RPL.servoWrite(0,1450)
