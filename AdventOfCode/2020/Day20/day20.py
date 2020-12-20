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
day = 20
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
        
    tiles_input = {}
    for tile in data:
        
        tile_num = int(re.findall(r'\d+', tile)[0]) # numbers = ['2', '3']
        tile_sep = []
        tile_str = tile.split(':\n')[1]
        for tile_line in tile_str.split('\n'):
            if tile_line != '':
                tile_sep += [[char for char in tile_line]]
            
        #print(tile_num, len(tile_sep))
        tiles_input[tile_num] = tile_sep


    def calc_tile(tiled, tile_borders, dimension, x=0, y=0, found=set()):
        
        if y == dimension:
            return tiled
        
        next_x = x + 1
        next_y = y
        
        if next_x == dimension:
            next_x = 0
            next_y += 1
        
        for tile_id, tiles in tile_borders.items():
            if tile_id in found:
                continue
            found.add(tile_id)
            
            for option_id, border in tiles.items():
                top, _, _, left = border
    
                if x > 0:
                    neighbor_id, neighbor_option = tiled[x-1][y]
                    _, neighbor_right, _, _ = tile_borders[neighbor_id][neighbor_option]
                    if neighbor_right != left:
                        continue
                if y > 0:
                    neighbor_id, neighbor_option = tiled[x][y-1]
                    _, _, neighbor_low, _ = tile_borders[neighbor_id][neighbor_option]
                    if neighbor_low != top:
                        continue
                
                tiled[x][y] = (tile_id, option_id)
                final = calc_tile(tiled, tile_borders, dimension,
                              x=next_x, y=next_y, found=found)
                
                if final is not None:
                    return final
            
            found.remove(tile_id)
        tiled[x][y] = None
        
        return None

    
    def borders(tile):
        return (tile[0], [line[-1] for line in tile], tile[-1], [line[0] for line in tile])
   

    def flips(tile):
        return [tile, tile[::-1], [line[::-1] for line in tile], [line[::-1] for line in tile][::-1]]
    

    def rotations(tile):
        rots = [tile]
        prev = tile
        
        for i in range(3): # 3 possible rotations
            tile = [line[:] for line in tile]
            
            for x in range(len(tile)):
                for y in range(len(tile[x])):
                    tile[x][y] = prev[len(tile[x])-y-1][x]
            
            prev = tile
            rots.append(tile)
        
        return rots
    
    
    
    def combinations(tile):
        combination = []
        
        for flip in flips(tile):
            #print(flip)
            combination.extend(rotations(flip))
        
        output = []
        
        for pos in combination:
            if pos not in output:
                output.append(pos)
        
        return output
    
    
    def image(tiles):
        
        dimension = int(np.ceil(math.sqrt(len(tiles.keys()))))
        #print(dimension)
        tiled = [[None] * dimension for i in range(dimension)]
        
        tile_options = {tile_id: combinations(tile) for tile_id, tile in tiles.items()}
        tile_possible_borders = {}
        
        for tile_id, tiles in tile_options.items():
            for idx, tile in enumerate(tiles):
                
                if tile_id not in tile_possible_borders.keys():
                    tile_possible_borders[tile_id] = {}
                tile_possible_borders[tile_id][idx] = borders(tile)
        

        return tile_options, calc_tile(tiled, tile_possible_borders, dimension)
    

    combnations, image = image(tiles_input)

    mul = 1
    mul *= image[0][0][0]
    mul *= image[0][-1][0]
    mul *= image[-1][0][0]
    mul *= image[-1][-1][0] 
    
    print(mul)
        
    #### 2nd Task
    print('** Second part:')
    
        
   


    t2 = time.time()
    print('Program run for  {0} sec.'.format(round(t2 - t1, 2)))

