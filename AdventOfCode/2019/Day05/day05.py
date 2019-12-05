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
day = 5
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
        data = [line.strip().split(',') for line in f.readlines()]

    def param(k, mode):
        if mode == 1:
            return rr[k % n]
        elif mode == 0:
            return rr[rr[k % n]]
    
    rr = []
    for i in range(len(data[0])):
        rr.append(int(data[0][i]))

    ID = 1
    n = len(rr)
    i = 0
    while True:
        code = rr[i]
        code_str = str(abs(code))
        if len(code_str) == 5:
            modes = [int(code_str[0]), int(code_str[1]), int(code_str[2])]
        if len(code_str) == 4:
            modes = [0, int(code_str[0]), int(code_str[1])]                
        if len(code_str) == 3:
            modes = [0, 0, int(code_str[0])]
        if len(code_str) <= 2:
            modes = [0, 0, 0]        

        code = int(str(code)[-2:])
        #print(code)
        if code == 1: # add
            rr[rr[i+3] % n] = param(i+1, modes[-1]) + param(i+2, modes[-2])
            step = 4
        elif code == 2: # multi
            rr[rr[i+3] % n] = param(i+1, modes[-1]) * param(i+2, modes[-2])
            step = 4
        elif code == 3: # copy
            rr[rr[i+1]] = ID
            step = 2
        elif code == 4: # output
            print(rr[rr[i+1]])
            step = 2 
        elif code == 99:
            break #stop
        
        i += step
        
        
    #### 2nd Task
    print('** Second part:')

    rr = []
    for i in range(len(data[0])):
        rr.append(int(data[0][i]))
        

    ID = 5
    n = len(rr)
    i = 0
    while True:
        code = rr[i]
        code_str = str(abs(code))
        if len(code_str) == 5:
            modes = [int(code_str[0]), int(code_str[1]), int(code_str[2])]
        if len(code_str) == 4:
            modes = [0, int(code_str[0]), int(code_str[1])]                
        if len(code_str) == 3:
            modes = [0, 0, int(code_str[0])]
        if len(code_str) <= 2:
            modes = [0, 0, 0]        

        code = int(str(code)[-2:])
        if code == 1: # add
            rr[rr[i+3] % n] = param(i+1, modes[-1]) + param(i+2, modes[-2])
            step = 4
        elif code == 2: # multi
            rr[rr[i+3] % n] = param(i+1, modes[-1]) * param(i+2, modes[-2])
            step = 4
        elif code == 3: # copy
            rr[rr[i+1]] = ID
            step = 2
        elif code == 4: # output
            print(rr[rr[i+1]])
            step = 2 
        elif code == 5: # jump if true
            if param(i+1, modes[-1]) != 0:
                i = param(i+2, modes[-2])
                step = 0
            else:
                step = 3
        elif code == 6: # jump if false
            if param(i+1, modes[-1]) == 0:
                i = param(i+2, modes[-2])
                step = 0
            else:
                step = 3
        elif code == 7: # less than
            if param(i+1, modes[-1]) < param(i+2, modes[-2]):   
                rr[rr[i+3] % n] = 1
            else:
                rr[rr[i+3] % n] = 0
            step = 4
        elif code == 8: # equals
            if param(i+1, modes[-1]) == param(i+2, modes[-2]):   
                rr[rr[i+3] % n] = 1
            else:
                rr[rr[i+3] % n] = 0                
            step = 4
        elif code == 99:
            break #stop
        
        i += step
    
    
    t2 = time.time()
    print('Program run for  {0} sec.'.format(round(t2 - t1, 2)))