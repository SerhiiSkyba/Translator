import os
import sys
if sys.argv:
    filepath = sys.argv[0]
    folder, filename = os.path.split(filepath)
    folder = folder.replace("\\Difficulties","")
    os.chdir(folder)
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

score = 1
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
    global wylosowane_slowo
    global wylosowane_slowo_en
    global folder
    global zycia
    if x == wylosowane_slowo_en.get():
        btn1.configure(state = E) # E = Enabled
        btn2.configure(state = E)
        btn3.configure(state = E)
        btn4.configure(state = E)
        btn5.configure(state = E)
        btn6.configure(state = E)
        btn7.configure(state = E)
        btn8.configure(state = E)
        score = score+1
        wylosowane_slowo = random.choice(pytania)
        pytania.remove(wylosowane_slowo)
        wylosowane_slowo_pl.set(wylosowane_slowo)
        wylosowane_slowo_en.set(GoogleTranslator(source='pl', target='en').translate(wylosowane_slowo))
        zmien()
        my_image.configure(light_image=Image.open(folder+"\Images\\"+str(wylosowane_slowo_en.get())+'.jpg'))
        ilosc_pytan_odpowiedzialnych = ilosc_pytan_odpowiedzialnych + 1
        ilosc_pytan.set('Pytanie '+str(ilosc_pytan_odpowiedzialnych)+"/20")
        if ilosc_pytan_odpowiedzialnych == 21:
            window.destroy()
            messagebox.showinfo(title='Wygrałeś',message='Ty wygrałeś, twój wynik jest '+'20/20')
    else:
        zycia = zycia - 1
        if zycia == 0 or zycia < 0 :
            messagebox.showinfo(title='Przegrałeś',message='Ty przegrałeś, twój wynnik jest '+str(score))
            window.destroy()
        if x == odpA.get():
            btn1.configure(state = DISABLED)
        if x == odpB.get():
            btn2.configure(state = DISABLED)
        if x == odpC.get():
            btn3.configure(state = DISABLED)
        if x == odpD.get():
            btn4.configure(state = DISABLED)
        if x == odpE.get():
            btn5.configure(state = DISABLED)
        if x == odpF.get():
            btn6.configure(state = DISABLED)
        if x == odpG.get():
            btn7.configure(state = DISABLED)
        if x == odpH.get():
            btn8.configure(state = DISABLED)
        ilosc_zyc.set('Sprób zostało się '+str(zycia))
        windowm = ctk.CTkToplevel()
        my_imagem = ctk.CTkImage(Image.open(folder+"\Images\\"+str(wylosowane_slowo_en.get())+'.jpg'),size = (100,100))
        image_labelm = ctk.CTkLabel(windowm, image=my_imagem, text = "")
        labelm = ctk.CTkLabel(windowm,text = " To jest "+str(wylosowane_slowo_pl.get())+", po angielsku to bedzie "+str(wylosowane_slowo_en.get()))
        
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
odpG = ctk.StringVar()
odpH = ctk.StringVar()


