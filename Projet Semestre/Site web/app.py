from flask import Flask, render_template, request, Response
import sqlite3


app = Flask(__name__,
            static_url_path='', 
            static_folder='static',
            template_folder='templates')


DB_name = 'datas/data.db'

########################################################################################################################
#page appelée à l'url : http://localhost:5000/Architecture
@app.route('/Architecture')
def Architecture():
    str_mapage = """
    <!DOCTYPE html>
    <html lang="fr">
        <head>
        <meta charset="UTF-8">
        <link rel="stylesheet" type="text/css" href="/css/style.css">
        <link href="/fonts/Frutiger.ttf" rel="stylesheet">

        <title>L'architecture de mon site web </title>
        </head>
        <body>
          <!--Menu-->
            <nav>
                <a href="http://localhost:5000" class="nomMenu">MeteoSmith</a>
                <ul>
                    <li><a href="http://localhost:5000/Consultation" >Consultation des données </a></li>
                    <li><a href="http://localhost:5000/M5Stick" >M5stick</a></li>
                    <li><a href="http://localhost:5000/Architecture">L'architecture</a></li>
                    <li><a href="http://localhost:5000/Fonctionnalites">Les fonctionnalités</a></li>
                </ul>
            </nav>
            <article class="post">
                <h1> L'architecture de mon site web </h1>
    
              <img src="/figures/architectureSite2.png">

              <p class="meta">
                Ecrit par Daniella Smith,
                le 23 décembre 2025
              </p>
        
              <!-- Post content -->
              <div class="entry">
                <!-- Article-->
    
                <h2>La base de données </h2>
                <img src="/figures/SQLDiagramme.svg" style="max-height: 400px; width: auto>
                <p class="meta"> Schéma de la base de données. Créée sur <a href="https://drawdb.vercel.app/">DrawDB </a></p>

                <p> J’ai créé la base de données SQLite de la manière suivante.
                Elle contient une table intitulée Mesures, composée des colonnes
                <em>IdMesures, Température, Pression, Hygrométrie et DateTime</em>.
                </p>
            
                <p>
                    La clé primaire est <em>IdMesures</em>, définie en
                    auto-incrémentation.
                    Toutes les colonnes sont déclarées avec la contrainte
                    NOT NULL. Lors de la création de la base de données, le champ <em>DateTime</em> a été défini 
                    comme <em>unique</em> afin d’éviter l’insertion de doublons éventuels présents dans le fichier CSV.
                </p>
    
                <h2>Structure du site</h2>
                <img src="/figures/architectureSite.png">
                <p>
                La structure du site est relativement simple. La page Index, 
                située dans le dossier templates, permet d’accéder à l’ensemble 
                des autres pages du site. Les autres pages sont définies dans le fichier app.py.
                </p>
                
                <p>
                La seule particularité concerne la page de consultation des données 
                et des résultats. Cette page prend la forme d’un formulaire et utilise 
                donc les deux méthodes HTTP GET et POST. La méthode GET est utilisée pour 
                demander des données à partir d’une ressource, tandis que la méthode POST 
                permet d’envoyer des données au serveur.
                </p>
                
                <p>
                Ces méthodes offrent à l’utilisateur la possibilité de choisir lui-même
                les paramètres de consultation. Dans ce cas précis, l’utilisateur peut 
                sélectionner les données à afficher ainsi que la plage de dates souhaitée. 
                J’ai également mis en place une option permettant l'utilisateur de télécharger 
                les données sélectionnées au format CSV.
                </p>

               <h2>Structure des fichiers</h2>
               <pre><code>
                └── Projet Semestre/
                    ├── <span style="color:red; font-weight:bold;">app.py</span>
                    ├── <span class="cyan">templates</span>/
                    │   └── index.html
                    ├── <span class="cyan">datas</span>/
                    │   ├── CreateDb.py
                    │   ├── data.db
                    │   ├── InsertData.py
                    │   └── Meteo.csv
                    └── <span class="cyan">static</span>/
                        ├── <span class="pink">fonts</span>/
                        │   ├── Frutiger.ttf
                        │   ├── Frutiger.woff
                        │   ├── Frutiger_bold.ttf
                        │   └── Frutiger_bold.woff
                        ├── <span class="pink">figures</span>/
                        │   ├── architectureSite.png
                        │   ├── BlockInterface.png
                        │   ├── HEIG-VD.png
                        │   ├── loopBlock.svg
                        │   ├── M5Stick.jpeg
                        │   └── Etc...
                        └── <span class="pink">css</span>/
                            └── style.css
                </code></pre>
                <p class="meta">Créée sur <a href="https://malteiwanicki.github.io/filetree/" > File Tree | draw</a></p>


                <p>Mon site web est structuré autour de trois dossiers principaux : 
                templates, datas et static. Le dossier templates contient index.html, qui constitue la page 
                d’accueil du site.
                </p>
                
                <p> Le dossier datas regroupe la base de données SQLite, 
                le fichier CSV utilisé comme source d’entrée, ainsi que les scripts 
                Python chargé de créer la base de données et d’insérer les données dans la table <em>mesures</em>. 
                Cette séparation permet de centraliser toutes les ressources liées au stockage et au traitement des données.
                </p>
                
                <p>
                Le dossier static rassemble l’ensemble des fichiers frontend 
                servis directement au client, sans traitement par Flask. 
                On y trouve la feuille de style dans le sous dossier css, 
                les images et icônes dans figures, ainsi que les polices 
                d’écriture dans fonts.
                </p>
                
                <p> Le fichier app.py constitue le cœur de l’application. 
                Il importe et utilise toutes les ressources mentionnées ci-dessus, 
                initialise le site web et définit les différentes pages accessibles 
                via les routes Flask.
                </p>
             </div>
            </article>
                <!--Footer/Bas de Page-->
            <footer>
              <a href="https://heig-vd.ch/">
                <img src="/figures/HEIG-VD.png" alt="HEIG logo" class ="logo">
              </a>
              <p>&copy; 2025 MeteoSmith |
                <a href="http://localhost:5000">MeteoSmith</a> |
                <a href="http://localhost:5000/Consultation" >Consultation des données </a>|
                <a href="http://localhost:5000/M5Stick" >M5stick</a>|
                <a href="http://localhost:5000/Architecture" >L'architecture</a>|
                <a href="http://localhost:5000/Fonctionnalites" > Les fonctionnalités</a>|
                <a href="https://www.instagram.com/heigvd_depecg/">Instagram EC+G</a>
              </p>
            </footer>
        </body>
    </html>"""
    return str_mapage
