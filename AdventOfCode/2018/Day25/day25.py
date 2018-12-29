# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 20:42:22 2018

@author: Jan
"""

import numpy as np
import time
from scipy import spatial


## Advent of Code 2018, Day 25
day = 25


if __name__ == '__main__':
    
    t1 = time.time()
    print("***  It's Advent of Code 2018, Day {0}!  ***\n".format(day))
    print('** First part:')
    
    with open('day{0}.txt'.format(day), 'r') as f:
        points = [list(map(int, line.strip().split(','))) for line in f.readlines()]
        #points = [line.strip().split( for line in f.readlines()]
    
    def distance(p1, p2):
        dist = 0
        for i in range(len(p1)):
            dist += abs(p1[i] - p2[i])
        return dist
    
    groups = {}
    grp = 0                
            

    constelations = np.arange(0, len(points), 1)
    
    manh_distance = spatial.distance.pdist(points, metric='cityblock') # cityblock(u, v[, w]) 	Compute the City Block (Manhattan) distance. https://docs.scipy.org/doc/scipy/reference/spatial.distance.html
    matDistances = spatial.distance.squareform(manh_distance)
    
    
    candidates1, candidates2 = np.where((matDistances != 0) & (matDistances <= 3))
    join = np.stack((constelations[candidates1[candidates1 < candidates2]], constelations[candidates2[candidates1 < candidates2]]))

    print(len(constelations))
    print(join)
    while join.shape[1] > 0:
        # joining one constelation per iteration
        idx1, idx2 = join[:, 0]
        #print(idx1, idx2)
        join[join == constelations[idx2]] = constelations[idx1]
        constelations[constelations == constelations[idx2]] = constelations[idx1]
        join = join[:, join[0, :] != join[1, :]]
        

    res = len(np.unique(constelations))    
                                
            
    print('Silver star answer: \n{0}'.format(res))
    
    print('** Second part:')
    
    
    print('Golden star answer: \n{0}'.format(res))
    t2 = time.time()
    print('Program run for  {0} sec.'.format(round(t2-t1,2)))

