import pygame
from pygame.locals import *

#start_timer 
#timer_running
#difficulty
#x
#y
#row 
#col 
dict_cases = {}


import pygame

BLACK = (0,0,0)
WHITE = (255,255,255)
GREEN = (0,255,0)
WIDTH = 30
HEIGHT = 30
MARGIN = 0

grid = []

#create a matrix
for row in range (9):
    grid.append([])
    for col in range(9):
        grid[row].append(0)

#grid [1][5] = 1

#initialize pygame
pygame.display.init()
screen_width = 300
screen_height = 300
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("MINESWEEPER")
clock = pygame.time.Clock()
running = True

#load image and scale it to the correct size
button_image = pygame.image.load("button.png")
button_image = pygame.transform.scale(button_image, (WIDTH, HEIGHT))
#button_image.convert()



#Main
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()        #get the position of mouse click

            #get the grid coordinate
            column = pos[0] // (WIDTH+MARGIN)
            row = pos[1] // (HEIGHT+MARGIN)
            
            #considers the click only inside the grid
            grid[row][column] = 1
            print("Click ", pos, "Grid coordinates: ", row, column)

    screen.fill("grey")

#create grid  
    for row in range(9):
        for column in range(9):
            #color = WHITE
            if grid[row][column] == 1:
                color = BLACK
            #rect =pygame.draw.rect(screen, color, [(MARGIN + WIDTH)* column + MARGIN, (MARGIN + HEIGHT)* row + MARGIN, WIDTH,HEIGHT])
            screen.blit(button_image, [(MARGIN + WIDTH)* column + MARGIN, (MARGIN + HEIGHT)* row + MARGIN, WIDTH,HEIGHT])
    #pygame.display.flip()
    pygame.display.update()

    clock.tick(60)      #limit to 60 FPS

pygame.quit()