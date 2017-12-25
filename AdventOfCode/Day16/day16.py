# -*- coding: utf-8 -*-
"""
Created on Fri Dec 25 19:51:22 2017

@author: Jan
"""


import numpy as np
import pandas as pd
import time

## Advent of Code 2017, Day 16
day = 16

data = open('day16.txt', 'r')
data = data.read().split(',')

start = 'abcdefghijklmnop'
start_test = 'abcde'

data_test = ['s1', 'x3/4', 'pe/b']

def swap(c, i, j):
    c = list(c)
    c[i], c[j] = c[j], c[i]
    return ''.join(c)

def dance(pos, roll):
    """ Let's dance. """
    for move in roll:
        char = move[0]
        if char == 's': # Spin
            n = int(move[1:])
            #print(n)
            pos = pos[-n:] + pos[0:len(pos)-n]
        elif char == 'x': # Exchange
            A, B = list(map(int, move[1:].split('/')))
            pos = swap(pos, A, B)
            #print(A, B, pos[A], pos[B])
        elif char == 'p': # Partner
            A, B = move[1:].split('/')
            a = pos.find(A)
            b = pos.find(B)
            #print(A, B)
            pos = swap(pos, a, b)
            
    return pos
    
def get_tired(pos, roll, N):
    """ Dance until your drop dead. """
    start = pos
    for i in range(N):
        pos = dance(pos, roll)
        if pos == start:
            print('Eureka!', i)
            break
    return pos

t1 = time.time()
print("***  It's Advent of Code 2017, Day {}!  ***\n".format(day))
print('First part:')
print(dance(start_test, data_test))
print(dance(start, data))

print('Second part:')
print(get_tired(start_test, data_test, 2))
print(get_tired(start, data, 40))

t2 = time.time()
print('Program run for  {0} sec.'.format(round(t2-t1,2)))

