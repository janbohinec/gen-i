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
day = 9
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
        
    
    def intcode(inpt):
        
        relative_base = 0
        i = 0
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
                rr[rr[i+1] + offset] = inpt
                step = 2
            elif code == 4: # output
                #output = rr[rr[i+1]]
                output = param(i+1, modes[-1],  relative_base)
                print('Output:', output)
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
            
        return output
    
    
    
    #data = [109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99]
    #data = [1102,34915192,34915192,7,4,7,99,0]
    #data = [104,1125899906842624,99]
    #rr = defaultdict(lambda: 0, zip(range(len(data)),(int(r) for r in data)))
    
    intcode(1)
    intcode(2)
    

    #### 2nd Task
    print('** Second part:')

      
    
    t2 = time.time()
    print('Program run for  {0} sec.'.format(round(t2 - t1, 2)))