########################################################################################################################
#page appelée à l'url : http://localhost:5000/M5Stick
@app.route('/M5Stick')
def M5Stick():
    str_mapage = """
    <!DOCTYPE html>
    <html lang="fr">
        <head>
        <meta charset="UTF-8">
        <link rel="stylesheet" type="text/css" href="/css/style.css">
        <link href="/fonts/Frutiger.ttf" rel="stylesheet">

        <title>M5Stick</title>
        </head>
        <body>
          <!--Menu-->
          <nav>
            <a href="http://localhost:5000" class="nomMenu">MeteoSmith</a>
            <ul>
              <li><a href="http://localhost:5000/Consultation">Consultation des données </a></li>
              <li><a href="http://localhost:5000/M5Stick">M5stick</a></li>
              <li><a href="http://localhost:5000/Architecture">L'architecture</a></li>
              <li><a href="http://localhost:5000/Fonctionnalites">Problemes</a></li>
            </ul>
          </nav>
          <article class="post">
            <h1> Le fonctionnement du code du M5Stick </h1>
            <img src="/figures/M5Stick.jpeg">
            <p class="meta"> Ecrit par Daniella Smith, le 22 décembre 2025 </p>
            <!-- Post content -->
            <div class="entry">
              <!-- Article-->
              <h2>Introduction</h2>
              <p>Dans le cadre du cours <em>Informatique appliqué</em> de mon bachelor en Génie Territorial, 
              il a été demandé de réaliser un dispositif d’acquisition de données datées (température, 
              pression et hygrométrie). Pour le faire j’ai utilisé le M5 Stick qui permet d’afficher et
               sauvegarder des données et le capteur ENV Unit. </p>
              <h2>L’initialisation</h2>
              <img src="/figures/SetupBlock.svg">
              <p class="meta"> Le bloc d’initialisation </p>

              
              <p> Pour coder le M5 stick, il faut utiliser le logiciel UIFlow2.0 ; 
              il fonctionne avec des blocs et python. Ce bloc correspond à la phase 
              d’initialisation du programme. Il est exécuté une seule fois au démarrage 
              du M5Stick, avant l’exécution de la boucle principale (loop). Dans ce Block 
              <em>set up</em>, j’ai initailisé le hardware du M5 Stick et du capteur. </p>
              
              <h2> La boucle principale</h2>
              <img src="/figures/loopBlock.svg">
              <p class="meta"> Le bloc loop </p>

              
              <p>Le bloc <em>Loop</em> correspond à la boucle principale d’exécution du 
              programme. Il est exécuté en continu tant que le M5Stick est allumé. 
              Chaque itération correspond à un cycle de mesure, d’enregistrement 
              et d’affichage des données. 
              </p>
              
              <p>À chaque itération, le système ouvre le fichier Meteo.csv 
              situé dans la mémoire flash interne du M5Stick en mode ajout. 
              La température, la pression, l’humidité, la date et l’heure sont écrits 
              dans le fichier. Les valeurs sont séparées par un point-virgule " ; ",
              puis le fichier est vidé de son tampon mémoire et refermé à la fin de 
              l’opération. 
              </p>

              <p>Ensuite, le programme lit les données du capteur. La température est 
              récupérée en degrés Celsius, la pression en hectopascals et l’humidité 
              relative en pourcentage. Les valeurs mesurées sont affichées sur l’écran
              du M5Stick. Les champs de texte correspondants sont mis à jour pour 
              afficher les données. J'ai mis un "sleep" à la fin de chaque cycle avant
              le redémarrage de la boucle. Cela permet de chosir la fréquence de la 
              prise des données. Dans cette exemple, il est fixé à une seconde, mais de 
              manière générale pour le captage des données, je l'ai mis entre 10 et 60 
              secondes.
              </p>
              
              <img src="/figures/BlockInterface.png">
              <p class="meta">L'affichage sur le M5 stick </p>

              
              <h2>La date et l’heure : problèmes rencontrés</h2>
              <img src="/figures/BlockTime1.png">
              
              <p>J’ai rencontré plusieurs difficultés lors de l’affichage de la date et 
              de l’heure. En effet, le M5Stick ne peut pas récupérer automatiquement 
              l’heure actuelle sans connexion Wi-Fi. Il a donc été nécessaire de modifier 
              manuellement les paramètres dans le code.
              </p>
                            <p>Pour gérer la date et l’heure, j’ai utilisé la librairie machine et 
              <a href="https://docs.micropython.org/en/latest/library/machine.RTC.html"> la classe RTC</a> 
              (Real Time Clock). Cette classe permet de définir manuellement la date et l’heure,
              puis le M5Stick met ensuite son horloge interne à jour à partir de ces valeurs initiales. 
              Il est nécessaire de réactualiser ces paramètres à chaque fois avant de lancer 
              le code sur l’appareil. 
              </p>
          
              
              
              <p>Il est important de noter qu’à partir du moment où j’ai commencé à modifier 
              le code « à la main », la synchronisation entre les blocs UIFlow et le code 
              généré n’était plus assurée. Autrement dit, si je revenais ensuite 
              modifier les blocs, ces changements n’étaient plus répercutés dans le code 
              Python du M5Stick. J’ai donc choisi de résoudre ce problème en dernier, 
              une fois que les autres fonctionnalités (affichage et écriture des données 
              dans le fichier) étaient finalisées.
              </p>
              <img src="/figures/BlockTime3.png">
              <p class="meta">La diffèrence entre les bloc et le code python que j'ai modifié </p>

            </div>
          </article>
          <!--Footer/Bas de Page-->
          <footer>
            <a href="https://heig-vd.ch/">
              <img src="/figures/HEIG-VD.png" alt="HEIG logo" class="logo">
            </a>
            <p>&copy; 2025 MeteoSmith | <a href="http://localhost:5000">MeteoSmith</a> | <a href="http://localhost:5000/Consultation">Consultation des données </a>| <a href="http://localhost:5000/M5Stick">M5stick</a>| <a href="http://localhost:5000/Architecture">L'architecture</a>| <a href="http://localhost:5000/Fonctionnalites"> Les fonctionnalités</a>| <a href="https://www.instagram.com/heigvd_depecg/">Instagram EC+G</a>
            </p>
          </footer>
        </body>
    </html>"""
    return str_mapage



