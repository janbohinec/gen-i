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
day = 8
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
    
    
    def run_code(data):
        accumulator  = 0
        
        pos = 0
        visited = {-1}
        while pos < len(data):
            order = data[pos][0]
            value = int(data[pos][1])
            
            if pos in visited:
                return 'Loop', accumulator
            
            if order == 'nop':
                visited.add(pos)
                pos += 1
            elif order == 'acc':
                accumulator += value
                visited.add(pos)
                pos += 1
            elif order == 'jmp':
                visited.add(pos)
                pos += value
        
        return 'Terminated', accumulator
            
    print(run_code(data))
    
    #### 2nd Task
    print('** Second part:')
    
    status = ''
    acc = 0
    
    for k in range(len(data)):
        order = data[k][0]        
        
        alternate_data = copy.deepcopy(data)
        
        if order == 'nop':
            alternate_data[k][0] = 'jmp'
            status, acc = run_code(alternate_data)
        elif order == 'jmp':
            alternate_data[k][0] = 'nop'
            status, acc = run_code(alternate_data)
        
        
        if status == 'Terminated':
            print(acc)
            break
    
    
    t2 = time.time()
    print('Program run for  {0} sec.'.format(round(t2 - t1, 2)))

