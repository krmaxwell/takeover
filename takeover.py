#!/usr/bin/env python
import os
import pygame
import random
import sys

from pygame.locals import *

# define constants for objects on the board
BOARD_BLANK = 0
BOARD_VILLAGE_1 = 1
BOARD_VILLAGE_2 = 2
BOARD_WARRIOR_1 = 3
BOARD_WARRIOR_2 = 4
# able to expand as necessary for obstacles, powerups, etc.

# initialize board as global variable
board = [[]]

# necessary for PyGame to get set up
pygame.init()

def roll_die():
    # just for ease of reading later
    return random.randrange(6)+1

def init_board():
    # default board but may eventually offer different types
    board = [[BOARD_BLANK for i in xrange(8)] for j in xrange(8)]
    board[0][0] = BOARD_VILLAGE_1
    board[0][1] = BOARD_WARRIOR_1
    board[1][1] = BOARD_WARRIOR_1
    board[1][0] = BOARD_WARRIOR_1
    
    board[7][7] = BOARD_VILLAGE_2
    board[7][6] = BOARD_WARRIOR_2
    board[6][6] = BOARD_WARRIOR_2
    board[6][7] = BOARD_WARRIOR_2

def load_image(name, colorkey=None):
    fullname = os.path.join('images', name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error, message:
        print 'Cannot load image:', name
        raise SystemExit, message
    image = image.convert()
    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((0,0))
        image.set_colorkey(colorkey, RLEACCEL)
    return image, image.get_rect()

if __name__ == '__main__':
    init_board()
