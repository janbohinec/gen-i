# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 20:42:22 2018

@author: Jan
"""

import numpy as np
import pandas as pd
import time
import datetime as dt


## Advent of Code 2018, Day 13
day = 13

if __name__ == '__main__':
    
    t1 = time.time()
    print("***  It's Advent of Code 2018, Day {0}!  ***\n".format(day))
    print('** First part:')
    
    state = [0, 1, 2] #['L', 'S', 'R']
    
    states = {0: 'L',
              1: 'S',
              2: 'R'}
    
    cart_pos = {'>': {'L': '^', 'S': '>', 'R': 'v'},
                '^': {'L': '<', 'S': '^', 'R': '>'},
                '<': {'L': 'v', 'S': '<', 'R': '^'},
                'v': {'L': '>', 'S': 'v', 'R': '<'}}
    
    directions = {'>': [0, 1],
                  '^': [-1, 0],
                  '<': [0, -1],
                  'v': [1, 0]}
    carts = {} # 1: [x, y, s, direction, crashed]} # [x,y, state, crashed]
    cart_no = 1
    rr = []

    with open('day{0}.txt'.format(day), 'r') as f:
        #data = [line.strip() for line in f.readlines()]
        rr += [line.replace('\\', '\\').replace('\n', '') for line in f.readlines()]
    
    def find(s, ch):
        return [i for i, ltr in enumerate(s) if ltr == ch]
    
    for i in range(len(rr)):
        for y_k in find(rr[i], '>'):
            print('Found cart ', cart_no)
            carts[cart_no] = [i, y_k, 0, '>', 0]
            rr[i].replace('>', '-')
            cart_no += 1            
        for y_k in find(rr[i], '<'):
            print('Found cart ', cart_no, y_k, i)
            carts[cart_no] = [i, y_k, 0, '<', 0]
            rr[i].replace('<', '-')
            cart_no += 1   
        for y_k in find(rr[i], 'v'):
            print('Found cart ', cart_no)
            carts[cart_no] = [i, y_k, 0, 'v', 0]
            rr[i].replace('v', '|')
            cart_no += 1 
        for y_k in find(rr[i], '^'):
            print('Found cart ', cart_no, y_k, i)
            carts[cart_no] = [i, y_k, 0, '^', 0]
            rr[i].replace('^', '|')
            cart_no += 1
 
    print('Carts', cart_no-1)
    
    step = 0
    while True:
        #print(step)
        for cart in list(carts.keys()):
            #print(carts[cart])
            try:
                x, y, s, direction, crashed = carts[cart]
                x,y = np.array([x, y]) + directions[direction]
                if rr[x][y] == '\\':
                    if direction == '>':
                        direction = 'v'
                    elif direction == '^':
                        direction = '<'
                    elif direction == '<':
                        direction = '^'
                    elif direction == 'v':
                        direction = '>'                
                if rr[x][y] == '/':
                    if direction == '>':
                        direction = '^'
                    elif direction == '^':
                        direction = '>'
                    elif direction == '<':
                        direction = 'v'
                    elif direction == 'v':
                        direction = '<'
                if rr[x][y] == '+':
                    direction = cart_pos[direction][states[s]]
                    s += 1 
                    s = np.mod(s,3)
                carts[cart] = [x, y, s, direction, crashed]
                crash  = False
        
                carts_crashed = [0 for i in range(17)]        
                for cart1 in list(carts.keys()):
                    x1, y1, s, direction, crashed1 = carts[cart1]
                    for cart2 in list(carts.keys()):
                        x2, y2, s, direction, crashed2 = carts[cart2]
                        if cart1 != cart2:                    
                            if x1 == x2 and y1 == y2:
                                #crash = True
                                carts_crashed[cart1-1] = 1
                                carts_crashed[cart2-1] = 1
                                print('CRASH: ', y1, x1, step)
                                #print(carts)
                                carts[cart1] = [x,y, s, direction, 1]
                                carts[cart2] = [x,y, s, direction, 1]
        
                for cart in list(carts.keys()):
                    if carts_crashed[cart-1] == 1:
                        del carts[cart]
        
                notCrashed = 0
                for cart1 in list(carts.keys()):
                    x1, y1, s, direction, crashed1 = carts[cart1]
                    if crashed1 == 0:
                        notCrashed += 1
                finalCrash = False    
                if notCrashed == 1:
                    print('final crash')
                    #print(carts, step)
                    finalCrash = True
                    break
            except:
                pass
        if finalCrash:
            break
        if step > 13000 or crash:
            break
        step += 1
 

    print('Silver star answer: \n{0}'.format(carts))
    
    print('** Second part:')
    
    print('Golden star answer: \n{0}'.format(carts))
    t2 = time.time()
    print('Program run for  {0} sec.'.format(round(t2-t1,2)))

