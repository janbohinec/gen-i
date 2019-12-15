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


## Advent of Code 2019
day = 15
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
        data = [line.strip().split(',') for line in f.readlines()]
    
    rr = defaultdict(lambda: 0, zip(range(len(data[0])),(int(r) for r in data[0])))
    
    def param(k, mode, base=0):
        if mode == 1:
            return rr[k]
        elif mode == 0:
            return rr[rr[k]]
        elif mode == 2:
            return rr[rr[k] + base]
        
    def turn(direction, where):
        if where == 1: #turn left
            if direction == [0,1]: #up
                return [-1,0]
            elif direction == [-1,0]: #left
                return [0,-1]
            elif direction == [0,-1]: #down
                return [1,0]
            elif direction == [1,0]: # right
                return [0,1]
        else: # turn right
            if direction == [0,1]: #up
                return [1,0]
            elif direction == [1,0]: #right
                return [0,-1]
            elif direction == [0,-1]: # down
                return [-1,0]
            else: # left
                return [0,1]
    
    def move(x, y, direction):
        # north (1), south (2), west (3), and east (4)
        if direction == 1:
            y += 1
        elif direction == 2:
            y -= 1
        elif direction == 3:
            x -= 1
        else:
            x += 1
        return x, y
    
    hist = []
    def intcode(inpt):
        global hist
        relative_base = 0
        i = 0
        output = 0
        
        x, y = 0, 0
        map_ = defaultdict(set)
        map_ = dict()
        
        inputs = [1,2,3,4]
        inpt_ind = 0
        moves = 0
        found = False
        map_[(x,y)] = 1

        while True:
            code = rr[i]
            code_str = str(abs(code))
            if len(code_str) == 5:
                modes = [int(code_str[0]), int(code_str[1]), int(code_str[2])]
            if len(code_str) == 4:
                modes = [0, int(code_str[0]), int(code_str[1])]                
            if len(code_str) == 3:
                modes = [0, 0, int(code_str[0])]
            if len(code_str) <= 2:
                modes = [0, 0, 0]       
    
            code = int(str(code)[-2:])
            if code == 3:
                offset = 0 if modes[-1] != 2 else relative_base
            else:
                offset = 0 if modes[-3] != 2 else relative_base
            if code == 1: # add
                rr[rr[i+3] + offset] = param(i+1, modes[-1], relative_base) + param(i+2, modes[-2], relative_base)
                step = 4
            elif code == 2: # multi
                rr[rr[i+3] + offset] = param(i+1, modes[-1], relative_base) * param(i+2, modes[-2], relative_base)
                step = 4
            elif code == 3: # input
                # north (1), south (2), west (3), and east (4)
                inpt_ind = np.random.randint(0,4)
                input_ = inputs[inpt_ind] # This could be better than random.
                if found:
                    input_ = 0
                rr[rr[i+1] + offset] = input_
                step = 2
            elif code == 4: # output
                output = param(i+1, modes[-1],  relative_base)
                #print('Output ', output, input_)
                moves += 1
                x_next, y_next = move(x,y,input_)
                if output == 2: # found repair spot
                    map_[(x_next,y_next)] = 5
                    print('Found repair spot!')
                    found = True
                    x, y = x_next, y_next
                elif output == 1: #moved
                    map_[(x_next,y_next)] = output
                    x, y = x_next, y_next
                elif output == 0: # hit the wall, same location
                   map_[(x_next,y_next)] = 3 
                step = 2 
            elif code == 5: # jump if true
                if param(i+1, modes[-1], relative_base) != 0:
                    i = param(i+2, modes[-2], relative_base)
                    step = 0
                else:
                    step = 3
            elif code == 6: # jump if false
                if param(i+1, modes[-1], relative_base) == 0:
                    i = param(i+2, modes[-2], relative_base)
                    step = 0
                else:
                    step = 3
            elif code == 7: # less than
                if param(i+1, modes[-1], relative_base) < param(i+2, modes[-2], relative_base):   
                    rr[rr[i+3] + offset] = 1
                else:
                    rr[rr[i+3] + offset] = 0
                step = 4
            elif code == 8: # equals
                if param(i+1, modes[-1], relative_base) == param(i+2, modes[-2],relative_base):   
                    rr[rr[i+3] + offset] = 1
                else:
                    rr[rr[i+3] + offset] = 0                
                step = 4
            elif code == 9: #relative mode change
                relative_base += param(i+1, modes[-1], relative_base)
                step = 2
            elif code == 99:
                break #stop
                
            i += step
            
            
            
        return map_
    
    
    map_ = intcode(0)
    import matplotlib.pyplot as plt
    
    
    # See the game
    a = [[0 for i in range(60)] for k in range(60)]

    for pos in map_.keys():
        a[pos[1]+30][pos[0]+30] = map_[pos]

    plt.imshow(a)
    
    map_copy = map_.copy()
    map_copy_test = map_.copy()
    map_copy[(0,0)] = 4
    map_copy_test[(0,0)] = 4
    found = False
    steps = 0
    while not found:
        for chord, value in map_copy.items():
            #print(chord)
            x,y = chord
            if map_copy[(x,y)] == 4:
                if (x+1,y) in map_copy.keys() and map_copy[(x+1,y)] == 1:
                    map_copy_test[(x+1,y)] = 4
                if (x-1,y) in map_copy.keys() and map_copy[(x-1,y)] == 1:
                    map_copy_test[(x-1,y)] = 4
                if (x,y+1) in map_copy.keys() and map_copy[(x,y+1)] == 1:
                    map_copy_test[(x,y+1)] = 4
                if (x,y-1) in map_copy.keys() and map_copy[(x,y-1)] == 1:
                    map_copy_test[(x,y-1)] = 4
                    
                if (x+1,y) in map_copy.keys() and map_copy[(x+1,y)] == 5:
                    found = True
                if (x-1,y) in map_copy.keys() and map_copy[(x-1,y)] == 5:
                    found = True
                if (x,y+1) in map_copy.keys() and map_copy[(x,y+1)] == 5:
                    found = True
                if (x,y-1) in map_copy.keys() and map_copy[(x,y-1)] == 5:
                    found = True
        map_copy = map_copy_test.copy()
        steps += 1
    print(steps - 1)
    
    
    # See the game
    a = [[0 for i in range(60)] for k in range(60)]

    for pos in map_copy.keys():
        a[pos[1]+30][pos[0]+30] = map_copy[pos]

    plt.imshow(a)

    #### 2nd Task
    print('** Second part:')
    
    map_copy = map_.copy()
    map_copy_test = map_.copy()
    map_copy[(-20,-14)] = 4
    map_copy_test[(-20,-14)] = 4
    paint_needed = True # at least one painting
    steps = 0
    while paint_needed:
        paint_needed = False
        for chord, value in map_copy.items():
            #print(chord)
            x,y = chord
            
            if map_copy[(x,y)] == 1:
                paint_needed = True
            if map_copy[(x,y)] == 4:
                if (x+1,y) in map_copy.keys() and map_copy[(x+1,y)] == 1:
                    map_copy_test[(x+1,y)] = 4
                if (x-1,y) in map_copy.keys() and map_copy[(x-1,y)] == 1:
                    map_copy_test[(x-1,y)] = 4
                if (x,y+1) in map_copy.keys() and map_copy[(x,y+1)] == 1:
                    map_copy_test[(x,y+1)] = 4
                if (x,y-1) in map_copy.keys() and map_copy[(x,y-1)] == 1:
                    map_copy_test[(x,y-1)] = 4

        map_copy = map_copy_test.copy()
        steps += 1
    print(steps)
    

       
    
    
    
    
    t2 = time.time()
    print('Program run for  {0} sec.'.format(round(t2 - t1, 2)))