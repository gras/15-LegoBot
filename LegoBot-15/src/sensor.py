'''
Created on Mar 14, 2015

@author: Dead Robot Society
'''

import kovan as link
import constants as c
import servo
import time
import drive
import actions as act
from time import sleep

'''
def getLargestArea():
    link.camera_update()
    link.camera_update()
    link.camera_update()
    redArea = link.get_object_area(c.chanRed,0)
    print "red area", redArea
    greenArea = link.get_object_area(c.chanGreen,0)
    print "green area", greenArea
    if redArea > greenArea :
        return redArea
    else :
        return greenArea
'''

def sortTribble() :
    print "sortTribble"
    link.camera_update()
    time.sleep(.1)
    link.camera_update()
    print "camera updated"
    found = 0
    if link.get_object_area( c.chanGreen, 0 ) >= c.blobSize:
        print "green, y=", link.get_object_center_y(c.chanGreen, 0)
        if link.get_object_center_y(c.chanGreen, 0) >= 90:
            drive.withStop(30, 30, .5)
            link.camera_update()
            print "*******new y=", link.get_object_center_y(c.chanGreen, 0)
            #act.DEBUG("bad green alignment")
        print link.get_object_area( c.chanGreen, 0 )
        print "moveSorter"
        servo.moveSorter( c.sorterLeft, 100 )
        drive.withStop(-50, -50, 0.1)   
        time.sleep(.2)
        print "moveKicker"
        servo.moveKicker( c.kickerOut, 2000 )
        time.sleep(0.4) #0.5
        servo.moveSorter( c.sorterCenter ,200)
        servo.moveKicker( c.kickerReady, 2000 )
        time.sleep(0.1)#was .5
        found = 1
        
    elif link.get_object_area(c.chanRed, 0 ) >= c.blobSize or link.get_object_area(c.chanGold, 0 ) >= c.blobSize:
        print "red/gold"
        print "red, y=", link.get_object_center_y(c.chanRed, 0)
        if link.get_object_center_y(c.chanRed, 0) >= 90:
            drive.withStop(30, 30, .5)
            link.camera_update()
            print "*******new y=", link.get_object_center_y(c.chanRed, 0)
        print link.get_object_area( c.chanRed, 0 )
        print "moveSorter"  
        servo.moveSorter( c.sorterRight, 100 )
        drive.withStop(-50, -50, 0.1)   
        time.sleep(.2)
        print "moveKicker"
        servo.moveKicker( c.kickerOut, 2000 )
        time.sleep(0.4) #0.5
        servo.moveSorter( c.sorterCenter ,200)
        servo.moveKicker( c.kickerReady, 2000 )
        time.sleep(0.1) #was .5
        found = 1
        
    else:
        print "nothing found"
        found = 0
       
    
    return found
    


    