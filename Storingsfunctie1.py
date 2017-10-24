import requests
import xmltodict


def ongepland_storingen():
    auth_details = ('jannes.faber@student.hu.nl', 'V-sJnmzQn-O_1WsoRJ29fYEecL0hR7glXdadb2FjK91DEZQ6Fh5Iiw')
    api_url = 'http://webservices.ns.nl/ns-api-storingen?station='

    invoer = input("Voer uw station in waar u storingen wil zien: ")
    response = requests.get(api_url + invoer, auth=auth_details)

    storingXML = xmltodict.parse(response.text)
    if 'error' in storingXML.keys():
        return 'Er is geen station gevonden genaamd ' + invoer
    else:
        for storing in storingXML['Storingen']['Ongepland']['Storing']:
            Datum = storing['Datum']
            Tijd = Datum[11:16]  # 18:36
            Dag = Datum[0:10]  # 2017-10-24
            Traject = storing['Traject']
            Reden = storing['Reden']
            Bericht = storing['Bericht']

            result = "Er is een storing gemeld op " + Dag + " om " + Tijd + " Op het traject: " + Traject + " Vanwegen de volgende reden: " + Reden + " Met bericht geving: " + Bericht
            resultaat = []
            resultaat.append(result)
        print("\n Ongeplande storingen: ")
##      return result
        print(result)
        print('\n Geplanden storingen: \n')

        if 'error' in storingXML.keys():
            return 'Er is geen station gevonden genaamd ' + invoer
        else:
            for storing in storingXML['Storingen']['Gepland']['Storing']:
                Periode = storing['Periode']
                Traject = storing['Traject']
                Bericht = storing['Bericht']

                result = "Geplande storing zal plaats vinden op: " + Periode + " Op het traject: " + Traject + " Met bericht geving: " + Bericht
                resultaat = []
                resultaat.append(result)
                print(result)
        return result
##      print(result)


print(ongepland_storingen())
