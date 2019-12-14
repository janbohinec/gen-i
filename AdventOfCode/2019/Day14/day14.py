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
day = 14
year = 2019

def day_str(day):
    """ Return string from integer day. """
    return str(day) if day >= 10 else '0' + str(day)
    


class Item():
    
    def __init__(self, quantity):
        self.quantity = quantity
        self.required = {}
        self.acquired = 0
        self.count = 0
        
    def collect(self, needed):
        if len(self.required) > 0:
            while self.count < needed:
                multiplier = (needed - self.count) // self.quantity
                if (needed - self.count) % self.quantity != 0: # one more needed 
                    multiplier += 1
                for (name, qty) in self.required.items():
                    #print(name, qty)
                    materials[name].collect(multiplier * qty)
                self.count += self.quantity * multiplier
            self.count -= needed # use needed, but left the res in the inventory

        self.acquired += needed

        

if __name__ == '__main__':
    
    t1 = time.time()
    print("***  It's Advent of Code {1}, Day {0}!  ***\n".format(day, year))
    #### 1st Task
    print('** First part:')
    

    

    materials = dict()
    materials['ORE'] = Item(1) # without required.
    with open('day{0}.txt'.format(day_str(day)), 'r') as f:
        for line in f:
            line = line.strip().split(' => ')
            chemicals = []
            requires = {}
            for chem in line[0].split(', '):
                qty, name = chem.split(' ')
                requires[name] = int(qty)
            qty, name = line[1].split(' ')
            materials[name] = Item(int(qty))
            materials[name].required = requires
            
    
    print(materials['FUEL'].required)
    
    materials['FUEL'].collect(1)
    print(materials['ORE'].acquired)
    

    
    #### 2nd Task
    print('** Second part:')
    
    guess = 3340000
    materials['FUEL'].collect(guess)
    while materials['ORE'].acquired < 1000000000000: # Bruteforce
        materials['FUEL'].collect(1)
        #print(materials['FUEL'].acquired - 1)
        #break
    
    
    #materials['FUEL'].collect(10000)
    print(materials['ORE'].acquired)
    print(materials['FUEL'].acquired - 1)

      
        
    t2 = time.time()
    print('Program run for  {0} sec.'.format(round(t2 - t1, 2)))
    