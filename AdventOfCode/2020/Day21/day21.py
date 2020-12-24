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
day = 21
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
        
    ingrs_all = []
    allergens_all = []
    for food in data:
        ingrs, allergens = food.split('(contains ')
        ingrs = ingrs.strip().split(' ')
        allergens = allergens.replace(')', '').split(', ')
        #print(ingrs, allergens)
        for ingr in ingrs:
            if ingr not in ingrs_all:
                ingrs_all += [ingr]
    
    
        for a in allergens:
            if a not in allergens_all:
                allergens_all += [a]

        
    ingredients = {}
    for ingr in ingrs_all:
        ingredients[ingr] = copy.deepcopy(allergens_all)
        
    
    for food in data:
        ingrs, allergens = food.split('(contains ')
        ingrs = ingrs.strip().split(' ')
        allergens = allergens.replace(')', '').split(', ')
        
        for i in range(len(allergens)):
            for ing in ingredients.keys():
                if allergens[i] in ingredients[ing] and ing not in ingrs:
                    ingredients[ing].remove(allergens[i])
                    
                        
            
          
    cnt = 0

    for food in data:
        ingrs, allergens = food.split('(contains ')
        ingrs = ingrs.strip().split(' ')
        allergens = allergens.replace(')', '').split(', ')  
        
        #print(ingrs)
        for ing in ingrs:
            if len(ingredients[ing]) == 0:
                cnt += 1
                
    print(cnt)
        
    #### 2nd Task
    print('** Second part:')
    
    
    with_allergens = {}

    for allergen in allergens_all:
        seznam = []    
    
        for ing in ingredients.keys():
            if allergen in ingredients[ing]:
                seznam += [ing]
        
        with_allergens[allergen] = seznam
    
    
    for k in range(5):
        for allergen in allergens_all:
            if len(with_allergens[allergen]) == 1:
                for allergen2 in allergens_all:
                    if allergen != allergen2 and with_allergens[allergen][0] in with_allergens[allergen2]:
                        with_allergens[allergen2].remove(with_allergens[allergen][0])
    

    str_ = ''
    for allergen in sorted(allergens_all):
        str_ = str_ + with_allergens[allergen][0] + ','
        
    print(str_[:-1])


    t2 = time.time()
    print('Program run for  {0} sec.'.format(round(t2 - t1, 2)))

