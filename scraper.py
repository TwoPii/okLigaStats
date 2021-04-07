from bs4 import BeautifulSoup
import requests
import csv
import pandas as pd 

class OkLigaScraper():

    def __init__(self):
        # Assignar url
        self._url = "http://www.server2.sidgad.es/rfep/rfep_stats_1_"

        # Definir temporades
        self._seasons = [
            {
                'season' : '20/21',
                'id' : 1474,
            }, 
            {
                'season' : '19/20',
                'id' : 1285,
            }, 
            {
                'season' : '18/19',
                'id' : 1004,
            }, 
            {
                'season' : '17/18',
                'id' : 714,
            }, 
            {
                'season' : '16/17',
                'id' : 500,
            }
        ]

        # Inicialitzar matriu on guardar les dades
        self._data = []

    def __getHTML(self, season_id):
        #Fer request a la url per a obtenir l'HTML
        content = {'idc': season_id, 'tipo_stats' : 'goles', 'site_lang' : 'es'}
        response = requests.post(self._url + str(season_id) + '.php', data = content)
        html = response.text
        return html
    
    def __parseHTML(self, html):
        # A partir d'un html, omple la matriu de dades
        pass

    def __parseRow(self, row):
        # A partir d'una row html (<tr>), 
        # retorna una llista amb les dades del jugador
        jugador_info = []
        tds = row.findAll('td')
        for index, td in enumerate(tds):
            # Guardar variables del jugador
            if (td.string != None):
                if (index != 2 and index != 4 and index != 6):
                    jugador_info.append(td.string)
            else:
                if (index == 5):
                    # Treure nacionalitat a partir del nom de l'imatge
                    flag = td.img['src']
                    flag = flag[-6:-4]
                    jugador_info.append(flag)

                elif (index == 7):
                    jugador_info.append(td.a['player_name'])
                
                elif (index == 3):
                    escut = td.img['src']
                    if escut in self._all_escuts:
                        continue
                    else:
                        self._all_escuts.append(escut)

                elif(index == 2 or index == 4 or index == 6):
                    continue

                else:
                    jugador_info.append('')

        return jugador_info
    
    def toCSV(self):
        # Converteix la matriu de dades en un csv i 
        headers = ['Temporada','Rank','Equip','Nacionalitat','Jugador', 'Gols','PJ','Gpp','Asist','App','Pen', 'Pen %','FD','FD %','Az','Azpp','Rj', 'Rjpp']
        df = pd.DataFrame(self._data, index=None, columns=headers)
        df.to_csv('./csv/OKliga.csv', index=False)

    def scrape(self):
        # Efectua les 5 crides a getHTML per a obtenir 
        # les 5 ultimes temporades, i per a cada una
        # parseja la taula i l'afegeix a la matriu
        # de dades

        print("Scraping...")
        self._all_escuts = []
        for season in self._seasons:
            print('Scraping Season ' + season['season'] + '...')
            html = self.__getHTML(season['id'])

            bs = BeautifulSoup(html, 'html.parser')
            trs = bs.findAll('tr')

            for tr in trs:
                row_data = self.__parseRow(tr)
                row_data = [season['season']] + row_data
                self._data.append(row_data)
        
        print(self._all_escuts)
        print("Scraping completat")
