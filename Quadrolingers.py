# IMPORTOWANIE POTRZEBNYCH ROZSZEŻEŃ
import os
import sys
import random
import customtkinter as ctk
from tkinter import *
from tkinter import messagebox
from deep_translator import GoogleTranslator
from PIL import Image
if sys.argv:
    filepath = sys.argv[0]
    folder, filename = os.path.split(filepath)
    os.chdir(folder) # now your working dir is the parent folder of the script

# IMPORTUJE FOLDERY
sys.path.append("Database")
sys.path.append("Images")
sys.path.append("Textures")
sys.path.append("Difficulties")

# SPRAWDZA, CZY BAZA DANYCH ZOSTAŁA WŁĄCZONA
try:
    from Baza import listnum
    from Baza import listword
except:
    messagebox.showerror(title='Error',message='Baza danych nie została odznaleziona, sprawdz, czy baza danych została zainstalowana')

# SPRAWDZA, CZY WSZYSTKIE ZDJĘCIA SĄ ODZNALEZIONE
try:
    for i in range(0,len(listnum)):
        my_image = ctk.CTkImage(Image.open(folder+"\Images\\"+str(GoogleTranslator(source='pl', target='en').translate(listword[i]))+'.jpg'),size = (100,100))
except:
    messagebox.showerror(title='Error',message='Zdjęcie '+str(GoogleTranslator(source='pl', target='en').translate(listword[i]))+'.jpg')


def start():
    window.destroy()
    from Easy import windowgra
def start2():
    window.destroy()
    from Normal import windowgra
def start3():
    window.destroy()
    from NormalHard import windowgra
def start4():
    window.destroy()
    from Hard import windowgra
def exit():
    window.destroy()
    
# GŁÓWNE OKNO
window = ctk.CTk()
bg = PhotoImage(file = folder+"\\Textures\\tlo.png")
window.resizable(False,False)
window.geometry("600x330")
window.title("Quatrolingers")
a = random.randint(1,4) 
if (a!=1):
    window.iconbitmap(folder+"\\Textures\\image.ico")
else:
    window.iconbitmap(folder+"\\Textures\\Heinz_Doofenshmirtz.ico")

label = ctk.CTkLabel(window,image = bg, text="")
button1 = ctk.CTkButton(window, text = 'Poziom łatwy', command = lambda:start())
button2 = ctk.CTkButton(window, text = 'Poziom normalny', command = lambda:start2())
button3 = ctk.CTkButton(window, text = 'Poziom normalno-trudny', command = lambda:start3())
button4 = ctk.CTkButton(window, text = 'Poziom trudny', command = lambda:start4())
button5 = ctk.CTkButton(window,text="🚪",font=("Calibri",30),command=lambda:exit())

label.pack()
button1.pack(side=LEFT)
button2.pack(side=LEFT)
button3.pack(side=LEFT)
button4.pack(side=LEFT)
button5.pack(side=LEFT)

window.mainloop()