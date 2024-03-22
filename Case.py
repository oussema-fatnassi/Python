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
    
    def check_bomb(self, co_x, co_y):       # Sous-programme qui check si la case est une bombe
        if (co_x >= 0 and co_x < self.x_max) and (co_y >= 0 and co_y < self.y_max):
            if self.Matrice_case[co_y][co_x] == 'X':        # Si bombe -> game over
                self.Matrice_case[co_y][co_x] = 'x'
                self.game_over()
            else:
                if self.Matrice_case[co_y][co_x] != '0':    # Si case non vide alors elle est affichée
                    self.affichage(co_x,co_y)
                    self.Matrice_case[co_y][co_x] = '9'
                else:
                    self.recursive(co_x,co_y)               # Si case 0 alors fonction récursive
                    
    def recursive(self,co_x,co_y):          # Sous-programme récursif
        self.affichage(co_x,co_y)
        neighbors = [(co_x-1,co_y),(co_x+1,co_y),(co_x,co_y-1),(co_x,co_y+1),(co_x-1,co_y-1),(co_x-1,co_y+1),(co_x+1,co_y-1),(co_x+1,co_y+1)]
        for neighbor_x, neighbor_y in neighbors:
                if 0 <= neighbor_x < self.x_max and 0 <= neighbor_y < self.y_max:
                    if self.Matrice_case[neighbor_y][neighbor_x] != '0':
                        self.affichage(neighbor_x,neighbor_y)
                    elif self.Matrice_case[neighbor_y][neighbor_x] == '0':
                        if self.Matrice_case[co_y][co_x] == '0':
                            self.Matrice_case[co_y][co_x] = '9'
                        self.recursive(neighbor_x,neighbor_y)
    
    def clique(self):                # Récupération localisation de la case
        self.pos_case()
        if self.cpt_cases_mined == 0:       # Cas du premier clic
            self.plant_bombs(self.y_max,self.x_max)
        else:                               # Les autres clics
            self.check_bomb(self.x,self.y)
    
    def flag(self):                  # Sous-programme drapeau si clique droit ou '?' si déjà un drapeau
        self.pos_case()
        if self.Matrice_case[self.y][self.x] == '.' or self.Matrice_case[self.y][self.x] == 'X':
            if self.flag_var == 0:
                self.screen.blit(self.image_flag, ((self.MARGIN + self.WIDTH) * self.x + self.MARGIN, (self.MARGIN + self.HEIGHT) * self.y + self.MARGIN))
                pygame.display.update()
                self.flag_var = 1
            elif self.flag_var == 1:
                self.question_mark()
    
    def game_over(self):                    # Sous-programme en cas de défaite
        self.screen.blit(self.image_final_bomb, ((self.MARGIN + self.WIDTH) * self.x + self.MARGIN, (self.MARGIN + self.HEIGHT) * self.y + self.MARGIN))
        pygame.display.update()
        self.game_lost = True
        for i in range(self.y_max):
            for j in range(self.x_max):
                if self.Matrice_case[i][j] == 'X':
                    self.affichage(j,i)

    def game_win(self):                     # Sous-programme en cas de victoire
        print("Test victoire")
        # Ça finit le jeu avec un message de victoire
        # Ça ferme la fenêtre et revient au choix de la difficulté
        pass
    
    def plant_bombs(self,y,x):                  # Sous-programme qui plante les bombes au hasard et compte les cases
        self.pos_case()
        for i in range(y):                      # Rempli la matrice de X pour les bombes et . pour les cases non calculées
            for j in range(x):
                a = random.randint(0,100)
                if i == self.y and j == self.x:
                    self.Matrice_case[i][j] = '.'
                elif a <= 20:
                    self.Matrice_case[i][j] = 'X'
                    self.cpt_cases_mined += 1
                elif a > 20:
                    self.Matrice_case[i][j] = '.'
                    self.cpt_cases_demined += 1
            print(self.Matrice_case[i])
        for i in range(y):                      # Récupère les voisins de chaque case
            for j in range(x):
                neighbors = [(j-1,i),(j+1,i),(j,i-1),(j,i+1),(j-1,i-1),(j-1,i+1),(j+1,i-1),(j+1,i+1)]
                cpt = 0
                if self.Matrice_case[i][j] == 'X':
                    pass
                else:
                    for neighbor_x, neighbor_y in neighbors:        # Remplace les . par la valeur des cases autour
                        if 0 <= neighbor_x < self.x_max and 0 <= neighbor_y < self.y_max:
                            if self.Matrice_case[neighbor_y][neighbor_x] == 'X':
                                cpt += 1
                    self.Matrice_case[i][j] = str(cpt)
            print(self.Matrice_case[i])        
        self.check_bomb(self.x,self.y)
    
    def question_mark(self):                # Sous-programme qui affiche '?' ou rien si déjà '?'
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
             
    def affichage(self,x,y):                # Sous-programme qui affiche la case en fonction de sa valeur
        a = self.Matrice_case[y][x]
        if a == '0':
            self.screen.blit(self.image_empty, ((self.MARGIN + self.WIDTH) * x + self.MARGIN , (self.MARGIN + self.HEIGHT) * y + self.MARGIN ))
        elif a == '1':
            self.screen.blit(self.image1, ((self.MARGIN + self.WIDTH) * x + self.MARGIN , (self.MARGIN + self.HEIGHT) * y + self.MARGIN )) 
        elif a == '2':
            self.screen.blit(self.image2, ((self.MARGIN + self.WIDTH) * x + self.MARGIN , (self.MARGIN + self.HEIGHT) * y + self.MARGIN )) 
        elif a == '3':
            self.screen.blit(self.image3, ((self.MARGIN + self.WIDTH) * x + self.MARGIN , (self.MARGIN + self.HEIGHT) * y + self.MARGIN )) 
        elif a == '4':
            self.screen.blit(self.image4, ((self.MARGIN + self.WIDTH) * x + self.MARGIN , (self.MARGIN + self.HEIGHT) * y + self.MARGIN )) 
        elif a == '5':
            self.screen.blit(self.image5, ((self.MARGIN + self.WIDTH) * x + self.MARGIN , (self.MARGIN + self.HEIGHT) * y + self.MARGIN ))
        elif a == '6':
            self.screen.blit(self.image6, ((self.MARGIN + self.WIDTH) * x + self.MARGIN , (self.MARGIN + self.HEIGHT) * y + self.MARGIN ))
        elif a == '7':
            self.screen.blit(self.image7, ((self.MARGIN + self.WIDTH) * x + self.MARGIN , (self.MARGIN + self.HEIGHT) * y + self.MARGIN ))
        elif a == '8':
            self.screen.blit(self.image8, ((self.MARGIN + self.WIDTH) * x + self.MARGIN , (self.MARGIN + self.HEIGHT) * y + self.MARGIN ))
        elif a == 'X':
            self.screen.blit(self.image_bomb, ((self.MARGIN + self.WIDTH) * x + self.MARGIN , (self.MARGIN + self.HEIGHT) * y + self.MARGIN ))
        pygame.display.update()