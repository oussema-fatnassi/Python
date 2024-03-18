import tkinter as tk
import tkinter.font as tkFont
import tkinter.messagebox

class Difficulty():
    
    def __init__(self):
        self.x = 0
        self.y = 0

    def update_menubutton_text(self, *args):
        self.difficulty = self.diff_selection.get()
        self.diff_button.config(text=f"Difficulté : {self.difficulty}")

    def difficulty_choice(self):
        
        self.root1 = tk.Tk()
        self.root1.geometry("200x200")
        self.label = tk.Label(self.root1, text="Choix de la difficulté : ")
        self.label.pack()
        self.diff_selection = tk.StringVar()
        self.diff_button = tk.Menubutton(self.root1, text="Difficulté ?")
        self.menu = tk.Menu(self.diff_button, tearoff=False)
        self.diff_button["menu"] = self.menu
        self.menu.add_command(label="Facile" , command=lambda: self.diff_selection.set("Facile"))
        self.menu.add_command(label="Moyen" , command=lambda: self.diff_selection.set("Moyen"))
        self.menu.add_command(label="Difficile" , command=lambda: self.diff_selection.set("Difficile"))
        self.diff_button.pack()
        self.diff_selection = tk.StringVar()
        self.diff_selection.trace_add("write", self.update_menubutton_text)
        btn = tk.Button(self.root1, text="Confirmer", command=self.root1.destroy)
        btn.pack()
        self.root1.mainloop()

    def creation_grid(self):
        self.root = tk.Tk()
        self.font = tkFont.Font(family="Helvetica", size=20, weight = tkFont.BOLD)
        self.blank_image = tk.PhotoImage()
        
        self.x=5
        self.y=5
        if self.difficulty == "Facile":
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
                square_size = self.font.metrics('linespace')
                b.config(width=square_size, height=square_size)

                b.grid(row = i, column = j, sticky = "NWSE")

        self.root.mainloop()
        
test = Difficulty()
test.difficulty_choice()
test.creation_grid()