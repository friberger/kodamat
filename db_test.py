#!/usr/bin/env python
# -*- coding: utf-8 -*-

import csv
import sqlite3
import unicodedata
from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    print 'Hello, World!'

    with open('/Users/organization/PycharmProjects/foodcluster/LivsmedelsDB_201611160847_01_liten.csv') as csvfile:
        d = [tuple(line) for line in csv.reader(csvfile)]

    d = tuple(d)

    # d = csv.reader(csvfile, delimiter = ',')
    # data_tuple = ()
    # for row in d:
    #    data_tuple=tuple(row)
    print(d[0])
    print str(len(d[0])) + ' = antal varden'
    # 59 värden

    conn = sqlite3.connect('example.db')

    # This enables column access by name: row['column_name']
    conn.row_factory = sqlite3.Row

    curs = conn.cursor()

    # ('Livsmedelsnamn', 'Livsmedelsnummer', 'Energi (kcal)', 'Energi (kJ)', 'Kolhydrater (g)', 'Fett (g)', 'Protein (g)', 'Fibrer (g)', 'Vatten (g)', 'Alkohol (g)', 'Aska (g)', 'Monosackarider (g)', 'Disackarider (g)', 'Sackaros (g)', 'Fullkorn totalt (g)', 'Sockerarter (g)', 'Summa m\xc3\xa4ttade fettsyror (g)', 'Fettsyra 4:0-10:0 (g)', 'Fettsyra 12:0 (g)', 'Fettsyra 14:0 (g)', 'Fettsyra 16:0 (g)', 'Fettsyra 18:0 (g)', 'Fettsyra 20:0 (g)', 'Summa enkelom\xc3\xa4ttade fettsyror (g)', 'Fettsyra 16:1 (g)', 'Fettsyra 18:1 (g)', 'Summa flerom\xc3\xa4ttade fettsyror (g)', 'Fettsyra 18:2 (g)', 'Fettsyra 18:3 (g)', 'Fettsyra 20:4 (g)', 'EPA (Fettsyra 20:5) (g)', 'DPA (Fettsyra 22:5) (g)', 'DHA (Fettsyra 22:6) (g)', 'Kolesterol (mg)', 'Retinol (\xc2\xb5g)', 'Vitamin A (\xc2\xb5g)', '\xce\xb2-Karoten (\xc2\xb5g)', 'Vitamin D (\xc2\xb5g)', 'Vitamin E (mg)', 'Vitamin K (\xc2\xb5g)', 'Tiamin (mg)', 'Riboflavin (mg)', 'Vitamin C (mg)', 'Niacin (mg)', 'Niacinekvivalenter (mg)', 'Vitamin B6 (mg)', 'Vitamin B12 (\xc2\xb5g)', 'Folat (\xc2\xb5g)', 'Fosfor (mg)', 'Jod (\xc2\xb5g)', 'J\xc3\xa4rn (mg)', 'Kalcium (mg)', 'Kalium (mg)', 'Magnesium (mg)', 'Natrium (mg)', 'Salt (g)', 'Selen (\xc2\xb5g)', 'Zink (mg)', 'Avfall (skal etc.) (%)')

    fields = (
    'Livsmedelsnamn', 'Livsmedelsnummer', 'Energi (kcal)', 'Energi (kJ)', 'Kolhydrater (g)', 'Fett (g)', 'Protein (g)',
    'Fibrer (g)', 'Vatten (g)', 'Alkohol (g)', 'Aska (g)', 'Monosackarider (g)', 'Disackarider (g)', 'Sackaros (g)',
    'Fullkorn totalt (g)', 'Sockerarter (g)', 'Summa m\xc3\xa4ttade fettsyror (g)', 'Fettsyra 4:0-10:0 (g)',
    'Fettsyra 12:0 (g)', 'Fettsyra 14:0 (g)', 'Fettsyra 16:0 (g)', 'Fettsyra 18:0 (g)', 'Fettsyra 20:0 (g)',
    'Summa enkelom\xc3\xa4ttade fettsyror (g)', 'Fettsyra 16:1 (g)', 'Fettsyra 18:1 (g)',
    'Summa flerom\xc3\xa4ttade fettsyror (g)', 'Fettsyra 18:2 (g)', 'Fettsyra 18:3 (g)', 'Fettsyra 20:4 (g)',
    'EPA (Fettsyra 20:5) (g)', 'DPA (Fettsyra 22:5) (g)', 'DHA (Fettsyra 22:6) (g)', 'Kolesterol (mg)',
    'Retinol (\xc2\xb5g)', 'Vitamin A (\xc2\xb5g)', '\xce\xb2-Karoten (\xc2\xb5g)', 'Vitamin D (\xc2\xb5g)',
    'Vitamin E (mg)', 'Vitamin K (\xc2\xb5g)', 'Tiamin (mg)', 'Riboflavin (mg)', 'Vitamin C (mg)', 'Niacin (mg)',
    'Niacinekvivalenter (mg)', 'Vitamin B6 (mg)', 'Vitamin B12 (\xc2\xb5g)', 'Folat (\xc2\xb5g)', 'Fosfor (mg)',
    'Jod (\xc2\xb5g)', 'J\xc3\xa4rn (mg)', 'Kalcium (mg)', 'Kalium (mg)', 'Magnesium (mg)', 'Natrium (mg)', 'Salt (g)',
    'Selen (\xc2\xb5g)', 'Zink (mg)', 'Avfall (skal etc.) (%)')

    fields_list = list(fields)

    fields_list = fields_list[2:]

    for x in range(0, len(fields_list)):
        fields_list[x] = fields_list[x].replace(' ', '_').replace('\xc3\xa4','a').replace('\xc2\xb5', 'mikro').replace('\xce\xb2','beta').replace('(','').replace(')','').replace(':','').replace('.','').replace('%','')

    for x in range(0, len(fields_list)):
        fields_list[x] += ' real'

    fields_tuple = tuple(fields_list)

    print fields_tuple
    others = d[0][2:]

    print others

    sql_fill = ('name text', 'number text', others)
    sql_create = '''CREATE TABLE food2 ('name text', 'number text', %s)''' % fields_tuple

    curs.execute('''DROP TABLE IF EXISTS food2''')
    curs.execute(sql_create)

    d = d[1:]
    print d

    hurManga = '?'
    for x in range(len(d[0]) - 1):
        hurManga += ', ?'

    print hurManga + 'antal platshållare'

    curs.executemany("INSERT INTO food2 VALUES (%s)" % hurManga, d)

    conn.commit()

    # Now fetch back the inserted data and write it to JSON.
    curs.execute("SELECT * FROM food2")
    recs = curs.fetchall()

    print type(recs)
    print 'typ'

    print "DB data as a list with a dict per DB record:"
    rows = [dict(rec) for rec in recs]
    print rows

    for row in curs.execute('select * from food2 order by number'):
        print row

    print u'slut på det'

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

    print "DB data as a list with a dict per DB record:"
    rows = [dict(rec) for rec in recs]
    print rows

    # We can also close the connection if we are done with it.
    conn.close()

    return 'Good-bye World'


