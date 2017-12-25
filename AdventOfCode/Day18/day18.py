# -*- coding: utf-8 -*-
"""
Created on Fri Dec 25 19:51:22 2017

@author: Jan
"""


import numpy as np
import pandas as pd
import time

## Advent of Code 2017, Day 18
day = 18

data = open('day18test.txt', 'r')
#data = data.read().split(',')

def duet(data):
    register = {}
    extras = ['rcv', 'snd']
    last_sound = 0
    data = data.readlines()
    
    i = 0
    total = 0
    while i < len(data):
        line = data[i].replace('\n', '')
        if line[:3] not in extras:
            command, reg, value = line.split(' ')
            if reg not in register:
                register[reg] = 0
            try:
                value = int(value)
            except:
                value = register[reg]
            print(command, reg, value)
            if command == 'set':
                register[reg] = value
            elif command == 'add':
                register[reg] += value
            elif command == 'mul':
                register[reg] *= value
            elif command == 'mod':
                register[reg] = np.mod(register[reg], value)
            elif command == 'jgz':
                try:
                    jump_val = int(reg)
                except:
                    jump_val = register[reg]
                if jump_val > 0:
                    print(i, value)
                    i += value
                    continue
                
        else:
            command, value = line.split(' ')
            if command == 'rcv' and register[value] != 0:
                print('Recover! ', last_sound)
                break
            if command == 'snd':
                print('Play! ', register[value])
                last_sound = register[value]
                
            print(command, value)
        print('State of register: ', register, i)
        i += 1
        total += 1
        if total > 150:
            print('breaking')
            break
    print(last_sound)
    return register

       
class Day18():
    def __init__(self, input_str: str):              
        self.input = [line.replace('\n', '') for line in input_str]

    @staticmethod
    def __program(code: [str], register_p=0):
        registers = {letter: 0 for letter in 'abcdefghijklmnopqrstuvwxyz'}
        registers['p'] = register_p

        sending = []  # buffer of values to send

        program_counter = 0
        while 0 <= program_counter <= len(code):
            instruction, argument_1, *other_arguments = code[program_counter].split(' ')

            if other_arguments:  # might as well convert argument 2 here instead of repeating it for all instructions
                argument_2 = registers[other_arguments[0]] if other_arguments[0] in registers.keys() else int(other_arguments[0])

            if instruction == 'snd':  # no need to yield immediatelly, just makes things complicated (trust me)
                sending.append(registers[argument_1] if argument_1 in registers.keys() else int(argument_1))

            if instruction == 'set':
                registers[argument_1] = argument_2

            if instruction == 'add':
                registers[argument_1] += argument_2

            if instruction == 'mul':
                registers[argument_1] *= argument_2

            if instruction == 'mod':
                registers[argument_1] = registers[argument_1] % argument_2

            if instruction == 'rcv':  # send own values and wait for a new one
                registers[argument_1] = yield sending  
                sending = []

            if instruction == 'jgz':
                condition_value = registers[argument_1] if argument_1 in registers.keys() else int(argument_1)
                if condition_value > 0:
                    program_counter += argument_2
                    continue

            program_counter += 1

    def __solve_part_1(self):
        return next(self.__program(self.input))[-1]

    def __solve_part_2(self):
        program_0 = self.__program(self.input, register_p=0)
        program_1 = self.__program(self.input, register_p=1)

        # do an initial run because of the while loops below
        to_1, to_0 = next(program_0), next(program_1)

        sent_by_1_total = 0
        while True:
            while to_0:
                yielded_by_0 = program_0.send(to_0.pop(0))
                if yielded_by_0:
                    to_1 += yielded_by_0

            while to_1:
                yielded_by_1 = program_1.send(to_1.pop(0))
                if yielded_by_1:
                    to_0 += yielded_by_1
                    sent_by_1_total += len(yielded_by_1)

            if not (to_0 or to_1):  # both are waiting but there are no new values
                print('deadlock detected')
                break

        return sent_by_1_total    

    def solve_all(self):
        return [self.__solve_part_1(), self.__solve_part_2()]


t1 = time.time()
print("***  It's Advent of Code 2017, Day {}!  ***\n".format(day))
print('First part:')
register = duet(data)
print(register)

print('Second part:')
data = open('day18.txt', 'r')
a = Day18(data.readlines())
print(a.solve_all())

t2 = time.time()
print('\nProgram run for  {0} sec.'.format(round(t2-t1,2)))

