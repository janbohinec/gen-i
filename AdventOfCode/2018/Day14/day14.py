# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 20:42:22 2018

@author: Jan
"""

import numpy as np
import pandas as pd
import time
import datetime as dt


## Advent of Code 2018, Day 14
day = 14

if __name__ == '__main__':
    
    t1 = time.time()
    print("***  It's Advent of Code 2018, Day {0}!  ***\n".format(day))
    print('** First part:')
    
    inpt = '030121'
    
    recipes = [3, 7] # Starting recepies
    pos1 = 0
    pos2 = 1
    while len(recipes) < int(inpt) + 10:
        new = recipes[pos1] + recipes[pos2]
        if new >= 10:
            recipes.extend([new // 10, new % 10])
        else:
            recipes.append(new)
        pos1 = (pos1 + 1 + recipes[pos1]) % len(recipes)
        pos2 = (pos2 + 1 + recipes[pos2]) % len(recipes)
    
    res = ''.join(map(str, recipes[-10:]))
      

    print('Silver star answer: \n{0}'.format(res))
    
    print('** Second part:')
    

    recipes2 = [3, 7] # Starting recepies
    pos1 = 0
    pos2 = 1
    inptchr = [int(c) for c in inpt]
    inptlen = len(inptchr)
    while True:
        new = recipes2[pos1] + recipes2[pos2]
        if new >= 10:
            recipes2.extend([new // 10, new % 10])
        else:
            recipes2.append(new)
        pos1 = (pos1 + 1 + recipes2[pos1]) % len(recipes2)
        pos2 = (pos2 + 1 + recipes2[pos2]) % len(recipes2)
        if recipes2[-inptlen:] == inptchr or recipes2[-inptlen-1:-1] == inptchr:
            # pattern found, stop the loop
            break
    
    res = len(recipes2) - inptlen - 1
    
    print('Golden star answer: \n{0}'.format(res))
    t2 = time.time()
    print('Program run for  {0} sec.'.format(round(t2-t1,2)))