########################################################################################################################
#page appelée à l'url : http://localhost:5000/Fonctionnalites
@app.route('/Fonctionnalites')
def Fonctionnalites():
    str_mapage = """
    <!DOCTYPE html>
    <html lang="fr">
        <head>
        <meta charset="UTF-8">
        <link rel="stylesheet" type="text/css" href="/css/style.css">
        <title>M5Stick</title>
        </head>
        <body>
            <!--Menu-->
          <nav>
              <a href="http://localhost:5000" class="nomMenu">MeteoSmith</a>
            <ul>
                <li><a href="http://localhost:5000/Consultation" >Consultation des données </a></li>
                <li><a href="http://localhost:5000/M5Stick" >M5stick</a></li>
                <li><a href="http://localhost:5000/Architecture" >L'architecture</a></li>
                <li><a href="http://localhost:5000/Fonctionnalites" >Les fonctionnalités</a></li>
            </ul>
        </nav>
        <article class="post">
            <h1>  Un récapitulatif des fonctionnalités et des problèmes rencontrés </h1>

          <img src="/figures/Fonctionnalités.jpeg">

          <p class="meta">
            Ecrit par Daniella Smith,
            le 23 décembre 2025
          </p>
    
          <!-- Post content -->
              <div class="entry">
                <!-- Article-->
                <h2>Les fonctionnalités</h2>
                <p>La page de consultation des données permet d’afficher chaque type de mesure 
                température, pression et humidité) et de sélectionner l’intervalle de temps correspondant 
                aux données à visualiser. J’ai choisi de définir la date minimale et la date maximale comme 
                étant respectivement la première et la dernière valeurs enregistrées lors de l’acquisition des données.
                Par défaut, si aucune valeur n’est sélectionnée, la date et l’heure sont affichées 
                automatiquement sur la page des résultats.
                </p>
                
                <h3>Exemple </h3>
                <p>
                J'ai pris des données entre le 7 et 9 janvier 2026. 
                Pour tester la page consultation des données je vous propose de prendre 
                le 7 janvier à 23h comme date de début et le 8 janvier à 9h comme date de fin.
                </p>
                <h3>Télécharger les données </h3>
                <p>
                Sur la page des résultats, les données sont présentées sous forme de tableau. 
                Deux boutons fixes sont disponibles : l’un permet de revenir en haut du tableau, 
                tandis que l’autre permet d’exporter les données au format CSV.
                </p>
                
                <p>
                Un cas pratique a été envisagé : un ingénieur se rend sur le
                terrain avec son capteur connecté. En cas d’erreur lors de l’insertion
                des données météorologiques dans son Leica, il peut sélectionner les données nécessaires, 
                les exporter au format CSV et corriger l’erreur systématique.
                </p>

                <h2>Les problèmes rencontrés</h2>
                <h3>Valeur None et 0 dans le fichier d'entrée</h3>
                <p> J’ai constaté que certaines lignes du fichier <em>Meteo.csv</em> 
                contenaient des valeurs <code>None</code> ou <code>0</code>. 
                Afin de résoudre ce problème, j’ai effectué plusieurs modifications 
                à différents endroits du code.
                </p>

                <img src="/figures/noneValue.png">
                <p>Initialement, dans le code du <em>M5Stick</em>, les variables 
                météorologiques étaient initialisées à <code>0</code> dans la boucle 
                d’initialisation. La suppression de cette initialisation a permis de
                 corriger le problème. Cependant, souhaitant conserver le même fichier 
                 de données (plutôt que de le supprimer et de recommencer une nouvelle 
                 acquisition), j’ai décidé d’adapter le script Python <em>InsertData.py</em>.
                </p>
                
                <img src="/figures/noneSolution.png">
                <p>
                J’ai mis en place plusieurs conditions afin de filtrer les données erronées. 
                La condition permet 
                de s’assurer qu’aucune valeur n’est égale à <code>0</code> ou à <code>None</code>.
                Un bloc <code>try/except</code> intercepte les valeurs que le script ne 
                parvient pas à insérer dans la base de données. 
                Dans mon cas, ce mécanisme a permis d’identifier deux occurrences de valeurs 
                <code>None</code>.
                </p>
    
                <img src="/figures/noneSQLresultat.png">
                <p>
                La vérification des résultats dans <em>SQLite</em> confirme que seules les données
                valides ont été conservées dans la base de données.
                </p>
    
                <h2>Sources</h2>
                <img src="/figures/Sources.jpeg">
                <div class="source">
                    <ul class="source">
                      <li class="source"><a href="https://codepen.io/florantara/pen/dROvdb" class="source">Responsive Table HTML and CSS Only</a></li>
                      <li class="source"><a href="https://www.geeksforgeeks.org/python/how-to-create-csv-output-in-flask/" class="source">How to create CSV output in Flask? - GeeksforGeeks </a></li>
                      <li class="source"><a href="https://expertbeacon.com/how-to-create-a-sleek-blog-from-scratch-with-html-and-css/" class="source">How To Create A Sleek Blog From Scratch With HTML And CSS - ExpertBeacon</a></li>
                      <li class="source"><a href="https://docs.micropython.org/en/latest/library/machine.RTC.html" class="source" >class RTC – real time clock — MicroPython latest documentation</a></li>
                      <li class="source"><a href="https://drawdb.vercel.app/editor" class="source" > Editor | drawDB</a></li>
                      <li class="source"><a href="https://www.w3schools.com/" class="source" > w3Schools</a></li>
                      <li class="source"><a href="https://html-css-js.com/css/generator/border-outline/" class="source" > html-css-js.com</a></li>
                      <li class="source"><a href="https://docs.m5stack.com/en/" class="source" > m5stack.com</a></li>
                      <li class="source"><a href="https://malteiwanicki.github.io/filetree/" class="source" > File Tree | draw</a></li>
                      <li class="source"><a href="https://www.colabcodes.com/post/flask-application-structure-organizing-python-web-apps-for-scalability" class="source">Flask Application Structure: Organizing Python Web Apps for Scalability | Colabcodes</a></li>
                    </ul>
                </div>
              </div>
        </article>
            <!--Footer/Bas de Page-->
            <footer>
              <a href="https://heig-vd.ch/">
                <img src="/figures/HEIG-VD.png" alt="HEIG logo" class="logo">
              </a>
              <p>&copy; 2025 MeteoSmith | <a href="http://localhost:5000">MeteoSmith</a> | <a href="http://localhost:5000/Consultation">Consultation des données </a>| <a href="http://localhost:5000/M5Stick">M5stick</a>| <a href="http://localhost:5000/Architecture">L'architecture</a>| <a href="http://localhost:5000/Fonctionnalites"> Les fonctionnalités</a>| <a href="https://www.instagram.com/heigvd_depecg/">Instagram EC+G</a>
              </p>
            </footer>
        </body>
    </html>"""
    return str_mapage


