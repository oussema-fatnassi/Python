# Python

Ceci est le projet de création du jeu Minesweeper (Démineur) pour la prépa Logiciel groupe1.

Groupe de trois personnes:
Oussema
Baptiste 
Ali

Description des tâches effectuées:

- Installation de pygame;
- importation de Random, pygame
- création de quatres fichiers (GUI.py, Case.py, Difficulty.py, Main.py) et un fichier image et font.
- Création des différentes fenêtres et éléments d'interface graphique

Implémentation de la logique du jeu :

- Génération de la grille de jeu avec les cases et les bombes.
- Définition des règles du jeu (détection des cases voisines, gestion des clics de souris, etc.).
- Intégration des fonctionnalités de déminage et de marquage des cases.

Gestion de la difficulté :

- Mise en place des différentes difficultés (facile, moyen, difficile) avec des tailles de grille et des densités de bombes variables.

Quand on lance le jeu, la fenêtre principale du jeu affiche les options de boutons Play, Difficulty (choisir le niveau de jeu (facile, moyen ou difficile) ou Quit pour quitter le jeu.
- Si on clique sur play sans choisir l'option Difficulty, le jeu se lance automatiquement sur 'facile'

-La grille de jeu est représentée par un tableau de cases carrées, un bouton reset au milieu en bas, le nombre de bombes restantes à gauche du bouton reset et le temps écoulé à droite.
chaque case pouvant être soit vide, soit contenir une bombe.

- Cases de la grille :

Chaque case de la grille est clickable et peut réagir à différents événements (clic gauche, clic droit, double click droit).
Lorsque le joueur clique sur une case, elle peut se dévoiler pour révéler soit une case vide, soit une bombe, soit le nombre de bombes voisines.
Les cases vides peuvent être adjacentes à des cases contenant des bombes ou être entourées uniquement de cases vides. Dans ce dernier cas, toutes les cases vides adjacentes seront également dévoilées automatiquement.

- Marquage des cases :

Le joueur peut marquer une case qu'il soupçonne de contenir une bombe en la cliquant avec le bouton droit de la souris. Cela placera un drapeau sur la case et s'il clique droit sur le drapeau un point d'interrogation s'affiche.
s'il clique sur la grille minée, la partie prendra fin. 
