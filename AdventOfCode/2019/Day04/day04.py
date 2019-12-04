
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 20:42:22 2018

@author: Jan
"""

import numpy as np
import pandas as pd
import time
import datetime as dt

## Advent of Code 2019
day = 4
year = 2019

def day_str(day):
    """ Return string from integer day. """
    return str(day) if day >= 10 else '0' + str(day)
    
if __name__ == '__main__':
    
    t1 = time.time()
    print("***  It's Advent of Code {1}, Day {0}!  ***\n".format(day, year))
    #### 1st Task
    print('** First part:')
    

    fr = 235741
    to = 706948
    cnt = 0

    for i in range(fr, to):
        str_pass = str(i)
        int_pass = [int(str_pass[i]) for i in range(len(str_pass))]
        if all(i <= j for i, j in zip(int_pass, int_pass[1:])):
            count_int = [str_pass.count(str(i)) for i in range(10)]
            if count_int.count(2) >= 1 or count_int.count(3) >= 1 or count_int.count(4) >= 1 or count_int.count(5) >= 1 or count_int.count(6) >= 1:
                cnt += 1
    print(cnt)
    
    
    #### 2nd Task
    print('** Second part:')

    cnt = 0
    for i in range(fr, to):
        str_pass = str(i)
        int_pass = [int(str_pass[i]) for i in range(len(str_pass))]
        if all(i <= j for i, j in zip(int_pass, int_pass[1:])):
            count_int = [str_pass.count(str(i)) for i in range(10)]
            if count_int.count(2) >= 1:
                cnt += 1
    print(cnt)
    
    t2 = time.time()
    print('Program run for  {0} sec.'.format(round(t2 - t1, 2)))