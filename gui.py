from tkinter import *
from connection import *
from ongeplande_storingen import *
from geplande_storingen import *
import requests
import xmltodict

def showMainFrameNL():
    """"Haal de frame van Engels weg en verplaats het met de frame van Nederlands"""
    FunctieVertrektijdenZoekenFrame.pack_forget()
    FunctieVertrektijdenUC.pack_forget()
    FunctieOngeplandeStoringenFrame.pack_forget()
    FunctieGeplandeStoringenFrame.pack_forget()
    mainframeNL.pack()

def showVertrekTijdenUC():
    """"Haal de mainframe weg en vervang het met de frame van de functie VertrektijdenUC"""
    mainframeNL.pack_forget()
    FunctieVertrektijdenUC.pack()

def showVertrekTijdenZoeken():
    """"Haal de mainframe weg en vervang het met de frame van de functie Vertrektijdenzoeken"""
    mainframeNL.pack_forget()
    FunctieVertrektijdenZoekenFrame.pack()

def showOngeplandeStoringen():
    """"Haal de mainframe weg en vervang het met de frame van de functie Storingen"""
    mainframeNL.pack_forget()
    FunctieOngeplandeStoringenFrame.pack()

def showGeplandeStoringen():
    """"Haal de mainframe weg en vervang het met de frame van de functie Storingen"""
    mainframeNL.pack_forget()
    FunctieGeplandeStoringenFrame.pack()

def clickedVertrek_TijdenUC():
    """"Als er op de knop wordt gedrukt van Vertrek_TijdenUC, activeer dan de functie showVertrekTijden"""
    showVertrekTijdenUC()

def clickedVertrek_TijdenZoeken():
    """"Als er op de knop wordt gedrukt van Vertrek_TijdenZoeken, activeer dan de functie showVertrekTijdenZoeken"""
    showVertrekTijdenZoeken()

def clickedOngeplandeStoringen():
    """"Als er op de knop wordt gedrukt van Storingen, activeer dan de functie showStoringen"""
    showOngeplandeStoringen()

def clickedGeplandeStoringen():
    """"Als er op de knop wordt gedrukt van Storingen, activeer dan de functie showStoringen"""
    showGeplandeStoringen()

def TreinStationZoeken():
    """"Maak verbinding met de api, kijk wat er staat ingevuld bij de zoekveld en plak dat in de url, haal dan de gegevens op"""
    auth_details = ('kevin.brekelmans@student.hu.nl', 'z-Xst7CaonnKD2JBnFTrUji9OKI5Wp8wPs_lL-XTQzOgxpo3Cz52xg')
    api_url = 'http://webservices.ns.nl/ns-api-avt?station='

    treinstation = ZoekVeld.get()
    response = requests.get(api_url + treinstation, auth=auth_details)

    vertrekXML = xmltodict.parse(response.text)
    if 'error' in vertrekXML.keys():
        foutmelding = "Er is geen station gevonden genaamd " + treinstation
        labelZoeken["text"] = foutmelding
        return 'Er is geen station gevonden genaamd ' + treinstation
    else:
        lijst = []
        fileZoeken_write = open('VertrektijdenZoeken.txt', 'w')
        for vertrek in vertrekXML['ActueleVertrekTijden']['VertrekkendeTrein'][:5]:
            eindbestemming = vertrek['EindBestemming']
            vertrektijd = vertrek['VertrekTijd']  # 2016-09-27T18:36:00+0200
            vertrektijd = vertrektijd[11:16]  # 18:36
            vervoerder = vertrek['Vervoerder']
            vertrekspoor = vertrek['VertrekSpoor']['#text']

            result = 'Om ' + vertrektijd + ' vertrekt een trein naar ' + eindbestemming + '. Vervoerder is ' + vervoerder + '. De trein vertrekt van spoor ' + vertrekspoor + '\n'
            lijst.append(result)
            fileZoeken_write.write(result)
            waarde = labelZoeken["text"] = lijst[0:6]

            continue
        fileZoeken_write.close()
        fileZoeken_read = open('VertrektijdenZoeken.txt', 'r')
        linelist = fileZoeken_read.read()

        return result


