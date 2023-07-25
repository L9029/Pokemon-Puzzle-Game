import random
from config import cfg
from .moves import *

#Board Function
def CreateBoard(num_rows, num_cols, num_cells):
    board = []
    
    for i in range(num_cells):
        board.append(i)
    
    blank_cell_index = num_cells - 1
    board[blank_cell_index] = -1
    
    for i in range(cfg.RANDOM):
        direction = random.randint(0, 3)
        
        if direction == 0:
            blank_cell_index = moveL(board, blank_cell_index, num_cols)
        
        elif direction == 1:
            blank_cell_index = moveR(board, blank_cell_index, num_cols)
        
        elif direction == 2:
            blank_cell_index = moveU(board, blank_cell_index, num_cols, num_rows)
        
        elif direction == 3:
            blank_cell_index = moveD(board, blank_cell_index, num_cols)
    
    return board, blank_cell_index