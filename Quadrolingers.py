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
    if x == 2:
        from Normal import windowgra
    if x == 3:
        from NormalHard import windowgra
    if x == 4:
        from Hard import windowgra
window = ctk.CTk()

label = ctk.CTkLabel(window, text = 'Quadrolingers')
button1 = ctk.CTkButton(window, text = 'Poziom łatwy', command = lambda:start(1))
button2 = ctk.CTkButton(window, text = 'Poziom normalny', command = lambda:start(2))
button3 = ctk.CTkButton(window, text = 'Poziom normalno-trudny', command = lambda:start(3))
button4 = ctk.CTkButton(window, text = 'Poziom trudny', command = lambda:start(4))
label.pack()
button1.pack()
button2.pack()
button3.pack()
button4.pack()
window.mainloop()