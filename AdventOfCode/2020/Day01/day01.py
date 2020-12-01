# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 20:42:22 2018

@author: Jan B.
"""

import numpy as np
import pandas as pd
import time
import datetime as dt

## Advent of Code 2020
day = 1
year = 2020

def day_str(day):
    """ Return string from integer day. """
    return str(day) if day >= 10 else '0' + str(day)
    
if __name__ == '__main__':
    
    t1 = time.time()
    print("***  It's Advent of Code {1}, Day {0}!  ***\n".format(day, year))
    #### 1st Task
    print('** First part:')
    
    target = 2020
    
    with open('day{0}.txt'.format(day_str(day)), 'r') as f:
        data = [int(line.strip()) for line in f.readlines()]
    
    stop = False
    for line in data:
        for line2 in data:
            if line + line2 == target:
                print(line*line2)
                stop = True
                break
        if stop:
            break
    
    #### 2nd Task
    print('** Second part:')
    
    stop = False
    for line in data:
        for line2 in data:
            for line3 in data:
                if line + line2 + line3 == target:
                    print(line*line2*line3)
                    stop = True
                    break
            if stop:
                break
        if stop:
            break
    
    
    t2 = time.time()
    print('Program run for  {0} sec.'.format(round(t2 - t1, 2)))

