import sys
import os
if sys.argv:
    filepath = sys.argv[0]
    folder, filename = os.path.split(filepath)
    os.chdir(folder.replace("\\Difficulties","")) # now your working dir is the parent folder of the script
    print(folder.replace("\\Difficulties",""))
sys.path.append("Database")
import customtkinter as ctk
from deep_translator import GoogleTranslator
import random
from tkinter import messagebox
from Baza import listnum, listword

# FUNKCJA SPRAWDZAJĄCA
def funkcja_sprawdzenia():
    global zycia, score, ilosc_pytan_odpowiedzialnych, wylosowane_slowo
    
    
    # POPRAWNA ODPOWIEDZ
    if prompt.get() == GoogleTranslator(source='pl', target='en').translate(wylosowane_slowo):
        try:
            if (score%2 == 0):
                confirm_btn.configure(fg_color="#311f7a")
            else:
                confirm_btn.configure(fg_color="#3b278c")

            score = score + 1

            wylosowane_slowo = random.choice(pytania)

            pytania.remove(wylosowane_slowo)

            wylosowane_slowo_pl.set(wylosowane_slowo)

            wylosowane_slowo_en.set(GoogleTranslator(source='pl', target='en').translate(wylosowane_slowo))

            ilosc_pytan_odpowiedzialnych = ilosc_pytan_odpowiedzialnych+1

            prompt.set('')

            ilosc_pytan.set('Pytanie '+str(ilosc_pytan_odpowiedzialnych)+"/20")
            if ilosc_pytan_odpowiedzialnych == 21:
                windowgra.destroy()
                messagebox.showinfo(title='Wygrałeś',message='Ty wygrałeś, twój wynik jest '+'20/20')
        except:
            messagebox.showerror(title='Error',message='Sprawdż połączenie z internetem')
            windowgra.destroy()
    
    # ŻLA ODPOWIEDZ
    else:
        try:
            wylosowane_slowo = random.choice(pytania)

            pytania.remove(wylosowane_slowo)

            wylosowane_slowo_pl.set(wylosowane_slowo)

            wylosowane_slowo_en.set(GoogleTranslator(source='pl', target='en').translate(wylosowane_slowo))

            ilosc_pytan_odpowiedzialnych = ilosc_pytan_odpowiedzialnych+1

            ilosc_pytan.set('Pytanie '+str(ilosc_pytan_odpowiedzialnych)+"/20")

            zycia = zycia - 1
            ilosc_zyc.set('Sprób zostało się '+str(zycia))

            if zycia == 0 or zycia < 0 :
                messagebox.showinfo(title='Przegrałeś',message='Ty przegrałeś, twój wynnik jest '+str(score))
                windowgra.destroy()
        except:
            messagebox.showerror(title='Error',message='Sprawdż połączenie z internetem')
            windowgra.destroy()

windowgra = ctk.CTk()
windowgra.title("Quadrolingers")
windowgra.geometry('600x600')
windowgra.resizable("False","False")


# WYLOSOWANIE PYTAŃ
pytania = []
for i in range (1,23):
    x = random.choice(listword)
    pytania.append(x)
    listword.remove(x)

# print (pytania) Wypisuje pytania wylosowane z bazy

# ZMIENNE GRAFICZNE
wylosowane_slowo_pl = ctk.StringVar()
prompt = ctk.StringVar()
wylosowane_slowo_en = ctk.StringVar()
ilosc_pytan = ctk.StringVar()
ilosc_zyc = ctk.StringVar()

# STARTOWE VALUES ZMIENNYCH
score = 1
zycia = 4
ilosc_pytan_odpowiedzialnych = 1
ilosc_pytan.set('Pytanie '+str(ilosc_pytan_odpowiedzialnych)+"/20")
ilosc_zyc.set('Sprób zostało się '+str(zycia))
wylosowane_slowo = random.choice(pytania)
wylosowane_slowo_pl.set(wylosowane_slowo)
pytania.remove(wylosowane_slowo)
wylosowane_slowo_en.set(GoogleTranslator(source='pl', target='en').translate(wylosowane_slowo))

# CZĘŚĆ GRAFICZNA
slowo_pl = ctk.CTkLabel(windowgra,
                        font=("Comic Sans MS",50,'bold','italic','underline'),
                        textvariable = wylosowane_slowo_pl)

slowo_en = ctk.CTkLabel(windowgra,
                        textvariable = wylosowane_slowo_en)

questions = ctk.CTkLabel(windowgra,
                         font=("Comic Sans MS",20),
                         textvariable = ilosc_pytan)

lives = ctk.CTkLabel(windowgra,
                     font=("Comic Sans MS",20),
                     textvariable = ilosc_zyc)

confirm_btn = ctk.CTkButton(windowgra,
                            width=300,
                            height=120,
                            fg_color="#3b278c",
                            text = 'Zatwierdź',
                            command=lambda:funkcja_sprawdzenia())

pole_wpisu = ctk.CTkEntry(windowgra,
                          width=300,
                          height=120,
                          font=("Comic Sans MS",25),
                          textvariable=prompt)

# CZĘŚĆ IMPORTACJI GRAFIKI
slowo_pl.pack()
#slowo_en.pack()
questions.pack()
lives.pack()
pole_wpisu.pack()
confirm_btn.pack()

windowgra.mainloop()