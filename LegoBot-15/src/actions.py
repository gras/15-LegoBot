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
    #link.camera_load_config(red-green)
    #servo.moveClapper( c.clapperOpen )
    #servo.moveSorter( c.sorterCenter )
    #servo.moveKicker( c.kickerReady )
    print "We did it!!!"
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
            print "break"
            break  
    print "stop"
    drive.withStop(0, 0, 0)
    sensor.cameraTrack()
    
def getOutOfStartBox() :
    drive.withStop( -50, -100, 1 )
    drive.withStop( -100, -10, 1)
    drive.withStop(-60, 60, .2 )
    drive.withStop(20, 100, 3 )
    drive.withStop(70, 100, 1 )
    #servo.moveClapper( c.clapperClosed )

def eat() :
    servo.moveClapper(c.clapperOpen, 6)
    drive.noStop(75, 75, 1.5)
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
    print "DEBUG"
    link.camera_close()
    link.ao()
    exit()