def zmien():
    global odpP, odpA, odpB, odpC, odpD, odpE, odpG, odpH
    odpP.set(wylosowane_slowo_en.get())
    a = random.randint(1,8)
    if a == 1:
        odpA.set(odpP.get())
        odpB.set(GoogleTranslator(source='pl', target='en').translate(random.choice(listword)))
        odpC.set(GoogleTranslator(source='pl', target='en').translate(random.choice(listword)))
        odpD.set(GoogleTranslator(source='pl', target='en').translate(random.choice(listword)))
        odpE.set(GoogleTranslator(source='pl', target='en').translate(random.choice(listword)))
        odpF.set(GoogleTranslator(source='pl', target='en').translate(random.choice(listword)))
        odpG.set(GoogleTranslator(source='pl', target='en').translate(random.choice(listword)))
        odpH.set(GoogleTranslator(source='pl', target='en').translate(random.choice(listword)))
    if a == 2:
        odpB.set(odpP.get())
        odpA.set(GoogleTranslator(source='pl', target='en').translate(random.choice(listword)))
        odpC.set(GoogleTranslator(source='pl', target='en').translate(random.choice(listword)))
        odpD.set(GoogleTranslator(source='pl', target='en').translate(random.choice(listword)))
        odpE.set(GoogleTranslator(source='pl', target='en').translate(random.choice(listword)))
        odpF.set(GoogleTranslator(source='pl', target='en').translate(random.choice(listword)))
        odpG.set(GoogleTranslator(source='pl', target='en').translate(random.choice(listword)))
        odpH.set(GoogleTranslator(source='pl', target='en').translate(random.choice(listword)))
    if a == 3:
        odpC.set(odpP.get())
        odpA.set(GoogleTranslator(source='pl', target='en').translate(random.choice(listword)))
        odpB.set(GoogleTranslator(source='pl', target='en').translate(random.choice(listword)))
        odpD.set(GoogleTranslator(source='pl', target='en').translate(random.choice(listword)))
        odpE.set(GoogleTranslator(source='pl', target='en').translate(random.choice(listword)))
        odpF.set(GoogleTranslator(source='pl', target='en').translate(random.choice(listword)))
        odpG.set(GoogleTranslator(source='pl', target='en').translate(random.choice(listword)))
        odpH.set(GoogleTranslator(source='pl', target='en').translate(random.choice(listword)))
    if a == 4:
        odpD.set(odpP.get())
        odpA.set(GoogleTranslator(source='pl', target='en').translate(random.choice(listword)))
        odpB.set(GoogleTranslator(source='pl', target='en').translate(random.choice(listword)))
        odpC.set(GoogleTranslator(source='pl', target='en').translate(random.choice(listword)))
        odpE.set(GoogleTranslator(source='pl', target='en').translate(random.choice(listword)))
        odpF.set(GoogleTranslator(source='pl', target='en').translate(random.choice(listword)))
        odpG.set(GoogleTranslator(source='pl', target='en').translate(random.choice(listword)))
        odpH.set(GoogleTranslator(source='pl', target='en').translate(random.choice(listword)))
    if a == 5:
        odpE.set(odpP.get())
        odpA.set(GoogleTranslator(source='pl', target='en').translate(random.choice(listword)))
        odpB.set(GoogleTranslator(source='pl', target='en').translate(random.choice(listword)))
        odpD.set(GoogleTranslator(source='pl', target='en').translate(random.choice(listword)))
        odpC.set(GoogleTranslator(source='pl', target='en').translate(random.choice(listword)))
        odpF.set(GoogleTranslator(source='pl', target='en').translate(random.choice(listword)))
        odpG.set(GoogleTranslator(source='pl', target='en').translate(random.choice(listword)))
        odpH.set(GoogleTranslator(source='pl', target='en').translate(random.choice(listword)))
    if a == 6:
        odpF.set(odpP.get())
        odpA.set(GoogleTranslator(source='pl', target='en').translate(random.choice(listword)))
        odpB.set(GoogleTranslator(source='pl', target='en').translate(random.choice(listword)))
        odpD.set(GoogleTranslator(source='pl', target='en').translate(random.choice(listword)))
        odpE.set(GoogleTranslator(source='pl', target='en').translate(random.choice(listword)))
        odpC.set(GoogleTranslator(source='pl', target='en').translate(random.choice(listword)))
        odpG.set(GoogleTranslator(source='pl', target='en').translate(random.choice(listword)))
        odpH.set(GoogleTranslator(source='pl', target='en').translate(random.choice(listword)))
    if a == 7:
        odpG.set(odpP.get())
        odpA.set(GoogleTranslator(source='pl', target='en').translate(random.choice(listword)))
        odpB.set(GoogleTranslator(source='pl', target='en').translate(random.choice(listword)))
        odpD.set(GoogleTranslator(source='pl', target='en').translate(random.choice(listword)))
        odpE.set(GoogleTranslator(source='pl', target='en').translate(random.choice(listword)))
        odpC.set(GoogleTranslator(source='pl', target='en').translate(random.choice(listword)))
        odpF.set(GoogleTranslator(source='pl', target='en').translate(random.choice(listword)))
        odpH.set(GoogleTranslator(source='pl', target='en').translate(random.choice(listword)))
    if a == 8:
        odpH.set(odpP.get())
        odpA.set(GoogleTranslator(source='pl', target='en').translate(random.choice(listword)))
        odpB.set(GoogleTranslator(source='pl', target='en').translate(random.choice(listword)))
        odpD.set(GoogleTranslator(source='pl', target='en').translate(random.choice(listword)))
        odpE.set(GoogleTranslator(source='pl', target='en').translate(random.choice(listword)))
        odpC.set(GoogleTranslator(source='pl', target='en').translate(random.choice(listword)))
        odpG.set(GoogleTranslator(source='pl', target='en').translate(random.choice(listword)))
        odpF.set(GoogleTranslator(source='pl', target='en').translate(random.choice(listword)))
zmien()
my_image = ctk.CTkImage(Image.open(folder+"\Images\\"+str(wylosowane_slowo_en.get())+'.jpg'),size = (100,100))
image_label = ctk.CTkLabel(window, image=my_image, text = "")
zycia_napis = ctk.CTkLabel(window,textvariable = ilosc_zyc)
pytania_napis = ctk.CTkLabel(window,textvariable = ilosc_pytan)
btnf = ctk.CTkFrame(window, bg_color = '#ffffff')
btnf1 = ctk.CTkFrame(btnf, bg_color = '#ffffff')
btnf2 = ctk.CTkFrame(btnf, bg_color = '#ffffff')
btnf3 = ctk.CTkFrame(btnf, bg_color = '#ffffff')
btnf4 = ctk.CTkFrame(btnf, bg_color = '#ffffff')
label = ctk.CTkLabel(window, textvariable = wylosowane_slowo_pl)
btn1 = ctk.CTkButton(btnf1,textvariable=odpA,command=lambda:test(odpA.get()))
btn2 = ctk.CTkButton(btnf1,textvariable=odpB,command=lambda:test(odpB.get()))
btn3 = ctk.CTkButton(btnf2,textvariable=odpC,command=lambda:test(odpC.get()))
btn4 = ctk.CTkButton(btnf2,textvariable=odpD,command=lambda:test(odpD.get()))
btn5 = ctk.CTkButton(btnf3,textvariable=odpE,command=lambda:test(odpE.get()))
btn6 = ctk.CTkButton(btnf3,textvariable=odpF,command=lambda:test(odpF.get()))
btn7 = ctk.CTkButton(btnf4,textvariable=odpG,command=lambda:test(odpG.get()))
btn8 = ctk.CTkButton(btnf4,textvariable=odpH,command=lambda:test(odpH.get()))

label.pack()
zycia_napis.pack()
pytania_napis.pack()
btnf.pack(side = LEFT)
btnf.pack()
btnf1.pack()
btnf2.pack()
btnf3.pack()
btnf4.pack()
btn1.pack(side = LEFT)
btn2.pack(side = LEFT)
btn3.pack(side = LEFT)
btn4.pack(side = LEFT)
btn5.pack(side = LEFT)
btn6.pack(side = LEFT)
btn7.pack(side = LEFT)
btn8.pack(side = LEFT)

window.mainloop()