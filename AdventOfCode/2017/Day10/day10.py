# -*- coding: utf-8 -*-
"""
Created on Fri Dec 23 17:51:22 2017

@author: Jan
"""


import numpy as np
import pandas as pd
from itertools import count
import time

## Advent of Code 2017, Day 10

#data = open('day9.txt', 'r')

data = list(range(0,256))
data_inpt = [197,97,204,108,1,29,5,71,0,50,2,255,248,78,254,63]
test = [0,1,2,3,4]
test_inpt = [3,4,1,5]

def knot_hash(data, inpt):
    """ Elves knot hashing """
    skip = 0
    pos = 0
    for knot in inpt:
        if knot + pos < len(data):
            data[pos:pos+knot] = data[pos:pos+knot][::-1]
        else:
            test_data = data + data
            reverse = test_data[pos:pos+knot][::-1]
            data[pos:] = reverse[:len(data)-pos]
            data[:pos+knot-len(data)] = reverse[len(data)-pos:]
        pos += knot + skip
        pos = np.mod(pos, len(data))
        skip += 1
    print(data)
    return data[0]*data[1]


t1 = time.time()
print('Test')
print(knot_hash(test, test_inpt))

print(knot_hash(data, data_inpt))

print('2nd part test')
print()
print('2nd part anwswer')

t2 = time.time()
print('Program run for  {0} sec.'.format(round(t2-t1,2)))

