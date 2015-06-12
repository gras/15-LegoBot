'''
Created on Mar 14, 2015

@author: Dead Robot Society
'''

import actions as act

def main() :
    #act.test()                                    Programming score out of 10: ________
    #return

    act.init()
    
    # ride the east wall
    act.getOutOfStartBox()
    act.crossBumpNorth()
    act.sortAndGo(6) # 6 crashes into wall
    act.driveIntoWall(7)
    
    # ride the m wall
    act.startToTurn() # to the east
    act.driveIntoWall(5)  # east wall

    # ride the west wall
    act.getOutOfFarBox()
    act.crossBumpSouth()
    act.sortAndGo(6)
    act.driveIntoWall(7)
    
    # ride the south wall
    act.startToTurnTwo()
    act.driveIntoWall(5)
    
    # ride the east wall again 
    act.getOutOfStartBox2()
    act.crossBumpNorth()
    act.jettison()
    act.driveIntoWall(10)
    act.theSpinMove()
    act.theWiggleMove()
    
    # done
    act.shutdown()
    act.kill()
    act.DEBUG("Done!")
    
if __name__ == "__main__":
    main()
