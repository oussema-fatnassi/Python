import pygame
from pygame.locals import *



# create a matrix
class GUI():
    # initialize pygame
    def __init__(self):
        pygame.init()
        self.screen_width = 300
        self.screen_height = 300
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("MINESWEEPER")
        self.clock = pygame.time.Clock()
        self.running = True
        self.WIDTH = 30
        self.HEIGHT = 30
        self.MARGIN = 0

        self.grid = []

        for row in range(9):
            self.grid.append([])
            for col in range(9):
                self.grid[row].append(0)


    def load_images(self):
        self.image_button = pygame.image.load("button.png")
        self.image_button = pygame.transform.scale(self.image_button, (self.WIDTH, self.HEIGHT))

        self.image1 = pygame.image.load("1.png")
        self.image1 = pygame.transform.scale(self.image1, (self.WIDTH, self.HEIGHT))

        self.image2 = pygame.image.load("2.png")
        self.image2 = pygame.transform.scale(self.image2, (self.WIDTH, self.HEIGHT))

        self.image3 = pygame.image.load("3.png")
        self.image3 = pygame.transform.scale(self.image3, (self.WIDTH, self.HEIGHT))

        self.image4 = pygame.image.load("4.png")
        self.image4 = pygame.transform.scale(self.image4, (self.WIDTH, self.HEIGHT))

        self.image5 = pygame.image.load("5.png")
        self.image5 = pygame.transform.scale(self.image5, (self.WIDTH, self.HEIGHT))

        self.image6 = pygame.image.load("6.png")
        self.image6 = pygame.transform.scale(self.image6, (self.WIDTH, self.HEIGHT))

        self.image7 = pygame.image.load("7.png")
        self.image7 = pygame.transform.scale(self.image7, (self.WIDTH, self.HEIGHT))

        self.image8 = pygame.image.load("8.png")
        self.image8 = pygame.transform.scale(self.image8, (self.WIDTH, self.HEIGHT))

        self.image_empty = pygame.image.load("empty.png")
        self.image_empty = pygame.transform.scale(self.image_empty, (self.WIDTH, self.HEIGHT))

        self.image_flag = pygame.image.load("flag.png")
        self.image_flag = pygame.transform.scale(self.image_flag, (self.WIDTH, self.HEIGHT))

        self.image_question_mark = pygame.image.load("question_mark.png")
        self.image_question_mark = pygame.transform.scale(self.image_question_mark, (self.WIDTH, self.HEIGHT))

        self.image_bomb = pygame.image.load("bomb.png")
        self.image_bomb = pygame.transform.scale(self.image_bomb, (self.WIDTH, self.HEIGHT))

        self.image_final_bomb = pygame.image.load("final_bomb.png")
        self.image_final_bomb = pygame.transform.scale(self.image_final_bomb, (self.WIDTH, self.HEIGHT))

    # load images and scale them to the correct size


    # Create a matrix to store flag states
    def main(self):
        flags = [["none"] * 9 for _ in range(9)]

        self.load_images()

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:  # Left click
                        pos = pygame.mouse.get_pos()  # get the position of mouse click

                        # get the grid coordinate
                        column = pos[0] // (self.WIDTH + self.MARGIN)
                        row = pos[1] // (self.HEIGHT + self.MARGIN)

                        # considers the click only inside the grid
                        self.grid[row][column] = 1
                        print("Left Click ", pos, "Grid coordinates: ", row, column)
                    elif event.button == 3:  # Right click
                        pos = pygame.mouse.get_pos()
                        column = pos[0] // (self.WIDTH + self.MARGIN)
                        row = pos[1] // (self.HEIGHT + self.MARGIN)
                        print("Right click", pos, "Grid coordinates", row, column)

                        # Toggle flag state to know the status of each grid position
                        if flags[row][column] == "none":
                            flags[row][column] = "flag"
                        elif flags[row][column] == "flag":
                            flags[row][column] = "question"
                        else:
                            flags[row][column] = "none"

            self.screen.fill("grey")

            # create grid
            for row in range(9):
                for column in range(9):
                    if flags[row][column] == "flag":
                        self.screen.blit(self.image_flag, ((self.MARGIN + self.WIDTH) * column + self.MARGIN, (self.MARGIN + self.HEIGHT) * row + self.MARGIN))
                    elif flags[row][column] == "question":
                        self.screen.blit(self.image_question_mark, ((self.MARGIN + self.WIDTH) * column + self.MARGIN, (self.MARGIN + self.HEIGHT) * row + self.MARGIN))
                    else:
                        self.screen.blit(self.image_button, ((self.MARGIN + self.WIDTH) * column + self.MARGIN, (self.MARGIN + self.HEIGHT) * row + self.MARGIN))

            pygame.display.update()
            self.clock.tick(60)  # limit to 60 FPS

        pygame.quit()


GUI = GUI()
GUI.main()

# Main