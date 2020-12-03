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
day = 3
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
        data = [line.strip().split(' ') for line in f.readlines()]
    
    right = 3
    down = 1
    posx = 0
    posy = 0
    tree = '#'
    
    trees = 0
    while posy < len(data):
        if data[posy][0][posx] == tree:
            trees +=1
        posy += down
        posx += right
        if posx >= len(data[0][0]):
            posx -= len(data[0][0])

    print(trees)

    #### 2nd Task
    print('** Second part:')
    
    combinations = [[1,1],[3,1],[5,1],[7,1],[1,2]]
    
    multiply = 1
    for combination in combinations:
        
        right = combination[0]
        down = combination[1]
    
        posx = 0
        posy = 0
        
        trees = 0
        while posy < len(data):
            if data[posy][0][posx] == tree:
                trees +=1
            posy += down
            posx += right
            if posx >= len(data[0][0]):
                posx -= len(data[0][0])
        
        multiply *= trees
    
    print(multiply)
    
    
    t2 = time.time()
    print('Program run for  {0} sec.'.format(round(t2 - t1, 2)))

