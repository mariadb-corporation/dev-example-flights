import sys
import simplejson as json
import mariadb
import os
import flask
from flask import request
from flask import Blueprint
from dotenv import load_dotenv

load_dotenv()

airports = Blueprint('airports', __name__)

config = {
    'host': os.getenv("DB_HOST"),
    'port': int(os.getenv("DB_PORT")),
    'user': os.getenv("DB_USER"),
    'password': os.getenv("DB_PASS"),
    'database': os.getenv("DB_NAME"),
    'ssl_ca': os.getenv("SSL_CA")
}

@airports.route('/api/airports', methods=['GET'])
def index():
   conn = mariadb.connect(**config)
   cur = conn.cursor()
   cur.execute("select * from airports order by airport") 
   row_headers=[x[0] for x in cur.description] 
   rv = cur.fetchall()
   json_data=[]
   for result in rv:
        json_data.append(dict(zip(row_headers,result)))
   return json.dumps(json_data)