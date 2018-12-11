# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 20:42:22 2018

@author: Jan
"""


import numpy as np
import pandas as pd
import time
import datetime as dt
import re
import matplotlib.pyplot as plt
from scipy import sparse

## Advent of Code 2018, Day 11
day = 11

if __name__ == '__main__':
    
    t1 = time.time()
    print("***  It's Advent of Code 2018, Day {0}!  ***\n".format(day))
    print('** First part:')
    
    dim = 300
    gridSerial = 6392

    rr = np.zeros((dim, dim))
    
    def powerLvl(x,y, gridSerial):
        rackID = x + 10
        powerLvl = rackID * y
        powerLvl += gridSerial
        powerLvl *= rackID
        if powerLvl > 100:
            powerLvl = int(str(powerLvl)[-3])
        else:
            powerLvl = 0
        return powerLvl - 5
    
    #print(powerLvl(3,5,8))    
    #print(powerLvl(122,79,57))  
    #print(powerLvl(217,196,39)) 
    #print(powerLvl(101,153,71)) 
    
    for i in range(dim):
        for j in range(dim):
            rr[i][j] = powerLvl(i+1, j+1, gridSerial)
    
    def getTotalPower(grid):
        maxPower = 0
        for i in range(len(grid)-2):
            for j in range(len(grid)-2):
                curPower = sum(sum(rr[i:i+3,j:j+3]))
                if curPower > maxPower:
                    maxPower = curPower
                    cords = (i+1,j+1)
        return maxPower, cords
    
    a,b = getTotalPower(rr)
    print(a,b)

    print('Silver star answer: \n{0}'.format(b))
    
    print('** Second part:')
    
    def getTotalPower2(grid):
        maxPower = 0
        for i in range(len(grid)-2):
            for j in range(len(grid)-2):
                for k in range(1, 20): # try and hope 20 is enough
                    curPower = sum(sum(rr[i:i+k,j:j+k]))
                    if curPower > maxPower:
                        maxPower = curPower
                        cords = (i+1,j+1, k)
                        #print(cords)
        return maxPower, cords
    
    a,b = getTotalPower2(rr)
    print(a,b)
    
    print('Golden star answer: \n{0}'.format(b))
    t2 = time.time()
    print('Program run for  {0} sec.'.format(round(t2-t1,2)))

