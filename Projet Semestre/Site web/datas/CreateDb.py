
import sqlite3



nomDataBase = "data.db"
nomTable = "Mesures"

# Open only ONE connection
connect = sqlite3.connect(nomDataBase)
# Connect to SQLite database
def CreateDB(connect):
    curseur = connect.cursor()
    curseur.execute("DROP TABLE IF EXISTS Mesures;")
    curseur.execute("""
        CREATE TABLE IF NOT EXISTS Mesures(
            IdMesure INTEGER PRIMARY KEY AUTOINCREMENT, 
            Temperature INTERGER NOT NULL, 
            Pression INTERGER NOT NULL, 
            Hygrometrie  NOT NULL,
            DateTime TEXT NOT NULL UNIQUE
        );
    """)
    connect.commit()

CreateDB(connect)