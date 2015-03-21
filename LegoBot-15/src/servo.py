'''
Created on Mar 15, 2015

@author: Dead Robot Society
'''
import time 
import kovan as link
import constants as c

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
    if now > endPos:
        speed = -speed
    for i in range (now, endPos, speed ):
        link.set_servo_position( servo, i)
        time.sleep(0.010)
    link.set_servo_position( servo, endPos )
    time.sleep( 0.010 )