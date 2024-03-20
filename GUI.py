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

# load images and scale them to the correct size
image_button = pygame.image.load("button.png")
image_button = pygame.transform.scale(image_button, (WIDTH, HEIGHT))

image1 = pygame.image.load("1.png")
image1 = pygame.transform.scale(image1, (WIDTH, HEIGHT))

image_flag = pygame.image.load("flag.png")
image_flag = pygame.transform.scale(image_flag, (WIDTH, HEIGHT))

image_question_mark = pygame.image.load("question_mark.png")
image_question_mark = pygame.transform.scale(image_question_mark, (WIDTH, HEIGHT))

# Create a matrix to store flag states
flags = [["none"] * 9 for _ in range(9)]

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
                #print("Left Click ", pos, "Grid coordinates: ", row, column)
            elif event.button == 3:  # Right click
                pos = pygame.mouse.get_pos()
                column = pos[0] // (WIDTH + MARGIN)
                row = pos[1] // (HEIGHT + MARGIN)
                print("Right click", pos, "Grid coordinates", row, column)

                # Toggle flag state to know the status of each grid position
                if flags[row][column] == "none":
                    flags[row][column] = "flag"
                elif flags[row][column] == "flag":
                    flags[row][column] = "question"
                else:
                    flags[row][column] = "none"

    screen.fill("grey")

    # create grid
    for row in range(9):
        for column in range(9):
            if flags[row][column] == "flag":
                screen.blit(image_flag, ((MARGIN + WIDTH) * column + MARGIN, (MARGIN + HEIGHT) * row + MARGIN))
            elif flags[row][column] == "question":
                screen.blit(image_question_mark, ((MARGIN + WIDTH) * column + MARGIN, (MARGIN + HEIGHT) * row + MARGIN))
            else:
                screen.blit(image_button, ((MARGIN + WIDTH) * column + MARGIN, (MARGIN + HEIGHT) * row + MARGIN))

    pygame.display.update()
    clock.tick(60)  # limit to 60 FPS

pygame.quit()
