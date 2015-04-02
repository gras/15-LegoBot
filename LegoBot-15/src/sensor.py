'''
Created on Mar 14, 2015

@author: Dead Robot Society
'''

import kovan as link
import constants as c
import servo
import time
import drive

def getLargestArea():
    link.camera_update()
    link.camera_update()
    I = 0
    link.camera_update()
    redArea = link.get_object_area(c.chanRed,0)
    print "red area", I, redArea
    greenArea = link.get_object_area(c.chanGreen,0)
    print "green area", I, greenArea
    if redArea > greenArea :
        return redArea
    else :
        return greenArea

def sortTribble() :
    print "sortTribble"
    link.camera_update()
    link.camera_update()
    time.sleep (0.5)
    link.camera_update()
    if link.get_object_area( c.chanGreen, 0 ) >= c.blobSize:
        print "green"
        print link.get_object_area( c.chanGreen, 0 )  
        print "moveSorter"
        servo.moveSorter( c.sorterLeft, 100 )
        print "moveKicker"
        servo.moveKicker( c.kickerOut, 2000 )
        time.sleep(0.4) #0.5
        
    elif link.get_object_area(c.chanRed, 0 ) >= c.blobSize:
        print "red"
        print link.get_object_area( c.chanRed, 0 )
        print "moveSorter"  
        servo.moveSorter( c.sorterRight, 100 )
        print "moveKicker"
        servo.moveKicker( c.kickerOut, 2000 )
        time.sleep(0.4) #0.5
        
    else:
        print "nothing found"
        servo.moveClapper(c.clapperDrive, 200)
        drive.withStop(-50, 25, .5)
        servo.moveClapper(c.clapperClosed, 200)
        drive.withStop(50, -25, .65)
       
    servo.moveSorter( c.sorterCenter ,200)
    servo.moveKicker( c.kickerReady, 2000 )
