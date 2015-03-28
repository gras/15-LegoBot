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



def cameraSort():
    drive.noStop(75, 75, 0.1)
    servo.moveClapper(c.clapperParallel, 10)
    count = 0
    
    while sensor.getLargestArea() < c.blobSize:
        count = count+1
        if count >3:
            #print "break"
            #break  
            count = 0
            servo.moveClapper (c.clapperOpen, 20)
            drive.withStop (50, 0, 0.5)
            servo.moveClapper (c.clapperParallel, 5)
            drive.withStop (0, 50, 1)
            drive.withStop (-80, -75, .75)
            drive.withStop (75, 75, 1)
    print "stop"
    drive.withStop(0, 0, 0)
    sensor.sortTribble()
    
def getOutOfStartBox() :
    if c.isClone:
        drive.withStop( 75, -20, 1.75 )    #1.5
        servo.moveClapper (c.clapperDrive, 20)
        drive.withStop( 75, 75, .5 )#was .5
        drive.withStop( 75, 80, .75 )# .75
        drive.withStop(0, 75, 0.5)# 0.4
        drive.withStop(75, 90, 0.5)# 75, 75
      
          
    else:
      
        drive.withStop( 75, -20, 1.5 )
        servo.moveClapper (c.clapperDrive, 20)
        drive.withStop( 75, 75, .5 )
        drive.withStop( 75, 80, .75 )
        drive.withStop(0, 75, 0.3)
        

def crossBump (): 
    drive.noStop(55,50,.5)
    for _ in range(1) :#3
        servo.moveClapper(c.clapperOpen, 6)
        servo.moveClapper(c.clapperParallel, 6)
    drive.withStop(0, 0, 0)
    sensor.sortTribble()  
    
    
def test():
    drive.withStop(75, 75, 5)   
    
def getOutOfCorner():
    drive.withStop(25, 25, .5) #make time longer!
    servo.moveClapper(c.clapperTight, 6)
    drive.withStop(-25,-50, 1.5)
    
    
def sortAndGo(num):
    # drives while opening and closing Clapper, 
    # then stops to sort tribbles
    # repeats "num" times
    for _ in range (num):
        drive.noStop(55,50,.5)
        servo.moveClapper(c.clapperOpen, 6)
        servo.moveClapper(c.clapperParallel, 6)
        drive.withStop(0, 0, 0)
        sensor.sortTribble()
    

    
def DEBUG(msg) :
    link.ao()
    print msg
    link.camera_close()
    exit()
