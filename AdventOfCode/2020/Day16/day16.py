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
day = 16
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

    
    my_ticket = False
    nearby_tickets = False
    nearby_tickets_numbers = []
    words = {}
    # Parser
    for line in data:
        if line[0] == '':
            continue
        
        if not my_ticket and not nearby_tickets and line[0] != 'your ticket:':
            
            word, attrs = line[0].split(': ')
            
            first, second = attrs.split(' or ')
            
            valid_list = []
            first_1, first_2 = first.split('-')
            second_1, seconds_2 = second.split('-')

            valid_list += [[int(first_1), int(first_2)]]
            valid_list += [[int(second_1), int(seconds_2)]]

            words[word] = valid_list
        
        if my_ticket and not nearby_tickets and line[0] != 'nearby tickets:':
            my_ticket_numbers = [int(i) for i in line] 
        if nearby_tickets:
            nearby_tickets_numbers +=  [[int(i) for i in line] ]
        
        if line[0] == 'your ticket:':
            my_ticket = True
        if line[0] == 'nearby tickets:':
            nearby_tickets = True
        
    # Calculation

    error_rate = 0    
    for ticket in nearby_tickets_numbers:
        
        for num in ticket:
            num_valid = False
            
            for word in words.keys():
                condition1, condition2 = words[word]
                
                if condition1[0] <= num <= condition1[1] or condition2[0] <= num <= condition2[1]:
                    num_valid = True
                    break
                
            if not num_valid:
                error_rate += num
    
    print(error_rate)
    
    #### 2nd Task
    print('** Second part:')


    valid_tickets = []
    
    for ticket in nearby_tickets_numbers:
        valid_ticket = True
        
        for num in ticket:
            num_valid = False
            
            for word in words.keys():
                condition1, condition2 = words[word]
                
                if condition1[0] <= num <= condition1[1] or condition2[0] <= num <= condition2[1]:
                    num_valid = True
                    break
            
            if not num_valid:
                valid_ticket = False
                break
                
        if valid_ticket:
            valid_tickets += [ticket]
    
    
    words_index = {}
    for word in words.keys():
        
        list_of_is = []
        i = 0
        while i < len(ticket): # Loop through the tindex
            index_true = True
        
            for ticket in valid_tickets:
                condition1, condition2 = words[word]
                
                
                if not condition1[0] <= ticket[i] <= condition1[1] and not condition2[0] <= ticket[i] <= condition2[1]:
                    index_true = False
                    break
            
            if index_true:
                list_of_is += [i]
            i += 1

            
        words_index[word] = list_of_is
    
    
    
    words_index_true = {}
    
    k = 0
    while k < len(words_index.keys()):
        for word in words_index.keys():
            if len(words_index[word]) == 1:
                true_index = words_index[word][0]
                words_index_true[word] = true_index
                # delete this number from all other options
                for word2 in words_index.keys():
                    if true_index in words_index[word2]:
                        words_index[word2].remove(true_index)
        k += 1
             
    
    num = 1
    for key in words_index.keys():
        if 'departure' in key:          
            num *= my_ticket_numbers[words_index_true[key]]

    print(num)

    t2 = time.time()
    print('Program run for  {0} sec.'.format(round(t2 - t1, 2)))

