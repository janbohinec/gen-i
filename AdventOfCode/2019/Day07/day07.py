# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 20:42:22 2018

@author: Jan
"""

import numpy as np
import pandas as pd
import time
import datetime as dt

## Advent of Code 2019
day = 7
year = 2019

def day_str(day):
    """ Return string from integer day. """
    return str(day) if day >= 10 else '0' + str(day)
    
if __name__ == '__main__':
    
    t1 = time.time()
    print("***  It's Advent of Code {1}, Day {0}!  ***\n".format(day, year))
    #### 1st Task
    print('** First part:')
    
    #data = open('day{0}.txt'.format(day_str(day)), 'r')
    #rr = []
    
    with open('day{0}.txt'.format(day_str(day)), 'r') as f:
        data = [line.strip().split(',') for line in f.readlines()]
        #rr += [line.replace('\\', '\\').replace('\n', '') for line in f.readlines()]
    
    
    def param(rr, k, mode, n):
        if mode == 1:
            return rr[k % n]
        elif mode == 0:
            return rr[rr[k % n]]
    
    def phases_combinations(frm, to):
        comb = []
        for i in range(frm, to+1):
            for k in range(frm, to+1):
                for l in range(frm, to+1):
                    for m in range(frm, to+1):
                        for n in range(frm, to+1):
                            phases = [i, k, l, m, n]
                            if len(phases) == len(set(phases)):
                                comb += [[i, k, l, m, n]]
        return comb
            

    
    def intcode(inpt):
        
        rr = []
        for i in range(len(data[0])):
            rr.append(int(data[0][i]))
        
        
        n = len(rr)
        i = 0
        while True:
            code = rr[i]
            code_str = str(abs(code))
            if len(code_str) == 5:
                modes = [int(code_str[0]), int(code_str[1]), int(code_str[2])]
            if len(code_str) == 4:
                modes = [0, int(code_str[0]), int(code_str[1])]                
            if len(code_str) == 3:
                modes = [0, 0, int(code_str[0])]
            if len(code_str) <= 2:
                modes = [0, 0, 0]        
    
            code = int(str(code)[-2:])
            if code == 1: # add
                rr[rr[i+3] % n] = param(rr, i+1, modes[-1], n) + param(rr, i+2, modes[-2], n)
                step = 4
            elif code == 2: # multi
                rr[rr[i+3] % n] = param(rr, i+1, modes[-1], n) * param(rr, i+2, modes[-2], n)
                step = 4
            elif code == 3: # copy
                #print(inpt)
                rr[rr[i+1]] = inpt.pop()
                step = 2
            elif code == 4: # output
                output = rr[rr[i+1]]
                #print(output)
                step = 2 
            elif code == 5: # jump if true
                if param(rr, i+1, modes[-1], n) != 0:
                    i = param(rr, i+2, modes[-2], n)
                    step = 0
                else:
                    step = 3
            elif code == 6: # jump if false
                if param(rr, i+1, modes[-1]) == 0:
                    i = param(i+2, modes[-2], n)
                    step = 0
                else:
                    step = 3
            elif code == 7: # less than
                if param(rr, i+1, modes[-1], n) < param(rr, i+2, modes[-2], n):   
                    rr[rr[i+3] % n] = 1
                else:
                    rr[rr[i+3] % n] = 0
                step = 4
            elif code == 8: # equals
                if param(rr, i+1, modes[-1]) == param(rr, i+2, modes[-2], n):   
                    rr[rr[i+3] % n] = 1
                else:
                    rr[rr[i+3] % n] = 0                
                step = 4
            elif code == 99:
                break #stop
            
            i += step
        return output
    
    
    #data = [3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0]
    #data = [3,23,3,24,1002,24,10,24,1002,23,-1,23,101,5,23,23,1,24,23,23,4,23,99,0,0]
    #data = [[str(data[i]) for i in range(len(data))]]
    
    thrust = 0
    best_comb = []
    for comb in phases_combinations(0,4):
        a,b,c,d,e = comb
        a_o = intcode([0, a])
        b_o = intcode([a_o, b])
        c_o = intcode([b_o, c]) 
        d_o = intcode([c_o, d])
        e_o = intcode([d_o, e])
        if e_o > thrust:
            thrust = e_o
            best_comb = comb

        
    print(thrust, best_comb)
    
    #### 2nd Task
    print('** Second part:')
    
    
    class Amplifier():
        
        def __init__(self, amp):
            self.rr = []
            for i in range(len(data[0])):
                self.rr.append(int(data[0][i]))
            self.i = 0
            self.inpts = [amp]
            
            
        def param(rr, k, mode, n):
                if mode == 1:
                    return rr[k % n]
                elif mode == 0:
                    return rr[rr[k % n]]            
    
        def intcode(self):
            n = len(self.rr)
            while True:
                code = self.rr[self.i]
                code_str = str(abs(code))
                if len(code_str) == 5:
                    modes = [int(code_str[0]), int(code_str[1]), int(code_str[2])]
                if len(code_str) == 4:
                    modes = [0, int(code_str[0]), int(code_str[1])]                
                if len(code_str) == 3:
                    modes = [0, 0, int(code_str[0])]
                if len(code_str) <= 2:
                    modes = [0, 0, 0]        
        
                code = int(str(code)[-2:])
                if code == 1: # add
                    self.rr[self.rr[self.i+3] % n] = param(self.rr, self.i+1, modes[-1], n) + param(self.rr, self.i+2, modes[-2], n)
                    step = 4
                elif code == 2: # multi
                    self.rr[self.rr[self.i+3] % n] = param(self.rr, self.i+1, modes[-1], n) * param(self.rr, self.i+2, modes[-2], n)
                    step = 4
                elif code == 3: # copy
                    #print(self.inpt)
                    self.rr[self.rr[self.i+1]] = self.inpts.pop()
                    step = 2
                elif code == 4: # output
                    self.output = self.rr[self.rr[self.i+1]]
                    #print(output)
                    step = 2
                    if self.rr[self.i+step] == 99:
                        self.i += step
                        return self.output, False
                    else:
                        self.i += step
                        return self.output, True
#                    return self.output, active
                elif code == 5: # jump if true
                    if param(self.rr, self.i+1, modes[-1], n) != 0:
                        self.i = param(self.rr, self.i+2, modes[-2], n)
                        step = 0
                    else:
                        step = 3
                elif code == 6: # jump if false
                    if param(self.rr, self.i+1, modes[-1]) == 0:
                        self.i = param(self.i+2, modes[-2], n)
                        step = 0
                    else:
                        step = 3
                elif code == 7: # less than
                    if param(self.rr, self.i+1, modes[-1], n) < param(self.rr, self.i+2, modes[-2], n):   
                        self.rr[self.rr[self.i+3] % n] = 1
                    else:
                        self.rr[self.rr[self.i+3] % n] = 0
                    step = 4
                elif code == 8: # equals
                    if param(self.rr, self.i+1, modes[-1]) == param(self.rr, self.i+2, modes[-2], n):   
                        self.rr[self.rr[self.i+3] % n] = 1
                    else:
                        self.rr[self.rr[self.i+3] % n] = 0                
                    step = 4
                elif code == 99:
                    break #stop
                    active = False
                
                self.i += step
            return self.output, False
    

    
    #data = [3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5]
    #data = [[str(data[i]) for i in range(len(data))]]
    
    
    
    thrust = 0
    best_comb = []
    for comb in phases_combinations(5,9):
        a,b,c,d,e = comb
        e_o = 0
        aA = Amplifier(a)
        bA = Amplifier(b)
        cA = Amplifier(c)
        dA = Amplifier(d)
        eA = Amplifier(e)
        aA.inpts.insert(0,0)
        #print(a,b,c,d,e)
        while True:
            a_o,act_a = aA.intcode()
            bA.inpts.insert(0, a_o)
            b_o,act_b = bA.intcode()
            cA.inpts.insert(0, b_o)
            c_o,act_c = cA.intcode()
            dA.inpts.insert(0, c_o)
            d_o,act_d = dA.intcode()
            eA.inpts.insert(0, d_o)
            e_o,act_e = eA.intcode()
            aA.inpts.insert(0, e_o)
            if not act_a and not act_b and not act_c and not act_e and not act_e: # any engine not active
                break
        if e_o > thrust:
            thrust = e_o
            best_comb = comb

        
    print(thrust, best_comb)
    
    t2 = time.time()
    print('Program run for  {0} sec.'.format(round(t2 - t1, 2)))