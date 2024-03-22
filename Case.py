import random
import pygame
from pygame.locals import *
from GUI import GUI

class Case(GUI):
    
    def __init__(self):
        super().__init__()
        self.load_images()
        self.flag_var = 0
        self.question_mark_var = 0
    
    def check_bomb(self, co_x, co_y):                       # Function that checks if the case is a bomb or not
        if (co_x >= 0 and co_x < self.x_max) and (co_y >= 0 and co_y < self.y_max):
            if self.Matrice_case[co_y][co_x] == 'X':        # If it is a bomb then game over
                self.Matrice_case[co_y][co_x] = 'x'
                self.game_over()
            else:
                if self.Matrice_case[co_y][co_x] != '0':    # If the case has any value other than 0 it will show the image of that value
                    self.show(co_x,co_y)
                    self.Matrice_case[co_y][co_x] = '9'
                else:
                    self.recursivity(co_x,co_y)             # If the value is 0 then it launches the function recursivity

    def clique(self):                               # Function for each left click
        self.pos_case()
        if self.cpt_cases_mined == 0:       # Case for the first click
            self.plant_bombs(self.y_max,self.x_max)
        else:                               # Case for others clicks
            self.check_bomb(self.x,self.y)
    
    def flag(self):                                 # Function to check if there is a flag/question mark or not and then show it
        self.pos_case()
        if self.Matrice_case[self.y][self.x] == ('0' or '1' or '2' or '3' or '4' or '5' or '6' or '7' or '8' or 'X'):
            if self.flag_var == 0:
                self.screen.blit(self.image_flag, ((self.MARGIN + self.WIDTH) * self.x + self.MARGIN, (self.MARGIN + self.HEIGHT) * self.y + self.MARGIN))
                pygame.display.update()
                self.flag_var = 1
            elif self.flag_var == 1:
                self.question_mark()
    
    def game_over(self):                            # Function in case of defeat
        self.screen.blit(self.image_final_bomb, ((self.MARGIN + self.WIDTH) * self.x + self.MARGIN, (self.MARGIN + self.HEIGHT) * self.y + self.MARGIN))
        pygame.display.update()
        self.game_lost = True                       # When the game is over it shows all the bombs
        for i in range(self.y_max):
            for j in range(self.x_max):
                if self.Matrice_case[i][j] == 'X':
                    self.show(j,i)

    def game_win(self):                             # Function in case of victory
        print("Test victoire")
        # Ça finit le jeu avec un message de victoire
        # Ça ferme la fenêtre et revient au choix de la difficulté
    
    def plant_bombs(self,y,x):                      # Function to plant the bombs at the beginning
        self.pos_case()
        for i in range(y):                          # It put a value of '.' or 'X' in all the cases
            for j in range(x):
                a = random.randint(0,100)
                if i == self.y and j == self.x:     # Exception for the first case clicked
                    self.Matrice_case[i][j] = '.'
                elif a <= 20:
                    self.Matrice_case[i][j] = 'X'   # 'X' for a bomb case
                    self.cpt_cases_mined += 1
                elif a > 20:
                    self.Matrice_case[i][j] = '.'   # '.' for a case without bomb
                    self.cpt_cases_demined += 1
        for i in range(y):                          # Takes all the surroundings cases for each case
            for j in range(x):
                neighbors = [(j-1,i),(j+1,i),(j,i-1),(j,i+1),(j-1,i-1),(j-1,i+1),(j+1,i-1),(j+1,i+1)]
                cpt = 0
                if self.Matrice_case[i][j] == 'X':
                    pass
                else:                               # For each case count the bombs in the surroundings cases and put this value inside that case
                    for neighbor_x, neighbor_y in neighbors:
                        if 0 <= neighbor_x < self.x_max and 0 <= neighbor_y < self.y_max:
                            if self.Matrice_case[neighbor_y][neighbor_x] == 'X':
                                cpt += 1
                    self.Matrice_case[i][j] = str(cpt)
            print(self.Matrice_case[i])             # Cheating print to have the solution
        self.check_bomb(self.x,self.y)              # Check the first case
    
    def question_mark(self):                        # Function to show a question mark if there is already a flag
        self.pos_case()
        if self.Matrice_case[self.y][self.x] == '.' or self.Matrice_case[self.y][self.x] == 'X':
            if self.question_mark_var == 0:
                self.screen.blit(self.image_question_mark, ((self.MARGIN + self.WIDTH) * self.x + self.MARGIN, (self.MARGIN + self.HEIGHT) * self.y + self.MARGIN))
                pygame.display.update()
                self.question_mark_var = 1
            elif self.question_mark_var == 1:
                self.screen.blit(self.image_button, ((self.MARGIN + self.WIDTH) * self.x + self.MARGIN, (self.MARGIN + self.HEIGHT) * self.y + self.MARGIN))
                pygame.display.update()
                self.flag_var = 0
                self.question_mark_var = 0
             
    def recursivity(self,co_x,co_y):                # Function for recursivity
        self.show(co_x,co_y)
        neighbors = [(co_x-1,co_y),(co_x+1,co_y),(co_x,co_y-1),(co_x,co_y+1),(co_x-1,co_y-1),(co_x-1,co_y+1),(co_x+1,co_y-1),(co_x+1,co_y+1)]
        for neighbor_x, neighbor_y in neighbors:
                if 0 <= neighbor_x < self.x_max and 0 <= neighbor_y < self.y_max:
                    if self.Matrice_case[neighbor_y][neighbor_x] != '0':
                        self.show(neighbor_x,neighbor_y)
                    elif self.Matrice_case[neighbor_y][neighbor_x] == '0':
                        if self.Matrice_case[co_y][co_x] == '0':
                            self.Matrice_case[co_y][co_x] = '9'
                        self.recursivity(neighbor_x,neighbor_y)
                        
    def show(self,x,y):                             # Function to show an image corresponding to the value of the chosen case
        a = self.Matrice_case[y][x]
        if a == '0':
            self.screen.blit(self.image_empty, ((self.MARGIN + self.WIDTH) * x + self.MARGIN , (self.MARGIN + self.HEIGHT) * y + self.MARGIN ))
            self.cpt_cases_demined -= 1
        elif a == '1':
            self.screen.blit(self.image1, ((self.MARGIN + self.WIDTH) * x + self.MARGIN , (self.MARGIN + self.HEIGHT) * y + self.MARGIN ))
            self.cpt_cases_demined -= 1
        elif a == '2':
            self.screen.blit(self.image2, ((self.MARGIN + self.WIDTH) * x + self.MARGIN , (self.MARGIN + self.HEIGHT) * y + self.MARGIN ))
            self.cpt_cases_demined -= 1
        elif a == '3':
            self.screen.blit(self.image3, ((self.MARGIN + self.WIDTH) * x + self.MARGIN , (self.MARGIN + self.HEIGHT) * y + self.MARGIN ))
            self.cpt_cases_demined -= 1
        elif a == '4':
            self.screen.blit(self.image4, ((self.MARGIN + self.WIDTH) * x + self.MARGIN , (self.MARGIN + self.HEIGHT) * y + self.MARGIN ))
            self.cpt_cases_demined -= 1
        elif a == '5':
            self.screen.blit(self.image5, ((self.MARGIN + self.WIDTH) * x + self.MARGIN , (self.MARGIN + self.HEIGHT) * y + self.MARGIN ))
            self.cpt_cases_demined -= 1
        elif a == '6':
            self.screen.blit(self.image6, ((self.MARGIN + self.WIDTH) * x + self.MARGIN , (self.MARGIN + self.HEIGHT) * y + self.MARGIN ))
            self.cpt_cases_demined -= 1
        elif a == '7':
            self.screen.blit(self.image7, ((self.MARGIN + self.WIDTH) * x + self.MARGIN , (self.MARGIN + self.HEIGHT) * y + self.MARGIN ))
            self.cpt_cases_demined -= 1
        elif a == '8':
            self.screen.blit(self.image8, ((self.MARGIN + self.WIDTH) * x + self.MARGIN , (self.MARGIN + self.HEIGHT) * y + self.MARGIN ))
        elif a == 'X':
            self.screen.blit(self.image_bomb, ((self.MARGIN + self.WIDTH) * x + self.MARGIN , (self.MARGIN + self.HEIGHT) * y + self.MARGIN ))
        elif a == '9':
            self.cpt_cases_demined += 1
        pygame.display.update()                     # Update the gird for the visual
        print(self.cpt_cases_demined)
        if self.cpt_cases_demined == 0:
            self.game_win()