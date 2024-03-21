import pygame
from pygame.locals import *
import sys

class Difficulty():

    def __init__(self):

        pygame.init()               # Initialisation pygame
        self.screen_width = 700
        self.screen_height = 700
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Game Menu")
        self.difficulty = ""

    def main_menu(self):
        screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        screen.fill("black")

        play_button = pygame.Rect(self.screen_width // 2 - 250 // 2, 200, 250, 50)               # Menu button creation
        difficulty_button = pygame.Rect(self.screen_width // 2 - 250 // 2, 300, 250, 50)
        quit_button = pygame.Rect(self.screen_width // 2 - 250 // 2, 400, 250, 50)

        custom_font = pygame.font.Font("mine-sweeper.ttf", 36)

        minesweeper_text = custom_font.render("Minesweeper", True, (255, 255, 255))      # Text creation
        minesweeper_text = pygame.transform.scale(minesweeper_text, (350, 100))
        play_button_text = custom_font.render("PLAY", True, (255, 255, 255))
        difficulty_button_text = custom_font.render("DIFFICULTY", True, (255, 255, 255))
        quit_button_text = custom_font.render("QUIT", True, (255, 255, 255))

        screen.blit(minesweeper_text, (self.screen_width // 2 - minesweeper_text.get_width() // 2, 50))      
        
        pygame.draw.rect(screen, "black", play_button)
        pygame.draw.rect(screen, "black", difficulty_button)
        pygame.draw.rect(screen, "black", quit_button)

        screen.blit(play_button_text, (play_button.x + play_button.width // 2 - play_button_text.get_width() // 2, play_button.y + play_button.height // 2 - play_button_text.get_height() // 2))              
        screen.blit(quit_button_text, (quit_button.x + quit_button.width // 2 - quit_button_text.get_width() // 2, quit_button.y + quit_button.height // 2 - quit_button_text.get_height() // 2))        
        screen.blit(difficulty_button_text, (difficulty_button.x + difficulty_button.width // 2 - difficulty_button_text.get_width() // 2, difficulty_button.y + difficulty_button.height // 2 - quit_button_text.get_height() // 2))

        pygame.display.update()
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
                    if play_button.collidepoint(mouse_pos):
                        print("Play button clicked")
                        self.play_game()
                        run = False
                        print("im false")
                        play = 1
                    elif difficulty_button.collidepoint(mouse_pos):
                        self.difficulty_menu()
                        print("Difficulty button clicked")
                    elif quit_button.collidepoint(mouse_pos):
                        pygame.quit()
                        sys.exit()
        print("im out of loop")

    def play_game(self):
        print("Play game")
        print("Difficulty selected:", self.difficulty)
        #pygame.quit()

    def difficulty_menu(self):                          # Difficulty menu
        print("Difficulty menu")
        pygame.display.set_caption("Difficulty Menu")
        custom_font = pygame.font.Font("mine-sweeper.ttf", 36)
  
        self.screen.fill("black")

        easy_button = pygame.Rect(self.screen_width // 2 - 250 // 2, 100, 250, 50)
        medium_button = pygame.Rect(self.screen_width // 2 - 250 // 2, 150, 250, 50)
        hard_button = pygame.Rect(self.screen_width // 2 - 250 // 2, 200, 250, 50)
        back_button = pygame.Rect(self.screen_width // 2 - 250 // 2, 350, 250, 50)

        easy_button_text = custom_font.render("EASY", True, (255, 255, 255))
        medium_button_text = custom_font.render("MEDIUM", True, (255, 255, 255))
        hard_button_text = custom_font.render("HARD", True, (255, 255, 255))
        back_button_text = custom_font.render("BACK", True, (255, 255, 255))

        pygame.draw.rect(self.screen, "black", easy_button)
        pygame.draw.rect(self.screen, "black", medium_button)
        pygame.draw.rect(self.screen, "black", hard_button)
        pygame.draw.rect(self.screen, "black", back_button)

        self.screen.blit(easy_button_text, (easy_button.x + easy_button.width // 2 - easy_button_text.get_width() // 2, easy_button.y + easy_button.height // 2 - easy_button_text.get_height() // 2))
        self.screen.blit(medium_button_text, (medium_button.x + medium_button.width // 2 - medium_button_text.get_width() // 2, medium_button.y + medium_button.height // 2 - medium_button_text.get_height() // 2))
        self.screen.blit(hard_button_text, (hard_button.x + hard_button.width // 2 - hard_button_text.get_width() // 2, hard_button.y + hard_button.height // 2 - hard_button_text.get_height() // 2))
        self.screen.blit(back_button_text, (back_button.x + back_button.width // 2 - back_button_text.get_width() // 2, back_button.y + back_button.height // 2 - back_button_text.get_height() // 2))
        while True:
                for event in pygame.event.get():
                    if event.type == QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == MOUSEBUTTONDOWN:
                        mouse_pos = event.pos
                        if easy_button.collidepoint(mouse_pos):
                            print("Easy button clicked")
                            self.difficulty = "easy"
                        elif medium_button.collidepoint(mouse_pos):
                            print("Medium button clicked")
                            self.difficulty = "medium"
                        elif hard_button.collidepoint(mouse_pos):
                            print("Hard button clicked")
                            self.difficulty = "hard"
                        elif back_button.collidepoint(mouse_pos):
                            self.main_menu()
                pygame.display.update()

#Difficulty = Difficulty()
#Difficulty.main_menu()
