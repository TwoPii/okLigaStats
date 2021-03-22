from bs4 import BeautifulSoup
import requests

class OkLigaScraper():

    def __init__(self):
        #Assignar url
        #Definir temporades
        #Inicialitzar matriu on guardar les dades
        pass

    def __getHTML(self, url):
        #Fer request a la url per a obtenir l'HTML
        pass
    
    def __parseHTML(self, html):
        #A partir d'un html, omple la matriu de dades
        pass

    def __parseRow(self, row):
        #A partir d'una columna html (<tr>), 
        #retorna una llista amb les dades del jugador
        pass
    
    def toCSV(self, route):
        #Converteix la matriu de dades en un csv i 
        #el guarda a la ruta indicada per paràmetre
        pass

    def scrape(self):
        #Efectua les 5 crides a getHTML per a obtenir 
        #les 5 ultimes temporades, i per a cada una
        #parseja la taula i l'afegeix a la matriu
        #de dades
        print("Scrape.")