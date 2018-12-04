# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 20:42:22 2018

@author: Jan
"""


import numpy as np
import pandas as pd
import time
import datetime as dt

## Advent of Code 2018, Day 3
day = 3


if __name__ == '__main__':
    
    t1 = time.time()
    print("***  It's Advent of Code 2018, Day {0}!  ***\n".format(day))
    print('** First part:')
    
    with open('day3.txt', 'r') as f:
        data = [line.strip() for line in f.readlines()]

    dim = 1024
    arr = np.zeros((dim, dim))
    
    for claim in data:
        # Parsing
        id, _, pos, size = claim.split(' ')
        row, col = (int(x) for x in pos[:-1].split(','))
        side1, side2 = [int(x) for x in size.split('x')]
    
        arr[row:row + side1, col:col + side2] += 1
    
    res = (arr > 1).sum()
   
    #string = data.readline()
    #data = pd.read_excel('day2.xlsx', header=None)  
    #for idx, row in data.iterrows():    
        #print(row.loc[1], max(row), min(row))
    
    print('Silver star answer: \n{0}'.format(res))
    
    print('** Second part:')
    
    for claim in data:
        # Parsing
        id, _, pos, size = claim.split(' ')
        row, col = (int(x) for x in pos[:-1].split(','))
        side1, side2 = [int(x) for x in size.split('x')]
    
        if arr[row:row + side1, col:col + side2].sum() == side1 * side2:
            res = id
            break

    
    print('Golden star answer: \n{0}'.format(res))
    t2 = time.time()
    print('Program run for  {0} sec.'.format(round(t2-t1,2)))

