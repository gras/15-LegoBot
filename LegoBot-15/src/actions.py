'''
Created on Mar 15, 2015

@author: Dead Robot Society
'''

superSeeding = 0

import kovan as link

import constants as c 
import drive 
import servo
import sensor
import time
from constants import clapperTight

def getSuper():
    global superSeeding
    return superSeeding

def init():
    global superSeeding
    print "starting legoBot"
    if not link.camera_open():
        DEBUG("camera failed to open") 
    
    sensor.cameraTest
    servo.testServo()
    sensor.cameraTest
    drive.testGates()
    sensor.cameraTest
    # print "camera code is cleaned!"
    if c.isPrime :
        print "Running Prime"
    else :
        print "Running Clone"
    
    shutdown = 119
    print "Press the A button to start or the B button to exit or the C button for SUPERSEEDING"
    while not link.a_button() and not link.b_button() and not link.c_button():
        pass
    if link.b_button_clicked():
        DEBUG("exited")
    elif link.c_button_clicked():
        print "SUPERSEEDING MODE ACTIVATED"
        shutdown = 239
        superSeeding = 1 
    print "thank you!"
    print "max time =", shutdown 

    link.wait_for_light(0)
    link.shut_down_in(shutdown)
    c.startTime = link.seconds()
        
def getOutOfStartBox() :    
    drive.holdGateClosed(c.rightGate)
    drive.holdGateClosed(c.leftGate)
    drive.withStop(0, 75, .25)
    drive.withStop(50, 50, 0.7)
    servo.moveClapper (c.clapperWide, 50)
    drive.withStop(50, 50, 4)
    
def crossBumpNorth():

    if c.isPrime:  
        drive.withStop(25, 50, 1.0)
        servo.moveClapper(c.clapperOpen) #was clapperClosed
        drive.withStop(100, 97, 2.3) 
        servo.moveClapper(c.clapperParallel)  

        '''
        drive.withStop(35, 40, 1.0)
        servo.moveClapper(c.clapperClosed)
        drive.withStop(90, 90, 1.60) 
        servo.moveClapper(c.clapperParallel)
        drive.withStop(35, 0, .4) 
        '''
    else:
        drive.withStop(25, 50, 1.0)
        servo.moveClapper(c.clapperOpen)
        drive.withStop(100, 90, 1.60) 
        servo.moveClapper(c.clapperParallel)
 
def crossBumpSouth():
    servo.moveClapper(c.clapperOpen)
    drive.withStop(100, 90, 1.60) 
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
            servo.wiggle()
        drive.noStop( 55, 50, .5)
    sensor.sortTribble()

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
    drive.withStop(-50, -50, 1)
    drive.withStop(-50, 0, .7)
    drive.withStop(0, 100, 1.2)
    drive.holdGateOpen(c.rightGate)
      
def getOutOfFarBox(): 
    # drive.withStop(-50, -50, 1)
    # drive.withStop(0, 65, 2.5)
    if c.isPrime:
        drive.withStop(-50, -50, 1.66)
    else:
        drive.withStop(-50, -50, 1.33)
    drive.withStop(-50, 0, .7)
    drive.withStop(0, 100, 1.7)
    drive.withStop(70, 50, .65)
    servo.moveClapper (c.clapperWide, 50)
    # drive.withStop(0, 50, .25)
    drive.withStop(70, 50, 2)
    drive.closeGate(c.rightGate)
    drive.withStop(50, 50, 1.5) #was 4 

def getOutOfStartBox2():
    
    # The series of turns that gets us out of the start box for the second time
    if c.isPrime:
        drive.withStop(-50, -50, 1)
        drive.withStop(-50, 0, .7)
        drive.withStop(-50, 50, .5) 
        drive.withStop(20, 50, .3)
        drive.withStop(0, 80, 1)
        drive.withStop(35, 45, 1.0)
    
        drive.withStop(40, 40, 1.0)
        drive.withStop(90, 90, 2)  

    else:
        drive.withStop(-50, -50, 1)
        drive.withStop(-50, 0, .7)
        drive.withStop(-50, 50, .5) 
        drive.withStop(20, 40, .3)
        drive.withStop(0, 80, .6)
        drive.withStop(35, 45, 1.0)
    
        drive.withStop(40, 40, 1.0)
        drive.withStop(90, 90, 2)  


