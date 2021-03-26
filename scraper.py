from bs4 import BeautifulSoup
import requests

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
        print('-----------------')
        for index, td in enumerate(tds):
            # Guardar variables del jugador
            if (td.string != None):
                if (index != 2):
                    jugador_info.append(td.string)
            else:
                if (index == 5):
                    # Treure nacionalitat a partir del nom de l'imatge
                elif (index == 7):
                    jugador_info.append(td.a['player_name'])
                else:
                    jugador_info.append('')

        print(jugador_info)
        return jugador_info
    
    def toCSV(self, route):
        # Converteix la matriu de dades en un csv i 
        # el guarda a la ruta indicada per paràmetre
        pass

    def scrape(self):
        # Efectua les 5 crides a getHTML per a obtenir 
        # les 5 ultimes temporades, i per a cada una
        # parseja la taula i l'afegeix a la matriu
        # de dades

        print("Scraping...")
        for season in self._seasons:
            print('Scraping Season ' + season['season'] + '...')
            html = self.__getHTML(season['id'])

            bs = BeautifulSoup(html, 'html.parser')
            trs = bs.findAll('tr')

            for tr in trs:
                row_data = self.__parseRow(tr)
                row_data = [season['season']] + row_data
                self._data.append(row_data)
        
        print("Scraping completat")
