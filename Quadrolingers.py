import os
import sys

if sys.argv:
    filepath = sys.argv[0]
    folder, filename = os.path.split(filepath)
    os.chdir(folder) # now your working dir is the parent folder of the script
import customtkinter as ctk
import translator as tra
def start(x):
    if x == 1:
        from Easy import windowgra
window = ctk.CTk()

label = ctk.CTkLabel(window, text = 'Quadrolingers')
button1 = ctk.CTkButton(window, text = 'Poziom łatwy', command = start(1))
label.pack()
button1.pack()
window.mainloop()