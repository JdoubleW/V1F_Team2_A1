from tkinter import *
from connection import *
from tkinter import ttk
import xmltodict
import requests

def showMainFrameNL():
    """"Haal de frame van Engels weg en verplaats het met de frame van Nederlands"""
    FunctieVertrektijdenZoekenFrame.pack_forget()
    FunctieVertrektijdenUC.pack_forget()
    mainframeNL.pack()

def showVertrekTijdenUC():
    mainframeNL.pack_forget()
    FunctieVertrektijdenUC.pack()

def showVertrekTijdenZoeken():
    mainframeNL.pack_forget()
    FunctieVertrektijdenZoekenFrame.pack()

def clickedVertrek_TijdenUC():
    showVertrekTijdenUC()

def clickedVertrek_TijdenZoeken():
    showVertrekTijdenZoeken()


##################################################################################
root = Tk()
mainframeNL = Frame(master=root, width=200, height=100)          #Start mainframe van Nederlands
mainframeNL.pack(fill="both", expand=True)

labelNL = Label(master=mainframeNL,
               text='Welkom bij NS. \n Hier vindt u de meest recente reisinformatie \n van alle stations in Nederland.',
               background='#FFF760',
               foreground='#3333FF',
               font=('', 40, ''),
               width=40,
               height=12)

button1 = Button(master=mainframeNL,
                text='Weergeef vertrektijden \n van Utrecht Centraal',
                command=clickedVertrek_TijdenUC,
                foreground='white',
                background='#3333FF',
                width=20,
                height=4)

button2 = Button(master=mainframeNL,
                text='Weergeef vertrektijden \n van een ander treinstation',
                command=clickedVertrek_TijdenZoeken,
                foreground='white',
                background='#3333FF',
                width=20,
                height=4)

button3 = Button(master=mainframeNL,
                text='Reisplanner',
                foreground='white',
                background='#3333FF',
                width=20,
                height=4)

button4 = Button(master=mainframeNL,
                text='Storingen',
                foreground='white',
                background='#3333FF',
                width=20,
                height=4)

labelNL.pack()
button1.place(x=310, y=550)
button2.place(x=480, y=550)
button3.place(x=650, y=550)
button4.place(x=820, y=550)
##################################################################################
FunctieVertrektijdenUC = Frame(master=root, width=200, height=100)          #Start mainframe van Nederlands
FunctieVertrektijdenUC.pack(fill="both", expand=True)

vertrektijdenUC = Label(master=FunctieVertrektijdenUC,
               text='Welkom bij NS. \n Hier vindt u de meest recente reisinformatie \n van alle stations in Nederland.',
               background='#FFF760',
               foreground='#3333FF',
               font=('', 40, ''),
               width=40,
               height=12)


terugknop = Button(master=FunctieVertrektijdenUC, text='Vorige', command=showMainFrameNL)
terugknop.pack(padx=30, pady=20)

FunctieVertrektijdenUC.pack()
vertrektijdenUC

##################################################################################

FunctieVertrektijdenZoekenFrame = Frame(master=root, width=200, height=100)          #Start mainframe van Nederlands
FunctieVertrektijdenZoekenFrame.pack(fill="both", expand=True)

vertrektijdenzoeken = Label(master=FunctieVertrektijdenZoekenFrame,
               text='Welkom bij NS. \n Hier vindt u de meest recente reisinformatie \n van alle stations in Nederland.',
               background='#FFF760',
               foreground='#3333FF',
               font=('', 40, ''),
               width=40,
               height=12)

zoekveld = Entry(master=FunctieVertrektijdenZoekenFrame)
zoekveld.pack(padx=20, pady=20)
zoekknop = Button(master=FunctieVertrektijdenZoekenFrame, text='Zoek')
zoekknop.pack(padx=10, pady=20)
terugknop = Button(master=FunctieVertrektijdenZoekenFrame, text='Vorige', command=showMainFrameNL)
terugknop.pack(padx=30, pady=20)

FunctieVertrektijdenZoekenFrame.pack()
vertrektijdenzoeken

showMainFrameNL()
root.mainloop()