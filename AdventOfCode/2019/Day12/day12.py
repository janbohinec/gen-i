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


## Advent of Code 2019
day = 11
year = 2019

def day_str(day):
    """ Return string from integer day. """
    return str(day) if day >= 10 else '0' + str(day)
    
if __name__ == '__main__':
    
    t1 = time.time()
    print("***  It's Advent of Code {1}, Day {0}!  ***\n".format(day, year))
    #### 1st Task
    print('** First part:')
    

    pos = [[3,15,8],
           [5,-1,-2],
           [-10, 8, 2],
           [8,4,-5]
    ]
       
    
    vel = [[0, 0, 0],
           [0, 0, 0],
           [0, 0, 0],
           [0, 0, 0]
    ]
    
    
    def energy(pos, vel):
        pot = 0
        kin = 0
        e = 0
        for (i, moon) in enumerate(pos):
            pot = 0
            kin = 0
            for cord in moon:
                pot += abs(cord)
            for k in range(3):
                kin += abs(vel[i][k])
            e += pot * kin
        return e
            
    
    step = 0
    while step < 1000:
        # calc vels
        for (i, moon1) in enumerate(pos):
            for (k, moon2) in enumerate(pos):
                if i==k:
                    continue
                for (j, cord) in enumerate(moon1):
                    if moon1[j] > moon2[j]:
                        vel[i][j] += -1
                    elif moon1[j] < moon2[j]:
                        vel[i][j] += +1
        
        # apply vol
        for (i,moon) in enumerate(pos):
            for (j, cord) in enumerate(moon):
                pos[i][j] += vel[i][j]
            
        
        #print(pos)
        step += 1
    
    print(energy(pos, vel))

    #### 2nd Task
    print('** Second part:')

    
    pos = [[3,15,8],
           [5,-1,-2],
           [-10, 8, 2],
           [8,4,-5]
    ]
    
    pos0 = [[3,15,8],
           [5,-1,-2],
           [-10, 8, 2],
           [8,4,-5]
    ]
    
    vel = [[0, 0, 0],
           [0, 0, 0],
           [0, 0, 0],
           [0, 0, 0]
    ]
    
    vel0 = [[0, 0, 0],
           [0, 0, 0],
           [0, 0, 0],
           [0, 0, 0]
    ]
    
    found = []
    for j in range(3):
        step = 0
        while True:
            # calc vels
            for (i, moon1) in enumerate(pos):
                for (k, moon2) in enumerate(pos):
                    if i==k:
                        continue   
                    if moon1[j] > moon2[j]:
                        vel[i][j] += -1
                    elif moon1[j] < moon2[j]:
                        vel[i][j] += +1
            
            # apply vol
            for (i,moon) in enumerate(pos):
                pos[i][j] += vel[i][j]
                
            step += 1
    
    
            if pos == pos0 and vel == vel0:
                break
        
        
        print(step)
        found += [step]
        


    def gcd(a, b):
        """Return greatest common divisor using Euclid's Algorithm."""
        while b:      
            a, b = b, a % b
        return a

    def lcm(a, b):
        """Return lowest common multiple."""
        return a * b // gcd(a, b)        

    a = found[0]
    b = found[1]
    c = found[2]
    
    print(lcm(a,lcm(b,c)))
        
    t2 = time.time()
    print('Program run for  {0} sec.'.format(round(t2 - t1, 2)))
    