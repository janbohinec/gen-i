# -*- coding: utf-8 -*-
"""
Created on Fri Dec 25 19:51:22 2017

@author: Jan
"""


import numpy as np
import pandas as pd
import time

## Advent of Code 2017, Day 17
day = 17

#data = open('day16.txt', 'r')
#data = data.read().split(',')

data = 371
data_test = 3

def spinlock(data, N):
    """ Let's spin in this lock. """
    spin = [0]
    pos = 0
    for i in range(N):
        pos = np.mod(pos + data, len(spin))
        spin = spin[:pos+1] + [i+1] + spin[pos+1:]
        pos += 1
        #print(spin)
    print(spin[pos+1])
    return spin

def spinlock_mod(data, N):
    """ Let's spin in this lock. """
    spin = [0]
    pos = 0
    spin_mod = 1
    for i in range(N):
        pos = np.mod(pos + data, spin_mod)
        if pos == 0:
            print('New value at pos 1:', i+1)
        #spin = spin[:pos+1] + [i+1] + spin[pos+1:]
        pos += 1
        spin_mod += 1
    return spin


t1 = time.time()
print("***  It's Advent of Code 2017, Day {}!  ***\n".format(day))
print('First part:')
spinlock(data_test, 2017)
spinlock(data, 2017)

print('Second part:')
b = spinlock_mod(data, 50000000)


t2 = time.time()
print('Program run for  {0} sec.'.format(round(t2-t1,2)))