def startToTurnTwo():
    # back out of corner
    
    servo.moveClapper (c.clapperTight, 50)
    drive.withStop(-50, -50, 1)
    drive.withStop(-50, 0, .7)
    drive.withStop(0, 100, 1.2)
    drive.withStop(60, 0, .5)
    drive.withStop(0, 60, .6)
    drive.withStop(-60, 0, .5)
    drive.withStop(-60, -60, 1)
    drive.holdGateOpen(c.leftGate)
    drive.withStop(50, 0, .3)
    drive.withStop(50, 20, .5)

def jettison():
    while True: 
        find = sensor.sortTribble()
        if find:
            print "pom found"
            servo.wiggle()
        else:
            print "all good"
            break 

def thirdDriveIntoWall(var):
    # drives forward along a wall until the touch sensor in front bumps into something
    drive.noStop(100, 100, .05)
    done = link.seconds()+ var
    while link.digital(c.bumper) == 0:
        if link.seconds() > done:
            break
    drive.withStop(0, 0, 0)
    print "hit wall"

def theWiggleMove():
    print "wiggle?"
    time.sleep(.5)
    drive.openGate(c.rightGate)
    drive.withStop(20, -20, .4)
    drive.withStop(-20, 20, .4)
    drive.withStop(20, 20, .4)
    print "wiggle complete?"

def theSpinMove():
    drive.holdGateClosed(c.leftGate)
    drive.withStop(100, -100, .5)
    drive.withStop(-50, -80, 2)
    drive.withStop(50, 80, 2)

#SUPERSEED - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

def lineFollow():
    servo.moveClapper(c.clapperTight, 10)
    timez = link.seconds() + 10
    while not link.a_button() and not link.b_button() and link.seconds() < timez:
        '''
        frontHat = sensor.frontHat()
        if frontHat:
            print "***frontYes"
            drive.noStop(100, 25, 0)
        else:
            print "frontNo"
            drive.noStop(25, 50, 0)
        '''
        backHat = sensor.backHat()
        if backHat:
            print "***backYes"
            drive.noStop(-100, -25, 0)
        else:
            print "backNo"
            drive.noStop(-25, -50, 0)
        sensor.findTape()
        tape = sensor.findTape()
        if tape:
            drive.withStop(-50, -65, 7)
            break
        else:
            pass

# uses the tophat code to line
def lineUsUp():
    servo.moveClapper(clapperTight, 10)
    drive.holdGateClosed(c.rightGate)
    drive.withStop(-10, -100, 2.5)
    drive.withStop(50, -65, 1.25)
    drive.withStop(-50, -50, 5)
    drive.holdGateOpen(c.rightGate)
    drive.withStop(50, 0, 2)
    drive.withStop(70, 70, 3.5)
    drive.topStopFront(40, 40)
    DEBUG("NEIN")
    drive.holdGateClosed(c.rightGate)
    
    drive.topStopFront(50, 50)
    drive.topStopBack(50, -50)

# still unsure as to the final use
def getUsSet():
    drive.withStop(-50, 50, 1.25)
    drive.withStop(50, 50, 3)
        
def testFollow():
    while not link.a_button() and not link.b_button():
        frontHat = sensor.frontHat()
        if frontHat:
            print "***frontYes"
        else:
            print "frontNo"
        
        backHat = sensor.backHat()
        if backHat:
            print "***backYes"
        else:
            print "backNo"
            
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

def pause():
    print "pause"
    time.sleep(7)

def DEBUG( msg = "DEBUG" ) :
    link.ao()
    print msg
    link.camera_close()
    exit()

def shutdown():
    link.ao()
    print "elapsed time:" 
    print link.seconds() - c.startTime
    link.camera_close()
    exit() 