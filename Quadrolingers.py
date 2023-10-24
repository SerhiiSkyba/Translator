import os
import sys
if sys.argv:
    filepath = sys.argv[0]
    folder, filename = os.path.split(filepath)
    os.chdir(folder) # now your working dir is the parent folder of the script
import customtkinter as ctk
def start():
    from Easy import windowgra
def start2():
    from Normal import windowgra
def start3():
    from NormalHard import windowgra
def start4():
    from Hard import windowgra
window = ctk.CTk()

label = ctk.CTkLabel(window, text = 'Quadrolingers')
button1 = ctk.CTkButton(window, text = 'Poziom łatwy', command = lambda:start())
button2 = ctk.CTkButton(window, text = 'Poziom normalny', command = lambda:start2())
button3 = ctk.CTkButton(window, text = 'Poziom normalno-trudny', command = lambda:start3())
button4 = ctk.CTkButton(window, text = 'Poziom trudny', command = lambda:start4())
label.pack()
button1.pack()
button2.pack()
button3.pack()
button4.pack()
window.mainloop()