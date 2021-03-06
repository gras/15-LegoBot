'''
Created on Mar 15, 2015

@author: Dead Robot Society
'''
import time 
import sensor
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
    link.motor( c.mLeft, 0 )
    link.motor( c.mRight, 0 )

def topStopFront(leftSpeed, rightSpeed) :
    print "frontNo"        
    link.motor( c.mLeft, leftSpeed )
    link.motor( c.mRight, rightSpeed )
    while not sensor.frontHat():
        pass
        
            
            
def topStopBack(leftSpeed, rightSpeed) :
    while 1:
        backHat = sensor.backHat()
        if backHat:
            print "***backYes"
            break
        else:
            print "backNo"        
            link.motor( c.mLeft, leftSpeed )
            link.motor( c.mRight, rightSpeed )
            
def testGates():
    print "testing left gate"
    testOpenGate(c.leftGate)
    time.sleep(0.4)
    testCloseGate(c.leftGate)
    time.sleep(0.4)
    print "testing right gate"
    testOpenGate(c.rightGate)
    time.sleep(0.4)
    testCloseGate(c.rightGate)
    time.sleep(0.4)
    
def testOpenGate( gateNumber ):
    link.motor(gateNumber, 50)
    time.sleep(0.1)
    link.motor(gateNumber, 0)
    
def testCloseGate( gateNumber ):
    link.motor(gateNumber, -50)
    time.sleep(0.1)
    link.motor(gateNumber, 0)
    
def openGate( gateNumber ):
    link.motor(gateNumber, 50)
    time.sleep(0.4)
    link.motor(gateNumber, 0)
    
def closeGate( gateNumber ):
    link.motor(gateNumber, -50)
    time.sleep(0.4)
    link.motor(gateNumber, 0)
    
def holdGateOpen( gateNumber ):
    link.motor(gateNumber, 10)
   
def holdGateClosed( gateNumber ):
    link.motor(gateNumber, -10)