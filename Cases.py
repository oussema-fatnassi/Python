import tkinter as tk
import tkinter.font as tkFont
import tkinter.messagebox
import random
 
class Difficulty():
    
    def __init__(self):
        self.x = 0
        self.y = 0
        self.cpt_cases_mined = 0      # Compteur de cases minéees
        self.cpt_cases_demined = 0    # Compteur de cases déminées
        self.tab_valeur_case = [][]   # Tableau à comparer avec la localisation de la case

    def update_menubutton_text(self, *args):        # Sous-programme pour afficher la difficulté correctemnt
        self.difficulty = self.diff_selection.get()
        self.diff_button.config(text=f"Difficulté : {self.difficulty}")

    def difficulty_choice(self):                    # Programme pour afficher la fenêtre de choix de la difficulté
        
        self.root1 = tk.Tk()
        self.root1.geometry("200x200")
        self.label = tk.Label(self.root1, text="Choix de la difficulté : ")
        self.label.pack()
        self.diff_selection = tk.StringVar()        # Init variable diff
        self.diff_button = tk.Menubutton(self.root1, text="Difficulté ?")       # Init menu déroulant
        self.menu = tk.Menu(self.diff_button, tearoff=False)
        self.diff_button["menu"] = self.menu
        self.menu.add_command(label="Facile" , command=lambda: self.diff_selection.set("Facile"))
        self.menu.add_command(label="Moyen" , command=lambda: self.diff_selection.set("Moyen"))
        self.menu.add_command(label="Difficile" , command=lambda: self.diff_selection.set("Difficile"))
        self.diff_button.pack()
        self.diff_selection = tk.StringVar()
        self.diff_selection.trace_add("write", self.update_menubutton_text)     # Lancement sous-programme affichage correct
        btn = tk.Button(self.root1, text="Confirmer", command=self.root1.destroy)
        btn.pack()
        self.root1.mainloop()

    def plant_bombs(self):                  # Sous-programme qui plante les bombes au hasard
        for i in range(self.y):
            for j in range(self.x):
                a = random.randint(0,100)
                if a <= 15:
                    self.tab_valeur_case[i][j] = 1
                    self.cpt_cases_mined += 1
                elif a > 15:
                    self.tab_valeur_case[i][j] = 0
                    self.cpt_cases_demined += 1
            print(self.tab_valeur_case[i][j])

    def clique(self, event):                # Récupération localisation de la case
        print("Case cliquée : ",event.num)
        if self.cpt_cases_mined == 0:
            # lancement du timer
            self.plant_bombs()
        else:
            self.verification_bomb()
    

    def creation_grid(self):                # Création de la grille de boutons
        self.root = tk.Tk()
        self.font = tkFont.Font(family="Helvetica", size=20, weight = tkFont.BOLD)
        self.blank_image = tk.PhotoImage()
        
        if self.difficulty == "Facile":     # Changement de la taille suivant la difficulté
            self.x = 10
            self.y = 5
        elif self.difficulty == "Moyen":
            self.x = 10
            self.y = 10
        elif self.difficulty == "Difficile":
            self.x = 15
            self.y = 10

        for i in range(self.y):
            for j in range(self.x):
                b = tk.Button(self.root, image=self.blank_image,
                                font=self.font, compound=tk.CENTER)

            # get the height of the font to use as the square size
                square_size = self.font.metrics('linespace')
                b.config(width=square_size, height=square_size)

                b.grid(row = i, column = j, sticky = "NWSE")
                b.bind("<Double-Button-1>", self.clique)
        self.root.mainloop()
        
test = Difficulty()
test.difficulty_choice()
test.creation_grid()

"""class Matrice():
    
    def __init__(self, longueur_x, longueur_y):
        self.xx = longueur_x
        self.yy = longueur_y"""