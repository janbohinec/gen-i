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


## Advent of Code 2020
day = 9
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
        
    for i in range(len(data)):
        data[i] = int(data[i][0])
    
    def check_correct(series, num):
        found = False
        for num1 in series:
            for num2 in series:
                if num1 != num2:
                    if num1 + num2 == num:
                        found = True
                        break
        return found
    
    
    pre = 25
    for i in range(len(data) - pre):
        series = data[i:i+pre]
        
        if not check_correct(series, data[i+pre]):
            print('Found not correct num')
            print(i, data[i+pre])
            break

    res = i
    
    #### 2nd Task
    print('** Second part:')
    
    def encryption_weakness(series):
        return (max(series) + min(series))
    
    
    def check_correct2(series, num):       
        for i in range(len(series)):
            for j in range(i + 1, len(series)):                    
                if sum(series[i:j]) == num:
                    return series[i:j]


    a = check_correct2(data[0:i+pre], data[i+pre])
    res = encryption_weakness(a)
    print(res)
    
    
    t2 = time.time()
    print('Program run for  {0} sec.'.format(round(t2 - t1, 2)))

