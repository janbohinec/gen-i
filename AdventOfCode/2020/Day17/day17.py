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


## Advent of Code 2020
day = 17
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
        data = [line.strip().split(',') for line in f.readlines()]
        
    mat = []
    for line in data:
        new_line = list(line[0].replace('#', '1').replace('.', '0'))
        mat +=  [[int(i) for i in new_line]]


    def sum_all(mat):
        no = 0
        for x in range (len(mat)):
            for y in range(len(mat[0])):
                for z in range(len(mat[0][0])):
                    no += mat[x][y][z]
        return no
                       
    
    def count_neighbors(mat, x, y, z):
        cnt = 0
        for i in range(x - 1, x + 2):
            for j in range(y - 1, y + 2):
                for k in range(z - 1, z + 2):
                    if (i, j, k) != (x, y, z):
                        cnt += mat[i][j][k]
        return cnt
    
    dim = 20
    cube = [[[0 for i in range(dim)] for j in range(dim)] for k in range(dim)]
    
    print(sum_all(cube))
    
    # place initial state to the middle of the cube
    
    mid = 10
    
    for x in range(len(mat)):
        for y in range(len(mat[0])):
            cube[mid+x][mid+y][mid] = mat[x][y]
    
    print(sum_all(cube))
    
    # program cycle
    c = 0
    
    while c < 6:

        new_cube = [[[0 for i in range(dim)] for j in range(dim)] for k in range(dim)]

        for i in range(1, dim-1):
            for j in range(1, dim-1):
                for k in range(1, dim-1):
                    if cube[i][j][k] and 2 <= count_neighbors(cube, i, j, k) <= 3:
                        new_cube[i][j][k] = 1
                    elif not cube[i][j][k] and count_neighbors(cube, i, j, k) == 3:
                        new_cube[i][j][k] = 1
        
        
        #print(c, sum_all(new_cube))
        cube = copy.deepcopy(new_cube)
        c += 1
    
    print(sum_all(new_cube))
    
    #### 2nd Task
    print('** Second part:')

    def sum_all4(mat):
        no = 0
        for x in range (len(mat)):
            for y in range(len(mat[0])):
                for z in range(len(mat[0][0])):
                    for w in range(len(mat[0][0][0])):
                        no += mat[x][y][z][w]
        return no
                       
    
    def count_neighbors4(mat, x, y, z, w):
        cnt = 0
        for i in range(x - 1, x + 2):
            for j in range(y - 1, y + 2):
                for k in range(z - 1, z + 2):
                    for l in range(w - 1, w + 2):
                        if (i, j, k, l) != (x, y, z, w):
                            cnt += mat[i][j][k][l]
        return cnt    

    
    dim = 29
    cube = [[[[0 for i in range(dim)] for j in range(dim)] for k in range(dim)] for l in range(dim)]

    # place initial state to the middle of the cube
    mid = dim//2
    for x in range(len(mat)):
        for y in range(len(mat[0])):
            cube[mid+x][mid+y][mid][mid] = mat[x][y]
    
    print(sum_all4(cube))


    # program cycle
    c = 0
    
    while c < 6:

        new_cube = [[[[0 for i in range(dim)] for j in range(dim)] for k in range(dim)] for l in range(dim)]

        for i in range(1, dim-1):
            for j in range(1, dim-1):
                for k in range(1, dim-1):
                    for l in range(1, dim-1):
                        neigh = count_neighbors4(cube, i, j, k, l)
                        if cube[i][j][k][l] and 2 <= neigh <= 3:
                            new_cube[i][j][k][l] = 1
                        elif not cube[i][j][k][l] and neigh == 3:
                            new_cube[i][j][k][l] = 1
        
        
        print(c, sum_all4(new_cube))
        cube = copy.deepcopy(new_cube)
        c += 1

    print(sum_all4(new_cube))

    t2 = time.time()
    print('Program run for  {0} sec.'.format(round(t2 - t1, 2)))

