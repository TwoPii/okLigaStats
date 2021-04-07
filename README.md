# okLigaStats
## Instal·lació
+ Instal·lar Python.
+ Instal·lar virtualenv amb "python3 -m pip install --user virtualenv"
+ Crear entorn virtual amb "python3 -m venv env"
+ Per a Windows, executar ".\env\Scripts\activate.bat" en cas de cmd i ".\env\Scripts\Activate.ps1" en cas de Powershell.
+ Per a Linux/Mac, executar ".\env\bin\activate"
+ Instal·lar llibreries mitjançant "python -m pip install -r requirements.txt"
+ Executar script amb "./main.py"
+ Per a sortir, executar "deactivate"

## Context 
El conjunt de dades escollit per fer la nostra pràctica és la taula de golejadors de l'OK Liga de les últimes 5 temporades. Conseqüentment, el lloc web triat és el lloc web de la Real Federación Española de Patinaje ja que l'OK Liga pertany en aquesta federació. 

## Definir un títol pel dataset
Taula golejadors de l'OK Liga

## Descripció del dataset
El dataset està format per tots els jugadors que han marcat gols en aquesta lliga durant les últimes 5 temporades, és a dir, des de la temporada 2016/17 fins la temporada actual.

## Representació gràfica 

Primerament, us mostrem una de les taules on aplicarem web scraping, està formada pels golejadors de la temporada actual. No obstant, la nostra pràctica consistirà en unir els registres de les últimes 5 temporades. 

![image](https://user-images.githubusercontent.com/81186583/112234353-a3dc9200-8c3c-11eb-8383-d1428e1a1d56.png)

Per altra banda, a partir del dataset resultant del scraping, hem creat el següent gràfic dels TOP 10 golejadors unint les últimes temporades.

![image](https://user-images.githubusercontent.com/81186583/113789224-048cc400-973f-11eb-9a34-9f7207ac0bb5.png)


## Contingut 

Cada registre és un jugador únic per cada temporada, és a dir, no pot haver-hi dos registres del mateix jugador a la mateixa temporada. 

Com ja hem dit, el període de temps són les últimes 5 temporades. Tot i això, ens agradaria puntualitzar que només recollim aquest període de temps ja que només hi ha registres a partir de la temporada 2016/17. 

El dataset té els següents camps:

+ Temporada: Temporada en la qual el golejador ha fet els gols

+ Rank: Ranking ordenat de golejadors per temporada. Per tant, aquest índex no serà únic sino que hi haurà 5 rankings simultanis, és a dir, per exemple hi haurà 5 índexs amb valor 1 per cada pitxitxi de cada temporada.

+ Equip: Les sigles del club del qual forma part el golejador.

+ Escut: Imatge de l'escut del club del golejador.

+ Nacionalitat: Bandera nacional del país del golejador corresponent.

+ Jugador: Cognoms i nom del golejador corresponent, en aquest ordre.

+ Gols: Número de gols marcats pel jugador en aquella temporada.

+ PJ: Número de partits jugats pel jugador en aquella temporada

+ Gpp: Gols per partit del golejador en qüestió en aquella temporada.

+ Asist: Número d'assistències del jugador en aquella temporada.

+ App: Assistències per partit del jugador en aquella temporada.

+ Pen: Proporció d'encert en penaltis del jugador en aquella temporada. Aquesta variable és una fracció de valors enters.

+ Pen %: Percentatge d'encert en penaltis del jugador corresponent en aquella temporada. 

+ FD: Proporció d'encert en faltes directes del jugador en aquella temporada. Aquesta variable és una fracció de valors enters.

+ FD %: Percentatge d'encert en faltes directes del jugador corresponent en aquella temporada. 

+ Az: Número de targetes blaves del jugador en aquella temporada.

+ Azpp: Número de targetes blaves per partit del golejador en aquella temporada.

+ Rj: Número de targetes vermelles del jugador en aquella temporada.

+ Rjpp: Número de targetes vermelles per partit del jugador en aquella temporada.


## Agraïments 
#### Presentar el propietari del conjunt de dades. És necessari incloure cites d'anàlisis anteriors o, en cas de no haver-les, justificar aquesta cerca amb anàlisis similars.

Com hem comentat anteriorment, el propietari del conjunt de dades és la Real Federación Española de Patinaje. 

Per una banda, hi ha hagut històricament anàlisis d'aquest lloc web per part de diaris esportius i/o clubs que formen part d'aquesta lliga, però mai sobre la taula golejadors.

Únicament, hem pogut trobar aquesta entrada a la Wikipedia de la temporada 2017/18 (temporada que nosaltres també analitzem), on podem veure que hi ha una taula dels màxims golejadors. 

https://en.wikipedia.org/wiki/2017%E2%80%9318_OK_Liga 

![image](https://user-images.githubusercontent.com/81186583/112560185-e8019b00-8dd2-11eb-9406-d43dc6927349.png)

Tot i això, creiem que en aquests anàlisis no s'ha utilitzat web scraping per aquesta raó hem pensat que seria interessant.

## Inspiració 
#### Explicar per què és interessant aquest conjunt de dades i quines preguntes es pretenen respondre. És necessari comparar amb les anàlisis anteriors presentades a l’apartat 6..

Primerament, els dos som uns grans amants de l'esport i particularment un de nosaltres és un fidel aficionat de l'hoquei. 

El principal motiu pel qual vam decidir fer-ho sobre les estadístiques de l'Ok Liga és bàsicament perquè el lloc web de la mateixa federació és bastant senzill, arcaic i no es pot treure "suc" de les dades. Així mateix, les dades trobades en la wikipedia segueixen el mateix format. 

Per tant, vam decidir crear un dataset on es pogués comparar les estadístiques dels golejadors en diferents temporades i, d'aquesta manera, no tenir que anar canviant el filtre de temporada ni de quina taula visualitzar de forma lenta i rudimentària.

Així doncs, amb aquest dataset hem volgut analitzar les principals estadístiques de l'hoquei dels grans golejadors d'aquesta lliga com ara gols, assistències, targetes, etc. 
Per poder respodre les següents preguntes: Qui ha sigut el màxim golejador les últimes 5 temporades? Quin golejador marca més gols per partit jugat? Quin jugador té millor percentatge d'encert en penalits o faltes directes? Quin jugador ha rebut més targetes blaves i vermelles cada temporada?

## Zenodo
https://zenodo.org/record/4670386#.YG3beugzYuU
