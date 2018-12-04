# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 20:42:22 2018

@author: Jan
"""


import numpy as np
import pandas as pd
import time
import datetime as dt
from collections import defaultdict
import operator

## Advent of Code 2018, Day 4
day = 4

def part1(data):
    guard_id = 0
    guards = defaultdict(int)
    max_sleep = defaultdict(lambda: defaultdict(int))
    for line in sorted(data):
        
        elements = line.split(' ')
        print(elements)
        if elements[3].startswith('#'):
            guard_id = int(elements[3][1:])
            wake_up = int(line.split(':')[-1][:2])
        if 'wakes up' in line:
            wake_up = int(line.split(':')[-1][:2])
            duration = wake_up - sleep
            guards[guard_id] += duration
            for i in range(sleep, wake_up):
                max_sleep[guard_id][i] += 1
        if 'falls asleep' in line:
            sleep = int(line.split(':')[-1][:2])
    print(max_sleep)
    print(guards)
    chosen_id = max(guards.items(), key=operator.itemgetter(1))[0]
    return chosen_id*(max(max_sleep[chosen_id].items(), key=operator.itemgetter(1))[0])


def part2(data):
    cur_id = 0
    guards = defaultdict(int)
    max_sleep = defaultdict(lambda: defaultdict(int))
    for line in sorted(data):
        elements = line.split(' ')
        if elements[3].startswith('#'):
            cur_id = int(elements[3][1:])
            wake_up = int(line.split(':')[-1][:2])
        if "wakes up" in line:
            wake_up = int(line.split(':')[-1][:2])
            duration = wake_up - sleep
            guards[cur_id] += duration
            for i in range(sleep, wake_up):
                max_sleep[cur_id][i] += 1
        if "falls asleep" in line:
            sleep = int(line.split(':')[-1][:2])
    total_max = 0
    for cur_id, el in max_sleep.items():
        new_max = max(el.items(), key=operator.itemgetter(1))[1]
        if new_max > total_max:
            chosen_id = cur_id
            total_max = new_max
    return chosen_id*max(max_sleep[chosen_id].items(), key=operator.itemgetter(1))[0]

if __name__ == '__main__':
    
    t1 = time.time()
    print("***  It's Advent of Code 2018, Day {0}!  ***\n".format(day))
    print('** First part:')
    
    #with open('day4.txt', 'r') as f:
    #    data = [line.strip() for line in f.readlines()]
        
    data = open('day4.txt', 'r')
    data = data.readlines()        

    guard_id = 0
    guards = defaultdict(int)
    max_sleep = defaultdict(lambda: defaultdict(int))
    for line in sorted(data):
        
        elements = line.split(' ')
        #print(elements)
        if elements[3].startswith('#'):
            guard_id = int(elements[3][1:])
            wake_up = int(line.split(':')[-1][:2])
        if 'wakes up' in line:
            wake_up = int(line.split(':')[-1][:2])
            duration = wake_up - sleep
            guards[guard_id] += duration
            for i in range(sleep, wake_up):
                max_sleep[guard_id][i] += 1
        if 'falls asleep' in line:
            sleep = int(line.split(':')[-1][:2])
    #print(max_sleep)
    #print(guards)
    
    chosen_id = max(guards.items(), key=operator.itemgetter(1))[0]
    res =  chosen_id * (max(max_sleep[chosen_id].items(), key=operator.itemgetter(1))[0])

    

    print('Silver star answer: \n{0}'.format(res))
    
    print('** Second part:')
    
    guard_id = 0
    guards = defaultdict(int)
    max_sleep = defaultdict(lambda: defaultdict(int))
    for line in sorted(data):
        
        elements = line.split(' ')
        #print(elements)
        if elements[3].startswith('#'):
            guard_id = int(elements[3][1:])
            wake_up = int(line.split(':')[-1][:2])
        if 'wakes up' in line:
            wake_up = int(line.split(':')[-1][:2])
            duration = wake_up - sleep
            guards[guard_id] += duration
            for i in range(sleep, wake_up):
                max_sleep[guard_id][i] += 1
        if 'falls asleep' in line:
            sleep = int(line.split(':')[-1][:2])
    
    total_max = 0
    for cur_id, el in max_sleep.items():
        new_max = max(el.items(), key=operator.itemgetter(1))[1]
        if new_max > total_max:
            chosen_id = cur_id
            total_max = new_max
    res =  chosen_id * max(max_sleep[chosen_id].items(), key=operator.itemgetter(1))[0]
    
    print('Golden star answer: \n{0}'.format(res))
    t2 = time.time()
    print('Program run for  {0} sec.'.format(round(t2-t1,2)))

