# -*- coding: utf-8 -*-
"""
Created on Fri Dec 25 19:51:22 2017

@author: Jan
"""


import numpy as np
import pandas as pd
import time

## Advent of Code 2017, Day 14
day = 14

#data = open('day13.txt', 'r')
test = 'flqrgnkx'
inpt = 'hwlqcszp' 
N = 128

def used_squares(inpt):
    """ Counts used squares. """
    st = 0
    return st

t1 = time.time()
print("***  It's Advent of Code 2017, Day {}!  ***\n".format(day))
print('First part:')
print(used_squares(test))
print(used_squares(inpt))

print('Second part:')


t2 = time.time()
print('Program run for  {0} sec.'.format(round(t2-t1,2)))

