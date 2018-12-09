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

## Advent of Code 2018, Day 9
day = 9

if __name__ == '__main__':
    
    t1 = time.time()
    print("***  It's Advent of Code 2018, Day {0}!  ***\n".format(day))
    print('** First part:')
    
    #with open('day{0}.txt'.format(day), 'r') as f:
    #    data = [line.strip() for line in f.readlines()]
    
    playersNo = 468
    last_marble = 71010
    
    if True: # Test
        playersNo = 9
        last_marble = 25
    
    scores = defaultdict(int)
    
    marble = 1
    circle = [0]
    player = 1
    current_marble_pos = 0
    while marble <= last_marble:
        #print(player, marble)
        if marble % 23 == 0:
            current_marble_pos -= 7
            if current_marble_pos < 0:
                current_marble_pos = len(circle) + current_marble_pos
            scores[player] += marble + circle[current_marble_pos]
            #print('score', marble, player, circle[current_marble_pos])
            circle = circle[:current_marble_pos] + circle[current_marble_pos + 1:]

        else:    
            if current_marble_pos + 1 < len(circle):
                current_marble_pos += 2
            else:
                current_marble_pos = 1
            circle = circle[:current_marble_pos] + [marble] + circle[current_marble_pos:]

        marble += 1
        player += 1
        if player % (playersNo + 1) == 0:
            player = 1
      
    max_score = max(scores.items(), key=operator.itemgetter(1))[1]

    print('Silver star answer: \n{0}'.format(max_score))
    
    print('** Second part:')
    
    playersNo = 468
    last_marble = 71010 * 100
    
    if False: # Test
        playersNo = 13
        last_marble = 7999
    
    scores = defaultdict(int)
    
    marble = 2
    player = 2
    current_marble = 1
    circle = defaultdict(int)
    circle[0] = [1, 1]
    circle[1] = [0, 0]
    
    
    while marble <= last_marble:
        if marble % 23 == 0:
            current_marble = circle[circle[circle[circle[circle[circle[circle[current_marble][0]][0]][0]][0]][0]][0]][0]
            #print('score', current_marble)
            
            scores[player] += marble + current_marble 
            to_remove = current_marble

            current_marble = circle[current_marble][1]
            circle[current_marble][0] = circle[to_remove][0] # update left neighbour 
            circle[circle[to_remove][0]][1] = circle[to_remove][1] # update right neighbour
            circle[to_remove] = [-1, -1] 
            
        else:    
            circle[marble] = [circle[current_marble][1], circle[circle[current_marble][1]][1]] # new insert
            
            current_marble = marble
            circle[circle[current_marble][0]][1] = current_marble # update left neighbour 
            circle[circle[current_marble][1]][0] = current_marble # update right neighbour
            
        marble += 1
        player += 1
        if player % (playersNo + 1) == 0:
            player = 1
      
    max_score = max(scores.items(), key=operator.itemgetter(1))[1]
   
    
    print('Golden star answer: \n{0}'.format(max_score))
    t2 = time.time()
    print('Program run for  {0} sec.'.format(round(t2-t1,2)))

