# -*- coding: utf-8 -*-
"""
Created on Tue Dec 26 10:04:49 2017

@author: janb
"""


import numpy as np
import pandas as pd
import time


## Advent of Code 2017, Day 21
day = 21

data = open('day21.txt', 'r')
#data = data.read().split(',')

start = np.array([[0,1,0],[0,0,1],[1,1,1]])

def fractals(data):
    """ Art of fractal pic. """
    rules = []
    for line in data:
        firstpart = line[:line.find('=')-1]
        firstpart = firstpart.replace('#', '1').replace('.', '0').split('/')
        firstpart = np.array([[int(i) for i in firstpart[k]] for k in range(len(firstpart))])
                                            
        secondpart = line[line.find('>')+2:]
        secondpart = secondpart.replace('#', '1').replace('.', '0').replace('\n', '').split('/')
        secondpart = np.array([[int(i) for i in secondpart[k]] for k in range(len(secondpart))])
        #print(firstpart, secondpart)
        rules += [[firstpart, secondpart]]
        
    return rules
        
def find_match(mat1, mat2):
    """ Checks if mat1 rotated or flipped equals mat2. """
    mf = np.fliplr(mat1)
    mf2 = np.flipud(mat1)
    if np.array_equal(mat1, mat2) or np.array_equal(np.rot90(mat1, 1), mat2) or np.array_equal(np.rot90(mat1,2), mat2) or np.array_equal(np.rot90(mat1, 3), mat2):
        return True
    elif np.array_equal(mf, mat2) or np.array_equal(np.rot90(mf, 1), mat2) or np.array_equal(np.rot90(mf, 2), mat2) or np.array_equal(np.rot90(mf, 3), mat2):
        return True
    elif np.array_equal(mf2, mat2) or np.array_equal(np.rot90(mf2, 1), mat2) or np.array_equal(np.rot90(mf2, 2), mat2) or np.array_equal(np.rot90(mf2, 3), mat2):
        return True
    else:
        return False

        

def paint(pic, rules, ite = 1):
    """ Lets picture. """
    for i in range(ite): # Število iteracij
        n = len(pic)
        print(n, np.count_nonzero(pic))
        
        if np.mod(n, 2) == 0:
            l = n // 2 * 3
        else:
            l = n // 3 * 4
        newpic = np.zeros((l, l))
        
        if np.mod(n, 2) == 0: # Razdeli sliko na 2x2 enote
            l = n // 2
            for i in range(l):
                for j in range(l):
                    picpart = pic[i * 2: (i+1)*2,  j * 2: (j+1)*2]
                    for k in range(6):
                        if find_match(picpart, rules[k][0]):
                            newpic[i * 3: (i+1)*3,  j * 3: (j+1)*3] = rules[k][1]
                            break
                    
        else: # Razdeli sliko na 3x3 enote
            l = n // 3
            for i in range(l):
                for j in range(l):
                    picpart = pic[i * 3: (i+1)*3,  j * 3: (j+1)*3]
                    for k in range(6,len(rules)):
                        if find_match(picpart, rules[k][0]):
                            newpic[i * 4: (i+1)*4,  j * 4: (j+1)*4] = rules[k][1]
                            break
        pic = newpic
    return pic, np.count_nonzero(pic)



t1 = time.time()
print("***  It's Advent of Code 2017, Day {}!  ***\n".format(day))
print('First part:')
ruls = fractals(data)

print(start)
pic, counter = paint(start, ruls, 18)
print(counter)

print('Second part:')



t2 = time.time()
print('\nProgram run for  {0} sec.'.format(round(t2-t1,2)))

