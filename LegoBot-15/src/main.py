'''
Created on Mar 14, 2015

@author: Dead Robot Society
'''



import actions as act


def main() :
    #act.test()
    #return

    act.init()
    
    act.getOutOfStartBox()
    
    act.getToMidLine()
    
    act.crossBump()
    
    act.sortAndGo(6) # 6 crashes into wall
    
    act.DEBUG()
    
    act.getOutOfCorner()
    
    act.DEBUG("Stop")
    
    
if __name__ == "__main__":
    main()
