from GUI_test import GUI
from Case import Case
from Difficulty import Difficulty
import sys

import random
import pygame
from pygame.locals import *


def main(GUI, difficulty_choice):
    case_instance = Case()
    GUI.init_grille(difficulty_choice)
    timer_started = False
    start_timer = 0

    while GUI.running:
        GUI.pos_case()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                GUI.running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:           # Left click
                    pos = pygame.mouse.get_pos()                                                              # Récupère la position du clique
                    if GUI.x >= 0 and GUI.x < GUI.x_max and GUI.y >= 0 and GUI.y < GUI.y_max:                 # Check position mouse dans la grille
                        print("Left Click ", pos, "Matrice_case coordinates: ", GUI.x, GUI.y)
                        #GUI.pos_case()
                        case_instance.clique()
                        #GUI_test.cpt_cases_mined(case_instance.number_of_bombs)
                        if not timer_started:
                            start_timer = pygame.time.get_ticks()
                            timer_started = True         
                    else:
                        break
                    
                elif event.button == 3:         # Right click
                    pos = pygame.mouse.get_pos()
                    
                    if GUI.x >= 0 and GUI.x < GUI.x_max and GUI.y >= 0 and GUI.y < GUI.y_max:
                        print("Right click", pos, "Matrice_case coordinates", GUI.x, GUI.y)
                        case_instance.flag()
                    else:
                        break
    
            if timer_started:
                        elapsed_time = pygame.time.get_ticks() - start_timer
                        GUI_test.timer_gui(elapsed_time)


    pygame.display.flip()
    pygame.quit()

Difficulty_instance = Difficulty()
Difficulty_instance.main_menu()
#print("im in difficulty")
#print(Difficulty_instance.difficulty_choice)
GUI_test = GUI()
GUI_test.load_images()
main(GUI_test, Difficulty_instance.difficulty_choice)