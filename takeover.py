#!/usr/bin/env python

# define constants for objects on the board
BOARD_BLANK = 0
BOARD_VILLAGE_1 = 1
BOARD_VILLAGE_2 = 2
BOARD_WARRIOR_1 = 3
BOARD_WARRIOR_2 = 4

# initialize board as global variable
board = [[]]

def init_board()
    board = [[BOARD_BLANK for i in xrange(8)] for j in xrange(8)]
    board[0][0] = BOARD_VILLAGE_1
    board[0][1] = BOARD_WARRIOR_1
    board[1][1] = BOARD_WARRIOR_1
    board[1][0] = BOARD_WARRIOR_1
    
    board[7][7] = BOARD_VILLAGE_2
    board[7][6] = BOARD_WARRIOR_2
    board[6][6] = BOARD_WARRIOR_2
    board[6][7] = BOARD_WARRIOR_2

if __name__ == '__main__':
    init_board()
