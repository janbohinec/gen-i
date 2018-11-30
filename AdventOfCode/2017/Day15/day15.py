# -*- coding: utf-8 -*-
"""
Created on Fri Dec 25 19:51:22 2017

@author: Jan
"""


import numpy as np
import pandas as pd
import time

## Advent of Code 2017, Day 15
day = 15

#data = open('day13.txt', 'r')
A0 = 634
B0 = 301

Amulti = 16807
Bmulti = 48271
residual = 2147483647

A0_test = 65
B0_test = 8921

def judge(A, B):
    """ Judge counter of generators. """
    #N = 40000000
    N = 5000000
    st = 0
    for i in range(N):
        A = int(np.mod(A * Amulti, residual))
        while int(np.mod(A, 4)) != 0:
            A = int(np.mod(A * Amulti, residual))
        B = int(np.mod(B * Bmulti, residual))
        while int(np.mod(B, 8)) != 0:
            B = int(np.mod(B * Bmulti, residual))
        #print(A, B)
        Abin = "{0:b}".format(A)[-16:]
        Bbin = "{0:b}".format(B)[-16:]
        if Abin == Bbin:
            st += 1
        #print(Abin, Bbin)
    print(st)

t1 = time.time()
print("***  It's Advent of Code 2017, Day {}!  ***\n".format(day))
print('First part:')
#judge(A0_test, B0_test)
judge(A0, B0)

print('Second part:')


t2 = time.time()
print('Program run for  {0} sec.'.format(round(t2-t1,2)))

