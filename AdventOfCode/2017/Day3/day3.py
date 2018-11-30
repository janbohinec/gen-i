# -*- coding: utf-8 -*-
"""
Created on Thu Dec 21 20:19:43 2017

@author: Jan
"""


import numpy as np
import pandas as pd
from itertools import count
import time

## Advent of Code 2017, Day 3

data = 289326

def manhattan_distance(data):
    """ Manhattan distance in s spiral grid. """
    smallbox = np.floor(np.sqrt(data))
    bigbox = np.ceil(np.sqrt(data))
    ostanek = data - smallbox**2
    if bigbox % 2 == 0:
        ostanek = abs(data - bigbox**2)
        center = [bigbox // 2 + 1, bigbox // 2]
        if ostanek < smallbox:
            position = [1, 1 + ostanek]
        else:
            position = [1 + ostanek - smallbox, bigbox]
    else:
        center = [bigbox // 2 + 1, bigbox // 2 + 1]
    #position = [1,1]
    print(smallbox, bigbox, ostanek, center, position)
    return int(abs(position[0] - center[0]) + abs(position[1] - center[1]))
    
def sum_spiral():
    a, i, j = {(0,0) : 1}, 0, 0
    for s in count(1, 2):
        for (ds, di, dj) in [(0,1,0),(0,0,-1),(1,-1,0),(1,0,1)]:
            for _ in range(s+ds):
                i += di; j += dj
                a[i,j] = sum(a.get((k,l), 0) for k in range(i-1,i+2)
                                             for l in range(j-1,j+2))
                yield a[i,j]

def part2(n):
    for x in sum_spiral():
        if x>n: return x
    
    

t1 = time.time()
print('Test')
print(manhattan_distance(289326))

print('2nd part test')
print()
print('2nd part anwswer')
print(part2(data))

t2 = time.time()
print('Program run for  {0} sec.'.format(round(t2-t1,2)))

