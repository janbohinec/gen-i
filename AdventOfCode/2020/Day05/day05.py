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

## Advent of Code 2020
day = 5
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
        data = [line.strip() for line in f.readlines()]
    
    
    n_rows = 128
    n_cols = 8
    
    def seat_id(row, col):
        return row * 8 + col
    
    def calc_binary(string, max_, c_lower):
        pos_1 = 0
        pos_2 = max_
        for c in string:
            if c == c_lower:
                pos_2 = pos_2 - (pos_2 - pos_1)//2 - 1
            else: # Upper
                pos_1 = pos_1 + (pos_2 - pos_1)//2 + 1
        return pos_1

    
    seating = [[0 for i in range(n_cols)] for j in range(n_rows)]
    
    max_id = 0
    for line in data:
        row_str = line[:7]
        col_str = line[-3:]
        row = calc_binary(row_str, n_rows - 1, 'F')
        col = calc_binary(col_str, n_cols - 1, 'L')
        id_ = seat_id(row, col)
        # 1st part
        if id_ > max_id:
            max_id = id_
        # 2nd part
        seating[row][col] = 1
    
    print(max_id)
        


    #### 2nd Task
    print('** Second part:')
 
    def find_my_seat():
        for i in range(1, n_rows-1):
            for j in range(1, n_cols-1):
                if seating[i][j] == 0 and seating[i+1][j+1] == 1 and seating[i+1][j-1] == 1 \
                    and seating[i-1][j+1] == 1 and seating[i-1][j-1] == 1:
                    id_ = seat_id(i, j)
                    return i, j, id_
                 
    my_col, my_row, my_id = find_my_seat()
    print(my_id)
    
    t2 = time.time()
    print('Program run for  {0} sec.'.format(round(t2 - t1, 2)))

