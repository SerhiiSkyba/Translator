import string
from tkinter import *
from Baza import listnum  #nr 
from Baza import listword  #slowo
import random
window = Tk()

nr = random.choice(listnum)
slowo = random.choice(listword)
odpP = nr



def sprawdzenie(x):
    global punktyV
    



odpP = StringVar()  #poprawna odpowiedz z bazy
odpA = StringVar()  #odpowiedzi a - f, jedna to poprawna pozostale to losowe z bazy
odpB = StringVar()
odpC = StringVar()
odpD = StringVar()
odpE = StringVar()
odpF = StringVar()

punkty = StringVar()  #punkty wyswietlane
punktyV = 0   #variable dla punktow

pomylka = 0  #licznik pomylek, jesli =4 to koniec gry
btnf = Frame(window,height=16,width=60)
btn1 = Button(btnf,textvariable=odpA,height="8",width="20")
btn2 = Button(btnf,textvariable=odpB,height="8",width="20")
btn3 = Button(btnf,textvariable=odpC,height="8",width="20")
btn4 = Button(btnf,textvariable=odpD,height="8",width="20")
btn5 = Button(btnf,textvariable=odpE,height="8",width="20")
btn6 = Button(btnf,textvariable=odpF,height="8",width="20")


btnf.pack(anchor=S)
btn1.grid(column=1,row=2)
btn2.grid(column=2,row=2)
btn3.grid(column=3,row=2)
btn4.grid(column=1,row=3)
btn5.grid(column=2,row=3)
btn6.grid(column=3,row=3)

window.mainloop()