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
day = 13
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
    
    
    hist = []
    def intcode(inpt):
        global hist
        relative_base = 0
        i = 0
        output = 0
        

        block_cnt = 0
        meaning = 1 # 1 == x or 2 == y or 3 == tile id
        map_ = defaultdict(set)
        paddlex, paddley = 0, 0
        ballx, bally = 0, 0
        last_score = 0
        prev_ball_x, prev_ball_y = 0, 0
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
            elif code == 3: # copy
                # where does the ball go next?
                next_x = ballx + (ballx - prev_ball_x)
                next_y = bally + (bally - prev_ball_y)
                if (next_x, next_y) in map_.keys() and map_[(next_x, next_y)] in (1,2):
                    next_x = ballx
                
                if paddlex < next_x:
                    rr[rr[i+1] + offset] = +1    
                elif paddlex > next_x:
                    rr[rr[i+1] + offset] = -1
                step = 2
            elif code == 4: # output
                output = param(i+1, modes[-1],  relative_base)
                if meaning == 3 and output == 2:
                    block_cnt += 1
                if meaning == 1:
                    x = output
                elif meaning == 2:
                    y = output
                if meaning == 3:
                    tileID = output
                    if x == -1 and y == 0:
                        #print('New score: {0}'.format(output))
                        last_score = output
                    else:
                        map_[(x,y)] = tileID
                        if tileID == 4: # Its a ball
                            prev_ball_x, prev_ball_y = ballx, bally
                            ballx, bally = x, y
                            hist += [map_.copy()]
                            # where is ball?
                            #print('Ball: ({0},{1})'.format(ballx, bally))    
                        elif tileID == 3: # its a paddle
                            paddlex, paddley = x, y
                            # where is paddle?
                            #print('Paddle: ({0},{1})'.format(paddlex, paddley))
                    
                meaning += 1
                if meaning == 4:
                    meaning = 1
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

        return map_, block_cnt, ballx, bally, paddlex, paddley, last_score
    
    
    map_, block_cnt, ballx, bally, paddlex, paddley, last_score = intcode(0)
    print(block_cnt)


    #### 2nd Task
    print('** Second part:')
    
    
    rr[0] = 2 # play for free
    
    import matplotlib.pyplot as plt
    
    map_, blocks, ballx, bally, paddlex, paddley, last_score = intcode(0)
    print(last_score)
    
    # See the game
    a = [[0 for i in range(40)] for k in range(40)]


    for pos in hist[0].keys():
        a[pos[1]][pos[0]] = hist[0][pos]

    plt.imshow(a)
       
    
    
    
    
    t2 = time.time()
    print('Program run for  {0} sec.'.format(round(t2 - t1, 2)))