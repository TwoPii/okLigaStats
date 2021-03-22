import sys
from scraper import OkLigaScraper

print(sys.version) #Al tractar-se d'un venv, la versió hauria de ser 3.9.2

print("Inici de l'script. Inicialitzant scraper...")
scraper = OkLigaScraper()

print("Scraper Inicialitzat. Comença el web scraping...")
scraper.scrape()

print("Fi del web scraping. Guardant dades en fitxer csv...")
scraper.toCSV("./dataset.csv")

print("Finalitzat.")
