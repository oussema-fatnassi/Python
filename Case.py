import random
import pygame
from pygame.locals import *


class Case():
    
    def __init__(self):
        self.flag_var = 0
        self.question_mark_var = 0
    
    def check_bomb(self, co_x, co_y):       # Sous-programme qui check si la case est une bombe
        if self.dict_cases[(co_x,co_y)] == 'X':
            self.game_over()     
        elif self.dict_cases[(co_x,co_y)] == '.':
            self.verification_case  
    
    def clique(self, event):                # Récupération localisation de la case
        print("Case cliquée : ",event.num)
        if self.cpt_cases_mined == 0:
            # timer() lancement du timer
            self.plant_bombs()
        else:
            self.check_bomb()
    
    def flag(self, event):                  # Sous-programme drapeau si clique droit ou '?' si déjà un drapeau
        print("Test clique droit",event.num)
        if self.flag_var == 0:
            self.screen.blit(self.image_flag, ((self.MARGIN + self.WIDTH) * self.x + self.MARGIN, (self.MARGIN + self.HEIGHT) * self.y + self.MARGIN))
            print("Test drapeau affiché")
            self.flag_var = 1
        elif self.flag_var == 1:
            self.question_mark()
    
    def game_over(self):                    # Sous-programme en cas de défaite
        print("Test game over")
        # Ça finit le jeu avec un message de défaite
        # Ça ferme la fenêtre et revient au choix de la difficulté
        pass
    
    def game_win(self):                     # Sous-programme en cas de victoire
        print("Test victoire")
        # Ça finit le jeu avec un message de victoire
        # Ça ferme la fenêtre et revient au choix de la difficulté
        pass
    
    def plant_bombs(self):                  # Sous-programme qui plante les bombes au hasard et compte les cases
        for i in range(self.y):
            for j in range(self.x):
                a = random.randint(0,100)
                if a <= 15:
                    print("BOMBE")
                    self.dict_cases[(i,j)] = 'X'
                    self.cpt_cases_mined += 1
                elif a > 15:
                    print("PAS DE BOMBE")
                    self.dict_cases[(i,j)] = '.'
                    self.cpt_cases_demined += 1
            print(self.dict_cases[(i,j)])
    
    def question_mark(self):                # Sous-programme qui affiche '?' ou rien si déjà '?'
        print("Test arrivée sur ?")
        if self.question_mark_var == 0:
            self.screen.blit(self.image_question_mark, ((self.MARGIN + self.WIDTH) * self.x + self.MARGIN, (self.MARGIN + self.HEIGHT) * self.y + self.MARGIN))
            print("Test affichage ?")
            self.question_mark_var = 1
        elif self.question_mark_var == 1:
            self.screen.blit(self.image_button, ((self.MARGIN + self.WIDTH) * self.x + self.MARGIN, (self.MARGIN + self.HEIGHT) * self.y + self.MARGIN))
            print("Retour affichage vide")
            self.flag_var = 0
            self.question_mark_var = 0
    
    def set_flag(self, a):
        self.flag_var = a
    
    def set_question(self, a):
        self.question_mark_var = a
        
    def bomb_or_not(self, co_x, co_y):      # Sous-programme qui permet de compter les bombes autour
        if self.dict_cases[(co_x,co_y)] == 'X':
            return 1
        else:
            return 0
    
    def verification_case(self, co_x, co_y):        # Sous-programme qui vérifie et compte les cases bombes autour avant de changer la case
        cpt = 0
        if co_x == 0 and co_y == 0:                             # Coin haut gauche
            cpt = self.bomb_or_not(co_x +1,co_y) + self.bomb_or_not(co_x +1,co_y +1) + self.bomb_or_not(co_x,co_y +1)
        elif co_x == (self.x -1) and co_y == 0:                 # Coin haut droit
            cpt = self.bomb_or_not(co_x -1,co_y) + self.bomb_or_not(co_x -1,co_y +1) + self.bomb_or_not(co_x,co_y +1)
        elif co_x == 0 and co_y == (self.y -1):                 # Coin bas gauche
            cpt = self.bomb_or_not(co_x +1,co_y) + self.bomb_or_not(co_x +1,co_y -1) + self.bomb_or_not(co_x,co_y -1)
        elif co_x == (self.x -1) and co_y == (self.y -1):       # Coin bas droit
            cpt = self.bomb_or_not(co_x -1,co_y) + self.bomb_or_not(co_x -1,co_y -1) + self.bomb_or_not(co_x,co_y -1)
        elif co_x == 0:                                         # Côté gauche de la grille
            cpt = self.bomb_or_not(co_x,co_y -1) + self.bomb_or_not(co_x +1,co_y -1) + self.bomb_or_not(co_x +1,co_y)
            + self.bomb_or_not(co_x +1,co_y +1) + self.bomb_or_not(co_x,co_y +1)
        elif co_y == 0:                                         # Côté haut de la grille
            cpt = self.bomb_or_not(co_x -1,co_y) + self.bomb_or_not(co_x -1,co_y +1) + self.bomb_or_not(co_x,co_y +1)
            + self.bomb_or_not(co_x +1,co_y +1) + self.bomb_or_not(co_x +1,co_y)
        elif co_x == (self.x -1):                               # Côté droit de la grille
            cpt = self.bomb_or_not(co_x,co_y -1) + self.bomb_or_not(co_x -1,co_y -1) + self.bomb_or_not(co_x -1,co_y)
            + self.bomb_or_not(co_x -1,co_y +1) + self.bomb_or_not(co_x,co_y +1)
        elif co_y == (self.y -1):                               # Côté bas de la grille
            cpt = self.bomb_or_not(co_x -1,co_y) + self.bomb_or_not(co_x -1,co_y -1) + self.bomb_or_not(co_x,co_y -1)
            + self.bomb_or_not(co_x +1,co_y -1) + self.bomb_or_not(co_x +1,co_y)
        else:                                                   # Case random au milieu
            cpt = self.bomb_or_not(co_x -1,co_y) + self.bomb_or_not(co_x -1,co_y -1) + self.bomb_or_not(co_x,co_y -1) + self.bomb_or_not(co_x +1,co_y -1)
            + self.bomb_or_not(co_x +1,co_y) + self.bomb_or_not(co_x +1,co_y +1) + self.bomb_or_not(co_x,co_y +1) + self.bomb_or_not(co_x -1,co_y +1)
        
        if cpt == 0:                                # Si 0 bombe autour, check les cases autour
            self.dict_cases[(co_x,co_y)] = '0'
            self.check_bomb(co_x -1,co_y)
            self.check_bomb(co_x -1,co_y -1)
            self.check_bomb(co_x,co_y -1)
            self.check_bomb(co_x +1,co_y -1)
            self.check_bomb(co_x +1,co_y)
            self.check_bomb(co_x +1,co_y +1)
            self.check_bomb(co_x,co_y +1)
            self.check_bomb(co_x -1,co_y +1)
        elif cpt == 1:                              # Si bombe alors affiche le nombre et stop
            self.dict_cases[(co_x,co_y)] = '1'
        elif cpt == 2:
            self.dict_cases[(co_x,co_y)] = '2'
        elif cpt == 3:
            self.dict_cases[(co_x,co_y)] = '3'
        elif cpt == 4:
            self.dict_cases[(co_x,co_y)] = '4'
        elif cpt == 5:
            self.dict_cases[(co_x,co_y)] = '5'
        elif cpt == 6:
            self.dict_cases[(co_x,co_y)] = '6'
        elif cpt == 7:
            self.dict_cases[(co_x,co_y)] = '7'
        elif cpt == 8:
            self.dict_cases[(co_x,co_y)] = '8'           