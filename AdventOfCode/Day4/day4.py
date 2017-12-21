# -*- coding: utf-8 -*-
"""
Created on Thu Dec 21 21:08:22 2017

@author: Jan
"""



import numpy as np
import pandas as pd
from itertools import count
import time

## Advent of Code 2017, Day 4

data = pd.read_excel('Day4.xlsx', header = None)

def is_anagram(str1, str2):
    if isinstance(str1, str) and isinstance(str2, str):
        list_str1 = list(str1)
        list_str1.sort()
        list_str2 = list(str2)
        list_str2.sort()
        return (list_str1 == list_str2)
    else:
        return False

def check_passphrase(data):
    """ Counts valid phrases: """
    vsota = 0
    wrong = 0
    for index, row in data.iterrows():
        #print(row.values)
        end = False
        for i in range(len(row.values)):
            word = row.values[i]
            for j in range(len(row.values)):
                word2 = row.values[j]
                #print(word, word2)
                #print(is_anagram(word, word2), word, word2)
                if i != j and is_anagram(word, word2):
                    wrong += 1
                    end = True
                    break
            if end:
                break
        vsota += 1
    return vsota - wrong


t1 = time.time()
print('Test')
print(check_passphrase(data))

print('2nd part test')
print()
print('2nd part anwswer')

t2 = time.time()
print('Program run for  {0} sec.'.format(round(t2-t1,2)))

