# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 20:42:22 2018

@author: Jan B.
"""

import numpy as np
import pandas as pd
import time
import datetime as dt
import matplotlib.pyplot as plt
import re
import copy
import string
import math


## Advent of Code 2020
day = 13
year = 2020

def day_str(day):
    """ Return string from integer day. """
    return str(day) if day >= 10 else '0' + str(day)
    

if __name__ == '__main__':
    
    t1 = time.time()
    print("***  It's Advent of Code {1}, Day {0}!  ***\n".format(day, year))
    #### 1st Task
    print('** First part:')
    
    
    with open('day{0}.txt'.format(day_str(day)), 'r') as f:
        #data = f.read().split('\n\n')
        data = [line.strip().split(' ') for line in f.readlines()]


    my_time = int(data[0][0])
    busses = data[1][0].split(',')

    
    max_waiting = -np.inf
    last_ID = 0
    for bus in busses:
        if bus != 'x':
            ID = int(bus)
            
            waiting = my_time - (my_time//ID + 1) * ID
            if waiting > max_waiting:
                max_waiting = waiting
                last_ID = ID
    
    print(abs(max_waiting)*last_ID)

    
    #### 2nd Task
    print('** Second part:')

    busses2 = {}
    
    for i, bus in enumerate(busses):
        if bus != 'x':
            busses2[int(bus)] = i
        
    
    all_busses = list(busses2)
    
    
    def lcm(a, b):
        return abs(a*b) // math.gcd(a, b)
    
    max_bus = max(all_busses)
    max_bus_value = busses2[max_bus]
    
    step = 1
    for bus in busses2:
        busses2[bus] -= max_bus_value
        if busses2[bus] % bus == 0:
            busses2[bus] = 0
            step = lcm(step, bus)
    
    print(step)
    
    
    k = 1
    while k < 20000000:
        
        maybe_time = k * step
        
        maybe_true = True
        for bus in busses2:
            if busses2[bus] < 0:
                if maybe_time % bus != -busses2[bus]:
                    maybe_true = False
                    break
            elif busses2[bus] > 0:
                if (maybe_time + busses2[bus]) % bus != 0:
                    maybe_true = False
                    break
        
        if maybe_true:
            print('Found It', maybe_time)
            break
        k += 1
    
  
    print(maybe_time - max_bus_value)

    t2 = time.time()
    print('Program run for  {0} sec.'.format(round(t2 - t1, 2)))

