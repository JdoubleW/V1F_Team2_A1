import requests
import xmltodict

def stations():
    auth_details = ('kevin.brekelmans@student.hu.nl', 'z-Xst7CaonnKD2JBnFTrUji9OKI5Wp8wPs_lL-XTQzOgxpo3Cz52xg')
    api_url = 'http://webservices.ns.nl/ns-api-avt?station=Utrecht Centraal'

    response = requests.get(api_url, auth=auth_details)

    vertrekXML = xmltodict.parse(response.text)
    lijst = []
    file_write = open('VertrektijdenUC.txt', 'w')
    for vertrek in vertrekXML['ActueleVertrekTijden']['VertrekkendeTrein'][:5]:
        eindbestemming = vertrek['EindBestemming']
        vertrektijd = vertrek['VertrekTijd']  # 2016-09-27T18:36:00+0200
        vertrektijd = vertrektijd[11:16]  # 18:36
        vervoerder = vertrek['Vervoerder']
        vertrekspoor = vertrek['VertrekSpoor']['#text']

        result = 'Om ' + vertrektijd + ' vertrekt een trein naar ' + eindbestemming + '. Vervoerder is ' + vervoerder + '. De trein vertrekt van spoor ' + vertrekspoor + '\n'
        lijst.append(result)
        file_write.write(result)
    file_write.close()
    file_read = open('VertrektijdenUC.txt', 'r')
    linelist= file_read.read()
    return linelist

print(stations())