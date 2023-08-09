import pygame
import random
import sys
import os
from config import cfg
from func import *

#Principal Function
def main():
    pygame.init()
    
    clock = pygame.time.Clock()
    
    #This select a image of resources folder and fit it in the screen of the game
    game_image_used = pygame.image.load(Get_Images_Paths(cfg.PICTURES_PATH))
    game_image_used = pygame.transform.scale(game_image_used, cfg.SCREEN_SIZE) #This transform any type of image size to fit this in the screen of the game
    game_image_used_rect = game_image_used.get_rect()
    
    #Setting the screen and the caption
    screen = pygame.display.set_mode(cfg.SCREEN_SIZE)
    pygame.display.set_caption("Pokemon Puzzle")
    
    #Defining the size of the Start Screen and the numbers of columns, rows and cells
    size = Show_Start_Interface(screen, game_image_used_rect.width, game_image_used_rect.height)
    assert isinstance(size, int)
    num_rows, num_cols = size, size
    num_cells = size*size
    
    #Setting the size of the cells for the pictures in the game
    cell_width = game_image_used_rect.width // num_cols
    cell_height = game_image_used_rect.height // num_rows
    
    #Loop
    while True:
        #Return the board and the blank cell index of the game
        game_board, blank_cell_index = CreateBoard(num_rows, num_cols, num_cells)
        
        if not isGameOver(game_board, size):
            break
    
    is_running = True
    
    #Main Loop
    while is_running:
        for event in pygame.event.get():
            if (event.type == pygame.QUIT) or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                pygame.quit()
                sys.exit()
            
            #Setting the moving of the game with the keyboard
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT or event.key == ord("a"):
                    blank_cell_index = moveL(game_board, blank_cell_index, num_cols)
                
                elif event.key == pygame.K_RIGHT or event.key == ord("d"):
                    blank_cell_index = moveR(game_board, blank_cell_index, num_cols)
                
                elif event.key == pygame.K_UP or event.key == ord("w"):
                    blank_cell_index = moveU(game_board, blank_cell_index, num_cols, num_rows)
                
                elif event.key == pygame.K_DOWN or event.key == ord("s"):
                    blank_cell_index = moveD(game_board, blank_cell_index, num_cols)
            
            #Setting the moving of the game with the mouse
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                x , y = pygame.mouse.get_pos() #This get the positions coordinates of the cursor mouse
                
                x_pos = x // cell_width
                y_pos = y // cell_height
                
                idx = x_pos + y_pos * num_cols
                
                if idx == blank_cell_index - 1:
                    blank_cell_index = moveR(game_board, blank_cell_index, num_cols)
                
                elif idx == blank_cell_index + 1:
                    blank_cell_index = moveL(game_board, blank_cell_index, num_cols)
                
                elif idx == blank_cell_index + num_cols:
                    blank_cell_index = moveU(game_board, blank_cell_index, num_cols, num_rows)
                
                elif idx == blank_cell_index - num_cols:
                    blank_cell_index = moveD(game_board, blank_cell_index, num_cols)
        
        if isGameOver(game_board, size):
            game_board[blank_cell_index] = num_cells - 1
            is_running = False
        
        screen.fill(cfg.BACKGROUND_COLOR)
        
        for i in range(num_cells):
            if game_board[i] == -1:
                continue
            
            x_pos = i // num_cols
            y_pos = i % num_cols
            
            rect = pygame.Rect(y_pos * cell_width, x_pos * cell_height, cell_width, cell_height)
            image_area = pygame.Rect((game_board[i] % num_cols) * cell_width, (game_board[i] // num_cols) * cell_height, cell_width, cell_height)
            
            screen.blit(game_image_used, rect, image_area)
        
        for i in range(num_cols + 1):
            pygame.draw.line(screen, cfg.BLACK, (i * cell_width, 0), (i * cell_width, game_image_used_rect.height))
        
        for i in range(num_rows + 1):
            pygame.draw.line(screen, cfg.BLACK, (0, i * cell_height), (game_image_used_rect.width, i * cell_height))
        
        pygame.display.update()
        clock.tick(cfg.FPS)
    
    Show_End_Interface(screen, game_image_used_rect.width, game_image_used_rect.height)

if __name__ == "__main__":
    main()