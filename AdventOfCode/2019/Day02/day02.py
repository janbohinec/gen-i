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
day = 2
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
   

    def intcode(noun, verb):
        rr = []
        for i in range(len(data[0])):
            rr.append(int(data[0][i]))
            
        rr[1] = noun
        rr[2] = verb
        i = 0
        while True:
            code = rr[i]
            if code == 1: # add
                rr[rr[i+3]] = rr[rr[i+1]] + rr[rr[i+2]] 
            elif code == 2: # multi
                rr[rr[i+3]] = rr[rr[i+1]] * rr[rr[i+2]]    
            elif code == 99:
                break #stop
            i += 4
        return rr[0]
        
    
    print(intcode(12, 2))
    
    #### 2nd Task
    print('** Second part:')

    found = False
    for noun in range(120):
        for verb in range(80):
            if intcode(noun, verb) == 19690720: 
                found = True
                print('Found!', noun, verb, 100 * noun + verb)
                break
        if found:
            break
    
    t2 = time.time()
    print('Program run for  {0} sec.'.format(round(t2 - t1, 2)))