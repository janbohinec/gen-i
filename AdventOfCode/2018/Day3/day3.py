# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 20:42:22 2018

@author: Jan
"""


import numpy as np
import pandas as pd
import time
import datetime as dt

## Advent of Code 2018, Day 3
day = 3


if __name__ == '__main__':
    
    t1 = time.time()
    print("***  It's Advent of Code 2018, Day {}!  ***\n".format(day))
    print('** First part:')

    data = open('day3.txt', 'r')
    res = 0
   

    #string = data.readline()
    #data = pd.read_excel('day2.xlsx', header=None)  
    #for idx, row in data.iterrows():    
        #pass
        #print(row.loc[1], max(row), min(row))
    
    print('Silver star answer: \n{0}'.format(res))
    
    print('** Second part:')
    
  

    
    print('Golden star answer: \n{0}'.format(res))
    t2 = time.time()
    print('Program run for  {0} sec.'.format(round(t2-t1,2)))

