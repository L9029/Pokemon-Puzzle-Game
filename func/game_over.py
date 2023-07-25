def isGameOver(board, size):
    #This check if the size is integer
    assert isinstance(size, int)
    
    #the number of cells in the board
    num_cells = size * size
    
    for i in range(num_cells - 1):
        if board[i] != i:
            return False
    
    return True