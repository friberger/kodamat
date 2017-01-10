import numpy as np
from sklearn.cluster import KMeans
import json
import requests
import plotly
import plotly.graph_objs as go
import plotly.plotly as py
import csv

from flask import Flask, request, session, g, redirect, url_for, abort, \
    render_template, flash


app = Flask(__name__)

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
@app.route('/cluster-test/<name>')
def cluster_test():

    # fetch data from csv-file
    dataToChart = getDataSet()

    # cluster that data into the number of clusters specified by user
    labels = cluster(dataToChart.transpose())

    # create 3D array of data by label
    segmentedData = [[[],[],[]],[[],[],[]],[[],[],[]]] # @todo:fix so that number of clusters isn't hard coded

    for num, label in enumerate(labels):
        print (str(num) + ' ' + str(label))
        segmentedData[label][0].append(round(dataToChart[0][num], 2)) # @todo: figure out why rounding was neede here
        segmentedData[label][1].append(round(dataToChart[1][num], 2))
        segmentedData[label][2].append(round(dataToChart[2][num], 2))

    print(segmentedData)

    # create traces for plotly

    traces = []
    baseColor = 100
    i = 0
    while (i < numClusters):
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
            #text=names # @todo: fix names list
        )
        traces.append(trace)
        i+=1

    # trace1 = go.Scatter3d(
    #     x=dataToChart[0],
    #     y=dataToChart[1],
    #     z=dataToChart[2],
    #     mode='markers',
    #     marker=dict(
    #         size=12,
    #         line=dict(
    #             color='rgba(217, 217, 217, 0.14)',
    #             width=0.5
    #         ),
    #         opacity=0.8
    #     ),
    #     text=names
    # )

    # trace2 = go.Scatter3d(
    #     x=centroids.transpose()[0],
    #     y=centroids.transpose()[1],
    #     z=centroids.transpose()[2],
    #     mode='markers',
    #     marker=dict(
    #         size=8,
    #         line=dict(
    #             color='rgba(000, 200, 150, 0.14)',
    #             width = 0.2
    #         )
    #     )
    # )


    layout = go.Layout(
        scene=go.Scene(
            xaxis=go.XAxis(title='Carbs', tickprefix='Carbs ', showtickprefix='first'),
            yaxis=go.YAxis(title='Fat', tickprefix='Fat ', showtickprefix='first'),
            zaxis=go.ZAxis(title='Protein', tickprefix='Protein ', showtickprefix='first')
        )
    )

    fig = go.Figure(data=traces, layout=layout)
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return render_template('cluster-test.html', graphJSON=graphJSON)

@app.route('/add', methods=['POST'])
def update_num_clusters():
    global numClusters
    numClusters = int(request.form['numClustr'])
    return cluster_test()

def getDataSet():
    # Second version, read from csv


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

    # What to do next? Either get all values into dataset format, or read subset
    # if subset, random or what?


    ###############################


    # First hardcoded version

    # kolhydrater, fett, protein
    # 7
    # 8
    # 162 (was 136?) hart brod
    # 163 (was 137?) hart brod
    # 281 (was 236?) Schweizisk potatiskaka rosti fryst varmd
    # 282 (was 237?) Potatiskroketter frysta varmda

    #global name
    #name=['Bordsmargarin typ Milda 70 proc', 'Bordsmargarin typ Milda 60 proc', 'Hart brod Wasa Husman', 'Hart brod Ryvita morkt', 'Schweizisk potatiskaka rosti fryst varmd', 'Potatiskroketter frysta varmda']


    #dataSet = np.array([[0.5, 60, 0.4],
                        # [0.3, 70, 0.2],
                        # [64.4, 2.5, 10],
                        # [57.6, 2.5, 14.58],
                        # [23.4, 11.4, 2.4],
                        # [23.9, 7, 2.76]])

    #return dataSet.transpose()


def cluster(dataSet):

    kmeans = KMeans(n_clusters=numClusters)
    kmeans.fit(dataSet)

    centroids = kmeans.cluster_centers_
    labels = kmeans.labels_

    print (centroids)
    print (labels)

    return labels
    # print(X)
    #print(centroids)
    #print(labels)