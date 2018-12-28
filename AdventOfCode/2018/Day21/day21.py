# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 20:42:22 2018

@author: Jan
"""

import numpy as np
import pandas as pd
import time
import datetime as dt
import math
import operator
from collections import defaultdict


## Advent of Code 2018, Day 21
day = 21

## Aux Functions

# r - register
def addr(r, A, B, C): 
    r[C] = r[A] + r[B]
    return r

def addi(r, A, B, C): 
    #print(r, A, B, C)
    r[C] = r[A] + B
    return r

def mulr(r, A, B, C): 
    #print(r, A,B,C, r[A], r[B])
    r[C] = r[A] * r[B]
    return r

def muli(r, A, B, C): 
    r[C] = r[A] * B
    return r

def banr(r, A, B, C): 
    r[C] = r[A] & r[B]
    return r

def bani(r, A, B, C): 
    r[C] = r[A] & B
    return r

def borr(r, A, B, C): 
    r[C] = r[A] | r[B]
    return r

def bori(r, A, B, C): 
    r[C] = r[A] | B
    return r

def setr(r, A, B, C): 
    r[C] = r[A]
    return r

def seti(r, A, B, C): 
    r[C] = A
    return r

def gtir(r, A, B, C): 
    r[C] = int(A > r[B])
    return r

def gtri(r, A, B, C): 
    r[C] = int(r[A] > B)
    return r

def gtrr(r, A, B, C): 
    r[C] = int(r[A] > r[B])
    return r

def eqir(r, A, B, C): 
    r[C] = int(A == r[B])
    return r

def eqri(r, A, B, C): 
    r[C] = int(r[A] == B)
    return r

def eqrr(r, A, B, C): 
    r[C] = int(r[A] == r[B])
    return r


opcodes = {'addr': addr, 
           'addi': addi, 
           'mulr': mulr,
           'muli': muli, 
           'banr': banr,
           'bani': bani,
           'borr': borr, 
           'bori': bori,
           'setr': setr, 
           'seti': seti, 
           'gtir': gtir, 
           'gtri': gtri, 
           'gtrr': gtrr, 
           'eqir': eqir, 
           'eqri': eqri, 
           'eqrr': eqrr
          }

if __name__ == '__main__':
    
    t1 = time.time()
    print("***  It's Advent of Code 2018, Day {0}!  ***\n".format(day))
    print('** First part:')
    
      
    data = []
    with open('day{0}.txt'.format(day), 'r') as f:
        for line in f.readlines():
            row = line.strip().split()
            data += [[row[0]] + list(map(int, row[1:]))]
            
    ip_register = 3
    register = [0, 0, 0, 0, 0, 0]  
    res = 0
    def program(ip_register, register, max_iter = 15000, view = False):
        ip = 0
        st = 0
        while ip >= 0 and ip < len(data):
            register[ip_register] = ip
        
            opcode, A, B, C = data[ip]
            register = opcodes[opcode](register, A, B, C)
            
            ip = register[ip_register] + 1
            
            if view:
                print(st, ip, register, opcode, A, B, C, len(data))
            if opcode == 'eqrr':
                print('found eqrr', st, register)
                global res
                res = register[4]
                break
            
            st += 1
            if st > max_iter:
                print('forced stop', st, register)
                break
                
            
    program(ip_register, [0, 0, 0, 0, 0, 0])
    #program(ip_register, [11840402, 0,0,0,0,0], view = True)
    
    print('Silver star answer: \n{0}'.format(res))
    
    print('** Second part:')
    
    
    # Program in python
    r4 = 0 # start at 0
    pos = 1
    prev = defaultdict(int)
    
    while True:
        
        r5 = 65536 | r4
        r4 = 6152285
        
        for i in range(int(math.log(r5, 256)) + 1):
        #for i in range(r5):
            
            r2 = r5 & 255
            r4 += r2
            r4 *= 65899
            r4 = r4 & 16777215
            r5 = r5 // 256
            
        if r4 in prev:
            break
        else:
            prev[r4] = pos
        
        pos += 1   
    
    
    res = max(prev.items(), key=operator.itemgetter(1))[0]
    
    print('Golden star answer: \n{0}'.format(res))
    t2 = time.time()
    print('Program run for  {0} sec.'.format(round(t2-t1,2)))

