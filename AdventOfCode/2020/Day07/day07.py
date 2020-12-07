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

import string


## Advent of Code 2020
day = 7
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
        data = [line.strip().split('contain') for line in f.readlines()]
        
    
    colors = {}
    for rule in data:
        original_bag = rule[0].replace(' bags', '').strip()
        contains = rule[1].replace('.', '').replace('bags', '').replace('bag', '').strip().split(',')
        
        for contain in contains:
            if contain != 'no other':
                contain = contain.strip()
                number = list(map(int, re.findall('\d+', contain)))
                col = contain.replace(str(number[0]), '').strip()
                if original_bag not in colors.keys():
                    colors[original_bag] = {col: number[0]}
                else:
                    colors[original_bag][col] = number[0]
                
            else:
                colors[original_bag] = ''
        
    target_color = 'shiny gold'
    
    
    def depth_first(graph, current, visited):
        visited.append(current)
        for vertex in graph[current]:
            if vertex not in visited:
                depth_first(graph, vertex, visited.copy())
        all_paths.append(visited)
    
    
    cnt = 0
    for color in colors.keys():
        if color != target_color:
            all_paths = [[]]
            depth_first(colors, color, [])
            for l in all_paths:
                if target_color in l:
                    cnt += 1
                    break
    
    print(cnt)
    
    #### 2nd Task
    print('** Second part:')
    
    
    all_paths = [[]]
    depth_first(colors, target_color, [])
    
    cnt = 0
    for path in all_paths:
        if len(path) > 1:
            temp_cnt = 1
            for i in range(len(path) - 1, 0, -1):
                temp_cnt *= colors[path[i - 1]][path[i]]
            cnt += temp_cnt
    
    print(cnt)
    
    t2 = time.time()
    print('Program run for  {0} sec.'.format(round(t2 - t1, 2)))

