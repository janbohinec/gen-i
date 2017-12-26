# -*- coding: utf-8 -*-
"""
Created on Tue Dec 26 10:04:49 2017

@author: janb
"""


import numpy as np
import pandas as pd
import time


## Advent of Code 2017, Day 21
day = 21

data = open('day21.txt', 'r')
#data = data.read().split(',')

start = np.array([[0,1,0],[0,0,1],[1,1,1]])

def fractals(pic):
    """ Art of fractal pic. """
    for line in data:
        firstpart = line[:line.find('=')-1]
        firstpart = firstpart.replace('#', '1').replace('.', '0').split('/')
#        firstpart.replace('#', 1)
        secondpart = line[line.find('>')+2:]
        secondpart = secondpart.replace('#', '1').replace('.', '0').replace('\n', '').split('/')
        print(firstpart, secondpart)
        
        
np.rot90(start, 4)
np.fliplr(start)
np.flipud(start)

t1 = time.time()
print("***  It's Advent of Code 2017, Day {}!  ***\n".format(day))
print('First part:')
fractals(data)

print('Second part:')



t2 = time.time()
print('\nProgram run for  {0} sec.'.format(round(t2-t1,2)))

