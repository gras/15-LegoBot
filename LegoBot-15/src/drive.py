'''
Created on Mar 15, 2015

@author: Dead Robot Society
'''
import time 
import kovan as link
import constants as c


def noStop( leftSpeed, rightSpeed, driveTime) :
    # this method does not stop, 
    # to allow smooth transitions to the next drive command 
    link.motor( c.mLeft, leftSpeed )
    link.motor( c.mRight, rightSpeed )
    time.sleep( driveTime )

def withStop( leftSpeed, rightSpeed, driveTime) :
    link.motor( c.mLeft, leftSpeed )
    link.motor( c.mRight, rightSpeed )
    time.sleep( driveTime )
    link.ao()

def testGates():
    print "testing left gate"
    link.motor(c.leftGate, 20)
    time.sleep(.4)
    link.motor(c.leftGate, -20)
    time.sleep(.4)
    #link.motor(c.leftGate, 0)
    #time.sleep(.4)
    
    print "testing right gate"
    link.motor(c.rightGate, 20)
    time.sleep(.4)
    link.motor(c.rightGate, -20)
    time.sleep(.4)
    #link.motor(c.leftGate, 0)
    #time.sleep(.2)
    
def openGate( gateNumber ):
    link.motor(gateNumber, -50)
    time.sleep(0.1)
    