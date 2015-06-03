'''
Created on Mar 14, 2015

@author: Dead Robot Society
'''

import actions as act

def main() :
    #act.test()
    #return

    act.init()
    # ride the east wall
    act.getOutOfStartBox()
    act.crossBumpNorth()
    act.sortAndGo(6) # 6 crashes into wall
    act.driveIntoWall(7)
    act.DEBUG()
    
    # ride the m wall
    act.startToTurn()
    act.driveIntoWall(5)

    # ride the west wall
    act.getOutOfSecondBox()
    act.crossBumpSouth()
    act.sortAndGo(6)
    act.driveIntoWall(7)
    
    # ride the south wall
    act.startToTurnTwo()
    act.driveIntoWall(5)
    act.DEBUG()
    
    # ride the east wall again 
    act.getOutOfThirdBox()
    act.crossBumpNorth()
    act.jettison()
    act.driveIntoWall(10)
    act.theWiggleMove()
    
    # done
    act.shutdown()
    act.kill()
    act.DEBUG("Done!")
    
if __name__ == "__main__":
    main()
