from tkinter import *
from tkinter import ttk

def showMainFrameNL():
    """"Haal de frame van Engels weg en verplaats het met de frame van Nederlands"""
    mainframeENG.pack_forget()
    mainframeNL.pack()

def showMainFrameENG():
    """"Haal de frame van Nederlands weg en verplaats het met de frame van Engels"""
    mainframeNL.pack_forget()
    mainframeENG.pack()

def clickedENG():
    """"De functie showMainFrameENG wordt geactiveerd als er wordt geklikt op de knop."""
    showMainFrameENG()

def clickedNL():
    """"De functie showMainFrameNL wordt geactiveerd als er wordt geklikt op de knop."""
    showMainFrameNL()


##################################################################################


root = Tk()
mainframeNL = Frame(master=root)          #Start mainframe van Nederlands
mainframeNL.pack(fill="both", expand=True)

label = Label(master=mainframeNL,
               text='Welkom bij NS',
               background='yellow',
               foreground='#3333FF',
               font=('', 40, ''),
               width=40,
               height=12)

button1 = Button(master=mainframeNL,
                text='Weergeef vertrektijden \n van Utrecht Centraal',
                foreground='white',
                background='#3333FF',
                width=20,
                height=4)

button2 = Button(master=mainframeNL,
                text='Weergeef vertrektijden \n van Utrecht Centraal',
                foreground='white',
                background='#3333FF',
                width=20,
                height=4)

button3 = Button(master=mainframeNL,
                text='Weergeef vertrektijden \n van Utrecht Centraal',
                foreground='white',
                background='#3333FF',
                width=20,
                height=4)

button4 = Button(master=mainframeNL,
                text='Weergeef vertrektijden \n van Utrecht Centraal',
                foreground='white',
                background='#3333FF',
                width=20,
                height=4)

button_ENG = ttk.Button(master=mainframeNL,
                command=clickedENG)
engels = PhotoImage(file="ENG.gif")
tmi_eng = engels.subsample(3,3)
button_ENG.config(image=tmi_eng)


label.pack()
button1.place(x=310, y=550)
button2.place(x=480, y=550)
button3.place(x=650, y=550)
button4.place(x=820, y=550)
button_ENG.place()

##################################################################################

mainframeENG = Frame(master=root) #Start mainframe van Engels
mainframeENG.pack(fill="both", expand=True)

label = Label(master=mainframeENG,
               text='Welcome to NS',
               background='yellow',
               foreground='#3333FF',
               font=('', 40, ''),
               width=40,
               height=12)

button1 = Button(master=mainframeENG,
                text='Show departure times \n from Utrecht Centraal',
                foreground='white',
                background='#3333FF',
                width=20,
                height=4)

button2 = Button(master=mainframeENG,
                text='Weergeef vertrektijden \n van Utrecht Centraal',
                foreground='white',
                background='#3333FF',
                width=20,
                height=4)

button3 = Button(master=mainframeENG,
                text='Weergeef vertrektijden \n van Utrecht Centraal',
                foreground='white',
                background='#3333FF',
                width=20,
                height=4)

button4 = Button(master=mainframeENG,
                text='Weergeef vertrektijden \n van Utrecht Centraal',
                foreground='white',
                background='#3333FF',
                width=20,
                height=4)

button_NL = Button(master=mainframeENG,
                command=clickedNL,
                background='#3333FF',
                width=10,
                height=4)

button_NL = ttk.Button(master=mainframeENG,
                command=clickedNL)
nederlands = PhotoImage(file="NL.gif")
tmi_nl = nederlands.subsample(3,3)
button_NL.config(image=tmi_nl)


label.pack()
button1.place(x=310, y=550)
button2.place(x=480, y=550)
button3.place(x=650, y=550)
button4.place(x=820, y=550)
button_ENG.place(x=0, y=655)
button_NL.place(x=0, y=655)
showMainFrameNL()
root.mainloop()