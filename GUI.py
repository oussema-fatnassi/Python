import pygame
from pygame.locals import *

class GUI():
    
    def __init__(self):
        pygame.init()               # Initialisation pygame
        self.screen_width = 700
        self.screen_height = 700
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("MINESWEEPER")
        self.clock = pygame.time.Clock()
        self.running = True
        self.WIDTH = 30
        self.HEIGHT = 30
        self.MARGIN = 0
        self.game_lost = False
        self.x = 0           #pos x et y dans la matrice
        self.y = 0
        self.cpt_cases_mined = 0
        self.cpt_cases_demined = 0
        self.x_max = 9       #max taille difficulty
        self.y_max = 9

        self.Matrice_case = []                  # Initilisation de la matrice qui garde les valeurs des cases
        for row in range(self.y_max): 
            self.Matrice_case.append([])
            for col in range(self.x_max): 
                self.Matrice_case[row].append('')
    
    def pos_case(self):
        pos = pygame.mouse.get_pos()
        self.x = pos[0] // (self.WIDTH + self.MARGIN)
        self.y = pos[1] // (self.HEIGHT + self.MARGIN) 

    def load_images(self):                      # Sous-programme pour load les images et les scale à la bonne taille
        
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

    def init_grille(self):                             # Programme main
        
        #self.load_images()
        self.screen.fill("grey")
        for i in range(9):
            for j in range(9):
                self.screen.blit(self.image_button, ((self.MARGIN + self.WIDTH) * j + self.MARGIN , (self.MARGIN + self.HEIGHT) * i + self.MARGIN ))                     
        pygame.display.flip()
        self.clock.tick(60)                     # limit to 60 FPS
        #pygame.quit()
