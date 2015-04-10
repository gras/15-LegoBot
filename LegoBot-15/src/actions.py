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
from kovan import msleep
from time import sleep


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
    time.sleep(2)

def getOutOfStartBox() :    
    drive.withStop(0, 75, .25)
    drive.withStop(50, 50, 0.7)
    servo.moveClapper (c.clapperWide, 50)
    drive.withStop(50, 50, 4)
    
def getToMidLine():
    drive.withStop(25, 50, 1.0)
    
def crossBumpNorth():
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
            servo.moveClapper(c.clapperDrive, 200)
            drive.withStop(-50, 25, .5)
            servo.moveClapper(c.clapperOpen, 150) #200 #was closed
            drive.withStop(50, -25, .65)
            drive.noStop( 55, 50, .3)
            servo.moveClapper(c.clapperClosed)
            #DEBUG("Stop")
        drive.noStop( 55, 50, .5)
    sensor.sortTribble()
    
def driveIntoWall():
    # drives forward along a wall until the touch sensor in front bumps into something
    drive.noStop(65, 50, .05)
    while link.digital(c.bumper) == 0:
        pass
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
    drive.withStop(0, 50, .25) #50-75
    drive.withStop(70, 50, 1.5)
    #servo.moveClapper (c.clapperWide, 50)
    drive.closeGate(c.rightGate)
    
    if c.isPrime:
        drive.withStop(50, 50, 3.5) #was 4 
    else:
        drive.withStop(50, 65, 3)
        drive.withStop(-50, 50, .5)
    drive.closeGate(c.rightGate)
    
def startToTurnTwo():
    for _ in range(3):
        servo.moveClapper (c.clapperTight, 50)
        drive.withStop(0, -100, .5)
        drive.withStop(-80, 0, .5)
    drive.withStop(0, 50, .5)
    drive.withStop(50, 50, 1)
    drive.withStop(0, 85, 1.5)
    drive.withStop(-30, 30, .7)
    drive.withStop(-30, -30, 1)
    drive.withStop(0, -60, .5)
    drive.holdGateOpen(c.leftGate)
   
def thirdDriveIntoWall():
    # drives forward along a wall until the touch sensor in front bumps into something
    drive.noStop(55, 50, .05)
    while link.digital(c.bumper) == 0:
        pass
    drive.withStop(0, 0, 0)
    drive.closeGate(c.leftGate)
    print "hit wall again again"

def DEBUG( msg = "DEBUG" ) :
    link.ao()
    print msg
    link.camera_close()
    exit()