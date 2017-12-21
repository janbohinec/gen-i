# -*- coding: utf-8 -*-
"""
Created on Thu Dec 21 20:19:43 2017

@author: Jan
"""


import numpy as np
import pandas as pd
import time

## Advent of Code 2017, Day 3
        


t1 = time.time()
print('Test')
print(checksum(test_sheet))
data = pd.read_excel('Day2.xlsx', header=None)  
    
print('Day3')
print(checksum(data.values))

print('2nd part test')
print(divisible_sum(test_sheet2))
print('2nd part anwswer')
print(divisible_sum(data.values))

t2 = time.time()
print('Program run for  {0} sec.'.format(round(t2-t1,2)))

