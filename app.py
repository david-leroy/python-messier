import flask
from flask import request, jsonify, render_template
import sqlite3

app = flask.Flask(__name__, template_folder='templates')
app.config["DEBUG"] = True

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

#Get all messier
@app.route('/api/v1/resources/messier/all', methods=['GET'])
def api_messier_all():
    conn = sqlite3.connect('bdd-messier.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()
    all_messier = cur.execute('SELECT * FROM messier_table').fetchall()
    return jsonify(all_messier)


@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404


@app.route('/api/v1/resources/messier', methods=['GET'])
def api_filter():
    query_parameters = request.args

    Messier = query_parameters.get('N_messier')
    Magnitude = query_parameters.get('magnitude')
    Constellation_FR = query_parameters.get('constellation_FR')
    Year = query_parameters.get('year')

    query = "SELECT * FROM messier_table WHERE"
    to_filter = []

    if Messier:
        query += ' Messier=? AND'
        to_filter.append(Messier)
    if Magnitude:
        query += ' Magnitude=? AND'
        to_filter.append(Magnitude)
    if Constellation_FR:
        query += ' Constellation_FR=? AND'
        to_filter.append(Constellation_FR)
    if Year:
        query += ' Year=? AND'
        to_filter.append(Year)    
    if not (Messier or Magnitude or Constellation_FR or Year):
        return page_not_found(404)

    query = query[:-4] + ';'

    conn = sqlite3.connect('bdd-messier.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()

    results = cur.execute(query, to_filter).fetchall()

    return jsonify(results)

app.run(threaded=True, port=5000)