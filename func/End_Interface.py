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