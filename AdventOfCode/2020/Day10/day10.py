# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 20:42:22 2018

@author: Jan B.
"""

import numpy as np
import pandas as pd
import time
import datetime as dt
import matplotlib.pyplot as plt
import re
import copy
import string


## Advent of Code 2020
day = 10
year = 2020

def day_str(day):
    """ Return string from integer day. """
    return str(day) if day >= 10 else '0' + str(day)
    

if __name__ == '__main__':
    
    t1 = time.time()
    print("***  It's Advent of Code {1}, Day {0}!  ***\n".format(day, year))
    #### 1st Task
    print('** First part:')
    
    
    with open('day{0}.txt'.format(day_str(day)), 'r') as f:
        #data = f.read().split('\n\n')
        data = [line.strip().split(' ') for line in f.readlines()]
        
    
    for i in range(len(data)):
        data[i] = int(data[i][0])
        
    jolt_1 = 1
    jolt_3 = 1
    data.sort()
    for i in range(len(data)-1):
        if data[i+1] - data[i] == 1:
            jolt_1 += 1
        elif data[i+1] - data[i] == 3:
            jolt_3 += 1

        
    print(jolt_1,  jolt_3)

    print(jolt_1 * jolt_3)
    #### 2nd Task
    print('** Second part:')
    
      
    data = [0] + data
    
    graph = {0: 0}
    for i in range(len(data)):

        test = []
        for k in [1,2,3]:
            if data[i] + k in data:
                test += [data[i] + k]
        graph[data[i]] = test
            

    def find_all_paths(graph, start, end, path=[]):
        path = path + [start]
        if start == end:
            return [path]
        if not start in graph:
            return []
        paths = []
        for node in graph[start]:
            if node not in path:
                newpaths = find_all_paths(graph, node, end, path)
                for newpath in newpaths:
                    paths.append(newpath)
        return paths
    

    no = 1
    no = len(find_all_paths(graph, 0, 3))
    vortexes = list(graph.values())
    start = 0
    end = 0
    for i in range(len(vortexes)-1):
        if len(vortexes[i]) == 1 and len(vortexes[i+1]) > 1:
            start = vortexes[i][0]

        if start > 0 and len(vortexes[i]) > 1 and len(vortexes[i+1]) == 1:
            end = vortexes[i+1][0]
            
        if start > 0 and end > 0:
            no *= len(find_all_paths(graph, start, end))
            start = 0
            end = 0
    
    
    print(no)
    
    


    
    t2 = time.time()
    print('Program run for  {0} sec.'.format(round(t2 - t1, 2)))

