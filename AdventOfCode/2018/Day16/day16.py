# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 20:42:22 2018

@author: Jan
"""

import numpy as np
import pandas as pd
import time
import datetime as dt


## Advent of Code 2018, Day 16
day = 16


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


opcodes = [addr, addi, mulr, muli, banr, bani, borr, bori,
           setr, seti, gtir, gtri, gtrr, eqir, eqri, eqrr,
          ]

def check_and_count_opcode_results(inReg, A, B, C, outReg):
    """ """
    st = 0
    for opcode in opcodes:
        inRegCopy = inReg.copy()
        if opcode(inRegCopy, A, B, C) == outReg:
            st += 1
    return st

# remove_candidates discards functions that do not match the observed behavior
def delete_candidates(inReg, A, B, C, outReg, code, candidates):
    for opcode in opcodes:
        inRegCopy = inReg.copy()
        if opcode(inRegCopy, A, B, C) != outReg:
            candidates[code].discard(opcode)
    return candidates


if __name__ == '__main__':
    
    t1 = time.time()
    print("***  It's Advent of Code 2018, Day {0}!  ***\n".format(day))
    print('** First part:')
    
    print(check_and_count_opcode_results([3,2,1,1], 2, 1, 2, [3,2,2,1]))
   
    with open('day{0}.txt'.format(day), 'r') as f:
        data = [line.strip() for line in f.readlines()]
    
    i = 0
    cnt = 0
    while i < len(data):         
        inReg = list(map(int, data[i][9:19].split(',')))
        code, A, B, C = list(map(int, data[i + 1].split()))
        outReg = list(map(int, data[i+2][9:19].split(',')))
        #print(i, inReg, code, A, B, C, outReg, )
        
        if check_and_count_opcode_results(inReg, A, B, C, outReg) >= 3:
            cnt += 1
        i += 4
    

    print('Silver star answer: \n{0}'.format(cnt))
    
    print('** Second part:')
    
    
    # find code to opcodes
    opcodes_dict = {}
    found = []
    
    while len(found) < len(opcodes):
        
        candidates = {}        
        for k in range(len(opcodes)):
            candidates[k] = set(opcodes) - set(found)
    
        i = 0
        while i < len(data):
            inReg = list(map(int, data[i][9:19].split(',')))
            code, A, B, C = list(map(int, data[i + 1].split()))
            outReg = list(map(int, data[i+2][9:19].split(',')))
            
            candidates = delete_candidates(inReg, A, B, C, outReg, code, candidates)
            #print(inReg, len(candidates[code]), candidates[code])
            i += 4
        
        for k in range(len(opcodes)):
            if len(candidates[k]) == 1:
                opcode = candidates[k].pop()
                opcodes_dict[k] = opcode
                found += [opcode]
        
    # execute part 2
    r = [0,0,0,0]
    
    with open('day{0}part2.txt'.format(day), 'r') as f:
        data = [line.strip() for line in f.readlines()]
    
    for line in data:
        code, A, B, C = list(map(int, line.split()))
        opcode = opcodes_dict[code]
        opcode(r, A, B, C)
    
    
    print('Golden star answer: \n{0}'.format(r))
    t2 = time.time()
    print('Program run for  {0} sec.'.format(round(t2-t1,2)))

