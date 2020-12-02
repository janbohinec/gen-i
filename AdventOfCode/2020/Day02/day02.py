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
day = 2
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
        data = [line.strip().split(' ') for line in f.readlines()]
    
    cnt = 0
    for line in data:
        policy, char, password = line
        char = char[0]
        min_, max_ = policy.split('-')
        min_ = int(min_)
        max_ = int(max_)
        
        if password.count(char) >= min_ and password.count(char) <= max_:
            cnt += 1
        
    print(cnt)

    #### 2nd Task
    print('** Second part:')
    
    cnt = 0
    for line in data:
        policy, char, password = line
        char = char[0]
        min_, max_ = policy.split('-')
        min_ = int(min_)
        max_ = int(max_)
        
        if (password[min_-1] == char and password[max_-1] != char) \
            or (password[max_-1] == char and password[min_-1] != char):
            cnt += 1
    
    print(cnt)
    
    t2 = time.time()
    print('Program run for  {0} sec.'.format(round(t2 - t1, 2)))

