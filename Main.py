from GUI import GUI
from Case import Case
from Difficulty import Difficulty
import sys
import time

import random
import pygame
from pygame.locals import *


def main(GUI, chosen_difficulty):                                                               # Main function
    case_instance = Case(chosen_difficulty)
    GUI.init_grid(chosen_difficulty)
    timer_started = False
    start_timer = 0
    bomb_count = 0

    while GUI.running :                                                                         # Main loop
        GUI.pos_case()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                GUI.running = False
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:                  
                if event.button == 1 and not timer_started:
                    if GUI.x >= 0 and GUI.x < GUI.x_max and GUI.y >= 0 and GUI.y < GUI.y_max:   # If the click is in the grid we update the bomb count and start the timer 
                        case_instance.clique()
                        bomb_count = case_instance.count_bombs()
                        GUI.update_bomb_count(bomb_count)                                       # Update bomb count display
                        GUI.running = True
                        start_timer = pygame.time.get_ticks()
                        timer_started = True
                    else:
                        break
                elif event.button == 1 and timer_started:                                       # If the timer is started we can click on the reset button
                    if GUI.x >= 0 and GUI.x < GUI.x_max and GUI.y >= 0 and GUI.y < GUI.y_max:
                        case_instance.clique()
                    elif GUI.reset_button.collidepoint(pygame.mouse.get_pos()):
                        case_instance.reset_game()
                        timer_started = False 
                    else:
                        break
                elif event.button == 3:  # Right click
                    if GUI.x >= 0 and GUI.x < GUI.x_max and GUI.y >= 0 and GUI.y < GUI.y_max:   # If the click is in the grid we update the bomb count display
                        case_instance.flag()
                        bomb_count = case_instance.count_bombs()
                        GUI.update_bomb_count(bomb_count) 
                    else:
                        break
        
        timer_rect = pygame.Rect((GUI.screen_width - 85, GUI.screen_height - 55, 85, 50))       # Timer rectangle refresh
        GUI.screen.fill((0, 0, 0), timer_rect)

        if timer_started:                                                                       # Timer display
            passed_time = pygame.time.get_ticks() - start_timer
            GUI.timer_gui(passed_time)
        else:
            GUI.timer_gui(0)
            GUI.update_bomb_count(0)
        pygame.display.flip()
    pygame.quit()

Difficulty_instance = Difficulty()
Difficulty_instance.main_menu()
GUI_test = GUI()
GUI_test.load_images()
main(GUI_test,Difficulty_instance.difficulty_choice)