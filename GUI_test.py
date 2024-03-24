import pygame
import time
from pygame.locals import *

class GUI():
    
    def __init__(self):
        pygame.init()
        self.difficulty = ""              
        self.screen_width = 0
        self.screen_height = 0  
        #self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("MINESWEEPER")
        self.clock = pygame.time.Clock()
        self.running = True
        self.WIDTH = 30
        self.HEIGHT = 30
        self.MARGIN = 0

        self.x = 0                                              # Position of the case
        self.y = 0
        self.cpt_cases_mined = 0
        self.cpt_cases_demined = 0
        self.x_max = 30                                         # Size of the grid
        self.y_max = 16

        self.first_click = False                                # Variable for the first click
        self.start_time = 0                                     # Variable for the timer
        self.RED = (255, 0, 0)
        self.BLACK = (0, 0, 0)
        clock = pygame.time.Clock()
        
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))


        self.Matrice_case = []                                  # Initialisation of the grid
        for row in range(self.y_max): 
            self.Matrice_case.append([])
            for col in range(self.x_max): 
                self.Matrice_case[row].append('')
    
    def pos_case(self):
        pos = pygame.mouse.get_pos()
        self.x = pos[0] // (self.WIDTH + self.MARGIN)
        self.y = pos[1] // (self.HEIGHT + self.MARGIN) 

    def load_images(self):                                      # Load all the images
        
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
        self.image_reset = pygame.image.load("reset.png")
        self.image_reset = pygame.transform.scale(self.image_reset, (self.WIDTH*1.5, self.HEIGHT*1.5))

    def timer_gui(self, time):
        time_str = "{:03d}".format(time // 1000)                # Display the timer
        font = pygame.font.Font("DS-DIGIT.TTF", 50)
        text = font.render(time_str, True, self.RED)
        text_rect = text.get_rect(center=(self.screen_width -45, self.screen_height -30))  # Positionnement du timer
        #self.screen.fill(self.BLACK)
        self.screen.blit(text, text_rect)
        pygame.display.update(text_rect)

    def num_cpt_cases_mined(self):
        font = pygame.font.Font("DS-DIGIT.TTF", 50)
        text_cpt_cases_mined = font.render(str(self.cpt_cases_mined), True, self.RED)
        rect_cpt_cases_mined = text_cpt_cases_mined.get_rect(center=(self.screen_width +45, self.screen_height -30))  # CONTROL THE VALUES, MAYBE CORRECTION NEEDED
        self.screen.blit(text_cpt_cases_mined, rect_cpt_cases_mined)
        pygame.display.update(rect_cpt_cases_mined)

    def select_difficulty(self,difficulty_choice):
        if difficulty_choice == "easy":
            self.x_max = 9
            self.y_max = 9
            self.screen_width = 270
            self.screen_height = 330    
            print("im in easy init grid")
        elif difficulty_choice == "medium":
            self.x_max = 16
            self.y_max = 16
            self.screen_width = 480
            self.screen_height = 540
            print("im in medium init grid")
        elif difficulty_choice == "hard":
            self.x_max = 30
            self.y_max = 16
            self.screen_width = 900
            self.screen_height = 540
            print("im in hard init grid")
        else:
           self.x_max = 9
           self.y_max = 9
           self.screen_width = 270
           self.screen_height = 330  
           print("im in else init grid")

    def return_choice(self, difficulty):
        if difficulty == "easy":
            return "easy"
        elif difficulty == "medium":
            return "medium"
        elif difficulty == "hard":
            return "hard"

    def init_grid(self, chosen_difficulty):                             # Initialisation of the grid and change the size of the window after the difficulty choice
        self.difficulty = self.return_choice(chosen_difficulty)
        self.select_difficulty((self.difficulty))
        
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))

        #self.load_images()
        self.screen.fill("grey")
        for i in range(self.y_max):
            for j in range(self.x_max):
                self.screen.blit(self.image_button, ((self.MARGIN + self.WIDTH) * j + self.MARGIN , (self.MARGIN + self.HEIGHT) * i + self.MARGIN ))                     
        
        self.screen.blit(self.image_reset, (self.screen_width // 2 - self.image_reset.get_width() // 2, self.screen_height - self.image_reset.get_height() - 10))  # Position reset button below the grid
        
        self.timer_gui(0)
        #self.cpt_cases_mined()
        pygame.display.update()
        #pygame.display.flip()
        self.clock.tick(60)                     # limit to 60 FPS

pygame.quit()
