# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 20:42:22 2018

@author: Jan
"""

import numpy as np
import pandas as pd
import time
import datetime as dt
from collections import defaultdict
import matplotlib.pyplot as plt
from collections import deque, namedtuple
import string

    


## Advent of Code 2019
day = 18
year = 2019

def day_str(day):
    """ Return string from integer day. """
    return str(day) if day >= 10 else '0' + str(day)
   
if __name__ == '__main__':
   
    t1 = time.time()
    print("***  It's Advent of Code {1}, Day {0}!  ***\n".format(day, year))
    #### 1st Task
    print('** First part:')
   
    with open('day{0}.txt'.format(day_str(day)), 'r') as f:
        data = [list(line.strip()) for line in f.readlines()]

    rows = len(data)
    cols = len(data[0])
   

    possible_keys = string.ascii_lowercase
    doors = string.ascii_uppercase
    
    dirs = [[-1,0], [+1,0], [0, -1], [0, +1]]
    
    robot_states = deque()
    Log = namedtuple('Log', ['row', 'col', 'keys', 'dist'])
    all_keys = set()
    for row in range(rows):
        for col in range(cols):
            if data[row][col] == '@': # Robot starts here
                print('Robot',  data[row][col], row, col)
                robot_states.append(Log(row, col, set(), 0))
            if data[row][col] in possible_keys:
                all_keys.add(data[row][col])
    
    print(robot_states)
    print(all_keys)



    been_here = set()
    distance = {(40,40): 0}
    
    while robot_states:
        state = robot_states.popleft()
        status = (state.row, state.col, tuple(sorted(state.keys)))
        #print(key)
        if status in been_here:
            continue
        been_here.add(status) 
        
        
        new_keys = set(state.keys)
        if data[state.row][state.col] in possible_keys:
            new_keys.add(data[state.row][state.col])
            if new_keys == all_keys: # found all keys, win!
                print(state.dist)
                break
            
        for dir_ in dirs: # Try all directions, do not try walls
            new_row = state.row + dir_[0]
            new_col = state.col + dir_[1]
            if data[new_row][new_col] != '#':
                if data[new_row][new_col] in doors and data[new_row][new_col].lower() not in state.keys: # I don't have a key
                    continue
                if (new_row, new_col) in distance:
                    continue
                distance[(new_row, new_col)] = distance[(state.row, state.col)] + 1
                robot_states.append(Log(new_row, new_col, new_keys, state.dist + 1))
   
    
    #### 2nd Task
    print('** Second part:')

    with open('day{0}_p2.txt'.format(day_str(day)), 'r') as f:
        data = [list(line.strip()) for line in f.readlines()]

    rows = len(data)
    cols = len(data[0])

    dirs = [[-1,0], [+1,0], [0, -1], [0, +1]]
    
    robot_states = deque()
    Log = namedtuple('Log', ['pos', 'keys', 'dist'])
    all_keys = {}
    all_doors = {}
    start = []

    
    for row in range(rows):
        for col in range(cols):
            if data[row][col] == '@': # Robot starts here
                start.append((row,col))
                
            if data[row][col] in possible_keys:
                all_keys[data[row][col]] = (row,col)
                
            if data[row][col] in doors:
                all_doors[data[row][col]] = (row,col)
    
    print(len(all_keys), all_keys)
    
    print(len(all_doors), all_doors)
    
    robot_states.append(Log(start, set(), 0))
    N = len(start)
    
    

    best = 10**5
    been_here = {}
    while robot_states and False:
        state = robot_states.popleft()
        key = (tuple(state.pos), tuple(sorted(state.keys)))
        #print(key)
        
        if key in been_here and state.dist >= been_here[key]:
            continue
        been_here[key] = state.dist
        
        if len(been_here) % 10000 == 0:
            print(key,state.dist)
            print(len(been_here))
            
        new_keys = set(state.keys)
    
        D = {}
        robot_states_2 = deque()
        for i in range(N):
            robot_states_2.append((state.pos[i], i, 0))
        while robot_states_2:
            pos, robot, dd = robot_states_2.popleft()
            row, col = pos
            D[pos] = (dd,robot)
            for dir_ in dirs: # Try all directions, do not try walls
                new_row = row + dir_[0]
                new_col = col + dir_[1]
                if data[new_row][new_col] != '#':
                    if data[new_row][new_col] in doors and data[new_row][new_col].lower() not in state.keys: # I don't have a key
                        continue
                    if (new_row, new_col) in D:
                        continue
                    robot_states_2.append(((new_row, new_col), robot, dd+1))

    
        for k in all_keys:
            if k not in state.keys and all_keys[k] in D:
                distance, robot = D[all_keys[k]]
                new_pos = list(state.pos)
                new_pos[robot] = all_keys[k]
                new_keys = set(state.keys)
                new_keys.add(k)
                new_dist = state.dist + distance
                if len(new_keys) == len(all_keys):
                    if new_dist < best:
                        best = new_dist
                        print(best)
                ok = True
                for pos in new_pos:
                    new_row = pos[0]
                    new_col = pos[1]
                    if data[new_row][new_col] == '#':
                        ok = False
                        break
                    if data[new_row][new_col] in doors and data[new_row][new_col].lower() not in state.keys: # I don't have a key
                        ok = False
                        break
                if ok:
                    robot_states.append(Log(new_pos, new_keys, new_dist))
    
    
    t2 = time.time()
    print('Program run for  {0} sec.'.format(round(t2 - t1, 2)))