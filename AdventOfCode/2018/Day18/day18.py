# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 20:42:22 2018

@author: Jan
"""

import numpy as np
import time


## Advent of Code 2018, Day 18
day = 18

def neighbors(a, radius, rowNumber, columnNumber):
     return [[a[i][j] if i >= 0 and i < len(a) and j >= 0 and j < len(a[0]) else b'' 
              for j in range(columnNumber-radius, columnNumber+radius+1)] 
                for i in range(rowNumber-radius, rowNumber+radius+1)]

def counts(a, ele):
    cnt = 0
    for i in range(len(a)):
        try:
            cnt += a[i].count(ele).sum()
        except:
            cnt += a[i].count(ele)
    return cnt

def countNeighbours(i, j, ele):
    a = neighbors(charar, 1, i, j)
    return counts(a, ele)
    
if __name__ == '__main__':
    
    t1 = time.time()
    print("***  It's Advent of Code 2018, Day {0}!  ***\n".format(day))
    print('** First part:')
    
    n = 50
    charar = np.chararray((n, n))
    with open('day{0}.txt'.format(day), 'r') as f:
        i = 0
        for line in f.readlines():
            charar[i] = list(map(str, line.strip()))
            i += 1
    
    minute = 0
        
    print(counts(charar, b'.'), counts(charar, b'|'), counts(charar, b'#'))
    #print(charar)
    
    states = []
    while minute < 450:
        chararNew = charar.copy()
        for i in range(n):
            for j in range(n):
                if charar[i,j] == b'.' and countNeighbours(i,j, b'|') >= 3:
                    chararNew[i,j] = '|'
        
                if charar[i,j] == b'|' and countNeighbours(i,j, b'#') >= 3:
                    chararNew[i,j] = '#'
         
                if charar[i,j] == b'#' and countNeighbours(i,j, b'#')-1 >= 1 and countNeighbours(i,j, b'|') >= 1:
                    chararNew[i,j] = '#'
                elif charar[i,j] == b'#':
                    chararNew[i,j] = '.'      
        charar = chararNew
        
        for k in range(len(states)):
            if np.array_equal(charar, states[k]):
                print(k, minute, 'Found!!')
                print(minute, counts(charar, b'.'), counts(charar, b'|'), counts(charar, b'#'))
                break
        
        states += [charar]
        if minute == 9:
            print(minute, counts(charar, b'.'), counts(charar, b'|'), counts(charar, b'#'), counts(charar, b'|') * counts(charar, b'#'))
        #print(charar)
        minute += 1
    
    res = counts(charar, b'|') * counts(charar, b'#')
    
                
    maxMin = 1000000000
    a = (maxMin - 417) % 28 + 417 - 1
    
    
    res = counts(states[a], b'|') * counts(states[a], b'#')
                
    print('Silver star answer: \n{0}'.format(res))
    
    print('** Second part:')
    
        
    print('Golden star answer: \n{0}'.format(res))
    t2 = time.time()
    print('Program run for  {0} sec.'.format(round(t2-t1,2)))

