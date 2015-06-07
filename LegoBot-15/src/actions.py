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
    # fix crash caused by unclean camera calls
    '''
    from subprocess import call
    call(["killall","python"])
    print "cleaned camera code"
    '''
    # set print to unbuffered
    sys.stdout = os.fdopen(sys.stdout.fileno(),'w',0)
    
    print "starting legoBot"
    link.enable_servos()
    time.sleep (1.0)
    if not link.camera_open():
        DEBUG("camera failed to open") 
    
    print "testing camera"
    link.camera_update()
    time.sleep(.1)
    link.camera_update()
    
    servo.testServo() 
    
    print "testing camera"
    link.camera_update()
    time.sleep(.1)
    link.camera_update()
    drive.testGates()
    
    print "testing camera"
    link.camera_update()
    time.sleep(.1)
    link.camera_update()
    
    link.disable_servos()
    # print "camera code is cleaned!"
    if c.isPrime :
        print "Running Prime"
    else :
        print "Running Clone"


    # time.sleep(2)
    '''
    print "Press the A button to start or the B button to exit"
    while not link.a_button() and not link.b_button():
        pass
    if link.b_button_clicked():
        DEBUG("exited")
    print "thank you!"
    '''
    # link.wait_for_light(0)
    link.shut_down_in(119.0)
    c.startTime = link.seconds()
    link.enable_servos()
        
def getOutOfStartBox() :    
    drive.holdGateClosed(c.rightGate)
    drive.holdGateClosed(c.leftGate)
    drive.withStop(0, 75, .25)
    drive.withStop(50, 50, 0.7)
    servo.moveClapper (c.clapperWide, 50)
    drive.withStop(50, 50, 4)
    
def crossBumpNorth():

    if c.isPrime:   
        # drive.withStop(25, 50, 1.0)
        drive.withStop(35, 40, 1.0)
        servo.moveClapper(c.clapperClosed)
        drive.withStop(90, 90, 1.60) 
        servo.moveClapper(c.clapperParallel)
        drive.withStop(35, 0, .4) 
    else:
        drive.withStop(25, 50, 1.0)
        servo.moveClapper(c.clapperClosed)
        drive.withStop(100, 90, 1.60) 
        servo.moveClapper(c.clapperParallel)  
    
def crossBumpSouth():
    servo.moveClapper(c.clapperClosed)
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
            servo.moveSorter(c.sorterRightish, 100)
            servo.moveSorter(c.sorterLeftish, 100)
            servo.moveSorter(c.sorterCenter, 100)
            servo.moveClapper(c.clapperDrive, 200)
            drive.withStop(-50, 25, .5)
            servo.moveClapper(c.clapperOpen, 150) #200 #was closed
            drive.withStop(50, -25, .65)
            drive.noStop( 55, 50, .3)
            servo.moveClapper(c.clapperClosed)
            # DEBUG("Stop")
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
    '''for _ in range(3):
        drive.withStop(0, -100, .5)
        drive.withStop(-80, 0, .5)'''
    '''drive.withStop(0, 50, .5)
    drive.withStop(50, 50, 1)
    drive.withStop(0, 85, 1.5)'''
    drive.withStop(-50, -50, 1)
    drive.withStop(-50, 0, .7)
    drive.withStop(0, 100, 1.2)
    drive.openGate(c.rightGate)
      
def getOutOfSecondBox(): 
    # drive.withStop(-50, -50, 1)
    # drive.withStop(0, 65, 2.5)
    drive.withStop(-50, -50, 1)
    drive.withStop(-50, 0, .7)
    drive.withStop(0, 100, 1.2)
    drive.withStop(70, 50, .65)
    servo.moveClapper (c.clapperWide, 50)
    # drive.withStop(0, 50, .25)
    drive.withStop(70, 50, 2)
    drive.closeGate(c.rightGate)
    drive.withStop(50, 50, 1.5) #was 4 

def getOutOfThirdBox():
    '''
    drive.holdGateClosed(c.rightGate)
    drive.withStop(-50, -50, 1.5)
    drive.withStop(-20, 80, .5)
    drive.withStop(0, 100, 1.5)
    # servo.moveClapper (c.clapperWide, 50)
    # drive.withStop(0, 50, 2.5)
    
    if c.isPrime:
        drive.withStop(70, 50, 2.65)
        drive.withStop(50, 50, 1.5) #was 4 
    
    else:
        drive.withStop(0, 100, .5)
        drive.withStop(70, 50, 2.65)
        drive.withStop(50, 60, 1.5)
    
    drive.closeGate(c.rightGate)
    # drive.withStop(50, 50, 4)
    '''
    
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
    '''
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
    '''
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

#SUPERSEED

def lineFollow():
    timez = time.time()
    timerz = timez + 20
    while not link.a_button() and not link.b_button():
        frontHat = sensor.frontHat()
        if frontHat:
            print "***frontYes"
            drive.withStop(70, 25, .1)
        else:
            print "frontNo"
            drive.withStop(25, 70, .1)
        
        backHat = sensor.backHat()
        if backHat:
            print "***backYes"
        else:
            print "backNo"
        elapsedTime = (time.time() - timerz)
        if elapsedTime < 0:
            break
        else:
            pass
        
def testFollow():
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

def kill():
    from subprocess import call
    call(["killall","python"])
    print "cleaned camera code"