###############################################################################################$
@app.route("/download_csv")
def download_csv():

    # Meme parametres utilisés en ConsultationResultat
    result = request.args
    DateTimeMin = result.get('DateTimeMin') or '2026-01-07 00:00'
    DateTimeMax = result.get('DateTimeMax') or '2026-01-12 23:59'
    show_temp = 'Temperature' in result
    show_press = 'Pression' in result
    show_hum = 'Hygrometrie' in result

    conn = sqlite3.connect(DB_name)
    cursor = conn.cursor()

    columns = []
    columns.append("DateTime")
    if show_temp:
        columns.append("Temperature [°C]")
    if show_press:
        columns.append("Pression [hPa]")
    if show_hum:
        columns.append("Hygrometrie [%]")

    column_str = ", ".join(columns)

    requete = f"""
    SELECT {column_str}
    FROM Mesures
    WHERE datetime(DateTime) BETWEEN datetime(?) AND datetime(?) 
    ORDER BY DateTime;
    """

    res = cursor.execute(requete, (DateTimeMin, DateTimeMax))
    mesures = res.fetchall()
    conn.close()

    # Build CSV string
    csv_data = ",".join(columns) + "\n"
    for row in mesures:
        csv_data += ",".join(str(v) for v in row) + "\n"

    # Return CSV as downloadable file
    return Response(
        csv_data,
        mimetype="text/csv",
        headers={"Content-Disposition": "attachment; filename=exportedData.csv"}
    )

