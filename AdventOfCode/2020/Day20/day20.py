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


    def calc_tile(tiled, tile_borders, dimension, x = 0, y = 0, found = set()):
        
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
    

    combinations, image = image(tiles_input)

    mul = 1
    mul *= image[0][0][0]
    mul *= image[0][-1][0]
    mul *= image[-1][0][0]
    mul *= image[-1][-1][0] 
    
    print(mul)
        
    #### 2nd Task
    print('** Second part:')
    
    # Sea Monsters
    
    monster = """                  # \n#    ##    ##    ###\n #  #  #  #  #  #   """

    monster = monster.split('\n')
    for k in range(len(monster)):
        monster[k] = [1 if x=='#' else 0 for x in monster[k]]
    

    image_size = len(image)    
    mat = np.array([[0 for i in range(8*image_size)] for j in range(8*image_size)])
           
    
    for y, image_y in enumerate(image):
        for x, image_x in enumerate(image_y):
            tile = combinations[image_x[0]][image_x[1]]
            tile = np.array(tile).T
            temp_image_2 = []
            for row in tile[1:-1]:
                temp_image_2 += [[1 if z=='#' else 0 for z in row[1:-1]]]
              
            mat[y*8:(y+1)*8, x*8:(x+1)*8] = temp_image_2       

        
    # create image, without edges
    plt.matshow(mat)
    plt.matshow(monster)
    
    monster_cnt = 0
    i = 0
    while monster_cnt == 0:
        # Try finding monsters
        for row in range(len(mat)-2):
            for col in range(len(mat)-len(monster[0])):
                found = True
                for monster_row in range(len(monster)):
                    for monster_col in range(len(monster[0])):
                        if monster[monster_row][monster_col] == 1:
                            if mat[row + monster_row, col + monster_col] != 1:
                                found = False
                                break
                    if not found:
                        break
    
                if found:
                    monster_cnt += 1
                    
                    for monster_row in range(len(monster)):
                        for monster_col in range(len(monster[0])):
                            if monster[monster_row][monster_col] == 1:
                                mat[row + monster_row, col + monster_col] = 2
        
        if monster_cnt == 0:    
            if i == 3:
                mat = np.flip(mat, 0)
            else:
                mat = np.array(list(list(x)[::-1] for x in zip(*mat))) # matrix rotation right 
    
        i += 1
        
    print('Monster counter: {0}'.format(monster_cnt))
    
    
    plt.matshow(mat)
    

    # count # / 1s
    print(np.count_nonzero(mat == 1))
    

    t2 = time.time()
    print('Program run for  {0} sec.'.format(round(t2 - t1, 2)))

