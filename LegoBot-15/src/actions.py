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
    
    if c.isClone:
        drive.withStop( 75, -20, 1.50 )  # was ( 75, -20, 1.75 )   
        servo.moveClapper (c.clapperDrive, 20)        
        drive.withStop( 80, 75, .5 )#was 75, 75, .5
        drive.withStop( 80, 85, .75 )# 75, 85, .75
        drive.withStop(0, 60, 0.5)# 0, 75, 0.5        
        drive.withStop(75, 90, 0.5)# 75, 90, 0.5
    else:
        drive.withStop(50, 0, .750)
        drive.withStop(50, -50, 1.75)
        #DEBUG("stop")
        #drive.withStop( 75, -20, 3.0 )    #1.5
        servo.moveClapper (c.clapperWide, 20)
        drive.withStop(50, 50, 3.5)
         
def getToMidLine():
    drive.withStop(40, 50, 3)       
 
def crossBump (): 
    drive.noStop(70,50,.5)
    for _ in range(1) :#3
        servo.moveClapper(c.clapperOpen, 6)
        servo.moveClapper(c.clapperParallel, 6)
    drive.withStop(0, 0, 0)
    sensor.sortTribble()      
    
def sortAndGo(num):
    # drives while opening and closing Clapper, 
    # then stops to sort tribbles
    # repeats "num" times
    if c.isClone:
        for _ in range (num):
            drive.noStop(55,50,.5)
            servo.moveClapper(c.clapperOpen, 6)
            servo.moveClapper(c.clapperParallel, 6)
            drive.withStop(0, 0, 0)
            sensor.sortTribble()
    else: 
        for _ in range (num):
            drive.noStop( 55, 50, .5)
            servo.moveClapper(c.clapperOpen, 6)
            servo.moveClapper(c.clapperParallel, 6)
            drive.withStop(0, 0, 0)
            sensor.sortTribble()

def getOutOfCorner():
    drive.withStop(25, 25, 2) #make time longer!
    servo.moveClapper(c.clapperTight, 6)
    drive.withStop(-25,-50, 1.5)
    
def DEBUG( msg = "DEBUG" ) :
    link.ao()
    print msg
    link.camera_close()
    exit()

def test():
    drive.withStop(75, 75, 5)   
    
