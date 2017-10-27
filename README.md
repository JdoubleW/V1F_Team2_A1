# Team 2 Actuele vertrektijden op de NS Kaartverkoopautomaat

Klant beschrijving:
Om de Servicemedewerkers op de stations te ontlasten bestaat de wens om de reiziger op de NS Kaartverkoopautomaat de mogelijkheid te geven de actuele vertrekinformatie op te vragen. Dezelfde functie bestaat reeds op de NS website en in de Reisplanner app. Een grote groep reizigers benadert op de stations nog steeds de Servicemedewerkers met vragen over vertrektijden, vertragingen en vertreksporen. Door dezelfde functie ook onder te brengen in de NS Kaartautomaat is het de verwachting dat de druk op Servicemedewerkers afneemt.

## Programma klaarmaken


Om het programma te installeren klikt u op "NsReisplanner.py".
Na dit zal het programma starten en het hoofdvenster wordt getoond

Om het programma te starten gaan we er van uit dat de "NsReisplanner.py" op de root staat van het besturingssysteem. (c:NsReisplanner.py)
U kunt hierop dubbelklikken om het programma uit te voeren.

### randvoorwaarden 

Om de applicatie te kunnen draaien zijn er een aantal tools nodig.
Hieronder kunt u de juiste versie en tool vinden waarmee het programma uitgevoerd kan worden.

```
Python 3.6.0
	Support voor Windows, Mac, Linux
	32bit / 64bit
!Voor het runnen van de API is een werkende internetverbinding nodig!
!Het ZIP bestand moet compleet blijven, er mag niks uit het bestand gehaald worden!

```

### Het installeren


Om aanpassingen te kunnen verrichten aan het script kan er gekozen worden om het python script te wijzigen. Voor de ontwikkeling van het script hebben we gebruik gemaakt van het programma PyCharm gemaakt door Jetbrains. Hou rekening met dat er licentie kosten zijn verbonden aan het programma.

Het installeren van Python 3.6.0 en Pycharm op Windows (Als u de code niet wilt bewerken is Pycharm niet nodig):

1.Download de installer voor Python 3.6.0: 		https://www.python.org/ftp/python/3.6.0/python-3.6.0-amd64.exe
					  
2.Voer de installer uit en installeer Python 3.6.0

3.Maak een account aan bij JetBrains voor Pycharm: 	Student(gratis): https://www.jetbrains.com/shop/eform/students
						  	Geen student:	   https://account.jetbrains.com/login
 
4.Download hier de installer van Pycharm: 		https://www.jetbrains.com/pycharm/download/#section=windows
					
5.Voer de installer uit en installeer Pycharm
 -Start Pycharm op, u krijgt nu een venster te zien, log hier in met het eerder aangemaakte JetBrains account
 -Daarna krijg je de vraag of je instellingen van eerdere PyCharm edities wilt importeren. Je hebt waarschijnlijk nog niet eerder in Python geprogrammeerd, kies dan voor de onderste optie en klik OK
 -Het startscherm wordt geopend, klik OK om de voorgesteld initiële configuratie te accepteren
 -We gaan eerst instellen welke versie van Python PyCharm moet gebruiken:
 	• Klik op Configure en daarna op Settings (Windows).
	• Klik op Project Interpreter.
	• Kies in het drop-downmenu voor de geïnstalleerde versie van Python (3.6.0) en klik op OK!
	• !! soms staat de juiste versie er (nog) niet tussen. Herstart PyCharm om dit te verhelpen!!

6.Pycharm (en Python 3.6.0 zijn) is nu succesvol geïnstalleerd


```
Voorbeeld script:

Als we als input "Den Bosch" invullen, verwachten we als output alle treinen die op dit moment vertrekken vanaf Den Bosch, wie de vervoerder is en vanaf welk spoor die vertrekt.
Bijvoorbeeld {om 14:03 vertrekt een trein naar Dordrecht. Vervoerder is NS. De trein vertrekt van spoor 6b}
Als we als input een station invullen wat niet bestaat bijvoorbeeld "bestaatniet", dan is de output "Er is geen station gevonden genaamd bestaatniet".


```

### En codering stijl test

Wij maken gebruik van docstrings in the script, het script is te vinden in GitHub
Zie script voor verdere informatie

```
Voorbeeld docstring:
def showMainFrameNL():
    def clickedOngeplandeStoringen():
    """"Als er op de knop wordt gedrukt van Storingen, activeer dan de functie showStoringen"""		<----- docstring
    showOngeplandeStoringen()

def showVertrekTijdenUC():
    """"Haal de mainframe weg en vervang het met de frame van de functie VertrektijdenUC"""		<----- docstring
    mainframeNL.pack_forget()
    FunctieVertrektijdenUC.pack()

```

## Inzetten

Benodigdheden:
-Een Windows machine
-Een werkende internetverbinding
-Het ZIP-bestand met de code
-Python 3.6.0

Het uitvoeren:
-Zorg ervoor dat u op een Windows machine werkt
-Installeer Python 3.6.0 met behulp van het kopje "Installing" hierboven
-Download het ZIP-bestand van GitHub (link hier)
-Voer nu het (naam bestand) uit *Niks uit de folder halen!*

## Gemaakt met

-Pycharm
-Python 3.6.0


## Auteurs

Kevin Brekelmans 	(https://github.com/JdoubleW)
Nawid Hashemi		(https://github.com/NawidJan)
Jannes Faber		(https://github.com/FiatDriver007)
Baris Arkin		(https://github.com/baris333)

## Licentie

Dit project is gelicenseerd onder de MIT-licentie - zie het bestand [LICENSE.md] (LICENSE.md) voor details


