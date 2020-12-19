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


## Advent of Code 2020
day = 14
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
        data = [line.strip().split(' = ') for line in f.readlines()]


    def apply_mask(value, mask):
        string = "{0:b}".format(value)
        if len(mask) > len(string):
            string = '0' * (len(mask) - len(string))  + string
        string = list(string)
        for i, char in enumerate(mask):
            if char != 'X':
                string[i] = char
        string = ''.join(string)
        value = int(string, 2)
        return value
    
    
    memory = {}
    for line in data:
        first, second = line[0], line[1]
        if first == 'mask':
            mask = second
        else:
            i = int(first.replace('mem[', '').replace(']', ''))
            value = int(second)
        
            new_value = apply_mask(value, mask)
            memory[i] = new_value
    
    
    print(sum(memory.values()))

    
    #### 2nd Task
    print('** Second part:')


    def apply_mask2(value, mask):
        string = "{0:b}".format(value)
        if len(mask) > len(string):
            string = '0' * (len(mask) - len(string))  + string
        
        string = list(string)
        
        for i, char in enumerate(mask):
            if char == '1':
                string[i] = '1'
            elif char == 'X':
                string[i] = 'X'
                
        string = ''.join(string)
        
        return string


    memory = {}
    for line in data:
        first, second = line[0], line[1]
        if first == 'mask':
            mask = second
        else:
            i = int(first.replace('mem[', '').replace(']', ''))
            value = int(second)
        
            addresses = apply_mask2(i, mask)
            addresses = list(addresses)
            
            combinations = 2**addresses.count('X')
            
            
            for comb in range(combinations):
                string = "{0:b}".format(comb)
                
                if len(string) < addresses.count('X'):
                    string = '0' * (addresses.count('X') - len(string))  + string
                
                k = 0
                new_string = addresses.copy()
                for i, char in enumerate(addresses):
                    if char == 'X':
                        new_string[i] = string[k]
                        k += 1
                
                new_string = ''.join(new_string)
                address = int(new_string, 2)
                    
                memory[address] = value
    
    
    print(sum(memory.values()))
    

    t2 = time.time()
    print('Program run for  {0} sec.'.format(round(t2 - t1, 2)))

