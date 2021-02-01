
import RoboPiLib as RPL
import setup
import direction

print('Type "stop" to stop the motors and then type "exit" to close the program')

while True:
usrin = input(' ')

if usrin == 'w':
  direction.front()
elif usrin == 's':
  direction.back()
elif usrin == 'a':
  direction.left()
elif usrin == 'd':
  direction.right()
elif usrin == 'stop':
  direction.stop
else:
  print('please input a w,a,s,d,stop,exit')
