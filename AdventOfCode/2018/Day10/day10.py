# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 20:42:22 2018

@author: Jan
"""


import numpy as np
import pandas as pd
import time
import datetime as dt
import re
import matplotlib.pyplot as plt
from scipy import sparse

## Advent of Code 2018, Day 10
day = 10

if __name__ == '__main__':
    
    t1 = time.time()
    print("***  It's Advent of Code 2018, Day {0}!  ***\n".format(day))
    print('** First part:')
    
    with open('day{0}.txt'.format(day), 'r') as f:
        data = [line.strip() for line in f.readlines()]
     
    gifExport = False
    poss = []
    vels = []

    for line in data:
        r = re.findall('position=<(.*?)> velocity=<(.*?)>', line)
        poss += [list((int(x) for x in r[0][0].split(', ')))]
        vels += [list((int(x) for x in r[0][1].split(', ')))]
    
    
    def move1sec(poss, vels):
        for idx, pos in enumerate(poss):
            poss[idx] = [pos[0] + vels[idx][0], pos[1] + vels[idx][1]]
        return poss
        
    def draw(poss, i):
        minT, maxT = getLimits(poss)
        minT += 2
        minT = abs(minT)
        dim = abs(minT) + maxT + 2
        rr = np.zeros((dim, dim))
        for pos in poss:
            rr[pos[1] + minT][pos[0] + minT] = 1
        plt.matshow(rr)
        if gifExport:
            plt.savefig('stars{0}.png'.format(i))
        
    def getLimits(poss):
        max_pic = 0
        min_pic = 0
        for pos in poss:
            if max(pos) > max_pic:
                max_pic = max(pos)
            if min(pos) < min_pic:
                min_pic = min(pos)
        return min_pic, max_pic
        
    for i in range(10650):
        poss = move1sec(poss, vels)
        #print(i, getLimits(poss))
        if i > 10630:   
            print(i)
            draw(poss, i)
    
    
    if gifExport:
        import imageio
        images = []
        filenames = ['stars10631.png', 
                     'stars10632.png',
                     'stars10633.png',
                     'stars10634.png',
                     'stars10635.png',
                     'stars10636.png',
                     'stars10637.png',
                     'stars10638.png',
                     'stars10639.png',
                     'stars10640.png',
                     'stars10641.png',
                     'stars10642.png',
                     'stars10643.png',
                     'stars10644.png',
                     'stars10645.png',
                     'stars10646.png',
                     'stars10647.png',
                     'stars10648.png',
                     'stars10649.png',]
        for filename in filenames:
            images.append(imageio.imread(filename))
        imageio.mimsave('stars.gif', images)
        
    res = 0
    print('Silver star answer: \n{0}'.format(res))
    
    print('** Second part:')
    
    
    print('Golden star answer: \n{0}'.format(res))
    t2 = time.time()
    print('Program run for  {0} sec.'.format(round(t2-t1,2)))

