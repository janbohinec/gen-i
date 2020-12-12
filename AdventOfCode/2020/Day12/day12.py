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
day = 12
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
        

    
    row = 0
    col = 0
    x, y = +1, 0
    
    for inst in data:
        char, value = inst[0][0], int(inst[0][1:])
        #print(char, value)
        if char == 'N':
            col += value
        elif char == 'S':
            col -= value
        elif char == 'E':
            row += value
        elif char == 'W':
            row -= value    
        elif char == 'R':
            if value == 90:
                x, y = y, -x
            elif value == 180:
                x, y = -x, -y
            elif value == 270:
                x, y = -y, x
        elif char == 'L':
            if value == 90:
                x, y = -y, x
            elif value == 180:
                x, y = -x, -y
            elif value == 270:
                x, y = y, -x
        elif char == 'F':
            row += x * value
            col += y * value
         
    print(abs(row) + abs(col))
            
    
    #### 2nd Task
    print('** Second part:')
    


    waypoint_row = 1
    waypoint_col = 10
    row, col = 0, 0
    x, y = 1, 0
    
    for inst in data:
        char, value = inst[0][0], int(inst[0][1:])
        #print(char, value)
        if char == 'N':
            waypoint_row += value
        elif char == 'S':
            waypoint_row -= value
        elif char == 'E':
            waypoint_col += value
        elif char == 'W':
            waypoint_col -= value    
        elif char == 'R':
            if value == 90:
                waypoint_col, waypoint_row = waypoint_row, -waypoint_col
            elif value == 180:
                waypoint_col = -waypoint_col
                waypoint_row = -waypoint_row
            elif value == 270:
                waypoint_col, waypoint_row = -waypoint_row, waypoint_col
        elif char == 'L':
            if value == 90:
                waypoint_col, waypoint_row = -waypoint_row, waypoint_col
            elif value == 180:
                waypoint_col = -waypoint_col
                waypoint_row = -waypoint_row
            elif value == 270:
                waypoint_col, waypoint_row = waypoint_row, -waypoint_col
        elif char == 'F':
            row += waypoint_row * value
            col += waypoint_col * value
         
        #print(row, col, x , y)
    print(abs(row) + abs(col))


    
    t2 = time.time()
    print('Program run for  {0} sec.'.format(round(t2 - t1, 2)))

