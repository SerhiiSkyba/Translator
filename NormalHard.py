import customtkinter as ctk
from deep_translator import GoogleTranslator
import random
from tkinter import messagebox
from Baza import listnum, listword
windowgra = ctk.CTk()
# WYLOSOWANIE PYTAŃ
pytania = []
for i in range (0,20):
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

pytania.remove(wylosowane_slowo)
tluma = GoogleTranslator(source='pl', target='en').translate(wylosowane_slowo)
tluma2 = tluma
wylosowane_slowo_pl.set(wylosowane_slowo)
wylosowane_slowo_en.set(tluma)

print(len(wylosowane_slowo))
alpha = len(tluma)
for i in range (0,alpha):
    a = str(tluma[i])
    print (a)
    if a == 'i' or a == 'a' or a == 'e' or a == 'o' or a == 'u':
        tluma2 = tluma2.replace(a,'_')
prompt.set(tluma2)

def funkcja_sprawdzenia():
    global zycia, score, ilosc_pytan_odpowiedzialnych, wylosowane_slowo, tluma, tluma2
    
    
    # POPRAWNA ODPOWIEDZ
    if prompt.get() == GoogleTranslator(source='pl', target='en').translate(wylosowane_slowo):
        try:
            score = score + 1

            wylosowane_slowo = random.choice(pytania)

            pytania.remove(wylosowane_slowo)

            wylosowane_slowo_pl.set(wylosowane_slowo)
            tluma = GoogleTranslator(source='pl', target='en').translate(wylosowane_slowo)
            wylosowane_slowo_en.set(tluma)
            tluma2 = tluma

            print(len(wylosowane_slowo))
            print(len(wylosowane_slowo))
            alpha = len(tluma)
            for i in range (0,alpha):
                a = str(tluma[i])
                print (a)
                if a == 'i' or a == 'a' or a == 'e' or a == 'o' or a == 'u':
                    tluma2 = tluma2.replace(a,'_')
            prompt.set(tluma2)
            ilosc_pytan_odpowiedzialnych = ilosc_pytan_odpowiedzialnych+1
            ilosc_pytan.set(str(ilosc_pytan_odpowiedzialnych)+"/20")
            if ilosc_pytan_odpowiedzialnych == 21:
                messagebox.showinfo(title='Wygrałeś',message='Ty wygrałeś, twój wynnik jest '+str(score)+'/20')
                windowgra.destroy()
        except:
            messagebox.showinfo(title='Wygrałeś',message='Ty wygrałeś, twój wynnik jest '+str(score)+'/20')
            windowgra.destroy()
        
    
    # ŻLA ODPOWIEDZ
    else:
        try:
            wylosowane_slowo = random.choice(pytania)

            pytania.remove(wylosowane_slowo)

            wylosowane_slowo_pl.set(wylosowane_slowo)

            wylosowane_slowo_en.set(GoogleTranslator(source='pl', target='en').translate(wylosowane_slowo))

            ilosc_pytan_odpowiedzialnych = ilosc_pytan_odpowiedzialnych+1

            ilosc_pytan.set('Pytanie'+str(ilosc_pytan_odpowiedzialnych)+"/20")

            zycia = zycia - 1
            ilosc_zyc.set('Sprób zostało się'+str(zycia))

            if zycia == 0 or zycia < 0 :
                messagebox.showinfo(title='Przegrałeś',message='Ty przegrałeś, twój wynnik jest '+str(score))
                windowgra.destroy()
        except:
            messagebox.showinfo(title='Wygrałeś',message='Ty wygrałeś, twój wynnik jest '+str(score)+'/20')
            windowgra.destroy()

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