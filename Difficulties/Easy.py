import os
import sys
if sys.argv:
    filepath = sys.argv[0]
    folder, filename = os.path.split(filepath)
    os.chdir(folder.replace("\\Difficulties",""))
sys.path.append("Images")
sys.path.append("Database")

from tkinter import *
from Baza import listnum  #nr 
from Baza import listword  #slowo
from deep_translator import GoogleTranslator
import customtkinter as ctk
from tkinter import messagebox
from PIL import Image
import random

window = ctk.CTk()

pytania = []
for i in range (1,20):
    x = random.choice(listword)
    pytania.append(x)
    listword.remove(x)
wylosowane_slowo_pl = ctk.StringVar()
prompt = ctk.StringVar()
wylosowane_slowo_en = ctk.StringVar()
ilosc_pytan = ctk.StringVar()
ilosc_zyc = ctk.StringVar()
strona = ctk.StringVar()

score = 0
zycia = 4
ilosc_pytan_odpowiedzialnych = 1
ilosc_pytan.set('Pytanie '+str(ilosc_pytan_odpowiedzialnych)+"/20")
ilosc_zyc.set('Sprób zostało się '+str(zycia))
wylosowane_slowo = random.choice(pytania)
wylosowane_slowo_pl.set(wylosowane_slowo)
pytania.remove(wylosowane_slowo)
wylosowane_slowo_en.set(GoogleTranslator(source='pl', target='en').translate(wylosowane_slowo))




def test(x):
    global ilosc_pytan_odpowiedzialnych
    if x == wylosowane_slowo_en.get():
        zmien()
        ilosc_pytan_odpowiedzialnych = ilosc_pytan_odpowiedzialnych + 1
        ilosc_pytan.set('Pytanie '+str(ilosc_pytan_odpowiedzialnych)+"/20")
    else:
        #messagebox.showinfo(title='Niepoprawne',message=Image.open(folder+"\Images\\"+str(wylosowane_slowo_en.get())+'.jpg'),size=(100,100)+" To jest "+str(wylosowane_slowo_pl.get())+" po angielsku to bedzie "+str(wylosowane_slowo_en.get()))
        windowm = ctk.CTk()
        my_imagem = ctk.CTkImage(Image.open(folder+"\Images\\"+str(wylosowane_slowo_en.get())+'.jpg'),size = (100,100))
        image_labelm = ctk.CTkLabel(windowm, image=my_image, text = "")
        labelm = ctk.CTkLabel(windowm,text = " To jest "+str(wylosowane_slowo_pl.get())+" po angielsku to bedzie "+str(wylosowane_slowo_en.get()))
        image_labelm.pack()
        labelm.pack()
        windowm.mainloop()

    



odpP = ctk.StringVar()  #poprawna odpowiedz z bazy
odpA = ctk.StringVar()  #odpowiedzi a - f, jedna to poprawna pozostale to losowe z bazy
odpB = ctk.StringVar()
odpC = ctk.StringVar()
odpD = ctk.StringVar()
odpE = ctk.StringVar()
odpF = ctk.StringVar()


def zmien():
    global odpP, odpA, odpB, odpC, odpD, odpE
    odpP.set(wylosowane_slowo_en.get())
    a = random.randint(1,6)
    if a == 1:
        odpA.set(odpP.get())
        strona.set(Image.open(folder+"\Images\\"+str(wylosowane_slowo_en.get())+'.jpg'))
        odpB.set(random.choice(listword))
        odpC.set(random.choice(listword))
        odpD.set(random.choice(listword))
        odpE.set(random.choice(listword))
        odpF.set(random.choice(listword))
    if a == 2:
        odpB.set(odpP.get())
        strona.set(Image.open(folder+"\Images\\"+str(wylosowane_slowo_en.get())+'.jpg'))
        odpA.set(random.choice(listword))
        odpC.set(random.choice(listword))
        odpD.set(random.choice(listword))
        odpE.set(random.choice(listword))
        odpF.set(random.choice(listword))
    if a == 3:
        odpC.set(odpP.get())
        strona.set(Image.open(folder+"\Images\\"+str(wylosowane_slowo_en.get())+'.jpg'))
        odpA.set(random.choice(listword))
        odpB.set(random.choice(listword))
        odpD.set(random.choice(listword))
        odpE.set(random.choice(listword))
        odpF.set(random.choice(listword))
    if a == 4:
        odpD.set(odpP.get())
        strona.set(Image.open(folder+"\Images\\"+str(wylosowane_slowo_en.get())+'.jpg'))
        odpA.set(random.choice(listword))
        odpB.set(random.choice(listword))
        odpC.set(random.choice(listword))
        odpE.set(random.choice(listword))
        odpF.set(random.choice(listword))
    if a == 5:
        odpE.set(odpP.get())
        strona.set(Image.open(folder+"\Images\\"+str(wylosowane_slowo_en.get())+'.jpg'))
        odpA.set(random.choice(listword))
        odpB.set(random.choice(listword))
        odpD.set(random.choice(listword))
        odpC.set(random.choice(listword))
        odpF.set(random.choice(listword))
    if a == 6:
        odpF.set(odpP.get())
        strona.set(Image.open(folder+"\Images\\"+str(wylosowane_slowo_en.get())+'.jpg'))
        odpA.set(random.choice(listword))
        odpB.set(random.choice(listword))
        odpD.set(random.choice(listword))
        odpE.set(random.choice(listword))
        odpC.set(random.choice(listword))
zmien()
punkty = ctk.StringVar()  #punkty wyswietlane
punktyV = 0   #variable dla punktow

pomylka = 0  #licznik pomylek, jesli =4 to koniec gry
my_image = ctk.CTkImage(Image.open(folder+"\Images\\"+str(wylosowane_slowo_en.get())+'.jpg'),size = (100,100))
image_label = ctk.CTkLabel(window, image=my_image, text = "")
zycia_napis = ctk.CTkLabel(window,textvariable = ilosc_zyc)
pytania_napis = ctk.CTkLabel(window,textvariable = ilosc_pytan)
btnf = ctk.CTkFrame(window)
btn1 = ctk.CTkButton(btnf,textvariable=odpA,command=lambda:test(odpA.get()))
btn2 = ctk.CTkButton(btnf,textvariable=odpB,command=lambda:test(odpB.get()))
btn3 = ctk.CTkButton(btnf,textvariable=odpC,command=lambda:test(odpC.get()))
btn4 = ctk.CTkButton(btnf,textvariable=odpD,command=lambda:test(odpD.get()))
btn5 = ctk.CTkButton(btnf,textvariable=odpE,command=lambda:test(odpE.get()))
btn6 = ctk.CTkButton(btnf,textvariable=odpF,command=lambda:test(odpF.get()))

image_label.pack()
zycia_napis.pack()
pytania_napis.pack()
btnf.pack(side = LEFT)
btn1.pack()
btn2.pack()
btn3.pack()
btn4.pack()
btn5.pack()
btn6.pack()

window.mainloop()