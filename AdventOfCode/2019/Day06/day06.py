
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
day = 6
year = 2019

def day_str(day):
    """ Return string from integer day. """
    return str(day) if day >= 10 else '0' + str(day)
    
if __name__ == '__main__':
    
    t1 = time.time()
    print("***  It's Advent of Code {1}, Day {0}!  ***\n".format(day, year))
    #### 1st Task
    print('** First part:')
    
    with open('day{0}.txt'.format(day_str(day)), 'r') as f:
        data = [line.strip().split(')') for line in f.readlines()]
    
    maps = {}
    for orbit in data:
        a = orbit[0]
        b = orbit[1]
        if b in maps.keys():
            maps[b] += [a]
        else:
            maps[b] = [a]
            

    def circles1(planet, cnt):
        if planet in maps.keys():
            todo = maps[planet]
            for planetb in todo:         
                cnt += circles1(planetb, cnt)
        else:
            return 0
        cnt += 1
        return cnt

    cnt = 0
    for planet in maps.keys():            
        cnt += circles1(planet, 0)

    print(cnt)
    
    #### 2nd Task
    print('** Second part:')

    def circles2(planet, cnt, stop):
        if planet in maps.keys():
            todo = maps[planet]
            for planetb in todo:
                #cnt += 1
                if planetb in stop:
                    stop += [planetb] 
                    return cnt, stop
                stop += [planetb]            
                temp = circles2(planetb, cnt, stop)
                cnt += temp[0]   
        else:
            return 0, []
        cnt += 1
        return cnt, stop
    
    
    cnt = 0
    cntsan = 0
    for planet in maps.keys():
        if planet == 'YOU':
            a = circles2(planet, 0, stop = [])
            cnt +=  a[0]
            lenme = len(a[1])
        if planet == 'SAN':
            b = circles2(planet, 0, stop = a[1])            
            cntsan += b[0]
            lensnt = len(b[1])
            
    for planet in maps.keys():            
        if planet == 'YOU':
            c = circles2(planet, 0, stop = b[1][lenme:])
            cnt += c[0]  
            lenme = len(c[1])
    
    print(cnt, cntsan, lenme-2)


    t2 = time.time()
    print('Program run for  {0} sec.'.format(round(t2 - t1, 2)))