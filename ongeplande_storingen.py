import requests
import xmltodict

def ongepland_storingen():
    auth_details = ('jannes.faber@student.hu.nl', 'V-sJnmzQn-O_1WsoRJ29fYEecL0hR7glXdadb2FjK91DEZQ6Fh5Iiw')
    api_url = 'http://webservices.ns.nl/ns-api-storingen?station=Utrecht Centraal'

    response = requests.get(api_url, auth=auth_details)

    storingXML = xmltodict.parse(response.text)
    if storingXML['Storingen']['Ongepland'] == None:
        return 'Er zijn geen storingen op station Utrecht Centraal'
    else:
        file_write = open('OngeplandeStoringen.txt', 'w')
        for storing in storingXML['Storingen']['Ongepland']['Storing']:
            Datum = storing['Datum']
            Tijd = Datum[11:16]  # 18:36
            Dag = Datum[0:10]  # 2017-10-24
            Traject = storing['Traject']
            Reden = storing['Reden']
            Bericht = storing['Bericht']
            Bericht_update = Bericht.replace(".", '\n')
            result = "Er is een storing gemeld op " + Dag + " om " + Tijd + ". Op het traject: " + Traject + '\n' "Vanwegen de volgende reden: " + Reden + '\n' + '\n' "Met bericht geving: " + '\n' + Bericht_update + '\n' + '\n' '\n'

            file_write.write(result)
        file_write.close()
        file_read = open('OngeplandeStoringen.txt', 'r')
        linelist = file_read.read()
        return linelist

print(ongepland_storingen())