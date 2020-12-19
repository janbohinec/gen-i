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


## Advent of Code 2020
day = 15
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
        data = [line.strip().split(',') for line in f.readlines()]

    starting_list = [int(i) for i in data[0]]  

    i = 1
    numbers = {}
    prev_number = starting_list[0]
    while i < 2020:

        if i < len(starting_list):
            next_number = starting_list[i]
        else:
            if prev_number in numbers.keys():
                next_number =  i - numbers[prev_number]
            else:
                next_number = 0
                
        numbers[prev_number] = i
       
        i += 1
        prev_number = next_number
 
    print(next_number)
    
    #### 2nd Task
    print('** Second part:')


    i = 1
    numbers = {}
    prev_number = starting_list[0]
    while i < 30000000:

        if i < len(starting_list):
            next_number = starting_list[i]
        else:
            if prev_number in numbers.keys():
                next_number =  i - numbers[prev_number]
            else:
                next_number = 0
                
        numbers[prev_number] = i
       
        i += 1
        prev_number = next_number
 
    print(next_number)

    t2 = time.time()
    print('Program run for  {0} sec.'.format(round(t2 - t1, 2)))

