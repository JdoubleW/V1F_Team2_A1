import requests
import xmltodict


def stations():
    auth_details = ('kevin.brekelmans@student.hu.nl', 'z-Xst7CaonnKD2JBnFTrUji9OKI5Wp8wPs_lL-XTQzOgxpo3Cz52xg')
    api_url = 'http://webservices.ns.nl/ns-api-avt?station='

    invoer = input("Voer uw beginstation in: ")
    response = requests.get(api_url + invoer, auth=auth_details)

    vertrekXML = xmltodict.parse(response.text)
    if 'error' in vertrekXML.keys():
        return 'Er is geen station gevonden genaamd ' + invoer
    else:
        lijst = []
        for vertrek in vertrekXML['ActueleVertrekTijden']['VertrekkendeTrein']:
            eindbestemming = vertrek['EindBestemming']
            vertrektijd = vertrek['VertrekTijd']  # 2016-09-27T18:36:00+0200
            vertrektijd = vertrektijd[11:16]  # 18:36
            vervoerder = vertrek['Vervoerder']
            vertrekspoor = vertrek['VertrekSpoor']['#text']

            result = 'Om ' + vertrektijd + ' vertrekt een trein naar ' + eindbestemming + '. Vervoerder is ' + vervoerder + '. De trein vertrekt van spoor ' + vertrekspoor
            lijst.append(result)
        return lijst[0]


print(stations())