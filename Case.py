import random
import pygame
from pygame.locals import *
from GUI_test import GUI
from Difficulty import Difficulty

class Case(GUI):
    
    def __init__(self, chosen_difficulty):                                          # Receive chosen difficulty level
        super().__init__()
        self.load_images()
        self.flag_var = 0
        self.question_mark_var = 0
        self.chosen_difficulty = chosen_difficulty                                  # Store chosen difficulty level
        self.init_grid()                                                            # Initialize grid based on difficulty level
    
    def init_grid(self):
        if self.chosen_difficulty == "easy":                                        # Initialize other variables for easy difficulty
            self.x_max = 9
            self.y_max = 9
            self.screen_width = 270
            self.screen_height = 330
        elif self.chosen_difficulty == "medium":                                    # Initialize other variables for medium difficulty
            self.x_max = 16
            self.y_max = 16
            self.screen_width = 480
            self.screen_height = 540
        elif self.chosen_difficulty == "hard":                                      # Initialize other variables for hard difficulty
            self.x_max = 30
            self.y_max = 16
            self.screen_width = 900
            self.screen_height = 540
        else:                                                                       # Initialize other variables for default difficulty                
            self.x_max = 9
            self.y_max = 9
            self.screen_width = 270
            self.screen_height = 330
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))  # Adjust screen size
        self.Matrice_case = []                                                          # Initialisation of the grid
        for row in range(self.y_max): 
            self.Matrice_case.append([])
            for col in range(self.x_max): 
                self.Matrice_case[row].append('')
    
    def check_bomb(self, co_x, co_y):                                                   # Function that checks if the case is a bomb or not
        if (co_x >= 0 and co_x < self.x_max) and (co_y >= 0 and co_y < self.y_max):
            if self.Matrice_case[co_y][co_x] == 'X':                                    # If it is a bomb then game over
                self.Matrice_case[co_y][co_x] = 'x'
                self.game_over()
            else:
                if self.Matrice_case[co_y][co_x] != '0':                                # If the case has any value other than 0 it will show the image of that value
                    self.show(co_x,co_y)
                    self.Matrice_case[co_y][co_x] = '9'
                else:
                    self.recursivity(co_x,co_y)                                         # If the value is 0 then it launches the function recursivity

    def check_victory(self):                                                            # Function that checks if the player has won
        cpt_cases = 0
        for i in range(self.y_max):
            for j in range(self.x_max):
                if self.Matrice_case[i][j] == '9':
                    cpt_cases += 1
        if cpt_cases == self.cpt_cases_demined:                                         # If the number of cases discovered is equal to the number of cases without bomb then the player wins
            self.game_win()
    
    def clique(self):                               # Function for each left click
        self.pos_case()
        if self.cpt_cases_mined == 0:               # Case for the first click
            self.plant_bombs(self.y_max,self.x_max)
        else:                                       # Case for others clicks
            if self.WIN == True or self.GAME_OVER == True:
                self.WIN = False
                self.GAME_OVER = False
                self.reset_game()
            else:
                self.check_victory()
                self.check_bomb(self.x,self.y)
    
    def flag(self):
        self.pos_case()
        # Check if the case already has a flag or question mark
        if self.Matrice_case[self.y][self.x] in ['F0','F1','F2','F3','F4','F5','F6','F7','F8','FX','?0','?1','?2','?3','?4','?5','?6','?7','?8','?X']:
            if self.Matrice_case[self.y][self.x] in ['F0','F1','F2','F3','F4','F5','F6','F7','F8','FX']:  # If it's a flag, change to question mark
                if self.Matrice_case[self.y][self.x] == 'F0':
                    self.Matrice_case[self.y][self.x] = '?0'
                elif self.Matrice_case[self.y][self.x] == 'F1':
                    self.Matrice_case[self.y][self.x] = '?1'
                elif self.Matrice_case[self.y][self.x] == 'F2':
                    self.Matrice_case[self.y][self.x] = '?2'
                elif self.Matrice_case[self.y][self.x] == 'F3':
                    self.Matrice_case[self.y][self.x] = '?3'
                elif self.Matrice_case[self.y][self.x] == 'F4':
                    self.Matrice_case[self.y][self.x] = '?4'
                elif self.Matrice_case[self.y][self.x] == 'F5':
                    self.Matrice_case[self.y][self.x] = '?5'
                elif self.Matrice_case[self.y][self.x] == 'F6':
                    self.Matrice_case[self.y][self.x] = '?6'
                elif self.Matrice_case[self.y][self.x] == 'F7':
                    self.Matrice_case[self.y][self.x] = '?7'
                elif self.Matrice_case[self.y][self.x] == 'F8':
                    self.Matrice_case[self.y][self.x] = '?8'
                elif self.Matrice_case[self.y][self.x] == 'FX':
                    self.Matrice_case[self.y][self.x] = '?X'
                self.screen.blit(self.image_question_mark, ((self.MARGIN + self.WIDTH) * self.x + self.MARGIN, (self.MARGIN + self.HEIGHT) * self.y + self.MARGIN))
                pygame.display.update()
            else:  # If it's a question mark, change to button
                if self.Matrice_case[self.y][self.x] == '?0':
                    self.Matrice_case[self.y][self.x] = '0'
                elif self.Matrice_case[self.y][self.x] == '?1':
                    self.Matrice_case[self.y][self.x] = '1'
                elif self.Matrice_case[self.y][self.x] == '?2':
                    self.Matrice_case[self.y][self.x] = '2'
                elif self.Matrice_case[self.y][self.x] == '?3':
                    self.Matrice_case[self.y][self.x] = '3'
                elif self.Matrice_case[self.y][self.x] == '?4':
                    self.Matrice_case[self.y][self.x] = '4'
                elif self.Matrice_case[self.y][self.x] == '?5':
                    self.Matrice_case[self.y][self.x] = '5'
                elif self.Matrice_case[self.y][self.x] == '?6':
                    self.Matrice_case[self.y][self.x] = '6'
                elif self.Matrice_case[self.y][self.x] == '?7':
                    self.Matrice_case[self.y][self.x] = '7'
                elif self.Matrice_case[self.y][self.x] == '?8':
                    self.Matrice_case[self.y][self.x] = '8'
                elif self.Matrice_case[self.y][self.x] == '?X':
                    self.Matrice_case[self.y][self.x] = 'X'
                self.screen.blit(self.image_button, ((self.MARGIN + self.WIDTH) * self.x + self.MARGIN, (self.MARGIN + self.HEIGHT) * self.y + self.MARGIN))
                pygame.display.update()
        elif self.Matrice_case[self.y][self.x] in ['0','1','2','3','4','5','6','7','8','X']:  # If the case has no flag or question mark
            if self.Matrice_case[self.y][self.x] == '0':
                self.Matrice_case[self.y][self.x] = 'F0'
            elif self.Matrice_case[self.y][self.x] == '1':
                self.Matrice_case[self.y][self.x] = 'F1'
            elif self.Matrice_case[self.y][self.x] == '2':
                self.Matrice_case[self.y][self.x] = 'F2'
            elif self.Matrice_case[self.y][self.x] == '3':
                self.Matrice_case[self.y][self.x] = 'F3'
            elif self.Matrice_case[self.y][self.x] == '4':
                self.Matrice_case[self.y][self.x] = 'F4'
            elif self.Matrice_case[self.y][self.x] == '5':
                self.Matrice_case[self.y][self.x] = 'F5'
            elif self.Matrice_case[self.y][self.x] == '6':
                self.Matrice_case[self.y][self.x] = 'F6'
            elif self.Matrice_case[self.y][self.x] == '7':
                self.Matrice_case[self.y][self.x] = 'F7'
            elif self.Matrice_case[self.y][self.x] == '8':
                self.Matrice_case[self.y][self.x] = 'F8'
            elif self.Matrice_case[self.y][self.x] == 'X':
                self.Matrice_case[self.y][self.x] = 'FX'
            self.screen.blit(self.image_flag, ((self.MARGIN + self.WIDTH) * self.x + self.MARGIN, (self.MARGIN + self.HEIGHT) * self.y + self.MARGIN))
            pygame.display.update()

    def game_over(self):                            # Function in case of defeat
        self.screen.blit(self.image_final_bomb, ((self.MARGIN + self.WIDTH) * self.x + self.MARGIN, (self.MARGIN + self.HEIGHT) * self.y + self.MARGIN))
        pygame.display.update()
        for i in range(self.y_max):
            for j in range(self.x_max):
                if self.Matrice_case[i][j] == 'X':
                    self.show(j,i)
        self.GAME_OVER = True                       # When the game is over it shows all the bombs and the player can't play anymore

    def game_win(self):                             # Function in case of victory
        self.WIN = True                             # When the player wins he can't play anymore
   
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
        self.check_victory()
                        
    def show(self,x,y):                             # Function to show an image corresponding to the value of the chosen case
        a = self.Matrice_case[y][x]
        if a == ('0' or 'F0' or '?0'):
            self.screen.blit(self.image_empty, ((self.MARGIN + self.WIDTH) * x + self.MARGIN , (self.MARGIN + self.HEIGHT) * y + self.MARGIN ))
        elif a == ('1' or 'F1' or '?1'):
            self.screen.blit(self.image1, ((self.MARGIN + self.WIDTH) * x + self.MARGIN , (self.MARGIN + self.HEIGHT) * y + self.MARGIN ))
        elif a == ('2' or 'F2' or '?2'):
            self.screen.blit(self.image2, ((self.MARGIN + self.WIDTH) * x + self.MARGIN , (self.MARGIN + self.HEIGHT) * y + self.MARGIN ))
        elif a == ('3' or 'F3' or '?3'):
            self.screen.blit(self.image3, ((self.MARGIN + self.WIDTH) * x + self.MARGIN , (self.MARGIN + self.HEIGHT) * y + self.MARGIN ))
        elif a == ('4' or 'F4' or '?4'):
            self.screen.blit(self.image4, ((self.MARGIN + self.WIDTH) * x + self.MARGIN , (self.MARGIN + self.HEIGHT) * y + self.MARGIN ))
        elif a == ('5' or 'F5' or '?5'):
            self.screen.blit(self.image5, ((self.MARGIN + self.WIDTH) * x + self.MARGIN , (self.MARGIN + self.HEIGHT) * y + self.MARGIN ))
        elif a == ('6' or 'F6' or '?6'):
            self.screen.blit(self.image6, ((self.MARGIN + self.WIDTH) * x + self.MARGIN , (self.MARGIN + self.HEIGHT) * y + self.MARGIN ))
        elif a == ('7' or 'F7' or '?7'):
            self.screen.blit(self.image7, ((self.MARGIN + self.WIDTH) * x + self.MARGIN , (self.MARGIN + self.HEIGHT) * y + self.MARGIN ))
        elif a == ('8' or 'F8' or '?8'):
            self.screen.blit(self.image8, ((self.MARGIN + self.WIDTH) * x + self.MARGIN , (self.MARGIN + self.HEIGHT) * y + self.MARGIN ))
        elif a == ('X' or 'FX' or '?X'):
            self.screen.blit(self.image_bomb, ((self.MARGIN + self.WIDTH) * x + self.MARGIN , (self.MARGIN + self.HEIGHT) * y + self.MARGIN ))
        elif a == '9':
            pass
        self.Matrice_case[y][x] = '9'
        pygame.display.update()                     # Update the gird for the visual