# -*- coding: utf-8 -*-
"""
Created on Fri Dec 23 17:51:22 2017

@author: Jan
"""


import numpy as np
import pandas as pd
from itertools import count
import time

## Advent of Code 2017, Day 8

data = open('day8.txt', 'r')

def modifyRegister(register, direction, value):
    if direction == 'inc':
        register += value
    elif direction == 'dec':
        register -= value
    else:
        print('Error')
    return register

def registerMod(register, direction, value, testRegister, conditionDirection, condition):
    """ Modify register by value if it fits condition. """
    if conditionDirection == '>':
        if testRegister > condition:
            register = modifyRegister(register, direction, value)
    elif conditionDirection == '<':
        if testRegister < condition:
            register = modifyRegister(register, direction, value)
    elif conditionDirection == '>=':
        if testRegister >= condition:
            register = modifyRegister(register, direction, value)
    elif conditionDirection == '==':
        if testRegister == condition:
            register = modifyRegister(register, direction, value)
    elif conditionDirection == '<=':
        if testRegister <= condition:
            register = modifyRegister(register, direction, value)
    elif conditionDirection == '!=':
        if testRegister != condition:
            register = modifyRegister(register, direction, value)
    else:
        print('Error Condition Direction')
    return register
    

def goThrough(file):
    reg = {}
    highest = 0
    for line in file:
        register, direction, value, _, testRegister, conditionDirection, condition = line.split(' ')
        if not register in reg:
            reg[register] = 0
        if not testRegister in reg:
            reg[testRegister] = 0
        reg[register] = registerMod(reg[register], direction, int(value), reg[testRegister], conditionDirection, int(condition))
        if highest < reg[register]:
            highest = reg[register]
    print(highest)
    return reg


t1 = time.time()
print('Test')
res = goThrough(data)

print('2nd part test')
print()
print('2nd part anwswer')

t2 = time.time()
print('Program run for  {0} sec.'.format(round(t2-t1,2)))

