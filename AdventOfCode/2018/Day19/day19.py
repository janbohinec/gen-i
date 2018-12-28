# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 20:42:22 2018

@author: Jan
"""

import numpy as np
import pandas as pd
import time
import datetime as dt


## Advent of Code 2018, Day 19
day = 19

## Aux Functions

# r - register
def addr(r, A, B, C): 
    r[C] = r[A] + r[B]
    return r

def addi(r, A, B, C): 
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
    
    
    ip = 0
    
    while ip >= 0 and ip < len(data):
        register[ip_register] = ip
    
        opcode, A, B, C = data[ip]
        register = opcodes[opcode](register, A, B, C)
        
        ip = register[ip_register] + 1
        
        #print(ip, register, opcode, A, B, C, len(data))
           
    
    res = register[0]
    print('Silver star answer: \n{0}'.format(res))
    
    print('** Second part:')
    
    register2 = [1, 0, 0, 0, 0, 0]    
    
    ip = 0
    st = 0
    
    while ip >= 0 and ip < len(data):
        register2[ip_register] = ip
        
        opcode, A, B, C = data[ip]
        register2 = opcodes[opcode](register2, A, B, C)
        
        ip = register2[ip_register] + 1
        
        print(register2)
        
        st += 1
        if st > 20: # 20 is enough
            break
   
    n = register2[2] # int number that is being factorized
    total = 0 # computing when it stops
    for i in range(1, n + 1):
        if n % i == 0:
            total += i

        
    print('Golden star answer: \n{0}'.format(total))
    t2 = time.time()
    print('Program run for  {0} sec.'.format(round(t2-t1,2)))

