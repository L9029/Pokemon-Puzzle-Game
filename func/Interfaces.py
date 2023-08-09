import sys
import pygame
from config import cfg

def Show_End_Interface(screen, width, height):
    #Setting the Background of the screen
    screen.fill(cfg.BACKGROUND_COLOR)
    #Setting the Font for the screen
    font = pygame.font.Font(cfg.FONT_PATH, width / 15)
    #Setting the title for the end screen
    title = font.render("Good Job! You Won!", True, (233, 150, 122))
    #Defining the position and rect for the end title
    rect = title.get_rect()
    rect.midtop = (width / 2, height / 2.5)
    screen.blit(title, rect)
    
    pygame.display.update()
    
    #Loop for the end of the game
    while True:
        for event in pygame.event.get():
            if (event.type == pygame.QUIT) or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                pygame.quit()
                sys.exit()
        
        pygame.display.update()

def Show_Start_Interface(screen, width, height):
    #Setting the Background of the screen
    screen.fill(cfg.BACKGROUND_COLOR)
    
    #Setting the title font for the screen
    title_font = pygame.font.Font(cfg.FONT_PATH, width // 4)
    title = title_font.render("Puzzle Game", True, cfg.RED)
    
    #Setting the content font and the contents for the screen
    content_font = pygame.font.Font(cfg.FONT_PATH, width // 20)
    content1 = content_font.render("Press H, M or L to choose your puzzle", True, cfg.BLUE)
    content2 = content_font.render("H- 5x5, M- 4x4, L- 3x3", True, cfg.BLUE)
    
    #Defining the position and rect for title
    title_rect = title.get_rect()
    title_rect.midtop = (width / 2, height / 10)
    
    #Defining the position and rect for the contents
    c1_rect = content1.get_rect()
    c1_rect.midtop = (width / 2, height / 2.2)
    
    c2_rect = content2.get_rect()
    c2_rect.midtop = (width / 2, height / 1.8)
    
    #Updating the settings of the title and the contents in the screen
    screen.blit(title, title_rect)
    screen.blit(content1, c1_rect)
    screen.blit(content2, c2_rect)
    
    #Loop for the start of the game
    while True:
        for event in pygame.event.get():
            if (event.type == pygame.QUIT) or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                pygame.quit()
                sys.exit()
            
            elif event.type == pygame.KEYDOWN:
                if event.key == ord("l"):
                    return 3

                elif event.key == ord("m"):
                    return 4
            
                elif event.key == ord("h"):
                    return 5
        
        pygame.display.update()