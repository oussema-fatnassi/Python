import pygame
from pygame.locals import *
import sys

class Difficulty():

    def __init__(self):

        pygame.init()               
        self.screen_width = 700
        self.screen_height = 700
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Game Menu")
        self.difficulty_choice = ""                                                  
        self.play_button = pygame.Rect(self.screen_width // 2 - 250 // 2, 200, 250, 50)                 # Creation of all the button in the main menu and the difficulty menu      
        self.difficulty_button = pygame.Rect(self.screen_width // 2 - 250 // 2, 300, 250, 50)
        self.quit_button = pygame.Rect(self.screen_width // 2 - 250 // 2, 400, 250, 50)
        self.hard_button = pygame.Rect(self.screen_width // 2 - 250 // 2, 150, 250, 50)
        self.easy_button = pygame.Rect(self.screen_width // 2 - 250 // 2, 50, 250, 50)
        self.medium_button = pygame.Rect(self.screen_width // 2 - 250 // 2, 100, 250, 50)
        self.back_button = pygame.Rect(self.screen_width // 2 - 250 // 2, 350, 250, 50)

    def main_menu(self):                                                                                # Main menu                 
        screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        screen.fill("black")

        self.custom_font = pygame.font.Font("mine-sweeper.ttf", 36)                                     # Font initialization and button text rendering
        self.minesweeper_text = self.custom_font.render("Minesweeper", True, (255, 255, 255))          
        self.minesweeper_text = pygame.transform.scale(self.minesweeper_text, (350, 100))
        self.play_button_text = self.custom_font.render("PLAY", True, (255, 255, 255))
        self.difficulty_button_text = self.custom_font.render("DIFFICULTY", True, (255, 255, 255))
        self.quit_button_text = self.custom_font.render("QUIT", True, (255, 255, 255))

        screen.blit(self.minesweeper_text, (self.screen_width // 2 - self.minesweeper_text.get_width() // 2, 50))      
        
        pygame.draw.rect(screen, "black", self.play_button)
        pygame.draw.rect(screen, "black", self.difficulty_button)
        pygame.draw.rect(screen, "black", self.quit_button)

        screen.blit(self.play_button_text, (self.play_button.x + self.play_button.width // 2 - self.play_button_text.get_width() // 2, self.play_button.y + self.play_button.height // 2 - self.play_button_text.get_height() // 2))              
        screen.blit(self.quit_button_text, (self.quit_button.x + self.quit_button.width // 2 - self.quit_button_text.get_width() // 2, self.quit_button.y + self.quit_button.height // 2 - self.quit_button_text.get_height() // 2))        
        screen.blit(self.difficulty_button_text, (self.difficulty_button.x + self.difficulty_button.width // 2 - self.difficulty_button_text.get_width() // 2, self.difficulty_button.y + self.difficulty_button.height // 2 - self.quit_button_text.get_height() // 2))

        pygame.display.update()
        self.click_controller()
        
    def click_controller(self):                                                                         # Controlls all the interactions with the buttons            

        play = 0
        run = True
        while run:
            if play == 1:
                break
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == MOUSEBUTTONDOWN:
                    mouse_pos = event.pos
                    if self.play_button.collidepoint(mouse_pos):
                        run = False
                        play = 1
                    elif self.difficulty_button.collidepoint(mouse_pos):
                        self.difficulty_menu()
                    elif self.quit_button.collidepoint(mouse_pos):
                        pygame.quit()
                        sys.exit()
                    elif self.hard_button.collidepoint(mouse_pos):
                        play = 1
                        self.difficulty_choice = "hard"
                    elif self.easy_button.collidepoint(mouse_pos):
                        play = 1
                        self.difficulty_choice = "easy"
                    elif self.medium_button.collidepoint(mouse_pos):
                        play = 1
                        self.difficulty_choice = "medium"                   
                    elif self.back_button.collidepoint(mouse_pos):
                        self.main_menu()

    def difficulty_menu(self):                                                                          # Difficulty menu
        pygame.display.set_caption("Difficulty Menu")
        custom_font = pygame.font.Font("mine-sweeper.ttf", 36)

        self.screen.fill(((0,0,0)))
        self.easy_button_text = custom_font.render("EASY", True, (255, 255, 255))                       # Button text rendering and button creation
        self.medium_button_text = custom_font.render("MEDIUM", True, (255, 255, 255))
        self.hard_button_text = custom_font.render("HARD", True, (255, 255, 255))
        self.back_button_text = custom_font.render("BACK", True, (255, 255, 255))

        pygame.draw.rect(self.screen, "black", self.easy_button)
        pygame.draw.rect(self.screen, "black", self.medium_button)
        pygame.draw.rect(self.screen, "black", self.hard_button)
        pygame.draw.rect(self.screen, "black", self.back_button)

        self.screen.blit(self.easy_button_text, (self.easy_button.x + self.easy_button.width // 2 - self.easy_button_text.get_width() // 2, self.easy_button.y + self.easy_button.height // 2 - self.easy_button_text.get_height() // 2))
        self.screen.blit(self.medium_button_text, (self.medium_button.x + self.medium_button.width // 2 - self.medium_button_text.get_width() // 2, self.medium_button.y + self.medium_button.height // 2 - self.medium_button_text.get_height() // 2))
        self.screen.blit(self.hard_button_text, (self.hard_button.x + self.hard_button.width // 2 - self.hard_button_text.get_width() // 2, self.hard_button.y + self.hard_button.height // 2 - self.hard_button_text.get_height() // 2))
        self.screen.blit(self.back_button_text, (self.back_button.x + self.back_button.width // 2 - self.back_button_text.get_width() // 2, self.back_button.y + self.back_button.height // 2 - self.back_button_text.get_height() // 2))
       
        pygame.display.update()
