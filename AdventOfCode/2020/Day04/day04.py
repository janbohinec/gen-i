# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 20:42:22 2018

@author: Jan B.
"""

import numpy as np
import pandas as pd
import time
import datetime as dt
import re

## Advent of Code 2020
day = 4
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
        data = [line.strip() for line in f.readlines()]
    
    attrs = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'] 
    optional = ['cid']
    
    password_valid = 0
     
    i = 0
    pass_cnt = 0
    while i < len(data):
        if data[i] == '': # new one
            if pass_cnt == len(attrs):
                password_valid += 1 # has everything   
            pass_cnt = 0
            i += 1
            continue
        
        pass_values = data[i].split(' ')
        
        for pass_value in pass_values:
            atr, val = pass_value.split(':')
            if atr in attrs:
                pass_cnt += 1

        i += 1
        
    # Count the last one doh
    if pass_cnt == len(attrs):
            password_valid += 1 # has everything  
        
    print(password_valid)
    
    #### 2nd Task
    print('** Second part:')

    # =============================================================================
    #     byr (Birth Year) - four digits; at least 1920 and at most 2002.
    #     iyr (Issue Year) - four digits; at least 2010 and at most 2020.
    #     eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
    #     hgt (Height) - a number followed by either cm or in:
    #     If cm, the number must be at least 150 and at most 193.
    #     If in, the number must be at least 59 and at most 76.
    #     hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
    #     ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
    #     pid (Passport ID) - a nine-digit number, including leading zeroes.
    #     cid (Country ID) - ignored, missing or not.  
    # =============================================================================

    limits = {
        'byr': {'min': 1920,
                'max': 2002},
        'iyr': {'min': 2010,
                'max': 2020},
        'eyr': {'min': 2020,
                'max': 2030},
        'hgt': {'cm': {'min': 150,
                       'max': 193},
                'in': {'min': 59,
                       'max': 76}
                },
        'hcl': {0: '#',
                'len': 6},
        'ecl': ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'],
        'pid':  {'len': 9},
        }

    
    password_valid = 0
     
    i = 0
    pass_cnt = 0
    while i < len(data):
        if data[i] == '': # new one
            if pass_cnt == len(attrs):
                password_valid += 1 # has everything   
            pass_cnt = 0
            i += 1
            continue
        
        pass_values = data[i].split(' ')
        
        for pass_value in pass_values:
            atr, val = pass_value.split(':')
            if atr in attrs:
                if atr in ['byr', 'iyr', 'eyr']:
                    if limits[atr]['min'] <= int(val) <= limits[atr]['max']:
                        pass_cnt += 1

                if atr == 'hgt':
                    if 'cm' in val or 'in' in val:
                        measure = val[-2:]
                        if limits[atr][measure]['min'] <= int(val[:-2]) <= limits[atr][measure]['max']:
                            pass_cnt += 1

                if atr == 'ecl':
                    if val in limits[atr]:
                       pass_cnt += 1
                        
                if atr == 'hcl':
                    if val[0] == limits[atr][0]:
                        len_char = len(re.findall('\w', val[1:])) # This is wrong, should include only a-f letters
                        if len_char == limits[atr]['len']:
                            pass_cnt += 1     
                       
                if atr == 'pid':
                    len_char = len(re.findall(r'\d', val))
                    if len_char == limits[atr]['len']:
                            pass_cnt += 1

        i += 1
        
    # Count the last one doh
    if pass_cnt == len(attrs):
            password_valid += 1 # has everything  
        
    print(password_valid)

    
    t2 = time.time()
    print('Program run for  {0} sec.'.format(round(t2 - t1, 2)))

