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
day = 25
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
        
    card_public_key = int(data[0])
    door_public_key = int(data[1])
    card_secret_loop, door_secret_loop = 0, 0
    
    reminder = 20201227
    
    found = False
    k = 1
    subject_number = 7
    number = 1
    
    while not found:
        number = (number * subject_number) % reminder
        if number == card_public_key:
            card_secret_loop = k
            i = 0
        if number == door_public_key:
            door_secret_loop = k
            i = 1
        
        k += 1
        if card_secret_loop != 0 or door_secret_loop != 0:
            found = True
        

    print(card_secret_loop, door_secret_loop)
    
    if i == 0:
        encryption_key = door_public_key
        loops = card_secret_loop - 1
    else:
        encryption_key = card_public_key
        loops = door_secret_loop - 1
    
    for k in range(loops):
        encryption_key *= door_public_key
        encryption_key = encryption_key % reminder
        

    print(encryption_key)
   
        
    
    #### 2nd Task
    print('** Second part:')
    

    ### Game Over, Get Some Life Now And Spend Your Time With Urška


    t2 = time.time()
    print('Program run for  {0} sec.'.format(round(t2 - t1, 2)))

