# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 20:42:22 2018

@author: Jan
"""


import numpy as np
import pandas as pd
import time
import datetime as dt

## Advent of Code 2018, Day 1
day = 1



if __name__ == '__main__':
    
    t1 = time.time()
    print("***  It's Advent of Code 2018, Day {}!  ***\n".format(day))
    print('First part:')

    freq = 0
    data = open('day1.txt', 'r')
    
    dict_freq = [0]
    for line in data:
        freq += int(line)

    print(freq)
    
    print('Second part:')

    freq = 0
    found = False
    
    dict_freq = {freq: 1}
    while not found:
        
        data = open('day1.txt', 'r')
        for line in data:
            freq += int(line)
            if freq in dict_freq:
                print(freq)
                found = True
                break
            else:
                dict_freq[freq] = 1
        if found:
            break
    
    t2 = time.time()
    print('Program run for  {0} sec.'.format(round(t2-t1,2)))

