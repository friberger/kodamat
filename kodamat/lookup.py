from flask import Flask, request
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps
from kodamat import app, e

#Create a engine for connecting to SQLite3.
#Assuming salaries.db is in your app root folder

e = create_engine('sqlite:///livs.db')

api = Api(app)


class Livs_Meta(Resource):
    def get(self):
        #Connect to databse
        conn = e.connect()
        #Perform query and return JSON data
        query = conn.execute("select distinct Livsmedelsnamn from livs")
        return {'namn': [i[0] for i in query.cursor.fetchall()]}

class Livs_data(Resource):
    def get(self, livs_nummer):
        conn = e.connect()
        print livs_nummer
        query = conn.execute("select Livsmedelsnamn from livs where Livsmedelsnamn like '%{}%';".format(livs_nummer))
        print query.cursor
        #Query the result and get cursor.Dumping that data to a JSON is looked by extension
        result = {'data': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
        return result
        #We can have PUT,DELETE,POST here. But in our API GET implementation is sufficient

api.add_resource(Livs_data, '/livs/q=<string:livs_nummer>')
api.add_resource(Livs_Meta, '/livsmedel')