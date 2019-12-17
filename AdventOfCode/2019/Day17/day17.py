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
day = 17
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

        input_ = 0
        history = []

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
                print(input_)
                rr[rr[i+1] + offset] = input_
                step = 2
            elif code == 4: # output
                output = param(i+1, modes[-1],  relative_base)
                #print('Output ', output, input_)
                history += [output]
# =============================================================================
# =============================================================================
# #                 moves += 1
# #                 x_next, y_next = move(x,y,input_)
# #                 if output == 2: # found repair spot
# #                     map_[(x_next,y_next)] = 5
# #                     print('Found repair spot!')
# #                     x, y = x_next, y_next
# #                 elif output == 1: #moved
# #                     map_[(x_next,y_next)] = output
# #                     x, y = x_next, y_next
# #                 elif output == 0: # hit the wall, same location
# #                    map_[(x_next,y_next)] = 3 
# =============================================================================
# =============================================================================
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
            
            
            
        return history
    
    
    lab = intcode(0)
    import matplotlib.pyplot as plt
    
    lab2 = []
    temp = []
    for cord in lab:   
        if cord == 10: #new line
            if len(temp) > 0:
                lab2 += [temp]
            temp = []
        else:
            
            temp += [cord]
    
    # See the game
    plt.imshow(lab2)
    
  
    score = 0
    for x in range(len(lab2)):
        for y in range(len(lab2[0])):
            if x > 0 and y > 0 and x < 38 and y < 28 and  lab2[x][y] == 35:
                if lab2[x+1][y] == 35 and lab2[x-1][y] == 35 and lab2[x][y+1] == 35 and lab2[x][y-1] == 35:
                    print('Intersections ', x, y)
                    score += x*y
    print(score)

    
    
   

    #### 2nd Task
    print('** Second part:')
    
  
       
    
    
    
    
    t2 = time.time()
    print('Program run for  {0} sec.'.format(round(t2 - t1, 2)))