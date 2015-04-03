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


def init() :
    # set print to unbuffered
    sys.stdout = os.fdopen(sys.stdout.fileno(),'w',0)
    
    print "starting legoBot"
    link.enable_servos()
    time.sleep (1.0)
    link.camera_open() 
    
    servo.testServo()

    if c.isClone :
        print "Running Clone"
    else :
        print "Running Prime"


    # wait for light

def getOutOfStartBox() :    
    
    
    drive.withStop(50, 0, .750)
    drive.withStop(50, -50, 1.75)
    drive.withStop(50, 50, .2)
    #drive.withStop(50, 0, .15)
    drive.withStop(50, 50, 0.5)
    
    servo.moveClapper (c.clapperWide, 20)
    drive.withStop(50, 50, 4)
     
def getToMidLine():
    drive.noStop(25, 25, .25)
    servo.moveClapper(c.clapperParallel, 5)
    drive.withStop(0, 0, 0) 

def crossBump():
    servo.moveClapper(c.clapperWide)
    drive.withStop(90, 90, 1.60) # poms are catapulted forward from momentum / speed
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
        drive.noStop( 55, 50, .5)
    
       


def getOutOfCorner():
    drive.withStop(25, 25, 2) 
    servo.moveClapper(c.clapperTight, 6)
    drive.withStop(-25,-50, 1.5)
    
def DEBUG( msg = "DEBUG" ) :
    link.ao()
    print msg
    link.camera_close()
    exit()

def test():
    drive.withStop(65, 50, 15)   
    
