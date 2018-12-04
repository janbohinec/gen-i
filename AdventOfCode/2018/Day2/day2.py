# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 20:42:22 2018

@author: Jan
"""

import numpy as np
import pandas as pd
import time
import datetime as dt

## Advent of Code 2018, Day 2
day = 2

if __name__ == '__main__':
    
    t1 = time.time()
    print("***  It's Advent of Code 2018, Day {0}!  ***\n".format(day))
    print('** First part:')

    data = open('day2.txt', 'r')
    
    dic = {2: 0, 3:0}
    for line in data:
        temp_dic = {}
        for char in line:
            temp_dic[char] = line.count(char)
        temp_dic = list(set(temp_dic.values()))
        for i in temp_dic:
            if i > 1:
                dic[i] += 1

    res = 1
    for cnt in dic.values():
        res *= cnt

    print('Silver star answer: \n{0}'.format(res))
    
    print('** Second part:')
    
    data = open('day2.txt', 'r')

    string = []
    for line in data:
        string += [line]
    for line in string:
        for line2 in string:
            cnt = 0
            if line != line2:
                for i in range(len(line)):
                    if line2[i] != line[i]:
                        cnt += 1
            if cnt == 1:
                print(line, line2)
                res = ''
                for i in range(len(line)):
                    if line2[i] == line[i]:
                        res += line[i]
                break

    print('Golden star answer: \n{0}'.format(res))
    t2 = time.time()
    print('Program run for  {0} sec.'.format(round(t2-t1,2)))