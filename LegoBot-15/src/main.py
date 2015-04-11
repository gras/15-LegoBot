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
    act.crossBump()
    act.sortAndGo(6) # 6 crashes into wall
    act.driveIntoWall()
    
    # ride the north wall
    act.startToTurn()
    act.driveIntoWall()

    # ride the west wall
    act.getOutOfSecondBox()
    act.crossBump()
    act.sortAndGo(6)
    act.driveIntoWall()
    
    # ride the south wall
    act.startToTurnTwo()
    act.driveIntoWall()
    
    # ride the east wall again 
    act.getOutOfThirdBox()
    act.crossBump()
    act.driveIntoWall()
    
    # done
    act.DEBUG("Done!")
    
if __name__ == "__main__":
    main()
