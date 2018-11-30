# -*- coding: utf-8 -*-
"""
Created on Fri Dec 22 22:27:22 2017

@author: Jan
"""


import numpy as np
import pandas as pd
from itertools import count
import time

## Advent of Code 2017, Day 6


initial_bank_config = [11, 11, 13, 7, 0, 15, 5, 5, 4, 4, 1, 1, 7, 1, 15, 11]
#initial_bank_config = [0, 2, 7, 0]
all_bank_configs = [initial_bank_config]

def redistribute(config):
    """ Redistributes wealth in a bank. """
    max_wealth = config.index(max(config)) # get index at max wealth position
    wealth = config[max_wealth] # Get max wealth
    config[max_wealth] = 0 # Set max_wealth to 0 
    for i in range(wealth): # Redistribute
        config[np.mod(max_wealth + i + 1, len(config))] += 1                
    return config
    
def count_redistributions(initial):
    """ Counts redistirbutions. """
    config = initial
    all_bank_configs = []
    while config not in all_bank_configs:
        all_bank_configs += [config.copy()]
        config = redistribute(config)
    when = all_bank_configs.index(config)
    print(len(all_bank_configs) - when)
    return len(all_bank_configs)


t1 = time.time()
print('Test')
#print(redistribute(initial_bank_config))
print(count_redistributions(initial_bank_config))

print('2nd part test')
print()
print('2nd part anwswer')

t2 = time.time()
print('Program run for  {0} sec.'.format(round(t2-t1,2)))

