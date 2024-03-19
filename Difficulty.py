import pygame

import tkinter as tk
import tkinter.messagebox
 
class Difficulty():
    
    def __init__(self):
        self.difficulty = ""

    def update_menubutton_text(self, *args):        # Sous-programme pour afficher la difficulté correctemnt
        self.difficulty = self.diff_selection.get()
        self.diff_button.config(text=f"Difficulté : {self.difficulty}")

    def difficulty_choice(self):                    # Programme pour afficher la fenêtre de choix de la difficulté
        
        self.root1 = tk.Tk()
        self.root1.geometry("200x200")
        self.label = tk.Label(self.root1, text="Choix de la difficulté : ")
        self.label.pack()
        self.diff_selection = tk.StringVar()                                    # Init variable diff
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

test = Difficulty()
test.difficulty_choice()
print(test.difficulty)