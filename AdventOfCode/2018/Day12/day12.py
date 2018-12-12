# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 20:42:22 2018

@author: Jan
"""

import numpy as np
import pandas as pd
import time
import datetime as dt


## Advent of Code 2018, Day 12
day = 12

if __name__ == '__main__':
    
    t1 = time.time()
    print("***  It's Advent of Code 2018, Day {0}!  ***\n".format(day))
    print('** First part:')
    
    inState = '###.......##....#.#.#..###.##..##.....#....#.#.....##.###...###.#...###.###.#.###...#.####.##.#....#'
    #inState = '#..#.#..##......###...###'
    state = '..' + inState + '.......'
    #rule = 'LLCRR => N'
    
    with open('day{0}.txt'.format(day), 'r') as f:
        data = [line.strip() for line in f.readlines()]
    
    if True: # prvi del
        for generation in range(20): # generations
            newState = '..'
            for i in range(2,len(state)-2): # string
                #print(generation, i)
                for idx, mutation in enumerate(data):
                    if state[i-2:i+3] == mutation[0:5]:
                        newState += mutation[-1]
                        #print(generation, idx, i,  state[i-2:i+3], mutation)
                        found = True
                        break
                if not found:
                    newState += state[i]
            #print(generation, state, len(state))        
            #print(generation, newState+'..')
            state = newState + '...'
        
        print(20, state)
    
        cnt = 0
        for k in range(len(state)):
            if state[k] == '#':
                #print(k)
                cnt += k - 2
        
        print(cnt)
        res = 0

    print('Silver star answer: \n{0}'.format(res))
    
    print('** Second part:')
    
    generationsMax = 50000000000
    
    inState = '###.......##....#.#.#..###.##..##.....#....#.#.....##.###...###.#...###.###.#.###...#.####.##.#....#'
    #inState = '#..#.#..##......###...###'
    state = '..' + inState + '.....'
    #rule = 'LLCRR => N'
    
    def countPlants(state, generation):
        cnt = 0
        for k in range(len(state)):
            if state[k] == '#':
                cnt += k - 2 + generation - 41
        return cnt
    
    with open('day{0}.txt'.format(day), 'r') as f:
        data = [line.strip() for line in f.readlines()]
    
    gens = 150
    oldS = []
    for generation in range(gens): # generations
        newState = '..'
        for i in range(2,len(state)-2): # string
            #print(generation, i)
            for idx, mutation in enumerate(data):
                if state[i-2:i+3] == mutation[0:5]:
                    newState += mutation[-1]
                    #print(generation, idx, i,  state[i-2:i+3], mutation)
                    found = True
                    break
            if not found:
                newState += state[i]
        #print(generation, state, len(state))        
        #print(generation, newState+'..')
        state = newState + '...'
        if generation > 40:
            state = state[1:]
        #print(generation+1, countPlants(state, generation+1))
    
    #print(gens+1, countPlants(state, gens+1))
    print(generationsMax, countPlants(state, generationsMax))
   
    
    print('Golden star answer: \n{0}'.format(res))
    t2 = time.time()
    print('Program run for  {0} sec.'.format(round(t2-t1,2)))

