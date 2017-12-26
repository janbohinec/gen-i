# -*- coding: utf-8 -*-
"""
Created on Tue Dec 26 10:04:49 2017

@author: janb
"""


import numpy as np
import pandas as pd
import time
import string

## Advent of Code 2017, Day 20
day = 20

data = open('day20.txt', 'r')
#data = data.read().split(',')

def distance(position):
    """ Manhattan distance of the position """
    return sum(abs(i) for i in position)

def find_closest(particles):
    """ """
    max_dist = float('inf')
    part = 0
    for particle in particles:
        dist = distance(particles[particle]['p'])
        if dist < max_dist:
            max_dist = dist
            part = particle
    print('Max distance: {0} at particle {1}.'.format(max_dist, part))
    return part
            

def particle_swarm(data):
    particles = {}
    part = 0
    for line in data:
        first = line.find('>')
        p = list(map(int, line[line.find('<')+1:first].split(',')))
        line = line[first + 1:]
        second = line.find('>')
        v = list(map(int, line[line.find('<')+1:second].split(',')))
        line = line[second + 1:]
        third = line.find('>')
        a = list(map(int, line[line.find('<')+1:third].split(',')))
        
        particles[part] = {'p': 0, 'v': 0, 'a': 0}
        particles[part]['p'] = p
        particles[part]['v'] = v
        particles[part]['a'] = a
        part += 1
    return particles



def swarm(particles):
    """ Make particles swarm: """
    i = 0
    
    while i < 2000:
        list_to_delete = []#[k for k,v in start.items() if np.array_equal(start[k]['p'], start[0]['p']) and k != 0]
        for p in particles:
            list_to_delete += [k for k,v in particles.items() if np.array_equal(particles[k]['p'], particles[p]['p']) and k != p]
        for e in list_to_delete:
            print(list_to_delete)
            try:
                del particles[e]
            except:
                pass
                    
        for p in particles:
            particles[p]['v'] = np.add(particles[p]['v'], particles[p]['a'])
            particles[p]['p'] = np.add(particles[p]['p'], particles[p]['v'])
        print(len(particles))
        if len(particles) < 2:
            break
        #find_closest(particles) # 1st part
        i += 1    
    return len(particles)

t1 = time.time()
print("***  It's Advent of Code 2017, Day {}!  ***\n".format(day))
print('First part:')
start = particle_swarm(data)
find_closest(start)
#print(swarm(start))

print('Second part:')
test = {0: {'p': [-6,0,0], 'v': [3,0,0], 'a': [0,0,0]},
        1: {'p': [-4,0,0], 'v': [2,0,0], 'a': [0,0,0]},
        2: {'p': [-2,0,0], 'v': [1,0,0], 'a': [0,0,0]},
        3: {'p': [3,0,0], 'v': [-1,0,0], 'a': [0,0,0]}}

print(swarm(test))
print(swarm(start))

t2 = time.time()
print('\nProgram run for  {0} sec.'.format(round(t2-t1,2)))

