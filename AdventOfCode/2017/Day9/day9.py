# -*- coding: utf-8 -*-
"""
Created on Fri Dec 23 17:51:22 2017

@author: Jan
"""


import numpy as np
import pandas as pd
from itertools import count
import time

## Advent of Code 2017, Day 9

data = open('day9.txt', 'r')

def goThrough(data):
    data = data.read()
    
    cancel = False
    garbage = False
    
    vsota = 0
    vsota_garbage = 0
    
    nivo = 0
    for char in data:
        if cancel:
            cancel = False
        elif char == '!':
            cancel = True
        elif char == '>':
            garbage = False
        elif garbage:
            vsota_garbage += 1
        elif char == '<':
            garbage = True
        elif char == '{':
            nivo += 1
        elif char == '}':
            vsota += nivo
            nivo -= 1
    return vsota, vsota_garbage


t1 = time.time()
print('Test')
print(goThrough(data))

print('2nd part test')
print()
print('2nd part anwswer')

t2 = time.time()
print('Program run for  {0} sec.'.format(round(t2-t1,2)))

