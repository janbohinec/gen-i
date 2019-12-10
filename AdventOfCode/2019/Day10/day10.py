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
import math

## Advent of Code 2019
day = 10
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
        data = [line for line in f.readlines()]
    
    
    asteroids = []
    for y, row in enumerate(data):
        for x, char in enumerate(row.strip()):
            if char == '#':
                asteroids.append((x,y))
        
    max_cnt = 0
    best_loc = None
    for x1, y1 in asteroids:
        angles = defaultdict()
        for x2, y2 in asteroids:
            if x1 == x2 and y1 == y2:
                continue
            angle = math.atan2(x2-x1, y2-y1)
            if angle in angles.keys():
                angles[angle] += [x2, y2]
            else:
                angles[angle] = [x2, y2]
        if len(angles) > max_cnt:
            max_cnt = len(angles)
            best_loc = (x1, y1)

    
    
    print(max_cnt)
    print(best_loc)
    
    #### 2nd Task
    print('** Second part:')
    
    def dist(x1,y1,x2,y2):
        return (x2-x1)**2 + (y2-y1)**2
    
    vapor_cnt = 0
    angles = defaultdict()
    x1,y1 = best_loc
    for x2, y2 in asteroids:
        if x1 == x2 and y1 == y2:
            continue
        angle = math.atan2(x2-x1, y2-y1)
        if angle in angles.keys():
            angles[angle] += [[x2, y2]]
        else:
            angles[angle] = [[x2, y2]]
    

    for angle in sorted(angles.keys(), reverse=True):
        min_dist = 10**4
        for x2,y2 in angles[angle]:
            if dist(x1,y1,x2,y2) < min_dist:
                vapor_candidate = x2, y2
        vapor_cnt += 1
        angles[angle].remove([vapor_candidate[0], vapor_candidate[1]])
        #print(vapor_cnt, angle, vapor_candidate)
        
        #if not angles[angle]:
        #    del angles[angle]
        
        if vapor_cnt == 200:
            break
            


    print(vapor_candidate[0]*100 + vapor_candidate[1])

    
    t2 = time.time()
    print('Program run for  {0} sec.'.format(round(t2 - t1, 2)))