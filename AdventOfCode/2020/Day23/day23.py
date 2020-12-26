0# -*- coding: utf-8 -*-
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
import math
import itertools

## Advent of Code 2020
day = 23
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
        data = f.read().split('\n')
        #data = [line.strip() for line in f.readlines()]
    
    cups = '215694783'
    #cups = '389125467'
    
    cups = [int(c) for c in cups]
    current = cups[0]

    
    def ordering(cups):
        i = cups.index(1)
        order = cups[i + 1:] + cups[:i]
        return ''.join(str(c) for c in order)
    
   
    n = 100
    
    i = 0
    while i < n:        
        current_i = cups.index(current)
        temp_cups = cups + cups
        pick_ups = temp_cups[current_i + 1 : current_i + 4]


        for pick_up in pick_ups:
            pick_up_i = cups.index(pick_up)
            cups.pop(pick_up_i)

        # find destination
        dest = 0
        dest_try = current - 1
        while dest == 0:
            if dest_try in cups:
                dest = dest_try
            dest_try -= 1
            if dest_try <= 0:
                dest_try = max(cups)
        
        dest_i = cups.index(dest)
        
        cups = cups[0:dest_i+1] + pick_ups + cups[dest_i+1:]
        
        current_i = cups.index(current) + 1
        if current_i == len(cups):
            current_i = 0
        
        current = cups[current_i]
        
        i += 1
         
    
    print(ordering(cups))
  
        
    #### 2nd Task
    print('** Second part:')
    
    cups = '215694783'
    #cups = '389125467'
    
    cups = [int(c) for c in cups]
    current = cups[0]
    
    cups = cups + [i for i in range(len(cups) + 1, 1000000 + 1)]
    
    n = 10000000
    
    cups_linked = {}
    for i, cup in enumerate(cups[:-1]):
        cups_linked[cup] = cups[i+1]
    cups_linked[cups[-1]] = cups[0]
    
    
    i = 0
    while i < n:            
        pick_up_start = cups_linked[current]
        pick_up_mid = cups_linked[cups_linked[current]]
        pick_up_end = cups_linked[cups_linked[cups_linked[current]]]
        cups_linked[current] = cups_linked[cups_linked[cups_linked[cups_linked[current]]]]

         # find destination
        dest = 0
        dest_try = current - 1
        while dest == 0:
            if dest_try >= 0:
                if dest_try not in [pick_up_start, pick_up_mid, pick_up_end]:
                    dest = dest_try
            dest_try -= 1
            if dest_try <= 0:
                dest_try = max(cups_linked.keys())
        
        cups_linked[pick_up_end] = cups_linked[dest]
        cups_linked[dest] = pick_up_start
        
        current = cups_linked[current]
        
        i += 1
    
    
    print(cups_linked[1] * cups_linked[cups_linked[1]])
    
    t2 = time.time()
    print('Program run for  {0} sec.'.format(round(t2 - t1, 2)))

