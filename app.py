# -*- coding: utf-8 -*-
"""
Created on Tue Dec 16 14:36:05 2025

@author: carfa
"""

from flask import Flask, render_template, request, redirect
import os
import sqlite3
import random
import datetime as dt


app = Flask(__name__,
            static_url_path='', 
            static_folder='static',#indique où se trouvent mes fichiers statiques (CSS, figures, fonts)
            template_folder='templates') #indique où sont mes fichiers HTML


DB_name = 'datas/Mesures_Meteo.db'


###############################################################################################################
@app.route('/Affichage')
def Affichage():
    conn = sqlite3.connect(DB_name)
    cursor = conn.cursor()

    # Récupère toutes les données
    cursor.execute("SELECT * FROM Mesures_meteo ORDER BY Timestamp;")
    donnees = cursor.fetchall()
    # Récupère la liste des dates
    cursor.execute("SELECT DateTime FROM Mesures_meteo ORDER BY Timestamp;")
    DateTime = cursor.fetchall() 
    conn.close()
    
    # Construction de la page HTML
    str_mapage="""
<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="UTF-8">
<link rel="stylesheet" type="text/css" href="/css/Affichage.css">
<title>Affichage des données</title>
</head>
<body>

<div class="header">
<h1>Affichage des données</h1>
</div>

<div class="text">
<h2><form action="./AffichageResultat" method="get">
<label for="date">Choisissez une date et une heure:</label>
<select name="code_datetime1" id="code_datetime1">
"""
    # Ajoute chaque date dans la liste déroulante
    for row in DateTime:
     d = row[0]  # la valeur de la date
     str_mapage += f"<option value=\"{d}\">{d}</option>\n"

    str_mapage += """
</select>

<input type="submit" value="Envoyer">
</form></h2>
<table>
<caption> Mesures Météo <caption\>
<tr>
    <th> ID		            </th>
	<th> Timestamp		    </th>
	<th> Date - Heure		    </th>
	<th> Température [C°]	</th>
	<th> Pression [hpa]		    </th>
	<th> humidité [%]	        </th>
</tr>
    """
    for row in donnees:
            str_mapage += (
                f"<tr>"
                f"<td>{row[0]}</td>"
                f"<td>{row[1]}</td>"
                f"<td>{row[2]}</td>"
                f"<td>{row[3]}</td>"
                f"<td>{row[4]}</td>"
                f"<td>{row[5]}</td>"
                f"</tr>\n"
            )

    str_mapage +="""
    </table>
</div>
<div class="footer">
<a href="http://localhost:5000/">Accueil<a/>
</div>
</body>
</html>
"""
    return str_mapage
#########################################################################################
@app.route('/AffichageResultat')
def AffichageResultat():
    # Récupère la date sélectionnée
    code_date = request.args.get('code_datetime1')
        
    conn = sqlite3.connect(DB_name)
    cursor = conn.cursor()
    requete = (
            "SELECT * FROM Mesures_meteo "
            "WHERE DateTime ='" + str(code_date) + "'"
            "ORDER BY Timestamp;"
    )

    cursor.execute(requete)
    lignes=cursor.fetchall()
    conn.close()
    
    # Construit la page HTML
    str_mapage="""
<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="UTF-8">
<link rel="stylesheet" type="text/css" href="/css/Affichage.css">
</head>
<body>
<div class="header">
<h1>Résultat</h1>
</div>

<div class="text">
<table>
<caption> Mesures Météo <caption\>
<tr>
    <th> ID		            </th>
	<th> Timestamp		    </th>
	<th> Date - Heure		</th>
	<th> Température [C°]	</th>
	<th> Pression [hpa]		</th>
	<th> humidité [%]	    </th>
</tr>
"""
    for row in lignes:
            str_mapage += (
                f"<tr>"
                f"<td>{row[0]}</td>"
                f"<td>{row[1]}</td>"
                f"<td>{row[2]}</td>"
                f"<td>{row[3]}</td>"
                f"<td>{row[4]}</td>"
                f"<td>{row[5]}</td>"
                f"</tr>\n"
            )

    str_mapage +="""
</table>
<p><a href="http://localhost:5000/Affichage">Retour<a/></p>
</div>
<div class="footer">
<a href="http://localhost:5000/">Accueil<a/></li></a>
</div>
</body>
</html>
"""

    return str_mapage
########################################################################################################################
#page appelée à l'url : http://localhost:5000/Rapport
@app.route('/Rapport')
def Rapport():
    return render_template('1_Rapport.html')
########################################################################################################################
#page appelée à l'url : http://localhost:5000/Rapport/Introduction
@app.route('/Rapport/Introduction')
def Introduction():
    return render_template('2_Introduction.html')
########################################################################################################################
#page appelée à l'url : http://localhost:5000/Rapport/Acquisition
@app.route('/Rapport/Acquisition')
def Acquisition():
    return render_template('3_Acquisition.html')
########################################################################################################################
#page appelée à l'url : http://localhost:5000/Rapport/Traitement
@app.route('/Rapport/Traitement')
def Traitement():
    return render_template('4_Traitement.html')
########################################################################################################################
#page appelée à l'url : http://localhost:5000/Rapport/Construction
@app.route('/Rapport/Construction')
def Construction():
    return render_template('5_Construction.html')
########################################################################################################################
#page appelée à l'url : http://localhost:5000/Rapport/Difficultes
@app.route('/Rapport/Difficultes')
def Difficultes():
    return render_template('6_Difficultes.html')
########################################################################################################################
#page appelée à l'url : http://localhost:5000/Rapport/Conclusion
@app.route('/Rapport/Conclusion')
def Conclusion():
    return render_template('7_Conclusion.html')
########################################################################################################################
#page appelée à l'url : http://localhost:5000/
@app.route('/')
def index():
    return render_template('0_index.html')

########################################################################################################################
#lancé au démarrage de l'application
if __name__ == '__main__':
    app.run(debug=True)