###########################################################################################
########################      START  MAINFRAME       ######################################
###########################################################################################
root = Tk()
root.geometry("1920x1080")
mainframeNL = Frame(master=root, width=200, height=100)          #Start mainframe
mainframeNL.pack(fill="both", expand=True)

labelNL = Label(master=mainframeNL,
               text='Welkom bij NS. \n Hier vindt u de meest recente reisinformatie \n van alle stations in Nederland.',
               background='#FFF760',
               foreground='#3333FF',
               font=('', 30, ''),
               width=80,
               height=20)

labelBlue = Label(master=mainframeNL,
               text='Station: Utrecht Centraal',
               background='#3333FF',
               foreground='white',
               font=('', 40, ''),
               width=80,
               height=1)

button_vertrekUC = Button(master=mainframeNL,
                text='Weergeef vertrektijden \n van Utrecht Centraal',
                command=clickedVertrek_TijdenUC,
                foreground='white',
                background='#3333FF',
                width=20,
                height=4)

button_vertrekZoeken = Button(master=mainframeNL,
                text='Weergeef vertrektijden \n van een ander treinstation',
                command=clickedVertrek_TijdenZoeken,
                foreground='white',
                background='#3333FF',
                width=20,
                height=4)

button_ongeplandeStoring = Button(master=mainframeNL,
                text='Ongeplande \n storingen',
                command=clickedOngeplandeStoringen,
                foreground='white',
                background='#3333FF',
                width=20,
                height=4)

button_geplandeStoring = Button(master=mainframeNL,
                text='Geplande \n werkzaamheden',
                command=clickedGeplandeStoringen,
                foreground='white',
                background='#3333FF',
                width=20,
                height=4)

labelBlue.pack()
labelNL.pack()
button_vertrekUC.place(x=430, y=550)
button_vertrekZoeken.place(x=600, y=550)
button_ongeplandeStoring.place(x=770, y=550)
button_geplandeStoring.place(x=930, y=550)
###########################################################################################
########################       EINDE MAINFRAME       ######################################
###########################################################################################

###########################################################################################
################  BEGIN FRAME VAN FUNCTIE VERTREKTIJDEN UC       ##########################
###########################################################################################

FunctieVertrektijdenUC = Frame(master=root, width=200, height=100)          #Start mainframe van Functie Vertrektijden UC
FunctieVertrektijdenUC.pack(fill="both", expand=True)

vertrektijdenUC = Label(master=FunctieVertrektijdenUC,
               text='{} \n'.format(stations()),
               background='#FFF760',
               foreground='#3333FF',
               font=('', 15, ''),
               width=140,
               height=40)

labelBlue = Label(master=FunctieVertrektijdenUC,
               text='Station: Utrecht Centraal',
               background='#3333FF',
               foreground='white',
               font=('', 40, ''),
               width=80,
               height=1)

labelBlue.pack()
vertrektijdenUC.pack()
terugknopUC = Button(master=FunctieVertrektijdenUC, text='Terug naar \n hoofdscherm', command=showMainFrameNL,
                   foreground='white', background='#3333FF', width=20, height=4)

terugknopUC.pack(padx=100, pady=20)
terugknopUC.place(x=0, y=730)
FunctieVertrektijdenUC.pack()

###########################################################################################
################  EINDE FRAME VAN FUNCTIE VERTREKTIJDEN UC       ##########################
###########################################################################################

###########################################################################################
################  BEGIN FRAME VAN FUNCTIE VERTREKTIJDEN ZOEKEN   ##########################
###########################################################################################

FunctieVertrektijdenZoekenFrame = Frame(master=root, width=200, height=100)          #Start mainframe van functie Vertrektijden zoeken
FunctieVertrektijdenZoekenFrame.pack(fill="both", expand=True)

labelBlue = Label(master=FunctieVertrektijdenZoekenFrame,
               text='Station: Utrecht Centraal',
               background='#3333FF',
               foreground='white',
               font=('', 40, ''),
               width=80,
               height=1)
labelBlue.pack()
vertrektijdenzoeken1 = Label(master=FunctieVertrektijdenZoekenFrame,
               text='Voer station in:',
               background='#FFF760',
               foreground='#3333FF',
               font=('', 20, ''),
               width=140,
               height=2)
