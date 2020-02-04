import pandas as pd

from flask import (
    Flask,
    render_template,
    jsonify)

from flask_sqlalchemy import SQLAlchemy

from sqlalchemy.sql import func


app = Flask(__name__)

# The database URI
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///db/cancellations_m.sqlite"

db = SQLAlchemy(app)


#Create our database model
class Cancellation(db.Model):
    __tablename__ = 'CANCELLATIONS_M'

    id = db.Column(db.Integer, primary_key=True)
    FLIGHT_DATE = db.Column(db.String)
    FLIGHT_DATE_Y = db.Column(db.String)
    CANCELLED = db.Column(db.Integer)
 
    def __repr__(self):
        return '<Cancellation %r>' % (self.name)


# Create database tables
@app.before_first_request
def setup():
    # Recreate database each time for demo
    # db.drop_all()
    db.create_all()


@app.route("/")
def home():
    """Render Home Page."""
    return render_template("index.html")


@app.route("/FLIGHT_DATE")
def flight_date_y_data():
    """Return first year data with cancellations"""

    # Query for the top 10 cancellations data
    results = db.session.query(
        Cancellation.FLIGHT_DATE, 
        (Cancellation.CANCELLED))

    # Create lists from the query results
    FLIGHT_DATE = [result[0] for result in results]
    cancellations = [int(result[1]) for result in results]

    # Generate the plot trace
    trace = {
        "x": FLIGHT_DATE,
        "y": cancellations,
        "type": "bar"
    }
    return jsonify(trace)


@app.route("/FLIGHT_DATE_Y_2015")
def flight_date_data():
    """Return second year and cancellation"""

    # Query for the top cancellations in yearly proportions
    query_statement = db.session.query(Cancellation.filter(FLIGHT_DATE_Y.id == "2015"),
    Cancellation.filter(CANCELLED.id == "2015"))
    df = pd.read_sql_query(query_statement, db.session.bind)

    # Format the data for Plotly
    trace = {
        "x": df["FLIGHT_DATE_Y_2015"].values.tolist(),
        "y": df["CANCELLED"].values.tolist(),
        "type": "bar"
    }
    return jsonify(trace)

@app.route("/FLIGHT_DATE_Y_2016")
def flight_date_data():
    """Return second year and cancellation"""

    # Query for the top cancellations in yearly proportions
    query_statement = db.session.query(Cancellation.filter(FLIGHT_DATE_Y.id == "2016"),
    Cancellation.filter(CANCELLED.id == "2016"))
    df = pd.read_sql_query(query_statement, db.session.bind)

    # Format the data for Plotly
    trace = {
        "x": df["FLIGHT_DATE_Y_2016"].values.tolist(),
        "y": df["CANCELLED"].values.tolist(),
        "type": "bar"
    }
    return jsonify(trace)

@app.route("/FLIGHT_DATE_Y_2017")
def flight_date_data():
    """Return second year and cancellation"""

    # Query for the top cancellations in yearly proportions
    query_statement = db.session.query(Cancellation.filter(FLIGHT_DATE_Y.id == "2017"),
    Cancellation.filter(CANCELLED.id == "2017"))
    df = pd.read_sql_query(query_statement, db.session.bind)

    # Format the data for Plotly
    trace = {
        "x": df["FLIGHT_DATE_Y_2017"].values.tolist(),
        "y": df["CANCELLED"].values.tolist(),
        "type": "bar"
    }
    return jsonify(trace)

@app.route("/FLIGHT_DATE_Y_2018")
def flight_date_data():
    """Return second year and cancellation"""

    # Query for the top cancellations in yearly proportions
    query_statement = db.session.query(Cancellation.filter(FLIGHT_DATE_Y.id == "2018"),
    Cancellation.filter(CANCELLED.id == "2018"))
    df = pd.read_sql_query(query_statement, db.session.bind)

    # Format the data for Plotly
    trace = {
        "x": df["FLIGHT_DATE_Y_2018"].values.tolist(),
        "y": df["CANCELLED"].values.tolist(),
        "type": "bar"
    }
    return jsonify(trace)



if __name__ == '__main__':
    app.run(debug=True)
