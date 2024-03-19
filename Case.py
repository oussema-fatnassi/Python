import random

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
            # Image drapeau
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
    
    def plant_bombs(self):                  # Sous-programme qui plante les bombes au hasard
        for i in range(self.y):
            for j in range(self.x):
                a = random.randint(0,100)
                if a <= 15:
                    print("BOMBE")
                    self.dict_cases[(i,j)] = 'X'
                    # self.tab_valeur_case[i][j] = 1
                    # self.cpt_cases_mined += 1
                elif a > 15:
                    print("PAS DE BOMBE")
                    self.dict_cases[(i,j)] = '.'
                    # self.tab_valeur_case[i][j] = 0
                    # self.cpt_cases_demined += 1
            print(self.dict_cases[(i,j)])
    
    def question_mark(self):                # Sous-programme qui affiche '?' ou rien si déjà '?'
        print("Test arrivée sur ?")
        if self.question_mark_var == 0:
            # Affichage '?'
            print("Test affichage ?")
            self.question_mark_var = 1
        elif self.question_mark_var == 1:
            # Affichage ' '
            print("Retour affichage vide")
            self.flag_var = 0
            self.question_mark_var = 0
    
    def set_flag(self, a):
        self.flag_var = a
    
    def set_question(self, a):
        self.question_mark_var = a
    
    def verification_case(self, co_x, co_y):
        pass