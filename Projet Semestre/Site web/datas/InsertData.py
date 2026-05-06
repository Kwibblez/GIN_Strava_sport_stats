import sqlite3
import csv

nomDataBase = "data.db"
nomTable = "Mesures"

connect = sqlite3.connect(nomDataBase)
curseur = connect.cursor()

cheminFichier = "Meteo.csv"

with open(cheminFichier, "r", encoding="utf-8") as csv_file:
    reader = csv.reader(csv_file, delimiter=";", quotechar='"')

    for line in reader:
        try:
            # Strip whitespace
            line = [x.strip() for x in line]

            # Sauter 'none' ou 0
            if any(x == "" or x == "0" or x == 0 for x in line):
                continue

            # Convertir les valeurs
            temp = float(line[0])
            press = float(line[1])
            hum = float(line[2])
            dateTime = line[3]


            # Inscrer dans la base de données
            curseur.execute(
                "INSERT INTO Mesures (Temperature, Pression, Hygrometrie, DateTime) VALUES (?, ?, ?, ?)",
                (temp, press, hum, dateTime)
            )

        except Exception as e:
            print("Skipping line:", line, "Error:", e)

connect.commit()
connect.close()
