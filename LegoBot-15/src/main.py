'''
Created on Mar 14, 2015

@author: Dead Robot Society
'''
from kovan import msleep
from kovan import motor
from kovan import ao

import os
import sys

# set print to unbuffered
sys.stdout = os.fdopen(sys.stdout.fileno(),'w',0)

def main() :
    print "Starting...."
    testMotors()
    print "Finished"

def testMotors() :
    motor(1,100)
    motor(3,100)
    msleep(500)
    ao()


if __name__ == "__main__":
    main()