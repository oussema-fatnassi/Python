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
            if self.Matrice_case[co_y][co_x] == 'X':
                if self.game_lost == True:
                    self.screen.blit(self.image_bomb, ((self.MARGIN + self.WIDTH) * self.x + self.MARGIN, (self.MARGIN + self.HEIGHT) * self.y + self.MARGIN))
                    pygame.display.update()
                else:
                    self.game_over()     
            elif self.Matrice_case[co_y][co_x] == '.':
                self.verification_case(self.x,self.y) 
    
    def clique(self):                # Récupération localisation de la case
        self.pos_case()
        if self.cpt_cases_mined == 0:
            # timer() lancement du timer
            self.plant_bombs(self.y_max,self.x_max)
        else:
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
        print("Test game over")
        self.screen.blit(self.image_bomb, ((self.MARGIN + self.WIDTH) * self.x + self.MARGIN, (self.MARGIN + self.HEIGHT) * self.y + self.MARGIN))
        pygame.display.update()
        self.game_lost = True
        # for i in range(self.y_max):
        #     for j in range(self.x_max):
        #         self.check_bomb(j,i)
        #     print(self.Matrice_case[i])
        # Ça finit le jeu avec un message de défaite
        # Ça ferme la fenêtre et revient au choix de la difficulté
    
    def game_win(self):                     # Sous-programme en cas de victoire
        print("Test victoire")
        # Ça finit le jeu avec un message de victoire
        # Ça ferme la fenêtre et revient au choix de la difficulté
        pass
    
    def plant_bombs(self,y,x):                  # Sous-programme qui plante les bombes au hasard et compte les cases
        self.pos_case()
        for i in range(y):
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
        
    def bomb_or_not(self, co_x, co_y):      # Sous-programme qui permet de compter les bombes autour
        if self.Matrice_case[co_y][co_x] == 'X':
            return 1
        else:
            return 0
    
    def revele(self,co_x,co_y):
        
        cpt = 0  
        if co_x == 0 and co_y == 0:                             # Coin haut gauche
            cpt = self.bomb_or_not(co_x +1,co_y) + self.bomb_or_not(co_x +1,co_y +1) + self.bomb_or_not(co_x,co_y +1)
        elif co_x == (self.x_max -1) and co_y == 0:                 # Coin haut droit
            cpt = self.bomb_or_not(co_x -1,co_y) + self.bomb_or_not(co_x -1,co_y +1) + self.bomb_or_not(co_x,co_y +1)
        elif co_x == 0 and co_y == (self.y_max -1):                 # Coin bas gauche
            cpt = self.bomb_or_not(co_x +1,co_y) + self.bomb_or_not(co_x +1,co_y -1) + self.bomb_or_not(co_x,co_y -1)
        elif co_x == (self.x_max -1) and co_y == (self.y_max -1):       # Coin bas droit
            cpt = self.bomb_or_not(co_x -1,co_y) + self.bomb_or_not(co_x -1,co_y -1) + self.bomb_or_not(co_x,co_y -1)
        elif co_x == 0:                                         # Côté gauche de la grille
            cpt = self.bomb_or_not(co_x,co_y -1) + self.bomb_or_not(co_x +1,co_y -1) + self.bomb_or_not(co_x +1,co_y) + self.bomb_or_not(co_x +1,co_y +1) + self.bomb_or_not(co_x,co_y +1)
        elif co_y == 0:                                         # Côté haut de la grille
            cpt = self.bomb_or_not(co_x -1,co_y) + self.bomb_or_not(co_x -1,co_y +1) + self.bomb_or_not(co_x,co_y +1) + self.bomb_or_not(co_x +1,co_y +1) + self.bomb_or_not(co_x +1,co_y)
        elif co_x == (self.x_max -1):                               # Côté droit de la grille
            cpt = self.bomb_or_not(co_x,co_y -1) + self.bomb_or_not(co_x -1,co_y -1) + self.bomb_or_not(co_x -1,co_y) + self.bomb_or_not(co_x -1,co_y +1) + self.bomb_or_not(co_x,co_y +1)
        elif co_y == (self.y_max -1):                               # Côté bas de la grille
            cpt = self.bomb_or_not(co_x -1,co_y) + self.bomb_or_not(co_x -1,co_y -1) + self.bomb_or_not(co_x,co_y -1) + self.bomb_or_not(co_x +1,co_y -1) + self.bomb_or_not(co_x +1,co_y)
        else:                                                   # Case random au milieu
            cpt = self.bomb_or_not(co_x -1,co_y) + self.bomb_or_not(co_x -1,co_y -1) + self.bomb_or_not(co_x,co_y -1) + self.bomb_or_not(co_x +1,co_y -1) + self.bomb_or_not(co_x +1,co_y) + self.bomb_or_not(co_x +1,co_y +1) + self.bomb_or_not(co_x,co_y +1) + self.bomb_or_not(co_x -1,co_y +1)
        
        if cpt == 0:
            self.Matrice_case[co_y][co_x] = '0'
            self.diffusion(co_x,co_y)
        elif cpt == 1:
            self.Matrice_case[co_y][co_x] = '1'
        elif cpt == 2:
            self.Matrice_case[co_y][co_x] = '2'
        elif cpt == 3:
            self.Matrice_case[co_y][co_x] = '3'
        elif cpt == 4:
            self.Matrice_case[co_y][co_x] = '4'
        elif cpt == 5:
            self.Matrice_case[co_y][co_x] = '5'
        elif cpt == 6:
            self.Matrice_case[co_y][co_x] = '6'
        elif cpt == 7:
            self.Matrice_case[co_y][co_x] = '7'
        elif cpt == 8:
            self.Matrice_case[co_y][co_x] = '8'
    
    def diffusion(self, co_x, co_y):
        if self.Matrice_case[co_y][co_x] == '0':
            if co_x -1 >= 0:
                self.check_bomb(co_x -1, co_y)
            # if co_x -1 >= 0 and co_y -1 >= 0:
            #     self.check_bomb(co_x -1, co_y -1)
            if co_y -1 >= 0:
                self.check_bomb(co_x , co_y -1)
            # if co_x +1 >= 0 and co_y -1 >= 0:
            #     self.check_bomb(co_x +1, co_y -1)
            if co_x +1 >= 0:
                self.check_bomb(co_x +1, co_y)
            # if co_x +1 >= 0 and co_y +1 >= 0:
            #     self.check_bomb(co_x +1, co_y +1)
            if co_y +1 >= 0:
                self.check_bomb(co_x , co_y +1)
            # if co_x -1 >= 0 and co_y +1 >= 0:
            #     self.check_bomb(co_x -1, co_y +1)
        elif self.Matrice_case[co_y][co_x] == ('1' or '2' or '3' or '4' or '5' or '6' or '7' or '8' or 'X'):
            return
        else:
            self.revele(co_x,co_y)
            if self.Matrice_case[co_y][co_x] == ('1' or '2' or '3' or '4' or '5' or '6' or '7' or '8' or 'X'):
                return
            if co_x -1 >= 0:
                self.check_bomb(co_x -1, co_y)
            # if co_x -1 >= 0 and co_y -1 >= 0:
            #     self.check_bomb(co_x -1, co_y -1)
            if co_y -1 >= 0:
                self.check_bomb(co_x , co_y -1)
            # if co_x +1 >= 0 and co_y -1 >= 0:
            #     self.check_bomb(co_x +1, co_y -1)
            if co_x +1 >= 0:
                self.check_bomb(co_x +1, co_y)
            # if co_x +1 >= 0 and co_y +1 >= 0:
            #     self.check_bomb(co_x +1, co_y +1)
            if co_y +1 >= 0:
                self.check_bomb(co_x , co_y +1)
            # if co_x -1 >= 0 and co_y +1 >= 0:
            #     self.check_bomb(co_x -1, co_y +1)
    
    def verification_case(self, co_x, co_y):        # Sous-programme qui vérifie et compte les cases bombes autour avant de changer la case

        cpt = 0  
        if co_x == 0 and co_y == 0:                             # Coin haut gauche
            cpt = self.bomb_or_not(co_x +1,co_y) + self.bomb_or_not(co_x +1,co_y +1) + self.bomb_or_not(co_x,co_y +1)
        elif co_x == (self.x_max -1) and co_y == 0:                 # Coin haut droit
            cpt = self.bomb_or_not(co_x -1,co_y) + self.bomb_or_not(co_x -1,co_y +1) + self.bomb_or_not(co_x,co_y +1)
        elif co_x == 0 and co_y == (self.y_max -1):                 # Coin bas gauche
            cpt = self.bomb_or_not(co_x +1,co_y) + self.bomb_or_not(co_x +1,co_y -1) + self.bomb_or_not(co_x,co_y -1)
        elif co_x == (self.x_max -1) and co_y == (self.y_max -1):       # Coin bas droit
            cpt = self.bomb_or_not(co_x -1,co_y) + self.bomb_or_not(co_x -1,co_y -1) + self.bomb_or_not(co_x,co_y -1)
        elif co_x == 0:                                         # Côté gauche de la grille
            cpt = self.bomb_or_not(co_x,co_y -1) + self.bomb_or_not(co_x +1,co_y -1) + self.bomb_or_not(co_x +1,co_y) + self.bomb_or_not(co_x +1,co_y +1) + self.bomb_or_not(co_x,co_y +1)
        elif co_y == 0:                                         # Côté haut de la grille
            cpt = self.bomb_or_not(co_x -1,co_y) + self.bomb_or_not(co_x -1,co_y +1) + self.bomb_or_not(co_x,co_y +1) + self.bomb_or_not(co_x +1,co_y +1) + self.bomb_or_not(co_x +1,co_y)
        elif co_x == (self.x_max -1):                               # Côté droit de la grille
            cpt = self.bomb_or_not(co_x,co_y -1) + self.bomb_or_not(co_x -1,co_y -1) + self.bomb_or_not(co_x -1,co_y) + self.bomb_or_not(co_x -1,co_y +1) + self.bomb_or_not(co_x,co_y +1)
        elif co_y == (self.y_max -1):                               # Côté bas de la grille
            cpt = self.bomb_or_not(co_x -1,co_y) + self.bomb_or_not(co_x -1,co_y -1) + self.bomb_or_not(co_x,co_y -1) + self.bomb_or_not(co_x +1,co_y -1) + self.bomb_or_not(co_x +1,co_y)
        else:                                                   # Case random au milieu
            cpt = self.bomb_or_not(co_x -1,co_y) + self.bomb_or_not(co_x -1,co_y -1) + self.bomb_or_not(co_x,co_y -1) + self.bomb_or_not(co_x +1,co_y -1) + self.bomb_or_not(co_x +1,co_y) + self.bomb_or_not(co_x +1,co_y +1) + self.bomb_or_not(co_x,co_y +1) + self.bomb_or_not(co_x -1,co_y +1)
        
        if cpt == 0:                                # Si 0 bombe autour, check les cases autour
            self.Matrice_case[co_y][co_x] = '0'
            self.screen.blit(self.image_empty, ((self.MARGIN + self.WIDTH) * self.x + self.MARGIN , (self.MARGIN + self.HEIGHT) * self.y + self.MARGIN ))
            self.diffusion(co_x+1,co_y)

        elif cpt == 1:                              # Si bombe alors affiche le nombre et stop
            self.Matrice_case[co_y][co_x] = '1'
            self.screen.blit(self.image1, ((self.MARGIN + self.WIDTH) * self.x + self.MARGIN , (self.MARGIN + self.HEIGHT) * self.y + self.MARGIN ))                     
        elif cpt == 2:
            self.Matrice_case[co_y][co_x] = '2'
            self.screen.blit(self.image2, ((self.MARGIN + self.WIDTH) * self.x + self.MARGIN , (self.MARGIN + self.HEIGHT) * self.y + self.MARGIN ))                     
        elif cpt == 3:
            self.Matrice_case[co_y][co_x] = '3'
            self.screen.blit(self.image3, ((self.MARGIN + self.WIDTH) * self.x + self.MARGIN , (self.MARGIN + self.HEIGHT) * self.y + self.MARGIN ))
        elif cpt == 4:
            self.Matrice_case[co_y][co_x] = '4'
            self.screen.blit(self.image4, ((self.MARGIN + self.WIDTH) * self.x + self.MARGIN , (self.MARGIN + self.HEIGHT) * self.y + self.MARGIN ))
        elif cpt == 5:
            self.Matrice_case[co_y][co_x] = '5'
            self.screen.blit(self.image5, ((self.MARGIN + self.WIDTH) * self.x + self.MARGIN , (self.MARGIN + self.HEIGHT) * self.y + self.MARGIN ))
        elif cpt == 6:
            self.Matrice_case[co_y][co_x] = '6'
            self.screen.blit(self.image6, ((self.MARGIN + self.WIDTH) * self.x + self.MARGIN , (self.MARGIN + self.HEIGHT) * self.y + self.MARGIN ))
        elif cpt == 7:
            self.Matrice_case[co_y][co_x] = '7'
            self.screen.blit(self.image7, ((self.MARGIN + self.WIDTH) * self.x + self.MARGIN , (self.MARGIN + self.HEIGHT) * self.y + self.MARGIN ))
        elif cpt == 8:
            self.Matrice_case[co_y][co_x] = '8'
            self.screen.blit(self.image8, ((self.MARGIN + self.WIDTH) * self.x + self.MARGIN , (self.MARGIN + self.HEIGHT) * self.y + self.MARGIN )) 

        pygame.display.update()