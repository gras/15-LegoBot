'''
Created on Mar 15, 2015

@author: Dead Robot Society
'''
import kovan as link

# servo ports
sorter = 0
clapper = 1
kicker = 3

# motor ports
mRight = 0
mLeft = 2

# gates are by robot's left and right
rightGate = 1
leftGate = 3

# digital ports
bumper = 10
clonePort = 15

# analog ports
topHatFront = 3
topHatBack = 4

# analog readings
topFrontSee = 200 #550
topBackSee = 200 #700
#------------------------------------ 

# color channels    0 = green     1 = red    2 = gold    3 = pink
chanGreen = 0
chanRed = 1 
chanGold = 2
chanPink = 3
 
# servo positions
clapperWide = 100
clapperDrive = 150
clapperOpen = 400 
clapperClosed = 700
clapperParallel = 750
clapperTight = 915

# sorter positions
sorterLeft = 0
sorterRight = 2047
sorterCenter = 1050 #1000 
sorterRightish = ((sorterRight-sorterCenter)/2)+sorterCenter
sorterLeftish = sorterCenter-((sorterCenter-sorterCenter)/2)

# kicker positions
kickerReady = 900 #1300
kickerOut = 1600 #1850

# camera
blobSize = 2000
tapeBlobSize = 500 #superseeding line follow only

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
    sorterCenter = 1065 #1020
    
    # kicker positions
    kickerReady = 500 #400
    kickerOut = 1100 #1850
 
   
    
    
