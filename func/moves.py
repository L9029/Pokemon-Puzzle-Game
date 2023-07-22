#Moving Right
def moveR(board, blank_cell_index, num_cols):
    if blank_cell_index % num_cols == 0:
        return blank_cell_index
    
    board[blank_cell_index - 1], board[blank_cell_index] = board[blank_cell_index], board[blank_cell_index - 1]
    
    return blank_cell_index - 1

#Moving Left
def moveR(board, blank_cell_index, num_cols):
    if (blank_cell_index + 1) % num_cols == 0:
        return blank_cell_index
    
    board[blank_cell_index + 1], board[blank_cell_index] = board[blank_cell_index], board[blank_cell_index + 1]
    
    return blank_cell_index + 1