from flask import Flask, render_template, request, Response, redirect
import sqlite3
import os
import urllib.parse
from flask import Flask, request, Response, jsonify, redirect
from flask_cors import CORS
import requests

app = Flask(__name__,
            static_url_path='', 
            static_folder='static',
            template_folder='templates')


DB_name = 'datas/data.db'



app = Flask(__name__)
CORS(app)

STRAVA_CLIENT_ID = os.environ.get('STRAVA_CLIENT_ID')
STRAVA_CLIENT_SECRET = os.environ.get('STRAVA_CLIENT_SECRET')
REDIRECT_URI = os.environ.get('REDIRECT_URI')

def exchange_token(code):
    strava_request = requests.post(
        'https://www.strava.com/oauth/token',
        data={
            'client_id': STRAVA_CLIENT_ID,
            'client_secret': STRAVA_CLIENT_SECRET,
            'code': code,
            'grant_type': 'authorization_code'
        }
    )
    return jsonify(strava_request.json())

@app.route('/strava_authorize', methods=['GET'])
def strava_authorize():
    params = {
        'client_id': STRAVA_CLIENT_ID,
        'redirect_uri': REDIRECT_URI,
        'response_type': 'code',
        'scope': 'activity:read_all'
    }
    return redirect('{}?{}'.format(
        'https://www.strava.com/oauth/authorize',
        urllib.parse.urlencode(params)
    ))

@app.route('/strava_token', methods=['GET'])
def strava_token():
    code = request.args.get('code')
    if not code:
        return Response('Error: Missing code param', status=400)
    return exchange_token(code)


########################################################################################################################
#page appelée à l'url : http://localhost:5000/A propos
@app.route('/A_propos')
def A_propos():
    return render_template('A_propos.html')


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
          <a href="http://localhost:5000" class="nomMenu">Géoinformatique</a>
        <ul>
            <li><a href="http://localhost:5000/Consultation" >Consultation des données </a></li>
            <li><a href="http://localhost:5000/A_propos" >A propos</a></li>

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

    return render_template('stravaForm.html')


########################################################################################################################
#page appelée à l'url : http://localhost:5000/
@app.route('/')
def index():
    return render_template('index.html')

########################################################################################################################
#lancé au démarrage de l'application
if __name__ == '__main__':
    app.run(debug=True)
