from flask import Flask, render_template, request, Response, redirect, jsonify
import psycopg2
import os
import urllib.parse
from flask_cors import CORS
import requests

app = Flask(__name__,
            static_url_path='', 
            static_folder='static',
            template_folder='templates')


try:
    conn = psycopg2.connect("dbname='data' user='postgres' host='localhost' password='postgres'")
    cursor = conn.cursor()
except:
    print("I am unable to connect to the database")


app = Flask(__name__)
CORS(app)

####################################################################################
# Strava API configuration
##########################################################################################
STRAVA_CLIENT_ID = os.getenv('STRAVA_CLIENT_ID')
STRAVA_CLIENT_SECRET = os.getenv('STRAVA_CLIENT_SECRET')
STRAVA_PORT = int(os.getenv('FLASK_PORT', '3000'))
STRAVA_REDIRECT_URI = f'http://localhost:{STRAVA_PORT}/callback'


class StravaAPI:
    def __init__(self):
        self.base_url = 'https://www.strava.com/api/v3'

    def get_auth_url(self):
        """Generate Strava OAuth authorization URL"""
        return (f"https://www.strava.com/oauth/authorize?"
                f"client_id={STRAVA_CLIENT_ID}&"
                f"redirect_uri={STRAVA_REDIRECT_URI}&"
                f"response_type=code&"
                f"scope=read,activity:read")

    def exchange_code_for_token(self, code):
        """Exchange authorization code for access token"""
        token_url = 'https://www.strava.com/oauth/token'
        data = {
            'client_id': STRAVA_CLIENT_ID,
            'client_secret': STRAVA_CLIENT_SECRET,
            'code': code,
            'grant_type': 'authorization_code'
        }

        response = requests.post(token_url, data=data)
        return response.json()

    def get_activities(self, access_token, start_date, end_date, per_page=200):
        """Fetch activities from Strava API"""
        headers = {'Authorization': f'Bearer {access_token}'}

        # Convert dates to Unix timestamps
        start_timestamp = int(start_date.timestamp())
        end_timestamp = int(end_date.timestamp())

        print(
            f"DEBUG: Fetching activities from {start_date} (timestamp: {start_timestamp}) to {end_date} (timestamp: {end_timestamp})")

        activities = []
        page = 1

        while True:
            params = {
                'after': start_timestamp,
                'before': end_timestamp,
                'per_page': per_page,
                'page': page
            }

            response = requests.get(f'{self.base_url}/athlete/activities',
                                    headers=headers, params=params)

            if response.status_code != 200:
                break

            page_activities = response.json()
            if not page_activities:
                break

            activities.extend(page_activities)
            page += 1

            # Strava API rate limit protection
            if len(page_activities) < per_page:
                break

        print(f"DEBUG: Fetched {len(activities)} activities")
        if activities:
            print(f"DEBUG: First activity date: {activities[0].get('start_date_local')}")
            print(f"DEBUG: Last activity date: {activities[-1].get('start_date_local')}")

        return activities


strava_api = StravaAPI()

########################################################################################################################
#page appelée à l'url : http://localhost:5000/A propos
@app.route('/A_propos')
def A_propos():
    return render_template('A_propos.html')


###########################################
@app.route('/ConsultationResultat', methods=["GET", "POST"])
def ConsultationResultat():

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

    str_mapage = str_mapage + """
    
    </div></table> """
    str_mapage += f""" 

    <div id="bottom"></div>
    </body></html>
"""
    return str_mapage

########################################################################################################################
#page appelée à l'url : http://localhost:5000/Consultation
@app.route('/Consultation')
def Consultation():

    return render_template('stravaForm.html')


########################################################################################################################
#page appelée à l'url : http://localhost:5000/
@app.route('/')
def index():
    return render_template('index.html')

########################################################################################################################
#page appelée à l'url : http://localhost:5000/statistiques
@app.route('/statistiques')
def carte():
    str_mapage = """
<!DOCTYPE html>
<html><head><meta charset="UTF-8">
<link rel="stylesheet" type="text/css" href="/css/style.css">
<title>Données météo</title>
</head>
<body>
<h1>Statistiques</h1>
<div id="map"></div>"""




    str_mapage += """</body></html>"""
    return str_mapage


########################################################################################################################
#lancé au démarrage de l'application
if __name__ == '__main__':
    app.run(debug=True)
