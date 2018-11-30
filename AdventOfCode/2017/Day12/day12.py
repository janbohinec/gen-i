# -*- coding: utf-8 -*-
"""
Created on Fri Dec 23 17:51:22 2017

@author: Jan
"""


import numpy as np
import pandas as pd
import time

## Advent of Code 2017, Day 12

data = open('day12.txt', 'r')

def village_connections(data):
    """ Get village connections in a dictionary/graph. """
    connections = {}
    for pipe in data:
        ID_ = int(pipe[:pipe.find('<')])
        neighbors = list(map(int, pipe[pipe.find('>')+1:-1].replace(' ','').split(',')))
        connections[ID_] = neighbors
    return connections
   
def count_connections(cons, ID):
    """ Count all indirectly connected to ID. """     
    connected = cons[ID].copy()
    st = 0
    while st < len(connected):
        for neigh in cons[connected[st]]:
            if neigh not in connected:
                connected += [neigh]
        st += 1
    return connected

def count_groups(cons):
    """ Count all groups. """
    groups = 0
    connected = {}
    for program in cons:
        if program not in connected:
            connections = count_connections(cons, program)
            for p in connections:
                connected[p] = True
            groups += 1
    return groups
    

t1 = time.time()
print('Test')
cons = village_connections(data)
result = count_connections(cons, 0)
print(len(result))

print('2nd part anwswer')
print(count_groups(cons))

t2 = time.time()
print('Program run for  {0} sec.'.format(round(t2-t1,2)))

