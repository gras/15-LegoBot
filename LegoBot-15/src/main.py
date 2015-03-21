'''
Created on Mar 14, 2015

@author: Botball
'''



import actions as act




"""
TRY HAVING THE ROBOT RUN STRAIGHT FOR 5 SECONDS
start robot with clapper facing away from ping pong balls, right tire on pencil mark
"""


def main() :
    act.init()
    #act.testRun() -- tests servo values
    #act.printSize() 
    act.eat() 
    for i in range(3):
        act.cameraSort()
        
    # act.filter()
    # act.filter()
    # drive.withStop(100, 100, 0.5)
    # drive.withStop(-100,-100, 0.5)
    #act.DEBUG()
    #act.getOutOfStartBox()
    #act.grabFirstPile()
    #act.getTribbles()
    #act.testDrive()
    #sen.cameraTrack()
 

if __name__ == "__main__":
    main()