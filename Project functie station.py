import requests
import xmltodict

def stations():
    auth_details = ('b.arkin@hotmail.nl', 'FBmTQQTogDk8JzSBcjzoQspPvlHGYgP2T645VIcAtc4EjGWjaLaXHg')
    api_url1 = 'http://webservices.ns.nl/ns-api-treinplanner?fromStation='
    api_url2 = '&toStation='
    invoer_begin = input("Voer uw beginstation in: ")
    invoer_eind = input("Voer uw eindstation in: ")
    print ("")
    response = requests.get(api_url1 + invoer_begin +api_url2 + invoer_eind, auth=auth_details)

    vertrekXML = xmltodict.parse(response.text)
    if 'error' in vertrekXML.keys():
        return 'Er is geen station gevonden genaamd '
    else:
        for vertrek in vertrekXML['ReisMogelijkheden']['ReisMogelijkheid']:
            if vertrek['AantalOverstappen'] == '0':
                print ("U stapt in op :", invoer_begin)
                for data in vertrek['ReisDeel']["ReisStop"]:
                    print (" -  {:30} Tijd: {}".format(data['Naam'], data['Tijd'][11:16]))
                print ("U stapt uit in:", invoer_eind, "\n")
            else:
                print ("U stapt in op :", invoer_begin + ". Hier moet u:", vertrek['AantalOverstappen'] + "x overstappen.")
                for data in vertrek['ReisDeel']:
                    for each in data["ReisStop"]:
                        print (" -  {:30} Tijd: {}".format(each['Naam'], each['Tijd'][11:16]))
                    if data != vertrek['ReisDeel'][len(vertrek['ReisDeel'])-1]:
                        print (" -  Overstap")
                print ("U stapt uit in:", invoer_eind, "\n")
stations()