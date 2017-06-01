#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask, request, session, g, redirect, url_for, abort, \
    render_template, flash
import sqlite3
import json
import numpy as np

app = Flask(__name__)
debug = False  # Note that this is different from the DEBUG under app.config.update (@todo: I need to look into that one does)

# Load default config and override config from an environment variable
app.config.update(dict(
    DEBUG=True,
    SECRET_KEY='development key',
))

def getDataSetFromDatabase():
    # @todo update to use sqllite (using function getDataSetFromDatabase() below, rather than separate file db_test.py)
    conn = sqlite3.connect('kodamat/livs.db')  # create db and establish connection

    # This enables column access by name: row['column_name']
    conn.row_factory = sqlite3.Row

    curs = conn.cursor()

    result = []
    # hämtar som tupler @todo: kolla Simons anteckningar så att det verkligen var så
    for row in curs.execute('select "Kolhydrater_g", "Fett_g", "Protein_g" from livs'):
        result.append(row)

    result = result[1:]  # skippa första raden, den är kolumnrubriker

    if debug:
        print 'result'
        print result

    conn.close()

    return np.array(result)

npDataSet = getDataSetFromDatabase()

@app.route('/getDataSetJSON', methods=['GET'])
def getDataSetJSON():
    conn = sqlite3.connect('kodamat/livs.db')  # create db and establish connection

    # This enables column access by name: row['column_name']
    conn.row_factory = sqlite3.Row

    curs = conn.cursor()

    rows = curs.execute('select "Livsmedelsnummer", "Livsmedelsnamn", "Kolhydrater_g", "Fett_g", "Protein_g" from livs').fetchall()

    conn.close()
    return json.dumps( [dict(ix) for ix in rows] )


jsonDataSet = getDataSetJSON()

import kodamat.lookup
import kodamat.clusterTest

@app.route('/')
def hello_world():
    # Render the Template
    return render_template('index.html')

@app.route('/food-line')
def food_line():
    print jsonDataSet
    return render_template ('food-line.html', jsonData = jsonDataSet)


