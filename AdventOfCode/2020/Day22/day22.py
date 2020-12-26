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
import itertools

## Advent of Code 2020
day = 22
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
        data = f.read().split('\n\n')
        #data = [line.strip() for line in f.readlines()]
        
    
    player_1 = [int(i) for i in data[0].split(':\n')[1].split('\n')]
    player_2 = [int(i) for i in data[1].split(':\n')[1].split('\n')]
    
    while len(player_1) > 0 and len(player_2) > 0:
        card_1 = player_1.pop(0)
        card_2 = player_2.pop(0)
        
        if card_1 > card_2:
            player_1.append(card_1)
            player_1.append(card_2)
        else:
            player_2.append(card_2)
            player_2.append(card_1)
    

    def get_score(player_1, player_2):
        # Score
        if len(player_1) == 0:
            deck = player_2
            print('Player 1 won!')
        elif len(player_2) == 0:
            deck = player_1
            print('Player 2 won!')
        else:
            return 0
        n = len(deck)
        score = 0
        for i, card in enumerate(deck):
            score += (n - i) * card
            
        return score
    
    print(get_score(player_1, player_2))
    
    
    #### 2nd Task
    print('** Second part:')
    
    player_1 = [int(i) for i in data[0].split(':\n')[1].split('\n')]
    player_2 = [int(i) for i in data[1].split(':\n')[1].split('\n')]

    
    def combat_game(deck_1, deck_2):
        
        previous_games = set()
        
        while len(deck_1) > 0 and len(deck_2) > 0:
            card_1 = deck_1.pop(0)
            card_2 = deck_2.pop(0)
            
            
            if (card_1, card_2, len(deck_1), len(deck_2)) in previous_games: # games seen before, player_1 wins instantly
                #print('Game seen before!')
                deck_1.append(card_1)
                deck_1.append(card_2)
            else:
                previous_games.add((card_1, card_2, len(deck_1), len(deck_2)))
                if len(deck_1) >= card_1 and len(deck_2) >= card_2:
                    new_deck_1 = deck_1[:card_1]
                    new_deck_2 = deck_2[:card_2]
    
                    p_1, p_2 = combat_game(new_deck_1, new_deck_2)
                    if len(p_1) == 0: #player 2 won
                        deck_2.append(card_2)
                        deck_2.append(card_1)
                    else: # player 1 won
                        deck_1.append(card_1)
                        deck_1.append(card_2)
                else:
                    if card_1 > card_2:
                        deck_1.append(card_1)
                        deck_1.append(card_2)
                    else:
                        deck_2.append(card_2)
                        deck_2.append(card_1)
            
        return deck_1, deck_2

    player_1, player_2 = combat_game(player_1, player_2)

    print(get_score(player_1, player_2))
    
    t2 = time.time()
    print('Program run for  {0} sec.'.format(round(t2 - t1, 2)))