@app.route('/fields')
def fields_test():
    fields = ('Livsmedelsnamn', 'Livsmedelsnummer', 'Energi (kcal)', 'Energi (kJ)', 'Kolhydrater (g)', 'Fett (g)', 'Protein (g)',
     'Fibrer (g)', 'Vatten (g)', 'Alkohol (g)', 'Aska (g)', 'Monosackarider (g)', 'Disackarider (g)', 'Sackaros (g)',
     'Fullkorn totalt (g)', 'Sockerarter (g)', 'Summa m\xc3\xa4ttade fettsyror (g)', 'Fettsyra 4:0-10:0 (g)',
     'Fettsyra 12:0 (g)', 'Fettsyra 14:0 (g)', 'Fettsyra 16:0 (g)', 'Fettsyra 18:0 (g)', 'Fettsyra 20:0 (g)',
     'Summa enkelom\xc3\xa4ttade fettsyror (g)', 'Fettsyra 16:1 (g)', 'Fettsyra 18:1 (g)',
     'Summa flerom\xc3\xa4ttade fettsyror (g)', 'Fettsyra 18:2 (g)', 'Fettsyra 18:3 (g)', 'Fettsyra 20:4 (g)',
     'EPA (Fettsyra 20:5) (g)', 'DPA (Fettsyra 22:5) (g)', 'DHA (Fettsyra 22:6) (g)', 'Kolesterol (mg)',
     'Retinol (\xc2\xb5g)', 'Vitamin A (\xc2\xb5g)', '\xce\xb2-Karoten (\xc2\xb5g)', 'Vitamin D (\xc2\xb5g)',
     'Vitamin E (mg)', 'Vitamin K (\xc2\xb5g)', 'Tiamin (mg)', 'Riboflavin (mg)', 'Vitamin C (mg)', 'Niacin (mg)',
     'Niacinekvivalenter (mg)', 'Vitamin B6 (mg)', 'Vitamin B12 (\xc2\xb5g)', 'Folat (\xc2\xb5g)', 'Fosfor (mg)',
     'Jod (\xc2\xb5g)', 'J\xc3\xa4rn (mg)', 'Kalcium (mg)', 'Kalium (mg)', 'Magnesium (mg)', 'Natrium (mg)', 'Salt (g)',
     'Selen (\xc2\xb5g)', 'Zink (mg)', 'Avfall (skal etc.) (%)')

    fields_list=list(fields)

    for x in range(0,len(fields)):
        fields_list[x]=fields_list[x].replace(' ', '_')

    for x in range(0, len(fields)):
        fields_list[x] += ' real'


    fields_tuple = tuple(fields_list)
    print fields_tuple

    return 'Slut på fields'
