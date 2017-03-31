#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
from sklearn.cluster import KMeans
import json
import requests
import plotly
import plotly.graph_objs as go
import plotly.plotly as py
import csv
import sqlite3
import lookup

from flask import Flask, request, session, g, redirect, url_for, abort, \
    render_template, flash

debug = False  # Note that this is different from the DEBUG under app.config.update (@todo: I need to look into that one does)

app = lookup.getApp()

names = []

numClusters = 2

# Load default config and override config from an environment variable
app.config.update(dict(
    DEBUG=True,
    SECRET_KEY='development key',
))

@app.route('/')
def hello_world():
    # Render the Template
    return render_template('cluster-test.html')

@app.route('/cluster-test/')
def cluster_test():

    dataSet = getDataSetFromDatabase()

    labels = cluster(dataSet)

    # transpose to work with Plotly-format (don't remember if it is sklear.cluster or plotly that is counterintuitive)
    dataToChart = dataSet.transpose()

    # create multi dimensional array of data by label
    segmentedData = [[[] for _ in xrange(3)] for _ in xrange(numClusters)]

    for num, label in enumerate(labels):
        print (str(num) + ' ' + str(label))
        segmentedData[label][0].append(dataToChart[0][num])
        segmentedData[label][1].append(dataToChart[1][num])
        segmentedData[label][2].append(dataToChart[2][num])

    if debug:
        print(segmentedData)

    # create traces for plotly
    traces = []
    baseColor = 100
    i = 0
    while i < numClusters:
        trace = go.Scatter3d(
            x=segmentedData[i][0],
            y=segmentedData[i][1],
            z=segmentedData[i][2],
            mode='markers',
            marker=dict(
                size=12,
                line=dict(
                    color='rgba(baseColor+(i*2), baseColor+(i*2), baseColor+(i*2), 0.14)',
                    width=0.5
                ),
                opacity=0.8
            ),
            # @todo: fix names list for plotly
            #text=names
        )
        traces.append(trace)
        i+=1

    layout = go.Layout(
        scene=go.Scene(
            xaxis=go.XAxis(title='Carbs', tickprefix='Carbs ', showtickprefix='first'),
            yaxis=go.YAxis(title='Fat', tickprefix='Fat ', showtickprefix='first'),
            zaxis=go.ZAxis(title='Protein', tickprefix='Protein ', showtickprefix='first')
        ),
        height = 800,
        width = 800,
    )

    fig = go.Figure(data=traces, layout=layout)
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return render_template('cluster-test.html', graphJSON=graphJSON)

def cluster(dataSet):

    kmeans = KMeans(n_clusters=numClusters)
    kmeans.fit(dataSet)

    centroids = kmeans.cluster_centers_
    labels = kmeans.labels_

    if debug:
        print (centroids)
        print (labels)

    return labels

@app.route('/cluster', methods=['POST'])
def update_num_clusters():
    global numClusters
    numClusters = int(request.form['numClustr'])
    return cluster_test()

def getDataSetFromDatabase():
    # @todo update to use sqllite (using function getDataSetFromDatabase() below, rather than separate file db_test.py)
    conn = sqlite3.connect('livs.db')  # create db and establish connection

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

# This was the old method, the format of the returned data might not work with code above.
def getDataSetFromCSV():

    global names
    names = []
    numbers = []
    carbs = []
    fats = []
    proteins = []

    with open('LivsmedelsDB_201611160847_01.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        first = True

        for row in readCSV:
            if first:
                first=False

            else:
                if (len(numbers)<50):
                    name = row[0]
                    number = int(row[1])
                    carb = float(row[4])
                    fat = float(row[5])
                    protein = float(row[6])

                    names.append(name)
                    numbers.append(number)
                    carbs.append(carb)
                    fats.append(fat)
                    proteins.append(protein)
                else:
                    break

        print(names)
        print(numbers)
        print (carbs)
        print(fats)
        print(proteins)

    return np.array((carbs, fats, proteins), dtype=float)