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
day = 16
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
        signal_orig = [int(char) for char in next(f)]


    def FFT(signal):
        new = []
        for i in range(len(signal)):
            sum_ = 0
            
            k = i
            
            while k < len(signal):
                sum_ += sum(signal[k : k + (i + 1)])
                k += 2 * (i + 1)
                
                sum_ -= sum(signal[k : k + (i + 1)])
                k += 2 * (i + 1)
            
            new.append(abs(sum_) % 10)
        return new
    

    i = 0
    signal = signal_orig.copy()
    while i < 100:
        signal = FFT(signal)
        i += 1
        
        
    solution = ''.join((str(char) for char in signal[0:8]))
    print(solution)
        



    #### 2nd Task
    print('** Second part:')

    n = 10000 # test 100, prod 10000
    signal = signal_orig.copy() * n
    offset = int(''.join(str(char) for char in signal[:7]))

    i = 0
    while i < 100: # bruteforce, 15sec
        sum_ = 0
        for j in range(len(signal) - 1, offset - 1, -1):
            sum_ += signal[j] 
            signal[j] = abs(sum_) % 10
        i += 1
    
    solution = ''.join([str(char) for char in signal[offset : offset + 8]])
    print(solution)
    
    t2 = time.time()
    print('Program run for  {0} sec.'.format(round(t2 - t1, 2)))
    
