#Moving Right
def moveR(board, blank_cell_index, num_cols):
    if blank_cell_index % num_cols == 0:
        return blank_cell_index
    
    board[blank_cell_index - 1], board[blank_cell_index] = board[blank_cell_index], board[blank_cell_index - 1]
    
    return blank_cell_index - 1

#Moving Left
def moveL(board, blank_cell_index, num_cols):
    if (blank_cell_index + 1) % num_cols == 0:
        return blank_cell_index
    
    board[blank_cell_index + 1], board[blank_cell_index] = board[blank_cell_index], board[blank_cell_index + 1]
    
    return blank_cell_index + 1

#Moving Down
def moveD(board, blank_cell_index, num_cols):
    if blank_cell_index < num_cols:
        return blank_cell_index
    
    board[blank_cell_index - num_cols], board[blank_cell_index] = board[blank_cell_index], board[blank_cell_index - num_cols]
    
    return blank_cell_index - num_cols


#Moving Up
def moveU(board, blank_cell_index, num_cols, num_rows):
    if blank_cell_index >= (num_rows - 1) * num_cols:
        return blank_cell_index
    
    board[blank_cell_index + num_cols], board[blank_cell_index] = board[blank_cell_index], board[blank_cell_index + num_cols]
    
    return blank_cell_index + num_cols