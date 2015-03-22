'''
Created on Mar 14, 2015

@author: Dead Robot Society
'''

import kovan as link
import constants as c
import servo
import time

def getLargestArea():
    link.camera_update()
    link.camera_update()
    I = 0
    #while link.get_object_area(c.chanRed, 0) < 0 and link.get_object_area(c.chanGreen, 0) < 0:
    #    I+=1
    link.camera_update()
        #print I
    redArea = link.get_object_area(c.chanRed,0)
    print "red area", I, redArea
    greenArea = link.get_object_area(c.chanGreen,0)
    print "green area", I, greenArea
    if redArea > greenArea :
        return redArea
    else :
        return greenArea

def cameraTrack() :
    print "cameraTrack"
    link.camera_update()
    link.camera_update()
    time.sleep (0.5)
    link.camera_update()
    if link.get_object_area( c.chanGreen, 0 ) >= c.blobSize:
        print "green"
        print link.get_object_area( c.chanGreen, 0 )  
        print "moveSorter"
        servo.moveSorter( c.sorterLeft )
        print "moveKicker"
        servo.moveKicker( c.kickerOut, 2000 )
        
    elif link.get_object_area(c.chanRed, 0 ) >= c.blobSize:
        print "red"
        print link.get_object_area( c.chanRed, 0 )
        print "moveSorter"  
        servo.moveSorter( c.sorterRight )
        print "moveKicker"
        servo.moveKicker( c.kickerOut, 2000 )
        
    else:
        print "nothing found"
         
    servo.moveSorter( c.sorterCenter)
    servo.moveKicker( c.kickerReady )
