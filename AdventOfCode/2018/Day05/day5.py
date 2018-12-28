# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 20:42:22 2018

@author: Jan
"""


import numpy as np
import pandas as pd
import time
import datetime as dt


## Advent of Code 2018, Day 5
day = 5


if __name__ == '__main__':
    
    t1 = time.time()
    print("***  It's Advent of Code 2018, Day {0}!  ***\n".format(day))
    print('** First part:')
    
    with open('day{0}.txt'.format(day), 'r') as f:
        data = f.read().strip()
        
    
    lc = ord('a')
    uc = ord('A')

    def reacting(polymer):  
        """ Reacts the polymer """
        polymer = polymer.strip()
        polymer_new = []

        for i in range(len(polymer)):
            polymer_new.append(polymer[i])
            if len(polymer_new) > 1:
                if abs(ord(polymer_new[-1]) - ord(polymer_new[-2])) == lc - uc:
                    polymer_new.pop()
                    polymer_new.pop()
        return polymer_new
         
    
    polymer_new = reacting(data)

    res = len(polymer_new)
    
       
    #res = len(data)
    print('Silver star answer: \n{0}'.format(res))
    
    print('** Second part:')
    
    import string
    
    alphabet = string.ascii_lowercase
    minimal = len(data)
    
    for char in alphabet:
        polymer = data.replace(char, '').replace(char.upper(), '')
        polymer_new = reacting(polymer)

        if len(polymer_new) < minimal:
            minimal = len(polymer_new)
            print(len(polymer_new), char)
    
    print('Golden star answer: \n{0}'.format(minimal))
    t2 = time.time()
    print('Program run for  {0} sec.'.format(round(t2-t1,2)))

