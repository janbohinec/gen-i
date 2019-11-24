# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 20:42:22 2018

@author: Jan
"""

import numpy as np
import pandas as pd
import time
import datetime as dt

## Advent of Code 2019, Day 1
day = 1
year = 2019

if __name__ == '__main__':
    
    t1 = time.time()
    print("***  It's Advent of Code {1}, Day {0}!  ***\n".format(day, year))
    print('** First part:')

    freq = 0
    data = open('day01.txt', 'r')
    
    dict_freq = [0]
    for line in data:
        freq += int(line)

    print('Silver star answer: \n{0}'.format(freq))
    
    print('** Second part:')

    freq = 0
    found = False
    loop_cnt = 0
    
    dict_freq = {freq: 1}
    while not found:
        data = open('day01.txt', 'r')
        for line in data:
            freq += int(line)
            if freq in dict_freq:
                print('Golden star answer: \n{0}'.format(freq))
                found = True
                break
            else:
                dict_freq[freq] = 1
        if found:
            break
        loop_cnt += 1
    #print(loop_cnt)
    
    t2 = time.time()
    print('Program run for  {0} sec.'.format(round(t2 - t1, 2)))

