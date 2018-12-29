# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 20:42:22 2018

@author: Jan
"""

import numpy as np
import time
import datetime as dt
import re
from scipy import spatial



## Advent of Code 2018, Day 23
day = 23


if __name__ == '__main__':
    
    t1 = time.time()
    print("***  It's Advent of Code 2018, Day {0}!  ***\n".format(day))
    print('** First part:')
   
    points = []
    radious = []
    with open('day{0}.txt'.format(day), 'r') as f:
        for line in f.readlines():
            m = re.match('pos=<(-?\d+),(-?\d+),(-?\d+)>, r=([- ]?\d+)', line)
            point = [int(i) for i in m.groups()[0:3]]
            rad = int(m.groups()[3])
            
            points += [point] 
            radious += [rad] 

    def distance(p1, p2):
        dist = 0
        for i in range(len(p1)):
            dist += abs(p1[i] - p2[i])
        return dist

    res = 0    
    print(len(points))
    
    target_point = points[np.argmax(radious)]
    

    distances = spatial.distance.cdist([target_point], points, metric='cityblock')
    
    print(np.sum(distances <= np.max(radious)))
    
    print('Silver star answer: \n{0}'.format(res))
    
    print('** Second part:')
    
    maxNanos = 0
    for idx,p in enumerate(points):
        distances = spatial.distance.cdist([p], points, metric='cityblock')
        if np.sum(distances <= radious[idx]) >= maxNanos:
            maxNanos = np.sum(distances <= radious[idx]) 
            print(idx, maxNanos, p)

    
    
    
    print('Golden star answer: \n{0}'.format(res))
    t2 = time.time()
    print('Program run for  {0} sec.'.format(round(t2-t1,2)))

