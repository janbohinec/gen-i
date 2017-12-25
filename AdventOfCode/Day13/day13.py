# -*- coding: utf-8 -*-
"""
Created on Fri Dec 23 17:51:22 2017

@author: Jan
"""


import numpy as np
import pandas as pd
import time

## Advent of Code 2017, Day 13
day = 13

data = open('day13.txt', 'r')
config_test = {0:3, 1:2, 4:4, 6:4}

def firewall_config(data):
    """ Get village connections in a dictionary/graph. """
    connections = {}
    for pipe in data:
        ID_ = int(pipe[:pipe.find(':')])
        neighbors = int(pipe[pipe.find(':')+1:-1].replace(' ',''))
        connections[ID_] = neighbors
    return connections
   

def severity(config, time = 0):
    """ Gets severity of the firewall. """
    severe = 0
    for layer in range(max(config.keys())+1):
        if layer in config:
            pos_of_scanner = np.mod(layer + time, 2*config[layer] - 2)            
            if pos_of_scanner >= config[layer]:
                pos_of_scanner = 2 * (config[layer] - 1) - pos_of_scanner
            if pos_of_scanner == 0:
                severe += layer * config[layer]
                if layer == 0 and time > 0:
                    severe += 1
        if time > 0 and severe > 0:
            break
    return severe

def get_delay(config):
    """ Min delay to not get cought. """
    delay = 0
    while severity(config, delay) != 0:
        delay += 1
        if delay > 10000000:
            break
    return delay

t1 = time.time()
print("***  It's Advent of Code 2017, Day {}!  ***\n".format(day))
print('First part:')
fire = firewall_config(data)
#print(fire)
print(severity(config_test))
print(severity(fire))

print('Second part:')
print(get_delay(config_test))
print(get_delay(fire))

t2 = time.time()
print('Program run for  {0} sec.'.format(round(t2-t1,2)))

