'''
Created on Mar 15, 2015

@author: Dead Robot Society
'''
import time 
import kovan as link
import constants as c
import drive

def testServo():
    
    print "testing clapper"
    link.set_servo_position(c.clapper, c.clapperTight)
    link.enable_servo(c.clapper)
    time.sleep(1.0)
    link.set_servo_position(c.clapper, c.clapperWide)
    time.sleep(1.0)
    print "testing sorter"
    link.set_servo_position(c.sorter, c.sorterLeft)
    link.enable_servo(c.sorter)
    time.sleep(1.0)
    link.set_servo_position(c.sorter, c.sorterRight)
    time.sleep(1.0)
    link.set_servo_position(c.sorter, c.sorterCenter)
    time.sleep(1.0)
    print "testing kicker"
    link.set_servo_position(c.kicker, c.kickerOut)
    link.enable_servo(c.kicker)
    time.sleep(1.0)
    link.set_servo_position(c.kicker, c.kickerReady)
    time.sleep(1.0)
    

def moveClapper( endPos, speed=10 ):
    moveServo( c.clapper, endPos, speed )

def moveSorter( endPos, speed=10 ):
    moveServo( c.sorter, endPos, speed )

def moveKicker( endPos, speed=10 ):
    moveServo( c.kicker, endPos, speed )


def moveServo( servo, endPos, speed=10 ) :
    # speed of 1 is slow
    # speed of 2000 is fast
    # speed of 10 is the default
    now = link.get_servo_position( servo )
    if now > 2048 :
        PROGRAMMER_ERROR( "Servo setting too large" )
    if now < 0 :
        PROGRAMMER_ERROR( "Servo setting too small" )
    if now > endPos:
        speed = -speed
    for i in range (now, endPos, speed ):
        link.set_servo_position( servo, i)
        time.sleep(0.010)
    link.set_servo_position( servo, endPos )
    time.sleep( 0.010 )

def wiggle():
    moveSorter(c.sorterRightish, 100)
    moveSorter(c.sorterLeftish, 100)
    moveSorter(c.sorterCenter, 100)
    moveClapper(c.clapperDrive, 200)
    drive.withStop(-50, 25, .5)
    moveClapper(c.clapperOpen, 150) #200 #was closed
    drive.withStop(50, -25, .65)
    drive.noStop( 55, 50, .3)
    moveClapper(c.clapperClosed)
    
def PROGRAMMER_ERROR( msg ) :
    link.ao()
    print msg
    link.camera_close()
    exit()

