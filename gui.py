from tkinter import *
from connection import *
from tkinter import ttk
import xmltodict
import requests

def showMainFrameNL():
    """"Haal de frame van Engels weg en verplaats het met de frame van Nederlands"""
    FunctieVertrektijdenZoekenFrame.pack_forget()
    FunctieVertrektijdenUC.pack_forget()
    FunctieReisplannerFrame.pack_forget()
    FunctieStoringenFrame.pack_forget()
    mainframeNL.pack()

def showVertrekTijdenUC():
    """"Haal de mainframe weg en vervang het met de frame van de functie VertrektijdenUC"""
    mainframeNL.pack_forget()
    FunctieVertrektijdenUC.pack()

def showVertrekTijdenZoeken():
    """"Haal de mainframe weg en vervang het met de frame van de functie Vertrektijdenzoeken"""
    mainframeNL.pack_forget()
    FunctieVertrektijdenZoekenFrame.pack()

def showReisplanner():
    """"Haal de mainframe weg en vervang het met de frame van de functie Reisplanner"""
    mainframeNL.pack_forget()
    FunctieReisplannerFrame.pack()

def showStoringen():
    """"Haal de mainframe weg en vervang het met de frame van de functie Storingen"""
    mainframeNL.pack_forget()
    FunctieStoringenFrame.pack()

def clickedVertrek_TijdenUC():
    """"Als er op de knop wordt gedrukt van Vertrek_TijdenUC, activeer dan de functie showVertrekTijden"""
    showVertrekTijdenUC()

def clickedVertrek_TijdenZoeken():
    """"Als er op de knop wordt gedrukt van Vertrek_TijdenZoeken, activeer dan de functie showVertrekTijdenZoeken"""
    showVertrekTijdenZoeken()

def clickedReisplanner():
    """"Als er op de knop wordt gedrukt van Reisplanner, activeer dan de functie showReisplanner"""
    showReisplanner()

def clickedStoringen():
    """"Als er op de knop wordt gedrukt van Storingen, activeer dan de functie showStoringen"""
    showStoringen()

###########################################################################################
########################      START  MAINFRAME       ######################################
###########################################################################################
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
                command=clickedReisplanner,
                foreground='white',
                background='#3333FF',
                width=20,
                height=4)

button4 = Button(master=mainframeNL,
                text='Storingen',
                command=clickedStoringen,
                foreground='white',
                background='#3333FF',
                width=20,
                height=4)

labelNL.pack()
button1.place(x=310, y=550)
button2.place(x=480, y=550)
button3.place(x=650, y=550)
button4.place(x=820, y=550)
###########################################################################################
########################       EINDE MAINFRAME       ######################################
###########################################################################################

###########################################################################################
################  BEGIN FRAME VAN FUNCTIE VERTREKTIJDEN UC       ##########################
###########################################################################################

FunctieVertrektijdenUC = Frame(master=root, width=200, height=100)          #Start mainframe van Functie Vertrektijden UC
FunctieVertrektijdenUC.pack(fill="both", expand=True)

vertrektijdenUC = Label(master=FunctieVertrektijdenUC,
               text='{}'.format(stations()),
               background='#FFF760',
               foreground='#3333FF',
               font=('', 30, ''),
               width=55,
               height=12)

vertrektijdenUC.pack()
terugknopUC = Button(master=FunctieVertrektijdenUC, text='Terug naar \n hoofdscherm', command=showMainFrameNL,
                   foreground='white', background='#3333FF', width=20, height=4)

terugknopUC.pack(padx=30, pady=20)
FunctieVertrektijdenUC.pack()

###########################################################################################
################  EINDE FRAME VAN FUNCTIE VERTREKTIJDEN UC       ##########################
###########################################################################################

###########################################################################################
################  BEGIN FRAME VAN FUNCTIE VERTREKTIJDEN ZOEKEN   ##########################
###########################################################################################



FunctieVertrektijdenZoekenFrame = Frame(master=root, width=200, height=100)          #Start mainframe van functie Vertrektijden zoeken
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
terugknop = Button(master=FunctieVertrektijdenZoekenFrame, text='Terug naar \n hoofdscherm', command=showMainFrameNL,
                   foreground='white', background='#3333FF',width=20, height=4)
terugknop.pack(padx=30, pady=20)

FunctieVertrektijdenZoekenFrame.pack()
vertrektijdenzoeken

###########################################################################################
################  EINDE FRAME VAN FUNCTIE VERTREKTIJDEN ZOEKEN   ##########################
###########################################################################################

###########################################################################################
#########################  BEGIN FRAME VAN FUNCTIE REISPLANNER   ##########################
###########################################################################################
FunctieReisplannerFrame = Frame(master=root, width=200, height=100)          #Start mainframe van functie Reisplanner
FunctieReisplannerFrame.pack(fill="both", expand=True)

reisplanner = Label(master=FunctieReisplannerFrame,
               text='Welkom bij NS. \n Hier vindt u de meest recente reisinformatie \n van alle stations in Nederland.',
               background='#FFF760',
               foreground='#3333FF',
               font=('', 40, ''),
               width=40,
               height=12)


terugknop = Button(master=FunctieReisplannerFrame, text='Terug naar \n hoofdscherm', command=showMainFrameNL,
                   foreground='white', background='#3333FF',width=20, height=4)
terugknop.pack(padx=30, pady=20)

FunctieReisplannerFrame.pack()
reisplanner

###########################################################################################
#########################  EINDE FRAME VAN FUNCTIE REISPLANNER   ##########################
###########################################################################################

###########################################################################################
#########################  BEGIN FRAME VAN FUNCTIE STORINGEN   ##########################
###########################################################################################
FunctieStoringenFrame = Frame(master=root, width=200, height=100)          #Start mainframe van functie Storingen
FunctieStoringenFrame.pack(fill="both", expand=True)

storingen = Label(master=FunctieStoringenFrame,
               text='Welkom bij NS. \n Hier vindt u de meest recente reisinformatie \n van alle stations in Nederland.',
               background='#FFF760',
               foreground='#3333FF',
               font=('', 40, ''),
               width=40,
               height=12)


terugknop = Button(master=FunctieStoringenFrame, text='Terug naar \n hoofdscherm', command=showMainFrameNL,
                   foreground='white', background='#3333FF',width=20, height=4)
terugknop.pack(padx=30, pady=20)

FunctieStoringenFrame.pack()
storingen

###########################################################################################
#########################  EINDE FRAME VAN FUNCTIE REISPLANNER   ##########################
###########################################################################################
showMainFrameNL()
root.mainloop()