import sys
import simplejson as json
import datetime
import decimal
import mariadb
import os
import flask
from flask import request
from flask import Blueprint
from dotenv import load_dotenv

load_dotenv()

flights = Blueprint('flights', __name__)

config = {
    'host': os.getenv("DB_HOST"),
    'port': int(os.getenv("DB_PORT")),
    'user': os.getenv("DB_USER"),
    'password': os.getenv("DB_PASS")
}

def converter(o):
    if isinstance(o, datetime.datetime):
        return o.__str__()

@flights.route('/api/flights/airlines_stats', methods=['GET'])
def airline_stats():
   origin = request.args.get('o')
   dest = request.args.get('dst')
   yearFrom = request.args.get('yf')
   yearTo = request.args.get('yt')
   month = request.args.get('m')
   day = request.args.get('d')

   conn = mariadb.connect(**config)
   cur = conn.cursor()

   query = "select " \
                    "q.carrier, " \
                    "q.airline, " \
                    "q.volume flight_count, " \
                    "round(100 * q.volume / sum(q.volume) over " \
                    "(order by q.airline rows between unbounded preceding and unbounded following),2) market_share_pct, " \
                    "round(100 * (q.`delayed` / q.volume), 2) delayed_pct, " \
                    "round(100 * (q.cancelled / q.volume), 2) cancelled_pct, " \
                    "round(100 * (q.diverted / q.volume), 2) diverted_pct " \
                    "from ( " \
                        "select f.carrier, a.airline, count(*) volume, " \
                        "sum(case when dep_delay > 0 then 1 else 0 end) `delayed`, " \
                        "sum(diverted) diverted, sum(cancelled) cancelled " \
                        "from flights f join airlines a on f.carrier = a.iata_code " \
                        "where " \
                           "f.origin = ? and " \
                           "f.dest = ? and " \
                           "f.year >= ? and " \
                           "f.year <= ?"

   if month is not None:
    query += " and f.month = " + month

   if day is not None:
    query += " and f.day = " + day

   query += " group by a.airline, f.carrier) q order by flight_count desc"
   cur.execute(query,(origin,dest,yearFrom,yearTo))
   row_headers=[x[0] for x in cur.description] 
   rv = cur.fetchall()

   json_data=[]
   for result in rv:
        json_data.append(dict(zip(row_headers,result)))

   return json.dumps(json_data)

@flights.route('/api/flights/airline_delays', methods=['GET'])
def airline_delays():
   origin = request.args.get('o')
   dest = request.args.get('dst')
   airline = request.args.get('a')
   yearFrom = request.args.get('yf')
   yearTo = request.args.get('yt')
   month = request.args.get('m')
   day = request.args.get('d')

   conn = mariadb.connect(**config)
   cur = conn.cursor()

   query = "select " \
                "round(100 * (weather_delayed / total_delayed), 2) weather_delay_pct, " \
                "round(100 * (carrier_delayed / total_delayed), 2) carrier_delay_pct, " \
                "round(100 * (nas_delayed / total_delayed), 2) nas_delay_pct, " \
                "round(100 * (security_delayed / total_delayed), 2) security_delay_pct, " \
                "round(100 * (late_aircraft_delayed / total_delayed), 2) late_aircraft_delay_pct " \
            "from (" \
                "select " \
                        "carrier_delayed, nas_delayed, security_delayed, late_aircraft_delayed, weather_delayed, " \
                        "(carrier_delayed+nas_delayed+security_delayed+late_aircraft_delayed+weather_delayed) total_delayed " \
                "from (" \
                    "select " \
                        "avg(carrier_delay) carrier_delayed, " \
                        "avg(nas_delay) nas_delayed, " \
                        "avg(security_delay) security_delayed, " \
                        "avg(late_aircraft_delay) late_aircraft_delayed, " \
                        "avg(weather_delay) weather_delayed " \
                    "from " \
                        "flights f join airlines a on f.carrier = a.iata_code " \
                    "where " \
                        "f.origin = ? and f.dest = ? and f.carrier = ? and f.year >= ? and f.year <= ?"
   
   if month is not None:
    query += " and f.month = " + month

   if day is not None:
    query += " and f.day = " + day

   query += " group by a.airline, f.carrier) a) b"

   cur.execute(query,(origin, dest, airline, yearFrom, yearTo))
   row_headers=[x[0] for x in cur.description] 
   result = cur.fetchone()
   json_obj=dict(zip(row_headers,result))

   return json.dumps(json_obj)

@flights.route('/api/flights/delays_comparison', methods=['GET'])
def delays_comparison():
   origin = request.args.get('o')
   dest = request.args.get('dst')
   airline = request.args.get('a')
   yearFrom = request.args.get('yf')
   yearTo = request.args.get('yt')
   month = request.args.get('m')
   day = request.args.get('d')

   conn = mariadb.connect(**config)
   cur = conn.cursor()

   query = "select " \
                "avg(carrier_delay) carrier, " \
                "avg(nas_delay) nas, " \
                "avg(security_delay) sec, " \
                "avg(late_aircraft_delay) late_aircraft, " \
                "avg(weather_delay) weather " \
            "from " \
                "flights f " \
            "where " \
                "f.origin = ? " \
                "and f.dest = ? " \
                "and f.carrier = ? " \
                "and f.year >= ? and f.year <= ?"

   if month is not None:
    query += " and f.month = " + month

   if day is not None:
    query += " and f.day = " + day

   query += " union select " \
                "avg(carrier_delay) carrier, " \
                "avg(nas_delay) nas, " \
                "avg(security_delay) sec, " \
                "avg(late_aircraft_delay) late_aircraft, " \
                "avg(weather_delay) weather " \
            "from " \
                "flights f " \
            "where " \
                "f.origin = ? " \
                "and f.dest = ? " \
                "and f.year >= ? and f.year <= ?"

   if month is not None:
    query += " and f.month = " + month

   if day is not None:
    query += " and f.day = " + day

   cur.execute(query,(origin, dest, airline, yearFrom, yearTo, origin, dest, yearFrom, yearTo))

   row_headers=[x[0] for x in cur.description] 
   rv = cur.fetchall()

   json_data=[]
   for result in rv:
        json_data.append(dict(zip(row_headers,result)))

   return json.dumps(json_data, default = converter)