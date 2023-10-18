import customtkinter as ctk
from deep_translator import GoogleTranslator
import random
from Baza import listnum, listword


def pri():
    global y
    global z
    if entryv.get() == GoogleTranslator(source='pl', target='en').translate(y):
        y = random.choice(list2)
        labelv.set(y)
        labelv2.set(GoogleTranslator(source='pl', target='en').translate(y))
        z=z+1
        labelv3.set(str(z)+"/20")
    else:
        y = random.choice(list2)
        labelv.set(y)
        labelv2.set(GoogleTranslator(source='pl', target='en').translate(y))
        z=z+1
        labelv3.set(str(z)+"/20")
        labelv4.set(labelv4.get()-1)
windowgra = ctk.CTk()

list2 = []
for i in range (1,20):
    x = random.choice(listword)
    list2.append(x)
    listword.remove(x)

print (list2)

labelv = ctk.StringVar()
entryv = ctk.StringVar()
labelv2 = ctk.StringVar()
labelv3 = ctk.StringVar()
labelv4 = ctk.IntVar()

z = 0
labelv3.set(str(z)+"/20")
labelv4.set(4)
y = random.choice(list2)
labelv.set(y)
labelv2.set(GoogleTranslator(source='pl', target='en').translate(y))

label = ctk.CTkLabel(windowgra, textvariable = labelv)
label2 = ctk.CTkLabel(windowgra, textvariable = labelv2)
label3 = ctk.CTkLabel(windowgra, textvariable = labelv3)
label4 = ctk.CTkLabel(windowgra, textvariable = labelv4)
button = ctk.CTkButton(windowgra, text = 'Zatwierdz', command=lambda:pri())
entry = ctk.CTkEntry(windowgra, textvariable=entryv)

label.pack()
label2.pack()
label3.pack()
label4.pack()
entry.pack()
button.pack()

windowgra.mainloop()