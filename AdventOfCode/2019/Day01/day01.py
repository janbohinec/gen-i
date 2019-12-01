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
day = 1
year = 2019

def day_str(day):
    """ Return string from integer day. """
    return str(day) if day >= 10 else '0' + str(day)
    
if __name__ == '__main__':
    
    t1 = time.time()
    print("***  It's Advent of Code {1}, Day {0}!  ***\n".format(day, year))
    #### 1st Task
    print('** First part:')
    
    fuel = 0
    
    with open('day{0}.txt'.format(day_str(day)), 'r') as f:
        data = [line.strip() for line in f.readlines()]
    
    for line in data:
        fuel += int(line)//3 - 2
    print(fuel)
    
    #### 2nd Task
    print('** Second part:')
    
    fuel = 0
    
    for line in data:
        temp = int(line)//3 - 2
        fuel += temp
        while temp >= 0:
            temp = int(temp)//3 - 2
            if temp > 0:
                fuel += temp
    print(fuel)
    
    t2 = time.time()
    print('Program run for  {0} sec.'.format(round(t2 - t1, 2)))

