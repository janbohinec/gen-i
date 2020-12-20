0# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 20:42:22 2018

@author: Jan B.
"""

import numpy as np
import pandas as pd
import time
import datetime as dt
import matplotlib.pyplot as plt
import re
import copy
import string
import math
import itertools

## Advent of Code 2020
day = 19
year = 2020

def day_str(day):
    """ Return string from integer day. """
    return str(day) if day >= 10 else '0' + str(day)
    

if __name__ == '__main__':
    
    t1 = time.time()
    print("***  It's Advent of Code {1}, Day {0}!  ***\n".format(day, year))
    #### 1st Task
    print('** First part:')
    
    
    with open('day{0}.txt'.format(day_str(day)), 'r') as f:
        #data = f.read().split('\n\n')
        data = [line.strip() for line in f.readlines()]
        
    # Parsing
    msgs = []
    rules = {}
    for line in data:
        row = line
        if row == '':
            continue
        elif 'a' in row and 'b' in row:
            msgs += [row]
        else:
            rule, instructions = row.split(': ')
            instructions = instructions.replace('"', '') 
            instructions = instructions.split(' | ') 
            rules[rule] = instructions
            
    
    def part_1(rules):
        completed = False
        while not completed: 
            for rule in rules.keys():
                instructions = rules[rule]
                new = []
        
                for instruction in instructions: 
                    instruction = instruction.strip().replace('a a', 'aa').replace('a b', 'ab').replace('b a', 'ba').replace('b b', 'bb')
                    combinations = instruction.replace('      ', '     ').replace('     ', '    ').replace('    ', '   ').replace('   ', '  ').replace('  ', ' ').split(' ')
                    
                    list_ = []
                    for comb in combinations:
                        if comb[0] != 'a' and comb[0] != 'b':
                            temp = []
                            for rule2 in rules[comb]:
                                temp += [rule2+' ']
                            list_ += [temp]
                        else:
                            list_ += [[comb+' ']]
                            
                    res = list(itertools.product(*list_))
                    new += [''.join(i) for i in res] 
                            
                rules[rule] = new
                
                
            
            completed = True
            for inst in rules['0']:
                numbers = re.findall(r'\d+', inst) # numbers = ['2', '3']
                if len(numbers) > 0:
                    completed = False
                    break
                
            if completed:
                print('good game')
            else:
                print('keep trying')
    
    
        final = []
        for rule in rules['0']:
            final += [rule.replace(' ', '')]
        
        cnt = 0
        for msg in msgs:
            if msg in final:
                cnt += 1
                
        print(cnt)
        return rules
        
    #part_1(copy.deepcopy(rules))
            
    #### 2nd Task
    print('** Second part:')
    
        
    rules = part_1(copy.deepcopy(rules))

    final = {}
    final42 = []
    for rule in rules['42']:
        final42 += [rule.replace(' ', '')]
    final['42'] = final42
    
    final31 = []
    for rule in rules['31']:
        final31 += [rule.replace(' ', '')]    
    final['31'] = final31
    
        
    def descending(a):
        return all(a[i] >= a[i+1] for i in range(len(a)-1))
        
    cnt = 0
    for msg in msgs:
        n = len(msg) // 8
        sequence = []
        for i in range(n):
            if msg[i * 8 : (i + 1) * 8] in final['42']:
                sequence += [42]
            elif msg[i * 8 : (i + 1) * 8] in final['31']:
                sequence += [31]
        if descending(sequence) and sequence.count(42) > sequence.count(31) and sequence.count(31) > 0:
                cnt += 1
            
    print(cnt)


    t2 = time.time()
    print('Program run for  {0} sec.'.format(round(t2 - t1, 2)))

