'''
Created on Mar 15, 2015

@author: Dead Robot Society
'''
import kovan as link

# servo ports
kicker = 3
sorter = 0
clapper = 1

# motor ports
mLeft = 2
mRight = 0
# gates are by robot's left and right
leftGate = 3
rightGate = 1

# digital ports
clonePort = 15
bumper = 10

# analog ports
ETPort = 0
 
#------------------------------------ 

# color channels    0 = green     1 = red    2 = gold
chanGreen = 0
chanRed = 1 
chanGold = 2
 
# servo positions
clapperWide = 100
clapperDrive = 150
clapperOpen = 400 #375
clapperParallel = 750
clapperClosed = 700
clapperTight = 915

# sorter positions
sorterLeft = 0
sorterRight = 2047
sorterCenter = 1000 #885 
sorterRightish = ((sorterRight-sorterCenter)/2)+sorterCenter
sorterLeftish = sorterCenter-((sorterCenter-sorterCenter)/2)

# kicker positions
# kickerBack = 400 #650
kickerReady = 900 #1300
kickerOut = 1600 #1850

# gate positions
"""
gateOpen = 1100 #1050
gateClose = 900 #480
"""

# camera
blobSize = 2000

startTime = 0

isClone = link.digital(clonePort)
isPrime = not isClone      

# define clone values here
if isClone:
    # servo positions
    clapperWide = 150
    clapperDrive = 300
    clapperOpen = 375 #500 
    clapperParallel = 820 #800
    clapperClosed = 700
    clapperTight = 915
    
    # sorter positions
    sorterLeft = 0
    sorterRight = 2047
    sorterCenter = 1020 #840
    
    # kicker positions
    # kickerBack = 400 #650
    kickerReady = 500 #400
    kickerOut = 1100 #1850
 
    # gate positions
    gateOpen = 1000 #850 
    gateClose = 800 #480
    
    # camera
    blobSize = 2000
    
    
    
