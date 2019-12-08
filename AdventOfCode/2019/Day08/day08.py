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
day = 8
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
    
    data  = data[0][0]
    
    pic = []
    width = 25
    tall = 6
    
    i = 0
    row_cnt = 0
    while i < len(data):
        layer = []
        for j in range(tall):
            row = []
            for k in range(width):
                row += [int(data[i])]
                i += 1
            layer += [row]
        row_cnt += 1
        pic += [layer]
            
    
    fewest = 10**12
    my_layer = 0
    i = 0
    for layer in pic:
        zeros = 0
        for row in layer:
            zeros += row.count(0)
        if zeros < fewest:
            fewest = zeros
            my_layer = i
        i += 1
            
    print(zeros, my_layer)

    ones = 0
    twos = 0
    for row in pic[my_layer]:
        ones += row.count(1)
        twos += row.count(2)
    print(ones*twos)

    
    #### 2nd Task
    print('** Second part:')
    
    
    my_pic = [[2 for i in range(width)] for k in range(tall)]
    
    
    for i,layer in enumerate(pic):
        for k,row in enumerate(layer):
            for j,c in enumerate(row):
                if c < 2 and my_pic[k][j] == 2:
                    my_pic[k][j] = c

    import matplotlib.pyplot as plt
    plt.imshow(my_pic)

    
    t2 = time.time()
    print('Program run for  {0} sec.'.format(round(t2 - t1, 2)))