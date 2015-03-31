'''
Created on Mar 14, 2015

@author: Dead Robot Society
'''



import actions as act


def main() :
    #act.test()
    act.init()
    
    act.getOutOfStartBox()
    
    act.getToMidLine()
    
    act.crossBump()
    
    act.DEBUG()
    
    act.sortAndGo(4)
    
    act.getOutOfCorner()
    
    act.DEBUG("Stop")
    
    
if __name__ == "__main__":
    main()
