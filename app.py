import datetime as dt
from dateutil.relativedelta import relativedelta
import numpy as np
import pandas as pd

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify


#################################################
# Database Setup
#################################################

engine = create_engine('sqlite:///hawaii.sqlite')

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save references to the tables
Measurement = Base.classes.measurements
Station = Base.classes.stations

# Create session from Python to the DB
session = Session(engine)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################

app = Flask(__name__)


# /
# Home page.
# List all routes that are available.
@app.route("/")
def welcome():
    return (
        f"<p>Welcome to the Hawaii Climate API!</p>"
        f"<p>Usage:</p>"
        f"/api/v1.0/precipitation<br/>Return the JSON representation of dictionary.<br/><br/>"
        f"/api/v1.0/stations<br/>Return a JSON list of stations from the dataset.<br/><br/>"
        f"/api/v1.0/tobs<br/>Return a JSON list of temperature observations (TOBS) for the previous year. between 8/23/16 and 8/23/17.<br/><br/>"
        f"/api/v1.0/start<br/>Return a JSON list of the minimum temperature, the average temperature, and the max temperature for the dates between the given start date and 8/23/17<br/><br/>."
        f"/api/v1.0/<start>/<end><br/>Calculate TMIN, TAVG, and TMAX.<br/><br/>"
    )
        
  
# /api/v1.0/precipitation
# Convert the query results to a dictionary using date as the key and prcp as the value.
# Return the JSON representation of your dictionary.
@app.route("/api/v1.0/precipitation")
def precipitation():
    precipitation = session.query(Measurement.date, Measurement.prcp).order_by(Measurement.date.desc()).all()
    return jsonify(precipitation)


# /api/v1.0/stations
# Return a JSON list of stations from the dataset.
@app.route("/api/v1.0/stations")
def stations():
    stations = session.query(Station.station, Station.name).order_by(Station.name).all()
    return jsonify(stations)


# /api/v1.0/tobs
# Query the dates and temperature observations of the most active station for the last year of data.
# Return a JSON list of temperature observations (TOBS) for the previous year.
# last 12 months variable
last_twelve_months = '2017-08-23'

@app.route("/api/v1.0/tobs")
def tobs():
    tobs = sessions.query(Meaurement.tobs, Measurement.tobs).order_by(Measurement.date.desc())filter(Meaurement.date >= last_twelve_months).all()
    return jsonify(tobs)


# /api/v1.0/<start> and /api/v1.0/<start>/<end>
# Return a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start or start-end range.
# When given the start only, calculate TMIN, TAVG, and TMAX for all dates greater than and equal to the start date.
# When given the start and the end date, calculate the TMIN, TAVG, and TMAX for dates between the start and end date inclusive.
start_date = '2017-08-23'

@app.route("/api/v1.0/<start>")
def start():
    start = session.query(Meaurement.date,
                    func.min(Measurement.tobs).label("lowest_temp"),
                    func.max(Measurement.tobs).label("highest_temp"),
                    func.avg(Measurement.tobs).label("average_temp")).all()
    print jsonify(start)


@app.route("/api/v1.0/<start>/<end>")
def start_end():
    qry = session.query(Meaurement.date,
                    func.min(Measurement.tobs).label("lowest_temp"),
                    func.max(Measurement.tobs).label("highest_temp"),
                    func.avg(Measurement.tobs).label("average_temp")).all()
    qry.tobs.find()

    def printrecord(qry):
        for record in qry.tobs.find()
            print(record)

    def qry_app():
        temp_result = "y"
        if temp_result = "y"
            start_date = input("Date: ")
            end_date = input("Date: ")


if __name__ == "__main__":
    app.run(debug=True)
