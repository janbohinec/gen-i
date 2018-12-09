# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 20:42:22 2018

@author: Jan
"""


import numpy as np
import pandas as pd
import time
import datetime as dt
from collections import defaultdict
import operator

## Advent of Code 2016, Day 1
day = 1

def dist(x1, y1, x2, y2):
    """ Return Manhattan distance of points (x1,y1) and (x2, y2) """
    return abs(x1-x2) + abs(y1-y2)

if __name__ == '__main__':
    
    t1 = time.time()
    print("***  It's Advent of Code 2016, Day {0}!  ***\n".format(day))
    print('** First part:')
    
    #with open('day4.txt', 'r') as f:
    #    data = [line.strip() for line in f.readlines()]
        
    with open('day{0}.txt'.format(day), 'r') as f:
        data = f.readline().strip()
    
    data = data.split(', ')
    
    x, y = 0, 0
    dirx, diry = 1, 0
    
    directions = {'N': [1, 0], 'S': [-1,0], 'W': [0,-1], 'E': [0, 1]}
    change_dir = {'N': {'R': 'E', 'L': 'W'},
                  'S': {'R': 'W', 'L': 'E'},
                  'E': {'R': 'S', 'L': 'N'},
                  'W': {'R': 'N', 'L': 'S'}}
    
    direction = 'N'
    
    locations = []
    twice = False    
    for step in data:
        turn, steps = step[0], int(step[1:])
        
        direction = change_dir[direction][turn]
        dirx, diry = directions[direction]
        for k in range(steps):
            x += dirx * 1
            y += diry * 1
            #print(direction, dirx, diry, x,y)
        
            
            if [x,y] in locations:
                print(x,y, locations)
                twice = True
                break
            locations += [[x,y]]
        if twice:
            break
            
        
        
    res = dist(0,0, x, y)

    

    print('Silver star answer: \n{0}'.format(res))
    
    print('** Second part:')
    

    
    print('Golden star answer: \n{0}'.format(res))
    t2 = time.time()
    print('Program run for  {0} sec.'.format(round(t2-t1,2)))

