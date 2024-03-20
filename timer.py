import pygame
import sys
import time

pygame.init()

BLANC = "white"
NOIR = "black"

largeur = 400
hauteur = 400
taille_case = 20

fenetre = pygame.display.set_mode((largeur, hauteur))
pygame.display.set_caption("Mineweeper")

def afficher_chronometre(temps):
    font = pygame.font.Font(None, 36)
    texte = font.render("Temps : " + str(temps), True, NOIR)
    fenetre.blit(texte, (10, 10))

def mineweeper():
    debut = time.time()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
        temps_ecoule = int(time.time() - debut)

        fenetre.fill(BLANC)
        afficher_chronometre(temps_ecoule)
        pygame.display.flip()
mineweeper()
