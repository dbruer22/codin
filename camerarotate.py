import RoboPiLib as RPL
import setup
w = 'w'
x = 0
while x == 0:
    while True:
        usrin = input()

        if usrin == 'w':
            print 'you pressed w'
        else:
            print 'thats not a w'
