'''
Created on Mar 15, 2015

@author: Dead Robot Society
'''

import os
import sys

import kovan as link

import constants as c 
import drive 
import servo
import sensor
import time
from drive import holdGateClosed
from servo import moveServo, moveSorter

def init() :
    # set print to unbuffered
    sys.stdout = os.fdopen(sys.stdout.fileno(),'w',0)
    
    print "starting legoBot"
    link.enable_servos()
    time.sleep (1.0)
    if not link.camera_open():
        DEBUG("camera failed to open") 
    
    servo.testServo()
    drive.testGates()

    if c.isPrime :
        print "Running Prime"
    else :
        print "Running Clone"


    #link.wait for light()
    # time.sleep(2)
    print "please press the 'A' button to start"
    while not link.a_button():
        pass
    print "thank you!"

def getOutOfStartBox() :    
    drive.withStop(0, 75, .25)
    drive.withStop(50, 50, 0.7)
    servo.moveClapper (c.clapperWide, 50)
    drive.withStop(50, 50, 4)
    
def crossBumpNorth():
    drive.withStop(25, 50, 1.0)
    servo.moveClapper(c.clapperClosed)
    drive.withStop(90, 90, 1.60) 
    servo.moveClapper(c.clapperParallel)

def crossBumpSouth():
    servo.moveClapper(c.clapperClosed)
    drive.withStop(90, 90, 1.60) 
    servo.moveClapper(c.clapperParallel)
    
def sortAndGo(num):
    # drives while opening and closing Clapper, 
    # then stops to sort tribbles
    # repeats "num" times
    pomsSorted = 0 
    while not link.digital(c.bumper) and pomsSorted < num:
        drive.withStop(0, 0, 0)
        found = sensor.sortTribble()
        if found:
            print "pom found"
            pomsSorted += 1 
            print "poms sorted", pomsSorted
        else:
            print "wiggle"
            servo.moveSorter(c.sorterRightish, 100)
            servo.moveSorter(c.sorterLeftish, 100)
            servo.moveSorter(c.sorterCenter, 100)
            servo.moveClapper(c.clapperDrive, 200)
            drive.withStop(-50, 25, .5)
            servo.moveClapper(c.clapperOpen, 150) #200 #was closed
            drive.withStop(50, -25, .65)
            drive.noStop( 55, 50, .3)
            servo.moveClapper(c.clapperClosed)
            #DEBUG("Stop")
        drive.noStop( 55, 50, .5)
    sensor.sortTribble()

def jettison():
    while True: 
        find = sensor.sortTribble()
        if find:
            print "pom found"
            servo.moveSorter(c.sorterRightish, 100)
            servo.moveSorter(c.sorterLeftish, 100)
            servo.moveSorter(c.sorterCenter, 100)
            servo.moveClapper(c.clapperDrive, 200)
            drive.withStop(-50, 25, .5)
            servo.moveClapper(c.clapperOpen, 150)
            drive.withStop(50, -25, .65)
            drive.noStop( 55, 50, .3)
            servo.moveClapper(c.clapperClosed)
            drive.withStop(20, 20, .2)
        else:
            print "all good"
            break 

def driveIntoWall(var):
    # drives forward along a wall until the touch sensor in front bumps into something
    drive.noStop(65, 50, .05)
    done = link.seconds()+ var
    while link.digital(c.bumper) == 0:
        if link.seconds() > done:
            break
    drive.withStop(0, 0, 0)
    print "hit wall"

def startToTurn():
    link.set_servo_position(c.clapper, c.clapperTight)
    if c.isPrime:
        for _ in range(3):
            drive.withStop(0, -100, .5)
            drive.withStop(-80, 0, .5)
        drive.withStop(0, 50, .5)
        drive.withStop(50, 50, 1)
        drive.withStop(0, 85, 1.5)
    else:
        for _ in range(3):
            drive.withStop(0, -100, .5)
            drive.withStop(-80, 0, .5)
        drive.withStop(0, 50, .5) # needs to be more # was 30
        drive.withStop(50, 50, 1)
        drive.withStop(0, 85, 1.5)   
    drive.openGate(c.rightGate)
      
def getOutOfSecondBox():
    drive.withStop(-50, -50, 1.5)
    drive.withStop(0, 50, 2.5)
    servo.moveClapper (c.clapperWide, 50)
    drive.withStop(0, 50, .25)
    drive.withStop(70, 50, 2.65)
    drive.closeGate(c.rightGate)
    
    if c.isPrime:
        drive.withStop(50, 50, 1.5) #was 4 
    else:
        drive.withStop(50, 65, 3)
        drive.withStop(-50, 50, .5)
    drive.closeGate(c.rightGate)

def getOutOfThirdBox():
    drive.holdGateClosed(c.rightGate)
    drive.withStop(-50, -50, 1.5)
    drive.withStop(0, 100, 2)
    # servo.moveClapper (c.clapperWide, 50)
    # drive.withStop(0, 50, 2.5)
    drive.withStop(70, 50, 2.65)
    if c.isPrime:
        drive.withStop(50, 50, 1.5) #was 4 
    else:
        drive.withStop(50, 65, 3)
        drive.withStop(-50, 50, .5)
    drive.closeGate(c.rightGate)
    # drive.withStop(50, 50, 4)
    
def startToTurnTwo():
    # back out of corner
    for _ in range(3):
        servo.moveClapper (c.clapperTight, 50)
        drive.withStop(0, -100, .5)
        drive.withStop(-80, 0, .5)
    drive.withStop(0, 50, .5)
    drive.withStop(50, 50, 1)
    drive.withStop(0, 85, 1.5)
    drive.withStop(-30, 30, .7)
    # drive backwards into wall
    drive.withStop(-30, -30, 1)
    drive.withStop(0, -60, 1.5)
    drive.holdGateOpen(c.leftGate)
    drive.withStop(60, 20, 2)
   
def thirdDriveIntoWall():
    # drives forward along a wall until the touch sensor in front bumps into something
    drive.noStop(55, 50, .05)
    while link.digital(c.bumper) == 0:
        pass
    drive.withStop(0, 0, 0)
    drive.closeGate(c.leftGate)
    print "hit wall again again"

def pause():
    print "pause"
    time.sleep(7)

def DEBUG( msg = "DEBUG" ) :
    link.ao()
    print msg
    link.camera_close()
    exit()