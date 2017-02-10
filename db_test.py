#!/usr/bin/env python
# -*- coding: utf-8 -*-

import csv
import sqlite3
import codecs
import unicodedata
import io
from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    print 'Hello, World!'


    # 59 värden

    conn = sqlite3.connect('example.db')

    # This enables column access by name: row['column_name']
    conn.row_factory = sqlite3.Row

    curs = conn.cursor()

    fields = list(('Livsmedelsnamn text', 'Livsmedelsnummer text', 'Energi_kcal real', 'Energi_kJ real', 'Kolhydrater_g real', 'Fett_g real', 'Protein_g real', 'Fibrer_g real', 'Vatten_g real', 'Alkohol_g real', 'Aska_g real', 'Monosackarider_g real', 'Disackarider_g real', 'Sackaros_g real', 'Fullkorn_totalt_g real', 'Sockerarter_g real', 'Summa_mattade_fettsyror_g real', 'Fettsyra_40-100_g real', 'Fettsyra_120_g real', 'Fettsyra_140_g real', 'Fettsyra_160_g real', 'Fettsyra_180_g real', 'Fettsyra_200_g real', 'Summa_enkelomattade_fettsyror_g real', 'Fettsyra_161_g real', 'Fettsyra_181_g real', 'Summa_fleromattade_fettsyror_g real', 'Fettsyra_182_g real', 'Fettsyra_183_g real', 'Fettsyra_204_g real', 'EPA_Fettsyra_205_g real', 'DPA_Fettsyra_225_g real', 'DHA_Fettsyra_226_g real', 'Kolesterol_mg real', 'Retinol_mikrog real', 'Vitamin_A_mikrog real', 'beta-Karoten_mikrog real', 'Vitamin_D_mikrog real', 'Vitamin_E_mg real', 'Vitamin_K_mikrog real', 'Tiamin_mg real', 'Riboflavin_mg real', 'Vitamin_C_mg real', 'Niacin_mg real', 'Niacinekvivalenter_mg real', 'Vitamin_B6_mg real', 'Vitamin_B12_mikrog real', 'Folat_mikrog real', 'Fosfor_mg real', 'Jod_mikrog real', 'Jarn_mg real', 'Kalcium_mg real', 'Kalium_mg real', 'Magnesium_mg real', 'Natrium_mg real', 'Salt_g real', 'Selen_mikrog real', 'Zink_mg real', 'Avfall_skal_etc_ real'))

    #string_test = str(['Livsmedelsnamn text', 'Livsmedelsnummer text', 'Energi_kcal real']).strip('[]')
    string_test = str(fields).strip('[]')

    string_test = string_test.decode()

    sql_create = '''CREATE TABLE food2 (%s)''' % string_test
    #sql_create = '''CREATE TABLE food2 ('Livsmedelsnamn text', 'Livsmedelsnummer text', 'Energi_kcal real')'''

    print sql_create
    print 'här!'

    curs.execute('''DROP TABLE IF EXISTS food2''')
    curs.execute(sql_create)

    #with io.open('/Users/organization/PycharmProjects/foodcluster/LivsmedelsDB_201611160847_01_liten.csv', encoding="utf-8") as csvfile:
    #    d = [tuple(line) for line in csv.reader(csvfile)]

    d=[]
    fields = tuple(d)

    #d=d[1]

    #('Vitt br\xc3\xb6d fibrer 3,5% ospec', '202', '265.6', '1111.4', '47.7', '3.61', '8.17', '3.5', '35.5', '0', '1.54', '1.96', '2.36', '0.05', '0', '', '0.43', '0', '0.01', '0.01', '0.25', '0.11', '0.01', '1.2', '0.01', '1.15', '0.77', '0.62', '0.14', '0', '0', '0', '0', '0', '17.7', '18.2', '6', '0', '0.88', '3.5', '0.22', '0.09', '0', '2.14', '3.5', '0.19', '0.14', '37.1', '141.7', '2', '1.12', '43.9', '173.8', '29.4', '400', '1', '4.4', '0.75', '0')

    mystring = 'u'


    print mystring
    print 'torsdag'


    print d
    print 'här!'

    e = (
        (u'Fått', 44, 34.5,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1),
        (u'Fisk', 37, 23.5,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1)
    )

    d=[(u'Vitt br\xf6d fibrer 3,5% ospec', u'202', u'265.6', u'1111.4', u'47.7', u'3.61', u'8.17', u'3.5', u'35.5', u'0', u'1.54', u'1.96', u'2.36', u'0.05', u'0', u'', u'0.43', u'0', u'0.01', u'0.01', u'0.25', u'0.11', u'0.01', u'1.2', u'0.01', u'1.15', u'0.77', u'0.62', u'0.14', u'0', u'0', u'0', u'0', u'0', u'17.7', u'18.2', u'6', u'0', u'0.88', u'3.5', u'0.22', u'0.09', u'0', u'2.14', u'3.5', u'0.19', u'0.14', u'37.1', u'141.7', u'2', u'1.12', u'43.9', u'173.8', u'29.4', u'400', u'1', u'4.4', u'0.75', u'0')]

    curs.executemany("INSERT INTO food2 VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", d)
    # curs.execute("INSERT INTO food VALUES ('Gurka ','45',454,0.5,'40')")

    # Commit the inserted rows.
    conn.commit()

    hurManga = '?'
    for x in range(len(fields) - 1):
        hurManga += ', ?'

    print str(len(hurManga)) + ' antal platshållare'

    #curs.executemany("INSERT INTO food2 VALUES (%s)" % hurManga, d)

    #conn.commit()

    # Now fetch back the inserted data and write it to JSON.
    curs.execute("SELECT * FROM food2 order by 'Livsmedelsnummer' ")
    recs = curs.fetchall()

    print type(recs)
    print 'typ'
    print 'torsdag'
    print "DB data as a list with a dict per DB record:"
    rows = [dict(rec) for rec in recs]
    print rows

    #Maries kod

    result=[]
    print 'Här blir det en tuple:'
    for row in curs.execute('select * from food2'):
        print row
        result=result.append(row)

    print 'result'
    print result

    print 'slut på det'

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

