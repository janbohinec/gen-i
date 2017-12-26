# -*- coding: utf-8 -*-
"""
Created on Tue Dec 26 10:04:49 2017

@author: janb
"""


import numpy as np
import pandas as pd
import time
import string

## Advent of Code 2017, Day 19
day = 19

data = open('day19test.txt', 'r')
data = open('day19.txt', 'r')


def read_lab(data):
    """ Reads labirinth data. """
    lab = []
    riddle = ''    
    letters = string.ascii_uppercase
    for line in data:
        lab += [line]
    
    pos = [lab[0].find('|'), 0] # Start position
    direction = [0, 1] #Start direction
    print(pos, direction)
    steps = 0
    while True:
        if lab[pos[1]][pos[0]] in letters:
            riddle += lab[pos[1]][pos[0]]
        pos[0], pos[1] = pos[0] + direction[0], pos[1] + direction[1]
        #print(lab[pos[1]][pos[0]] )

        if  lab[pos[1]][pos[0]] == '+': # Change direction
            if direction[0] == 0:
                if lab[pos[1]][pos[0]-1] != ' ' and lab[pos[1]][pos[0]-1] != '+':
                    direction = [-1, 0]
                else:
                    direction = [1, 0]
            else:
                if lab[pos[1]-1][pos[0]] != ' ' and lab[pos[1]-1][pos[0]] != '+':
                    direction = [0, -1]
                else:
                    direction = [0, 1]
        steps += 1
        if lab[pos[1]][pos[0]] == ' ':
            print('end')
            break
    print(riddle, steps)
    return lab



t1 = time.time()
print("***  It's Advent of Code 2017, Day {}!  ***\n".format(day))
print('First part:')
a = read_lab(data)

print('Second part:')



t2 = time.time()
print('\nProgram run for  {0} sec.'.format(round(t2-t1,2)))

