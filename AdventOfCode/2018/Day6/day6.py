# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 20:42:22 2018

@author: Jan
"""


import numpy as np
import pandas as pd
import time
import datetime as dt

## Advent of Code 2018, Day 6
day = 6

if __name__ == '__main__':
    
    t1 = time.time()
    print("***  It's Advent of Code 2018, Day {0}!  ***\n".format(day))
    print('** First part:')
    
    with open('day{0}.txt'.format(day), 'r') as f:
        data = [line.strip() for line in f.readlines()]
    
    dim = 352
    arr = np.zeros((dim, dim))
    
    def dist(x1,y1,x2,y2):
        return abs(x1-x2) + abs(y1-y2)
    
    for x in range(len(arr)):
        for y in range(len(arr)):
            min_dist = 1024
            guard_idx = 1024
            min_dist2 = 1024
            for idx, guard in enumerate(data):
                gx, gy = (int(x) for x in guard.split(','))    
                if dist(x, y, gx, gy) <= min_dist:
                    min_dist2 = min_dist
                    min_dist = dist(x,y,gx,gy)
                    guard_idx = idx + 1 # because 0 no claim
            if min_dist != min_dist2:
                arr[x][y] = guard_idx
    
    ele, counts = np.unique(arr, return_counts = True)
    
    max_area = 0
    for i in range(len(ele)):
        if counts[i] > max_area and ele[i] not in arr[0,:] and ele[i] not in arr[-1,:] and ele[i] not in arr[:,0] and ele[i] not in arr[:, -1]: # area not on edge
            max_area = counts[i]

    res = 0
    print('Silver star answer: \n{0}'.format(max_area))
    
    print('** Second part:')
    
    arr = np.zeros((dim, dim))
    cnt = 0
    for x in range(len(arr)):
        for y in range(len(arr)):
            total_dist = 0
            for idx, guard in enumerate(data):
                gx, gy = (int(x) for x in guard.split(','))    
                total_dist += dist(x,y,gx,gy)
            if total_dist < 10000:
                cnt += 1

    print('Golden star answer: \n{0}'.format(cnt))
    t2 = time.time()
    print('Program run for  {0} sec.'.format(round(t2-t1,2)))

