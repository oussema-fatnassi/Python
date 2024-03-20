
import time 
self.start_time = None # variable
self.timer_running = False  # variable


def start_timer(self):    #   Cette fonction démarre le chronomètre si ce dernier n'est pas déjà en cours d'exécution.
    if not self.timer_running:
        self.start_time = time.time()
        self.timer_running = True
        self.update_timer()

def update_timer(self):  # Cette fonction est appelée récursivement pour mettre à jour l'affichage du chronomètre chaque seconde. 
    if self.timer_running:
        elapsed_time = round(time.time() - self.start_time)
        self.timer_label.config(text="Temps écoulé : " + str(elapsed_time))
        self.root.after(1000, self.update_timer)
    
def on_cell_click(self, event):  # Cette fonction est appelée lorsqu'un bouton de la grille est cliqué.  
    if not self.timer_running:
        self.start_timer()

    b.bind("<Button-1>", self.on_cell_click) # lie un événement à une fonction dans Tkinter.

    self.timer_label = tk.Label(self.root, text="Temps écoulé: 0")
    self.timer_label.grid(row=self.y, columnspan=self.x, sticky="W")
