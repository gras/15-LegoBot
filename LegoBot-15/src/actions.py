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
from constants import rightGate, leftGate


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


    # wait for light

def getOutOfStartBox() :    
    
    drive.withStop(30, 0, .750)
    
    if c.isPrime:
        drive.withStop(50, -65, 1.75)
    else: 
        drive.withStop(50, -50, 1.65)# was 1.45
    
   
    
    drive.withStop(50, 50, 0.7)
    
    servo.moveClapper (c.clapperWide, 50)
    
    if c.isPrime:
        drive.withStop(50, 50, 4)
    else:
        drive.withStop(50, 65, 3)
        drive.withStop(-50, 50, .5)
    
def getToMidLine():
    drive.noStop(25, 25, .25)
    servo.moveClapper(c.clapperParallel, 5)
    drive.withStop(0, 0, 0) 

def crossBump():
    servo.moveClapper(c.clapperClosed)
    if c.isPrime:
        drive.withStop(90, 90, 1.60) 
    else:
        drive.withStop(90, 90, 1.30)
        drive.withStop(45, 0, .35)
    
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
            servo.moveClapper(c.clapperClosed, 200)
            drive.withStop(50, -25, .65)
            drive.noStop( 55, 50, .3)
            #DEBUG("Stop")
        drive.noStop( 55, 50, .5)
    
    sensor.sortTribble()
    
def getOutOfCorner():
    drive.withStop(25, 25, 2) 
    servo.moveClapper(c.clapperTight, 6)
    drive.withStop(-50,-100, 1.5)
    
def DEBUG( msg = "DEBUG" ) :
    link.ao()
    print msg
    link.camera_close()
    exit()
    
def driveIntoWall():
    # drives forward along a wall until the touch sensor in front bumps into something

    drive.noStop(65, 50, .05)
    while link.digital(c.bumper) == 0:
        pass
    drive.withStop(0, 0, 0)
    print "hit wall"
    
def secondDriveIntoWall():
    # drives forward along a wall until the touch sensor in front bumps into something
    drive.noStop(65, 50, .05)
    while link.digital(c.bumper) == 0:
        pass
    drive.withStop(0, 0, 0)
    print "hit wall again"
    
def startToTurn():
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
        drive.withStop(0, 50, .5)
        drive.withStop(50, 50, 1)
        drive.withStop(0, 85, 1.5)   
    '''
    drive.withStop(-30, -30, 2.0)
    
    #drive.withStop(-60, -25, 1.5)
    if c.isPrime:
        drive.withStop(0, -100, 1.0)
    else:
        drive.withStop(0, -100, 1.0)#1.5 
    
    
    drive.withStop( -100, 0, 1.0)
    
    if c.isPrime:
        drive.withStop( 75, 75, 0.75)
        drive.withStop( 20, 100, 1.5)
    else:
        drive.withStop( 75, 75, 0.5)
        drive.withStop( 10, 100, 2.75)
'''



def scoreRedTribbles():
    drive.openGate(c.rightGate)
    driveIntoWall()
    drive.withStop(-50, -50, 1.5)
    drive.withStop(0, 50, 2.5)
    
def scoreGreenTribbles():
    drive.openGate(c.leftGate)
    driveIntoWall()
    drive.closeGate(c.leftGate)
    
    '''
    drive.withStop(-50, -50, 1.5)
    drive.withStop(0, 50, 2.5)    
    '''
    
def getSecondPile(): 
    servo.moveClapper(c.clapperWide, 50)
    drive.withStop(50, 65, 2)
    drive.closeGate(rightGate)    
    drive.withStop(65, 50, 4)
    servo.moveClapper(c.clapperParallel)

    
def test():
    drive.withStop(65, 50, 15)   

def startToTurnTwo():
    for _ in range(3):
        drive.withStop(0, -100, .5)
        drive.withStop(-80, 0, .5)
    drive.openGate(leftGate)
    drive.withStop(0, 50, .5)
    drive.withStop(50, 50, 1)
    drive.withStop(0, 85, 1.5)
    
    
def thirdDriveIntoWall():
    # drives forward along a wall until the touch sensor in front bumps into something
    drive.noStop(55, 50, .05)
    while link.digital(c.bumper) == 0:
        pass
    drive.withStop(0, 0, 0)
    drive.closeGate(leftGate)
    print "hit wall again again"