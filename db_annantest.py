# DBtoJSON.py
# Author: Vasudev Ram - http://www.dancingbison.com
# Copyright 2014 Vasudev Ram
# DBtoJSON.py is a program to DEMOnstrate how to read
# SQLite database data and convert it to JSON.

import sys
import sqlite3
import simplejson
import urllib2

from flask import Flask

app = Flask(__name__)

@app.route('/hello')
def hello_world():
    print 'Hello, World!'

    response = urllib2.urlopen('http://www.matapi.se/foodstuff/')
    d = simplejson.load(response)
    print(d)
    #print (type(d['nutrientValues']['fat']))
    #print (d['nutrientValues']['fat'])
    #e= d['nutrientValues']
    #d['nutrientValues']=None
    #d.update(e)
    print d.keys()
    print d.values()


    # json {"name":"Dressing majonn\u00e4s fett ca 40% ","number":44,"nutrientValues":{"energyKj":1898,"energyKcal":454,"protein":0.5,"fat":40,"carbohydrates":24,"fibres":0.2,"salt":1.7,"ash":2.1,"water":33.2,"alcohol":0,"monosaccharides":3.1,"disaccharides":18.6,"saccharose":18.6,"wholegrain":0,"saturatedFattyAcids":6.1,"fattyAcid40100":0,"fattyAcid120":0,"fattyAcid140":0,"fattyAcid160":4.2,"fattyAcid180":1.5,"fattyAcid200":0.2,"monounsaturatedFattyAcids":9.8,"fattyAcid161":0,"fattyAcid181":9.8,"zink":0.1}}

    # d {u'nutrientValues': {u'monounsaturatedFattyAcids': 9.8, u'fibres': 0.2, u'protein': 0.5, u'fattyAcid40100': 0, u'saturatedFattyAcids': 6.1, u'wholegrain': 0, u'alcohol': 0, u'energyKcal': 454, u'fattyAcid180': 1.5, u'fattyAcid181': 9.8, u'carbohydrates': 24, u'fattyAcid200': 0.2, u'zink': 0.1, u'fattyAcid120': 0, u'fattyAcid160': 4.2, u'fattyAcid161': 0, u'fattyAcid140': 0, u'fat': 40, u'water': 33.2, u'ash': 2.1, u'saccharose': 18.6, u'salt': 1.7, u'energyKj': 1898, u'disaccharides': 18.6, u'monosaccharides': 3.1}, u'name': u'Dressing majonn\xe4s fett ca 40% ', u'number': 44}

    conn = sqlite3.connect('example.db')

    # This enables column access by name: row['column_name']
    conn.row_factory = sqlite3.Row

    curs = conn.cursor()

    # Create table.
    curs.execute('''DROP TABLE IF EXISTS food''')
    curs.execute('''CREATE TABLE food (name text, number int, fat real)''')

    # Insert a few rows of data.
    e = (
        ('Dressing', 44, 34.5),
        ('Groda', 37, 23.5)
    )

    curs.executemany("INSERT INTO food VALUES (?, ?, ?)", e)
    # curs.execute("INSERT INTO food VALUES ('Gurka ','45',454,0.5,'40')")

    # Commit the inserted rows.
    conn.commit()

    # Now fetch back the inserted data and write it to JSON.
    curs.execute("SELECT * FROM food")
    recs = curs.fetchall()

    print type(recs)
    print 'typ'

    print "DB data as a list w/items with a dict per DB record:"
    rows = [dict(rec).items() for rec in recs]
    print rows

    print "DB data as a list with a dict per DB record:"
    rows = [dict(rec) for rec in recs]
    print rows

    print

    print "DB data as a single JSON string:"
    rows_json = json.dumps(rows)
    print rows_json

    # We can also close the connection if we are done with it.
    conn.close()

    return 'Good-bye World'

@app.route('/')
def minfunktion():
    try:

        print 'Hej'
        conn = sqlite3.connect('example.db')

        # This enables column access by name: row['column_name']
        conn.row_factory = sqlite3.Row

        curs = conn.cursor()

        # Create table.
        curs.execute('''DROP TABLE IF EXISTS stocks''')
        curs.execute('''CREATE TABLE stocks
                 (date text, trans text, symbol text, qty real, price real)''')

        # Insert a few rows of data.
        curs.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.0)")
        curs.execute("INSERT INTO stocks VALUES ('2007-02-06','SELL','ORCL',200,25.1)")
        curs.execute("INSERT INTO stocks VALUES ('2008-03-06','HOLD','IBM',200,45.2)")

        # Commit the inserted rows.
        conn.commit()

        # Now fetch back the inserted data and write it to JSON.
        curs.execute("SELECT * FROM stocks")
        recs = curs.fetchall()

        print "DB data as a list with a dict per DB record:"
        rows = [ dict(rec) for rec in recs ]
        print rows

        print

        print "DB data as a single JSON string:"
        rows_json = json.dumps(rows)
        print rows_json

        cars = (
            (1, 'Audi', 52642),
            (2, 'Mercedes', 57127),
            (3, 'Skoda', 9000),
            (4, 'Volvo', 29000),
            (5, 'Bentley', 350000),
            (6, 'Hummer', 41400),
            (7, 'Volkswagen', 21600)
        )

        print cars
        print type(cars)

    except Exception, e:
        print "ERROR: Caught exception: " + repr(e)
        raise e
        sys.exit(1)

    return 'Hej da'
    # EOF

@app.route('/insert')
def infoga():

    conn = sqlite3.connect('example.db')

    # This enables column access by name: row['column_name']
    conn.row_factory = sqlite3.Row

    dict2= [{"date": "2017-01-05", "symbol": "RHAT", "trans": "BUY", "price": 35.0, "qty": 100.0},
            {"date": "2017-02-06", "symbol": "ORCL", "trans": "SELL", "price": 25.1, "qty": 200.0},
            {"date": "2017-03-06", "symbol": "IBM", "trans": "HOLD", "price": 45.2, "qty": 200.0}]

    curs = conn.cursor()
    conn.execute('insert into stocks values (?,?,?)', [dict2['date'], dict2['symbol'], dict2['trans']])

    # Now fetch back the inserted data and write it to JSON.
    curs.execute("SELECT * FROM stocks")
    recs = curs.fetchall()

    print "DB data as a list with a dict per DB record:"
    rows = [dict(rec) for rec in recs]
    print rows

    print

    print "DB data as a single JSON string:"
    rows_json = json.dumps(rows)
    print rows_json

    return 'slut pa insert'
