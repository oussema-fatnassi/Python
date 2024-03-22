from GUI_test import GUI
from Case import Case
from Difficulty import Difficulty
import sys
import time

import random
import pygame
from pygame.locals import *


def main(GUI, chosen_difficulty):
    case_instance = Case()
    GUI.init_grille(chosen_difficulty)
    timer_started = False
    start_timer = 0

    while GUI.running:
        GUI.pos_case()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                GUI.running = False
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1 and not timer_started:                                     # Left click and timer not started
                    if GUI.x >= 0 and GUI.x < GUI.x_max and GUI.y >= 0 and GUI.y < GUI.y_max:
                        case_instance.clique()
                        GUI.running = True
                        start_timer = pygame.time.get_ticks()
                        timer_started = True                                                    # Set timer_started to True
                    else:
                        break
                elif event.button == 1 and timer_started:                                       # Left click and timer started
                    if GUI.x >= 0 and GUI.x < GUI.x_max and GUI.y >= 0 and GUI.y < GUI.y_max:
                        case_instance.clique()
                    else:
                        break
                elif event.button == 3:  # Right click
                    if GUI.x >= 0 and GUI.x < GUI.x_max and GUI.y >= 0 and GUI.y < GUI.y_max:
                        case_instance.flag()
                    else:
                        break
                                                                                            
        timer_rect = pygame.Rect((GUI.screen_width - 85, GUI.screen_height - 55, 85, 50))     # Clear only the portion of the screen where the timer is displayed
        GUI.screen.fill((0, 0, 0), timer_rect)

        if timer_started:                                                                       # Only update timer if it has started
            passed_time = pygame.time.get_ticks() - start_timer
            GUI.timer_gui(passed_time)
        else:
            GUI.timer_gui(0)                                                                    # Display "000" before the first click
        pygame.display.flip()
    pygame.quit()

Difficulty_instance = Difficulty()
Difficulty_instance.main_menu()
GUI_test = GUI()
GUI_test.load_images()
main(GUI_test,Difficulty_instance.difficulty_choice)
