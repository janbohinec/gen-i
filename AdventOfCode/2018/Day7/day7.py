# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 20:42:22 2018

@author: Jan
"""


import numpy as np
import pandas as pd
import time
import datetime as dt

## Advent of Code 2018, Day 7
day = 7

def find_shortest_path(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    if not graph.has_key(start):
        return None
    shortest = None
    for node in graph[start]:
        if node not in path:
            newpath = find_shortest_path(graph, node, end, path)
            if newpath:
                if not shortest or len(newpath) < len(shortest):
                    shortest = newpath
    return shortest
    
def find_path(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    if not graph.has_key(start):
        return None
    for node in graph[start]:
        if node not in path:
            newpath = find_path(graph, node, end, path)
            if newpath: return newpath
    return None

def next_task():
    possible = []
    for key in steps.keys():
        if len(steps[key]) == 0:
            possible.append(key)
    for worker in workers:
        if worker[0] in possible:
            possible.remove(worker[0]) # We're working on it
    if len(possible) == 0:
        return None
    return min(possible)


if __name__ == '__main__':
    
    t1 = time.time()
    print("***  It's Advent of Code 2018, Day {0}!  ***\n".format(day))
    print('** First part:')
    
    with open('day{0}.txt'.format(day), 'r') as f:
        data = [line.strip() for line in f.readlines()]
    
    steps = {}
    for line in data:
        parsed_line = line.split(' ')
        key = parsed_line[1]
        value = parsed_line[-3]
        if key in steps.keys():
            steps[key] += [value]
        else:
            steps[key] = [value]
   
    possibles = []
    for key, value in steps.items():
        found = False
        for key2, value2 in steps.items():
            if key != key2 and key in value2:
                found = True
        if not found:
            possibles += [key]
            print(key)

    
    path = ''
    possibles = list(np.sort(list(set(possibles))))
    print(possibles)
    path += possibles[0]
    j = 0
    while j < 30:
        j += 1
        if path[-1] in steps.keys():
            possibles += steps[path[-1]]
        
        possibles = list(np.sort(list(set(possibles))))
        
        for i in range(len(possibles)):
            if possibles[i] not in path:
                candidate = True
                for key, values in steps.items():
                    if possibles[i] in values:
                        if key not in path:
                            candidate = False
                            break
                if candidate:
                    path += possibles[i]
                    possibles = possibles[i+1:]
                    break
    print(path)    
    
    print('Silver star answer: \n{0}'.format(path))
    
    print('** Second part:')
    import string
    
    steps = {x: [] for x in string.ascii_uppercase} # only works if all chars in alphabeth are in the task lists

    with open('day{0}.txt'.format(day), 'r') as f:
        data = f.readlines()
            
    for line in data:
        elements = line.split(' ')
        steps[elements[-3]].append(elements[1])
    
    path = ''
    time_spent = -1 # first step is at 0
    workers = [['', 0] for k in range(5)] # [Task, time_when_finish]
    
    while len(steps.keys()) != 0:
        #print(workers)

        time_spent += 1
        if all([(worker[1] > time_spent) for worker in workers]):  # everyone working
            continue

        for worker in workers:
            if worker[0] != '' and worker[1] <= time_spent:
                key = worker[0]
                worker[0] = ''
                worker[1] = 0
                
                
                for task_key in steps.keys(): # removing tasks
                    if key in steps[task_key]:
                        steps[task_key].remove(key)

                if len(steps[key]) == 0 and key in path: # delete task in steps
                    steps.pop(key, None)
                    continue
        
        for worker in workers:
            if worker[1] <= time_spent:
                next_element = next_task()
                if next_element is None or next_element in path:
                    continue
                path += next_element
                worker[0] = next_element
                worker[1] = time_spent + 60 + 1 + string.ascii_uppercase.index(next_element)

    print(path)
    print('Golden star answer: \n{0}'.format(time_spent))
    t2 = time.time()
    print('Program run for  {0} sec.'.format(round(t2-t1,2)))

