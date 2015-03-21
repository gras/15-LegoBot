'''
Created on Mar 15, 2015

@author: Botball
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
