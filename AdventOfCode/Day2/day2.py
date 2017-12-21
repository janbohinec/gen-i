# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 20:56:38 2017

@author: Jan
"""

import numpy as np
import pandas as pd
import time

## Advent of Code 2017, Day 2
        
test_sheet = np.array([[5,1,9,5],[7,5,3], [2,4,6,8]])
test_sheet2 = np.array([[5,9,2,8],[9,4,7,3], [3,8,6,5]])

def checksum(sheet):
    """ CheckSum function """
    checksum = 0
    for row in range(len(sheet)):
        row = sheet[row]
        checksum += max(row) - min(row)
    return checksum

def divisible_sum(sheet):
    """ Evenly divisible values. """
    vsota = 0
    for row in range(len(sheet)):
        row = sheet[row]
        found = False
        for num in row:
            for i in range(len(row)):
                if num % row[i] == 0 and num != row[i]:
                    vsota += int(num / row[i])
                    print(num, row[i], int(num / row[i]))
                    found = True
                    break
            if found:
                break
    return vsota

t1 = time.time()
print('TestSum')
print(checksum(test_sheet))
data = pd.read_excel('Day2.xlsx', header=None)  
    
print('Day2_sum')
print(checksum(data.values))

print('2nd part test')
print(divisible_sum(test_sheet2))
print('2nd part anwswer')
print(divisible_sum(data.values))

t2 = time.time()
print('Program run for  {0} sec.'.format(round(t2-t1,2)))

