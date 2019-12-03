
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 20:42:22 2018

@author: Jan
"""

import numpy as np
import pandas as pd
import time
import datetime as dt

## Advent of Code 2019
day = 3
year = 2019

def day_str(day):
    """ Return string from integer day. """
    return str(day) if day >= 10 else '0' + str(day)
    
if __name__ == '__main__':
    
    t1 = time.time()
    print("***  It's Advent of Code {1}, Day {0}!  ***\n".format(day, year))
    #### 1st Task
    print('** First part:')
    
    with open('day{0}.txt'.format(day_str(day)), 'r') as f:
        data = [line.strip() for line in f.readlines()]
    
    data1 = data[0].split(',')
    data2 = data[1].split(',')
    
    #data1 = 'R75,D30,R83,U83,L12,D49,R71,U7,L72'
    #data2 = 'U62,R66,U55,R34,D71,R55,D58,R83'

    #data1 = data1.split(',')
    #data2 = data2.split(',')


    def direction(step):
        direc = step[0]
        if direc == 'U':
            point = [0, 1]
        if direc == 'R':
            point = [1, 0]
        if direc == 'D':
            point = [0, -1]
        if direc == 'L':
            point = [-1, 0]
        return point
    
    def manhattan(x,y):
        return abs(x) + abs(y)
    
    x = 0
    y = 0
    lab = {}
    lab_steps = []
    
    for step in data1:
        point = direction(step)
        num = int(step[1:])
        for k in range(1,num+1):
            x += point[0] 
            y += point[1]
            if x not in lab.keys():
                lab[x] = [y]
            else:
                lab[x] += [y]
            lab_steps += [[x,y]]

    x = 0
    y = 0
    s = 0
    closest = 10**12
    minstep = 10**12
    
    for step in data2:        
        point = direction(step)
        num = int(step[1:])
        for k in range(1,num+1):
            s += 1
            x += point[0] 
            y += point[1] 
            if x in lab.keys():
                if y in lab[x]: 
                    # Intersection detected
                    if manhattan(x,y) < closest and abs(x) + abs(y) > 0:
                        closest = manhattan(x,y)
                    for k in range(len(lab_steps)): # measure the steps in the first rope
                        if lab_steps[k] == [x,y]:
                            s1 = k + 1
                    steps = s + s1
                    if steps < minstep:
                        minstep = steps
   
            
    print('Closest: ', closest)
    
    #### 2nd Task
    print('** Second part:')
    print('Min steps: ', minstep)
    
    t2 = time.time()
    print('Program run for  {0} sec.'.format(round(t2 - t1, 2)))