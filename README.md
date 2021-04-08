# Pràctica 1: Web scraping: okLigaStats
## Descripció 
Aquesta pràctica ha estat realitzada en el context de l'assignatura "Tipología i cicle de vida de les dades", perteneixent al Màster de Ciència de Dades de la Universitat Oberta de Catalunya. En aquesta, s'aplica web scraping per a extreure dades de la web HockeyPatines de la Real Federación Española de Patinaje i generar un dataset.

## Instal·lació
+ Instal·lar Python.
+ Instal·lar virtualenv amb "python3 -m pip install --user virtualenv"
+ Crear entorn virtual amb "python3 -m venv env"
+ Per a Windows, executar ".\env\Scripts\activate.bat" en cas de cmd i ".\env\Scripts\Activate.ps1" en cas de Powershell.
+ Per a Linux/Mac, executar ".\env\bin\activate"
+ Instal·lar llibreries mitjançant "python -m pip install -r requirements.txt"
+ Executar script amb "./main.py"
+ Per a sortir, executar "deactivate"

## Membres de l'equip
La pràctica ha estat realitzada de manera conjunta per:
+ Armengol Vall, Bernat
+ Bosch Pou, Genís

## Estructura del repositori
En aquest repositori es poden trobar les següents carpetes i fitxers:
+ **csv**: conté el dataset en format csv.
+ **escuts**: conté les imatges dels escuts del club en format png.
+ **pdf**: conté el document final (documentació) de la pràctica.
+ main.py: fitxer de codi principal
+ scraper.py: fitxer de codi que conté els mètodes.
+ requirements.txt: fitxer per a replicar l'entorn virtual amb venv o similars.

## Zenodo
El dataset ha estat publicat en línia a través de Zenodo, un repositori de dades de recerca. Aquest es pot trobar en la següent URL:
https://zenodo.org/record/4670386#.YG3beugzYuU
