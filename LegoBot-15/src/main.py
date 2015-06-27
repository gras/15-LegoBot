'''
Created on Mar 14, 2015

@author: Dead Robot Society
'''

import actions as act


def main() :
    print "hello"             
    

    act.init()

    print act.getSuper()
    
        
    # ride the east wall
    act.getOutOfStartBox()
   
    act.crossBumpNorth()
    
    pomsNotSorted = act.sortAndGo(6) # 6 crashes into wall
    
    act.driveIntoWall(7)
    
    
    # ride the north wall
    act.startToTurn() # to west east
    act.driveIntoWall(5)  # west wall
    
    # ride the west wall
    act.getOutOfFarBox()
    act.crossBumpSouth()
    
    
    act.sortAndGo(7 + pomsNotSorted)
    
    act.driveIntoWall(7)
    
    # ride the south wall
    act.startToTurnTwo()
    act.driveIntoWall(5)
    
    
    # ride the east wall again 
    act.getOutOfStartBox2()
    act.crossBumpNorth()
    act.jettison()
    act.driveIntoWall(10)
    act.finalStop()
    act.DEBUG("done")
    #act.theSpinMove()
    #act.theWiggleMove()
    
    
    

    # superseeding experimental WIP code
    if act.getSuper():
        act.lineUsUp()
        act.DEBUG("NEIN")
        act.lineFollow()
        act.getUsSet()
    # done
    act.shutdown()

if __name__ == "__main__":
    # set print to unbuffered
    import os
    import sys
    sys.stdout = os.fdopen(sys.stdout.fileno(),'w',0)
    main()