###########################################
@app.route('/ConsultationResultat', methods=["GET", "POST"])
def ConsultationResultat():
    result = request.args
    DateTimeMin = result.get('DateTimeMin') or '2026-01-07 00:00'
    DateTimeMax = result.get('DateTimeMax') or '2026-01-12 23:59'
    show_temp = 'Temperature' in result
    show_press = 'Pression' in result
    show_hum = 'Hygrometrie' in result

    conn = sqlite3.connect(DB_name)
    cursor = conn.cursor()

    columns = []
    columns.append("DateTime")
    if show_temp:
        columns.append("Temperature [°C]")
    if show_press:
        columns.append("Pression [hPa]")
    if show_hum:
        columns.append("Hygrometrie [%]")

    column_str = ", ".join(columns)

    requete = f"""
    SELECT {column_str}
    FROM Mesures
    WHERE datetime(DateTime) BETWEEN datetime(?) AND datetime(?) 
    ORDER BY DateTime;
    """

    res = cursor.execute(requete, (DateTimeMin, DateTimeMax))
    mesures = res.fetchall()

    str_mapage = """
<!DOCTYPE html>
<html><head><meta charset="UTF-8">
<link rel="stylesheet" type="text/css" href="/css/style.css">
<title>Données météo</title>
</head>
<body>
  <div id="top"></div>
  <!--Menu-->
      <nav>
          <a href="http://localhost:5000" class="nomMenu">MeteoSmith</a>
        <ul>
            <li><a href="http://localhost:5000/Consultation" >Consultation des données </a></li>
            <li><a href="http://localhost:5000/M5Stick" >M5stick</a></li>
            <li><a href="http://localhost:5000/Architecture" >L'architecture</a></li>
            <li><a href="http://localhost:5000/Fonctionnalites" >Les fonctionnalités</a></li>
        </ul>
    </nav>
    
    <div class="table-wrapper">
        <table border='1' class="fl-table">
"""

    for col in columns:
        str_mapage += f"<th>{col}</th>"
    str_mapage += "</tr>"

    """"""

    for row in mesures:
        str_mapage += "<tr>"
        for value in row:
            str_mapage += f"<td>{value}</td>"
        str_mapage += "</tr>"
    str_mapage = str_mapage + """
    
    </div></table> """
    query_string = request.query_string.decode()
    str_mapage += f""" 
    <div id="footer-buttons"> 
        <a href="/download_csv?{query_string}" class="buttonClass">⬇ Exporter les données (format .csv)</a> 
        <a href="#top" class="buttonClass">↑ Retourner en haut de la table</a> 
    </div> 
    <div id="bottom"></div>
    </body></html>
"""
    return str_mapage

