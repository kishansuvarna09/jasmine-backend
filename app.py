import os
import psycopg2
from dotenv import load_dotenv
from flask import Flask

CREATE_ROOMS_TABLE = ("CREATE TABEL IF NOT EXISTS rooms (id SERIAL PRIMARY KEY, name TEXT);")

CREATE_TEMPS_TABLE = """CREATE TABLE IF NOT EXISTS temperatures (room_id INTEGER, temperature REAL, date TIMESTAMP, FOREIGN KEY(room_id) REFERENCES rooms(id) ON DELETE CASCADE);"""

INSERT_ROOM_RETURN_ID = "INSERT INTO rooms (name) values (%s) RETURNING id;"

GLOBAL_NUMBER_OF_DAYS = """SELECT COUNT(DISTINCT DATE(date)) AS days FROM temperature;"""

GLOBAL_AVERAGE = """SELECT AVG(temperature) AS average FROM temperature;"""

load_dotenv()

app = Flask(__name__)
url = os.getenv("DATABASE_URL")
connection = psycopg2.connect(url)

@app.get('/')
def home():
    return 'Hello World'