@app.route('/import')
def prepare_import():

    with open('/Users/organization/PycharmProjects/foodcluster/LivsmedelsDB_201611160847_01_liten.csv') as csvfile:
        d = [tuple(line) for line in csv.reader(csvfile)]



    fields = tuple(d)

    fields = fields[0]

    print(fields)
    print str(len(fields)) + ' = antal varden'


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

    hurManga = '?'
    for x in range(len(fields) - 1):
        hurManga += ', ?'

    print hurManga + 'hej'

    fields_list = list(fields)

    fields_list = fields_list[2:]

    for x in range(0, len(fields_list)):
        fields_list[x] = fields_list[x].replace(' ', '_').replace('\xc3\xa4', 'a').replace('\xc2\xb5', 'mikro').replace(
            '\xce\xb2', 'beta').replace('(', '').replace(')', '').replace(':', '').replace('.', '').replace('%', '')

    for x in range(0, len(fields_list)):
        fields_list[x] += ' real'

    fields_list = ['Livsmedelsnamn text', 'Livsmedelsnummer text'] + fields_list

    fields_tuple = tuple(fields_list)

    print fields_tuple

    return 'Slut på import'

@app.route('/unicode')
def unicodeimport ():

    print (u'Här börjar det')

    def unicode_csv_reader(utf8_data, dialect=csv.excel, **kwargs):
        csv_reader = csv.reader(utf8_data, dialect=dialect, **kwargs)
        for row in csv_reader:
            yield [unicode(cell, 'utf-8') for cell in row]

    filename = '/Users/organization/PycharmProjects/foodcluster/LivsmedelsDB_201611160847_01_liten.csv'
    reader = unicode_csv_reader(open(filename))
    for field1 in reader:
        print tuple(field1)

    f=[]
    with codecs.open('/Users/organization/PycharmProjects/foodcluster/LivsmedelsDB_201611160847_01_liten.csv', encoding='utf-8'):
        for field1 in f:
            print tuple(field1)

    return (u'Hej då')