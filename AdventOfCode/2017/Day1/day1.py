# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 20:56:38 2017

@author: Jan
"""

import numpy as np
import pandas as pd
import time

## Advent of Code 2017, Day 1
        


t1 = time.time()

data = open('day1.txt', 'r')

string = data.readline()
total = 0
n = len(string)
string += string
for i in range(n):
    if string[i] == string[i + 1]:
        total += int(string[i])

print(total)
print('2nd part')

total = 0
for i in range(n):
    if string[i] == string[i + n//2]:
        total += int(string[i])


print(total)
t2 = time.time()
print('Program run for  {0} sec.'.format(round(t2-t1,2)))

