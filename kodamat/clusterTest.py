#!/usr/bin/env python
# -*- coding: utf-8 -*-
from sklearn.cluster import KMeans
import json
import plotly
import plotly.graph_objs as go
from kodamat import app, npDataSet, jsonDataSet

from flask import Flask, request, session, g, redirect, url_for, abort, \
    render_template, flash

debug = False  # Note that this is different from the DEBUG under app.config.update (@todo: I need to look into that one does)

names = []

numClusters = 2

@app.route('/cluster-test')
def cluster_test():

    labels = cluster(npDataSet)

    # transpose to work with Plotly-format (don't remember if it is sklear.cluster or plotly that is counterintuitive)
    dataToChart = npDataSet.transpose()

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