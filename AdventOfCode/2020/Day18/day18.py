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
day = 18
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
        data = [line.strip().split(',') for line in f.readlines()]
        
        
    def strange_math(expression):
        expression = expression.replace(' ', '')
        
        numbers = re.findall(r'\d+', expression)
        symbols = re.findall(r'\D+', expression)
                   
        math = int(numbers[0])
        i = 1
        for symbol in symbols:
            if symbol == '+':
                math += int(numbers[i])
            elif symbol == '*':
                math *= int(numbers[i])
            i += 1
        return math

    sum_ = 0
    for line in data:
        row = line[0]
        
        while '(' in row:
        
            p = re.compile(r'(\([^(]*?\))')
            items = p.findall(row)
            
            for item in items:
                first = p.findall(item)[0]
                first2 = first.replace('(','').replace(')','')
                
                mid_calc = strange_math(first2)
                row = row.replace(first, str(mid_calc))
    
        
        strange_result = strange_math(row)
        
        sum_ += strange_result
        
    print(sum_)


    #### 2nd Task
    print('** Second part:')

    def strange_math_advanced(expression):
        
        expression = expression.replace(' ', '')
        
        numbers = re.findall(r'\d+', expression)
        symbols = re.findall(r'\D+', expression)
             

        i = 0
        for symbol in symbols.copy():
            if symbol == '+':
                numbers[i] = int(numbers[i]) + int(numbers[i+1])
                del symbols[i]
                del numbers[i+1]
            else:
                i += 1
        
        if len(numbers) > 1:
            math = 1
            i = 0
            for number in numbers:
                math *= int(number)
        else:
            math = numbers[0]
        return math

    sum_ = 0
    for line in data:
        row = line[0]
        
        while '(' in row:
        
            p = re.compile(r'(\([^(]*?\))')
            items = p.findall(row)
            
            for item in items:
                first = p.findall(item)[0]
                first2 = first.replace('(','').replace(')','')
                
                mid_calc = strange_math_advanced(first2)
                row = row.replace(first, str(mid_calc))

        
        strange_result = strange_math_advanced(row)

        
        sum_ += strange_result
        
    print(sum_)

    t2 = time.time()
    print('Program run for  {0} sec.'.format(round(t2 - t1, 2)))

