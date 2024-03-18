import tkinter as tk
import tkinter.font as tkFont


root = tk.Tk()

font = tkFont.Font(family="Helvetica", size=20, weight = tkFont.BOLD)
blank_image = tk.PhotoImage()

for i in range(6):
    for j in range(15):
        b = tk.Button(root, image=blank_image,
                           font=font, compound=tk.CENTER)

    # get the height of the font to use as the square size
        square_size = font.metrics('linespace')
        b.config(width=square_size, height=square_size)

        b.grid(row = i, column = j, sticky = "NWSE")

root.mainloop()