# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 20:42:22 2018

@author: Jan
"""

import numpy as np
import pandas as pd
import time
import datetime as dt
import math
import operator
from collections import defaultdict


## Advent of Code 2018, Day 22
day = 22


if __name__ == '__main__':
    
    t1 = time.time()
    print("***  It's Advent of Code 2018, Day {0}!  ***\n".format(day))
    print('** First part:')
    
    depth = 11541
    target_x, target_y = 14, 778
    modulo = 20183
    geoInd_c1 = 16807
    geoInd_c2 = 48271
    
    
    cave = [[0] * (target_y + 1) for idx in range(target_x + 1)]

    res = 0

    cave[0][0] = depth % modulo
    res += cave[0][0] % 3
    for x in range(target_x + 1):
        cave[x][0] = (x * geoInd_c1 + depth) % modulo
        res += cave[x][0] % 3
        
    for y in range(target_y + 1):
        cave[0][y] = (y * geoInd_c2 + depth) % modulo
        res += cave[0][y] % 3
        
        
    for x in range(1, target_x + 1):
        for y in range(1, target_y + 1):
            cave[x][y] = (cave[x - 1][y] * cave[x][y - 1] + depth) % modulo
            res += cave[x][y] % 3
            
            
    res -= cave[target_x][target_y] % 3
    cave[target_x][target_y] = cave[0][0]
    res += cave[target_x][target_y] % 3


    
    print('Silver star answer: \n{0}'.format(res))
    
    print('** Second part:')
    

    
    
    
    print('Golden star answer: \n{0}'.format(res))
    t2 = time.time()
    print('Program run for  {0} sec.'.format(round(t2-t1,2)))

