# -*- coding: utf-8 -*-
"""
Created on Tue Dec 26 10:04:49 2017

@author: janb
"""


import numpy as np
import pandas as pd
import time


## Advent of Code 2017, Day 22
day = 22

#data = open('day22test.txt', 'r')
data = open('day22.txt', 'r')
#data = data.read().split(',')

def getMap(data):
    mapp = []
    for line in data:
        line = line.replace('\n', '').replace('#', '1').replace('.', '0')
        line = [int(i) for i in line]
        mapp += [line]
    return mapp

def turn_left(smer):
    if smer == [0,-1]:
        return [-1,0]
    elif smer == [-1,0]:
        return [0,1]
    elif smer == [0,1]:
        return [1,0]
    else:
        return [0,-1]

def turn_right(smer):
    if smer == [0,-1]:
        return [1,0]
    elif smer == [1,0]:
        return [0,1]
    elif smer == [0,1]:
        return [-1,0]
    else:
        return [0,-1]  

def turn_reverse(smer):
    if smer == [0,-1]:
        return [0,1]
    elif smer == [1,0]:
        return [-1,0]
    elif smer == [0,1]:
        return [0,-1]
    else:
        return [1,0]  

def worm(disc, bursts = 10):
    """ Let the worm do its magic. """
    smer = [0, -1]
    pos = [(len(disc) - 1)//2, (len(disc) - 1) // 2]
    infected = 0
    burst = 0
    # infected = 1, clean = 0, weakened = 2, flagged = 3
    while burst < bursts:
        status = disc[pos[1]][pos[0]]
        if status == 0: # infect and turn left
            disc[pos[1]][pos[0]] = 1
            smer = turn_left(smer)
            infected += 1
        else: # uninfect and turn right
            disc[pos[1]][pos[0]] = 0
            smer = turn_right(smer)
        # Move
        pos[0] = pos[0] + smer[0]
        pos[1] = pos[1] + smer[1]
        burst += 1
        #print(disc)
    return infected

def resize(disc, N):
    newdisc = np.zeros((N, N))
    n = len(disc)
    i = (N - n) // 2
    j = i
    newdisc[i:i+n, j:j+n] = disc
    
    return newdisc


t1 = time.time()
print("***  It's Advent of Code 2017, Day {}!  ***\n".format(day))
print('First part:')
disc = getMap(data)
disc = resize(disc, 455)
#print(disc)

print(worm(disc, 10000))

print('Second part:')



t2 = time.time()
print('\nProgram run for  {0} sec.'.format(round(t2-t1,2)))

