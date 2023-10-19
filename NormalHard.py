import customtkinter as ctk
from deep_translator import GoogleTranslator
import random
from tkinter import messagebox
from Baza import listnum, listword
windowgra = ctk.CTk()
# WYLOSOWANIE PYTAŃ
pytania = []
for i in range (1,20):
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
score = 0
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
                        textvariable = wylosowane_slowo_pl)

slowo_en = ctk.CTkLabel(windowgra,
                        textvariable = wylosowane_slowo_en)

questions = ctk.CTkLabel(windowgra,
                         textvariable = ilosc_pytan)

lives = ctk.CTkLabel(windowgra,
                     textvariable = ilosc_zyc)

confirm_btn = ctk.CTkButton(windowgra,
                            text = 'Zatwierdz',
                            command=lambda:funkcja_sprawdzenia())

pole_wpisu = ctk.CTkEntry(windowgra,
                          textvariable=prompt)

# CZĘŚĆ IMPORTACJI GRAFIKI
slowo_pl.pack()
slowo_en.pack()
questions.pack()
lives.pack()
pole_wpisu.pack()
confirm_btn.pack()
windowgra.mainloop()