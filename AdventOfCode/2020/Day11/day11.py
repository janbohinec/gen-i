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
day = 11
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
        
    rows = len(data)
    columns = len(data[0][0])
    
    for i in range(len(data)):
        data[i] = list(data[i][0])
        
        
    def count_adjacent(seats, row, col):
        cnt = 0
        max_rows = len(seats)
        max_cols = len(seats[0])
        if row + 1 < max_rows and seats[row+1][col] == '#': # up
            cnt += 1
        if col + 1 < max_cols and seats[row][col+1] == '#': # right
            cnt += 1
        if row - 1 >= 0 and seats[row-1][col] == '#' : # down
            cnt += 1    
        if col - 1 >= 0 and seats[row][col-1] == '#': # left
            cnt += 1
        if col - 1 >= 0 and row - 1 >= 0 and seats[row-1][col-1] == '#': # diagonal 1
            cnt += 1  
        if col + 1 < max_cols and row + 1 < max_rows and seats[row+1][col+1] == '#': # diagonal 2
            cnt += 1              
        if col - 1 >= 0 and row + 1 < max_rows and seats[row+1][col-1] == '#': # diagonal 3
            cnt += 1                  
        if row - 1 >= 0 and col + 1 < max_cols and seats[row-1][col+1] == '#' : # diagonal 4
            cnt += 1
        return cnt       
      
    def count_occupied(seats):
        cnt = 0
        for row in seats:
            cnt += row.count('#')
        return cnt
        

            
    pre_occupied = count_occupied(data)
    occupied = -1
    
    old = copy.deepcopy(data)
    times = 0
    while pre_occupied - occupied != 0:
        pre_occupied = occupied
        new = copy.deepcopy(old)
        
        for row in range(len(new)):
            for col in range(len(new[0])):
                if new[row][col] != '.':
                    no = count_adjacent(old, row, col)
                    if new[row][col] == 'L' and no == 0:
                        new[row][col] = '#'
                    if new[row][col] == '#' and no >= 4:
                        new[row][col] = 'L'

        occupied = count_occupied(new)
        old = copy.deepcopy(new)
        times += 1
        #print(times, occupied)
    
    print(occupied)          
    
    #### 2nd Task
    print('** Second part:')
    
    def count_first_visible(seats, row, col):
        cnt = 0
        max_rows = len(seats)
        max_cols = len(seats[0])
        
        k = 1
        while row + k < max_rows:
            if seats[row+k][col] != '.':
                if seats[row+k][col] == '#': # up
                    cnt += 1
                break
            k += 1
            

        k = 1
        while col + k < max_cols:
            if seats[row][col+k] != '.':
                if seats[row][col+k] == '#': # right
                    cnt += 1
                break
            k += 1
            
        k = 1
        while row - k >= 0:
            if seats[row-k][col] != '.':
                if seats[row-k][col] == '#': # down
                    cnt += 1
                break
            k += 1

        
        k = 1
        while col - k >= 0:
            if seats[row][col-k] != '.':
                if seats[row][col-k] == '#': # left
                    cnt += 1
                break
            k += 1


        k = 1
        while col - k >= 0 and row - k >= 0:
            if seats[row-k][col-k] != '.':
                if seats[row-k][col-k] == '#': # diagonal 1
                    cnt += 1
                break
            k += 1


        k = 1
        while col + k < max_cols and row + k < max_rows:
            if seats[row+k][col+k] != '.':
                if seats[row+k][col+k] == '#': # diagonal 2
                    cnt += 1
                break
            k += 1

        
        k = 1
        while col - k >= 0 and row + k < max_rows:
            if seats[row+k][col-k] != '.':
                if seats[row+k][col-k] == '#': # diagonal 3
                    cnt += 1
                break
            k += 1


        k = 1
        while row - k >= 0 and col + k < max_cols:
            if seats[row-k][col+k]  != '.':
                if seats[row-k][col+k] == '#': # diagonal 4
                    cnt += 1
                break
            k += 1


        return cnt  
    
      
    pre_occupied = count_occupied(data)
    occupied = -1
    
    old = copy.deepcopy(data)
    times = 0
    while pre_occupied - occupied != 0:
        pre_occupied = occupied
        
        new = copy.deepcopy(old)
        
        for row in range(len(new)):
            for col in range(len(new[0])):
                if new[row][col] != '.':
                    no = count_first_visible(old, row, col)
                    if new[row][col] == 'L' and no == 0:
                        new[row][col] = '#'
                    if new[row][col] == '#' and no >= 5:
                        new[row][col] = 'L'

        occupied = count_occupied(new)
        old = copy.deepcopy(new)
        times += 1
    
    print(times, occupied)


    
    t2 = time.time()
    print('Program run for  {0} sec.'.format(round(t2 - t1, 2)))