########################################################################################################################
#page appelée à l'url : http://localhost:5000/Consultation
@app.route('/Consultation')
def Consultation():
    conn = sqlite3.connect(DB_name)
    cursor = conn.cursor()
    cursor.execute('SELECT IdMesure, DateTime FROM Mesures;')
    mesures = cursor.fetchall()
    conn.close()

    str_mapage = """
    <!DOCTYPE html>
    <html>
        <head>
            <meta charset="UTF-8">
            <link rel="stylesheet" type="text/css" href="/css/style.css">
            <title>Affichage</title>
        </head>
        <body>
          <!--Menu-->
          <nav>
            <a href="http://localhost:5000" class="nomMenu">MeteoSmith</a>
            <ul>
              <li>
                <a href="http://localhost:5000/Consultation">Consultation des données </a>
              </li>
              <li>
                <a href="http://localhost:5000/M5Stick">M5stick</a>
              </li>
              <li>
                <a href="http://localhost:5000/Architecture">L'architecture</a>
              </li>
              <li>
                <a href="http://localhost:5000/Fonctionnalites">Les fonctionnalités</a>
              </li>
            </ul>
          </nav>
          <div class="title">
            <H1>Consulter les données </h1>
          </div>
          <form action="./ConsultationResultat" method="GET">
            <div class="form-row">
              <div class="form-field">
                <label for="DateTimeMin">
                  <h2>Date et heure de début</h2>
                </label>
                <input type="datetime-local" id="DateTimeMin" name="DateTimeMin" value="2026-01-07 00:00">
              </div>
              <div class="form-field">
                <label for="DateTimeMax">
                  <h2>Date et heure de fin</h2>
                </label>
                <input type="datetime-local" id="DateTimeMax" name="DateTimeMax" value="2026-01-12 23:59">
              </div>
            </div>
           
            <div class="checkbox-group">
              <h2>Données à afficher :</h2>
              <label class="switch">
                <input type="checkbox" id="Temperature" name="Temperature" value="Temperature" checked>
                <span class="slider"></span>
                <span class="label-text">Température</span>
              </label>
              <label class="switch">
                <input type="checkbox" id="Pression" name="Pression" value="Pression" checked>
                <span class="slider"></span>
                <span class="label-text">Pression</span>
              </label>
              <label class="switch">
                <input type="checkbox" id="Hygrometrie" name="Hygrometrie" value="Hygrometrie" checked>
                <span class="slider"></span>
                <span class="label-text">Hygrometrie</span>
              </label>
            </div>
            <div id="consultationButton">
              <input type="submit" class="buttonClass" value="Envoyer">
            </div>
          </form>
          <!--Footer/Bas de Page-->
          <footer>
            <a href="https://heig-vd.ch/">
              <img src="/figures/HEIG-VD.png" alt="HEIG logo" class="logo">
            </a>
            <p>&copy; 2025 MeteoSmith | <a href="http://localhost:5000">MeteoSmith</a> | <a href="http://localhost:5000/Consultation">Consultation des données </a>| <a href="http://localhost:5000/M5Stick">M5stick</a>| <a href="http://localhost:5000/Architecture">L'architecture</a>| <a href="http://localhost:5000/Fonctionnalites"> Les fonctionnalités</a>| <a href="https://www.instagram.com/heigvd_depecg/">Instagram EC+G</a>
            </p>
          </footer>
        </body>
    </html>
    """
    return str_mapage


########################################################################################################################
#page appelée à l'url : http://localhost:5000/
@app.route('/')
def index():
    return render_template('index.html')

########################################################################################################################
#lancé au démarrage de l'application
if __name__ == '__main__':
    app.run(debug=True)