vertrektijdenzoeken1.pack()

labelZoeken = Label(master=FunctieVertrektijdenZoekenFrame,
               text='',
               background='#FFF760',
               foreground='#3333FF',
               font=('', 15, ''),
               width=140,
               height=30)
labelZoeken.pack()

ZoekVeld = Entry(master=FunctieVertrektijdenZoekenFrame)
ZoekVeld.pack(padx=20, pady=20)
zoekknop = Button(master=FunctieVertrektijdenZoekenFrame, text='Zoek', command=TreinStationZoeken,
                  foreground = 'white', background = '#3333FF', width = 20, height = 4)
zoekknop.pack(padx=10, pady=20)
terugknop = Button(master=FunctieVertrektijdenZoekenFrame, text='Terug naar \n hoofdscherm', command=showMainFrameNL,
                   foreground='white', background='#3333FF',width=20, height=4)
terugknop.pack(padx=30, pady=20)

FunctieVertrektijdenZoekenFrame.pack()
ZoekVeld.place(x=700, y=150)
zoekknop.place(x=688, y=200)
terugknop.place(x=0, y=730)

###########################################################################################
################  EINDE FRAME VAN FUNCTIE VERTREKTIJDEN ZOEKEN   ##########################
###########################################################################################

###########################################################################################
################  BEGIN FRAME VAN FUNCTIE ONGEPLANDE STORINGEN UC   #######################
###########################################################################################
FunctieOngeplandeStoringenFrame = Frame(master=root, width=200, height=100)          #Start mainframe van functie Storingen
FunctieOngeplandeStoringenFrame.pack(fill="both", expand=True)

labelBlue = Label(master=FunctieOngeplandeStoringenFrame,
               text='Station: Utrecht Centraal',
               background='#3333FF',
               foreground='white',
               font=('', 40, ''),
               width=80,
               height=1)
labelBlue.pack()

storingen = Label(master=FunctieOngeplandeStoringenFrame,
               text='{}'.format(ongepland_storingen()),
               background='#FFF760',
               foreground='#3333FF',
               font=('', 14, ''),
               width=140,
               height=50)
storingen.pack()

terugknop = Button(master=FunctieOngeplandeStoringenFrame, text='Terug naar \n hoofdscherm', command=showMainFrameNL,
                   foreground='white', background='#3333FF',width=20, height=4)
terugknop.pack(padx=0, pady=20)

FunctieOngeplandeStoringenFrame.pack()
terugknop.place(x=0, y=730)
###########################################################################################
##############  EINDE FRAME VAN FUNCTIE ONGEPLANDE STORINGEN UC  ##########################
###########################################################################################

###########################################################################################
##################  BEGIN FRAME VAN FUNCTIE GEPLANDE STORINGEN   ##########################
###########################################################################################
FunctieGeplandeStoringenFrame = Frame(master=root, width=200, height=100)          #Start mainframe van functie Storingen
FunctieGeplandeStoringenFrame.pack(fill="both", expand=True)

labelBlue = Label(master=FunctieGeplandeStoringenFrame,
               text='Station: Utrecht Centraal',
               background='#3333FF',
               foreground='white',
               font=('', 40, ''),
               width=80,
               height=1)
labelBlue.pack()

storingen = Label(master=FunctieGeplandeStoringenFrame,
               text='{}'.format(gepland_storingen()),
               background='#FFF760',
               foreground='#3333FF',
               font=('', 14, ''),
               width=140,
               height=50)
storingen.pack()

terugknop = Button(master=FunctieGeplandeStoringenFrame, text='Terug naar \n hoofdscherm', command=showMainFrameNL,
                   foreground='white', background='#3333FF',width=20, height=4)
terugknop.pack(padx=0, pady=20)

FunctieGeplandeStoringenFrame.pack()
terugknop.place(x=0, y=730)
###########################################################################################
################  EINDE FRAME VAN FUNCTIE GEPLANDE STORINGEN     ##########################
###########################################################################################
showMainFrameNL()
root.mainloop()