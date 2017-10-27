import requests
import xmltodict

def gepland_storingen():
    auth_details = ('jannes.faber@student.hu.nl', 'V-sJnmzQn-O_1WsoRJ29fYEecL0hR7glXdadb2FjK91DEZQ6Fh5Iiw')
    api_url = 'http://webservices.ns.nl/ns-api-storingen?station=Utrecht Centraal'

    response = requests.get(api_url, auth=auth_details)

    storingXML = xmltodict.parse(response.text)
    if storingXML['Storingen']['Gepland'] == None:
        return 'Er zijn geen werkzaamheden op station Utrecht Centraal'
    else:
        file_write = open('GeplandeStoringen.txt', 'w')
        for storing in storingXML['Storingen']['Gepland']['Storing']:
            Periode = storing['Periode']
            Traject = storing['Traject']
            Bericht = storing['Bericht']
            for karakters in ['<b>', '<br/>', '</p>', '</b>', '<p>']:
                if karakters in Bericht:
                    Bericht = Bericht.replace(karakters,"")

            for speciale_tekens_Bericht in ['Ã¼']:
                if speciale_tekens_Bericht in Bericht:
                    Bericht = Bericht.replace(speciale_tekens_Bericht,"ü")

            for speciale_tekens_Traject in ['Ã¼']:
                if speciale_tekens_Traject in Traject:
                    Traject = Traject.replace(speciale_tekens_Traject, "ü")
            result = "Geplande storing zal plaats vinden op: " + Periode + " Op het traject: " + Traject + " Met bericht geving: " + Bericht + '\n' '\n'

            file_write.write(result)
        file_write.close()
        file_read = open('GeplandeStoringen.txt', 'r')
        linelist = file_read.read()
        return linelist

print(gepland_storingen())