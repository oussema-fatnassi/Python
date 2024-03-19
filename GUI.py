import pygame
from pygame.locals import *

WIDTH = 30
HEIGHT = 30
MARGIN = 0

grid = []

# create a matrix
for row in range(9):
    grid.append([])
    for col in range(9):
        grid[row].append(0)

# initialize pygame
pygame.init()
screen_width = 300
screen_height = 300
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("MINESWEEPER")
clock = pygame.time.Clock()
running = True

# load image and scale it to the correct size
button_image = pygame.image.load("button.png")
button_image = pygame.transform.scale(button_image, (WIDTH, HEIGHT))

image1 = pygame.image.load("1.png")
image1 = pygame.transform.scale(image1, (WIDTH, HEIGHT))

image_flag = pygame.image.load("flag.png")
image_flag = pygame.transform.scale(image_flag, (WIDTH, HEIGHT))

# Create a matrix to store flag states, 2D list with FALSE values
flags = [[False] * 9 for _ in range(9)]

# Main
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left click
                pos = pygame.mouse.get_pos()  # get the position of mouse click

                # get the grid coordinate
                column = pos[0] // (WIDTH + MARGIN)
                row = pos[1] // (HEIGHT + MARGIN)

                # considers the click only inside the grid
                grid[row][column] = 1
                print("Left Click ", pos, "Grid coordinates: ", row, column)
            elif event.button == 3:  # Right click
                pos = pygame.mouse.get_pos()
                column = pos[0] // (WIDTH + MARGIN)
                row = pos[1] // (HEIGHT + MARGIN)
                print("Right click", pos, "Grid coordinates", row, column)

                # Toggle flag state
                flags[row][column] = not flags[row][column]

    screen.fill("grey")

    # create grid
    for row in range(9):
        for column in range(9):
            if flags[row][column]:      #verify if flag is in position row column
                screen.blit(image_flag, ((MARGIN + WIDTH) * column + MARGIN, (MARGIN + HEIGHT) * row + MARGIN))
            else:
                screen.blit(button_image, ((MARGIN + WIDTH) * column + MARGIN, (MARGIN + HEIGHT) * row + MARGIN))

    pygame.display.update()
    clock.tick(60)  # limit to 60 FPS

pygame.quit()
