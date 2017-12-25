# -*- coding: utf-8 -*-
"""
Created on Fri Dec 23 17:51:22 2017

@author: Jan
"""


import numpy as np
import pandas as pd
import time

## Advent of Code 2017, Day 11

data = open('day11.txt', 'r')
data2 = pd.read_excel('day11.xlsx', header=None).values[0][0].split(',')

data = data.read().split(',')

def distance(x,y):
    # Take diagonal steps towards self.x == 0
    steps = abs(x)
    # y moves closer to 0 by steps because moving diagonal, but never moving too far
    if y > 0:
        # Might still be positive, but never negative
        y = max(y - steps, 0)
    else:
        # Might still be negative, but not positive
        y = min(y + steps, 0)
    # You move 2 positions north/south by a single move so divide y's by 2
    return abs(y) // 2 + abs(steps)

def hexEd(data):
    """ Hex Grid Walkover. """
    pos = np.zeros(2) # [n-s, e-w]
    max_dist = 0
    for step in data:
        if step == 'n':
            pos[1] += 1
        elif step == 's':
            pos[1] -= 1
        elif step == 'ne':
            pos[0] += 1
            pos[1] += 1
        elif step == 'sw':
            pos[0] -= 1
            pos[1] -= 1
        elif step == 'nw':
            pos[0] += -1
        elif step == 'se':
            pos[0] += 1 

            
        cur_dist = distance(pos[0], pos[1])
        max_dist = cur_dist if cur_dist > max_dist else max_dist
        
    print(max_dist)
    return pos, cur_dist
     


t1 = time.time()
print('Test')
print(hexEd(['ne', 'ne', 'ne']))
print(hexEd(['ne', 'ne', 'sw', 'sw']))
print(hexEd(['ne', 'ne', 's', 's']))
print(hexEd(['se', 'sw', 'se', 'sw', 'sw']))
print(hexEd(data2))

print('2nd part test')
print()
print('2nd part anwswer')

t2 = time.time()
print('Program run for  {0} sec.'.format(round(t2-t1,2)))

