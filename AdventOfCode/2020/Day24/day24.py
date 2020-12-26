0# -*- coding: utf-8 -*-
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
import math
import itertools

## Advent of Code 2020
day = 24
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
        data = f.read().split('\n')
        #data = [line.strip() for line in f.readlines()]
        

    black = set()

    
    for line in data:
        x, y = 0, 0 
        #print(line)
        while line:
            if line.startswith('e'):
                x += 1
                line = line[1:]
            elif line.startswith('se'):
                x += 1
                y -= 1
                line = line[2:]
            elif line.startswith('sw'):
                y -= 1
                line = line[2:]    
            elif line.startswith('w'):
                x -= 1
                line = line[1:]    
            elif line.startswith('nw'):
                x -= 1
                y += 1
                line = line[2:]        
            elif line.startswith('ne'):
                y += 1
                line = line[2:]

            #e, se, sw, w, nw, and ne
        if (x,y) not in black:
            black.add((x,y))
        else:
            black.remove((x,y))
       
    print(len(black))
    #### 2nd Task
    print('** Second part:')
    
    def get_black_neigbors(x,y):
        cnt = 0
        if (x + 1, y) in black:
            cnt += 1
        if (x - 1, y) in black:
            cnt += 1
        if (x, y + 1) in black:
            cnt += 1
        if (x, y - 1) in black:
            cnt += 1
        if (x + 1, y - 1) in black:
            cnt += 1
        if (x - 1, y + 1) in black:
            cnt += 1
        return cnt
    
    

    grid_size = 65
    
    for i in range(100):
        black_new = set()
        for x in range(-grid_size, grid_size):
            for y in range(-grid_size, grid_size):
                n = get_black_neigbors(x,y)
                if (x,y) in black and (n == 1 or n==2):
                    black_new.add((x,y))
                if (x,y) not in black and n == 2:
                    black_new.add((x,y))
        black = copy.deepcopy(black_new)
    
    print(len(black_new))

    t2 = time.time()
    print('Program run for  {0} sec.'.format(round(t2 - t1, 2)))

