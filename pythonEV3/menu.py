#!/usr/bin/env python3
#The following program is my first take on python ev3. using a menu to get the robot to do different things over an ssh connection
from ev3dev.ev3 import *
#config the motors
mA = LargeMotor('outA')
mB = LargeMotor('outB')

def move():
        print('robot: speed = ' + str(speed))
        mA.run_forever(speed_sp=speed)
        mB.run_forever(speed_sp=speed)


def moveBack():
    print('robot: speed = ' + str(speed))
    mA.run_forever(speed_sp=-speed)
    mB.run_forever(speed_sp=-speed)


def stop():
        mA.stop()
        mB.stop()

def turnLeft():
    mA.run_to_rel_pos(position_sp="180",speed_sp=speed,stop_action="hold")
def turnRight():
    mB.run_to_rel_pos(position_sp="180", speed_sp=speed, stop_action="hold")

speed = int(500)

print('Hello and welcome to the robot menu:\n')
while(True):
    option = int(input('[1]move forward\n[2]move backwards\n[3]turn to the left\n[4]turn to the right[5]exit\n[6]stop robot\nuser:'))
    if(option == 1):
        #move forward
        move()
    elif(option == 2):
        #move backwards
        moveBack()
    elif(option == 3):
        #turn left
        turnLeft()
    elif(option == 4):
        #turn right
        turnRight()
        print('robot:')
    elif(option == 5):
        print('robot: EXIT')
        break
    elif(option == 6):
        stop()
    else:
        print('not a valid option. try again')

