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

import string


## Advent of Code 2020
day = 6
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
        data = f.read().split('\n\n')
    
    questions = string.ascii_lowercase
    
    answers = 0
    for line in data:
        for question in questions:
            if question in line:
                answers += 1          
                
    print(answers)
        
    #### 2nd Task
    print('** Second part:')
 
  
    answers = 0
    for line in data:
        people = line.split('\n')
        people_cnt = 0
        empty = {}
        for p in people:
            people_cnt += 1
            for question in questions:
                if question in p:
                    if question in empty.keys():
                        empty[question] += 1
                    else:
                        empty[question] = 1
        for key in empty.keys():
            if empty[key] == people_cnt:
                answers += 1
                
    print(answers)
    
    
    # Alternative solution part 2
    answers = 0
    for line in data:
        for letter in set(line.replace('\n', '')):
            if line.count(letter) == len(line.split('\n')):
                answers += 1
    print(answers)
        
    
    t2 = time.time()
    print('Program run for  {0} sec.'.format(round(t2 - t1, 2)))

