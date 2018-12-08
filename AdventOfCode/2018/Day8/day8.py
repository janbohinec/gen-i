# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 20:42:22 2018

@author: Jan
"""


import numpy as np
import pandas as pd
import time
import datetime as dt

## Advent of Code 2018, Day 8
day = 8



if __name__ == '__main__':
    
    t1 = time.time()
    print("***  It's Advent of Code 2018, Day {0}!  ***\n".format(day))
    print('** First part:')
    
    with open('day{0}.txt'.format(day), 'r') as f:
        data = [line.strip() for line in f.readlines()]
    
    data = list((int(x) for x in data[0].split(' ')))
    
    def recursive_count(sequence):
        pos = 0
        no_childs = sequence[pos]
        no_metas = sequence[pos + 1]
        metadata = 0
        pos += 2
        
        for child in range(no_childs): # sprehod po otrocih
            counts, meta = recursive_count(sequence[pos:])    
            pos += counts
            metadata += meta
            
        metadata += sum(sequence[pos:pos + no_metas])
        return pos + no_metas, metadata
            
    
    pos = 0
    metadata = 0
    while pos < len(data):
        counts, meta = recursive_count(data[pos:])
        pos += counts
        metadata += meta
            
    res = metadata
    

    print('Silver star answer: \n{0}'.format(res))
    
    print('** Second part:')
    
    
    def recursive_value(sequence):
        pos = 0
        no_childs = sequence[pos]
        no_metas = sequence[pos + 1]
        total = 0
        pos += 2
        
        metadata = []
        for child in range(no_childs): # sprehod po otrocih
            counts, value = recursive_value(sequence[pos:])    
            pos += counts
            metadata.append(value)
        print(metadata)
                
        if no_childs > 0:
            for j in sequence[pos:pos + no_metas]:
                #print(j, metadata)
                if j == 0:
                    continue
                try:
                    total += metadata[j-1]
                except:
                    pass
        else:
            total += sum(sequence[pos:pos + no_metas])
            

        return pos + no_metas, total
            
    pos = 0
    total = 0
    while pos < len(data):
        counts, value = recursive_value(data[pos:])
        pos += counts
        total += value
            
    res = total
    
    print('Golden star answer: \n{0}'.format(res))
    t2 = time.time()
    print('Program run for  {0} sec.'.format(round(t2-t1,2)))

