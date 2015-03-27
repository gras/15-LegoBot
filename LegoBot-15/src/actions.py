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

    #link.camera_load_config(red-green)
    #servo.moveClapper( c.clapperOpen )
    #servo.moveSorter( c.sorterCenter )
    #servo.moveKicker( c.kickerReady )
    
    # wait for light

def printSize():
    for I in range(20):
        print sensor.getLargestArea()

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
    sensor.cameraTrack()
    
def getOutOfStartBox() :
    if c.isClone:
        drive.withStop( 75, -20, 1.5 )
        servo.moveClapper (c.clapperDrive, 20)
        drive.withStop( 75, 75, .5 )
        drive.withStop( 75, 80, .75 )
        drive.withStop(0, 75, 0.4)
    else:
        drive.withStop( 75, -20, 1.5 )
        servo.moveClapper (c.clapperDrive, 20)
        drive.withStop( 75, 75, .5 )
        drive.withStop( 75, 80, .75 )
        drive.withStop(0, 75, 0.3)
        '''
        drive.withStop( 75, -20, 2 )
        servo.moveClapper (c.clapperDrive, 20)
        drive.withStop( 75, 75, .5 )
        drive.withStop( 75, -75, .1 )
        drive.withStop( 75, 80, .75 )
        '''
    
def crossBump (): 
    drive.noStop(50,55,.5)
    for _ in range(3) :
        servo.moveClapper(c.clapperOpen, 6)
        servo.moveClapper(c.clapperParallel, 6)
    drive.withStop(0, 0, 0)
    sensor.cameraTrack()
    
def getSecondPile ():  
    time.sleep(1)  
    drive.withStop(-20, 75, 1.5)
    sortAndGo(1)
    time.sleep(.5)
    drive.withStop(50, 50, .3)
    drive.withStop(-20, 75, 1.35)
    time.sleep(.2)
    servo.moveClapper(c.clapperOpen, 6)
    drive.withStop(75, 75, 3)
    
def test():
    drive.withStop(75, 75, 5)   
    
    
def sortAndGo(n):
    for _ in range (n):
        drive.noStop(50,55,.5)
        servo.moveClapper(c.clapperOpen, 6)
        servo.moveClapper(c.clapperParallel, 6)
        drive.withStop(0, 0, 0)
        sensor.cameraTrack()
    
    
def eat() :
    servo.moveClapper(c.clapperOpen, 6)
    drive.noStop(70, 80, .4)
    #servo.moveClapper(c.clapperParallel, 10)
    #drive.withStop (0,0,0)
    #drive.withStop(100, 100, 0.5)
    
def filter() :
    # drive.withStop(100, 100, 0.5)
    servo.moveClapper(c.clapperOpen, 6)
    drive.withStop(100, 100, 0.5)
    servo.moveClapper(c.clapperClosed, 6)

def testRun() :
    drive.withStop(100, 100, 1)
    print"we should start moving now!"
    servo.moveClapper(c.clapperWide, 3)
    servo.moveClapper(c.clapperOpen, 3)
    servo.moveClapper(c.clapperClosed, 3)
    servo.moveClapper(c.clapperTight, 3)
    print"clap over"

def grabFirstPile() :
    drive.withStop(100, 100, 3.0)
    #servo.moveClapper( c.clapperClosed )

def sort() :
    #servo.moveClapper( c.clapperClosed )
    #thread tid = link.thread_create(sensor.cameraTrack)
    #link.thread_start()
    #drive.withStop(100, 100, 1.0)
    sensor.getLargestArea()
    
def printBlobSize():
    sensor.getLargestArea()
    
    
def getTribbles() :   
    drive.noStop( 100, 100, 0.01 )
    servo.moveSorter( c.sorterLeft )
    servo.moveKicker( c.kickerOut, 2000 )
    servo.moveSorter( c.sorterCenter )
    servo.moveKicker( c.kickerReady )
    drive.noStop( 50, 100, .5 )
    drive.noStop( 100, 50, .5 )
    servo.moveSorter( c.sorterRight )
    servo.moveKicker( c.kickerOut, 2000 )
    servo.moveSorter( c.sorterCenter )
    servo.moveKicker( c.kickerReady )
    drive.withStop( 100, 100, 0.10 )
    
def DEBUG() :
    link.ao()
    print "DEBUG"
    link.camera_close()
    exit()
