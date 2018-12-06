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
import operator

## Advent of Code 2018, Day 4
day = 4


if __name__ == '__main__':
    
    t1 = time.time()
    print("***  It's Advent of Code 2018, Day {0}!  ***\n".format(day))
    print('** First part:')
    
    #with open('day4.txt', 'r') as f:
    #    data = [line.strip() for line in f.readlines()]
        
    data = open('day5wagi.txt', 'r')
    data = data.readline()
    #data = text.copy()
         
    #data = 'dabAcCaCBAcCcaDA'
    
    found = True
    while found:
        found = False
        for i in range(len(data) - 1):
            try:
                if data[i] != data[i+1] and data[i].lower() == data[i+1].lower():
                    data = data[:i] + data[i+2:]
                    found = True
            except:
                pass
        
    res = len(data)
    ds 
    print('Silver star answer: \n{0}'.format(res))
    
    print('** Second part:')
    
  
    import string
    
    alphabet = string.ascii_lowercase
    data = data.lower()
    minimal = np.inf
    
    for char in alphabet:
        #data = text.copy()
        data = data.replace(char, '').replace(char.upper(), '')

        
        found = True
        while found:
            found = False
            for i in range(len(data) - 1):
                try:
                    if data[i] != data[i+1] and data[i].lower() == data[i+1].lower():
                        data = data[:i] + data[i+2:]
                        found = True
                except:
                    pass

        if len(data) < minimal:
            minimal = len(data)
            print(len(data), char)
    
    print('Golden star answer: \n{0}'.format(minimal))
    t2 = time.time()
    print('Program run for  {0} sec.'.format(round(t2-t1,2)))

