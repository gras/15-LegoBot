'''
Created on Mar 15, 2015

@author: Dead Robot Society
'''
import kovan as link

# servo ports
kicker = 3
sorter = 0
clapper = 1
gate = 2

# motor ports
mLeft = 2
mRight = 0

# digital ports
clonePort = 15

# analog ports
 
 
#------------------------------------ 

#color channels    0 = green     1 = red
chanGreen = 0
chanRed = 1 
 
# servo positions
clapperWide = 0
clapperDrive = 150
clapperOpen = 400 #375
clapperParallel = 750
clapperClosed = 700
clapperTight = 915

# sorter positions
sorterLeft = 0
sorterRight = 2047
sorterCenter = 880 #840

# kicker positions
#kickerBack = 400 #650
kickerReady = 900 #1300
kickerOut = 1600 #1850

#gate positions
gateOpen = 1050
gateClose = 480

#camera
blobSize = 2000





# hard code for now, but will be clone switch
isClone = link.digital(clonePort)
        

# define clone values here
if isClone:
    # servo positions
    clapperWide = 0
    clapperDrive = 300
    clapperOpen = 500 #375
    clapperParallel = 800
    clapperClosed = 700
    clapperTight = 915
    
    # sorter positions
    sorterLeft = 0
    sorterRight = 2047
    sorterCenter = 1020 #840
    
    # kicker positions
    #kickerBack = 400 #650
    kickerReady = 400 #1300
    kickerOut = 900 #1850
 
    #gate positions
    gateOpen = 1050
    gateClose = 480
    
    #camera
    blobSize = 2000
    
    
    