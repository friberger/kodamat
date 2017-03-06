#!/usr/bin/env python
# -*- coding: utf-8 -*-

import csv
import sqlite3
import codecs
import unicodedata
import io
#from flask import Flask

#app = Flask(__name__)


#@app.route('/')
def initialize_db():
    print 'Hello, brave new database!'


    # 59 värden

    conn = sqlite3.connect('example.db') # create db and establish connection

    # This enables column access by name: row['column_name']
    conn.row_factory = sqlite3.Row

    curs = conn.cursor()

    fields = str(('Livsmedelsnamn text', 'Livsmedelsnummer text', 'Energi_kcal real', 'Energi_kJ real', 'Kolhydrater_g real', 'Fett_g real', 'Protein_g real', 'Fibrer_g real', 'Vatten_g real', 'Alkohol_g real', 'Aska_g real', 'Monosackarider_g real', 'Disackarider_g real', 'Sackaros_g real', 'Fullkorn_totalt_g real', 'Sockerarter_g real', 'Summa_mattade_fettsyror_g real', 'Fettsyra_40-100_g real', 'Fettsyra_120_g real', 'Fettsyra_140_g real', 'Fettsyra_160_g real', 'Fettsyra_180_g real', 'Fettsyra_200_g real', 'Summa_enkelomattade_fettsyror_g real', 'Fettsyra_161_g real', 'Fettsyra_181_g real', 'Summa_fleromattade_fettsyror_g real', 'Fettsyra_182_g real', 'Fettsyra_183_g real', 'Fettsyra_204_g real', 'EPA_Fettsyra_205_g real', 'DPA_Fettsyra_225_g real', 'DHA_Fettsyra_226_g real', 'Kolesterol_mg real', 'Retinol_mikrog real', 'Vitamin_A_mikrog real', 'beta-Karoten_mikrog real', 'Vitamin_D_mikrog real', 'Vitamin_E_mg real', 'Vitamin_K_mikrog real', 'Tiamin_mg real', 'Riboflavin_mg real', 'Vitamin_C_mg real', 'Niacin_mg real', 'Niacinekvivalenter_mg real', 'Vitamin_B6_mg real', 'Vitamin_B12_mikrog real', 'Folat_mikrog real', 'Fosfor_mg real', 'Jod_mikrog real', 'Jarn_mg real', 'Kalcium_mg real', 'Kalium_mg real', 'Magnesium_mg real', 'Natrium_mg real', 'Salt_g real', 'Selen_mikrog real', 'Zink_mg real', 'Avfall_skal_etc_ real'))
    fields = fields.strip('()')

    print fields

    sql_create = '''CREATE TABLE food2 (%s)''' % fields

    #print sql_create

    curs.execute('''DROP TABLE IF EXISTS food2''')
    curs.execute(sql_create)

    def unicode_csv_reader(utf8_data, dialect=csv.excel, **kwargs):
        csv_reader = csv.reader(utf8_data, dialect=dialect, **kwargs)
        for row in csv_reader:
            yield [unicode(cell, 'utf-8') for cell in row]
    data = []
    filename = 'LivsmedelsDB_201611160847_01_liten.csv'
    reader = unicode_csv_reader(open(filename))
    for field1 in reader:
        data.append(tuple(field1))

    reader.close()

    #Sätt in data i databasen
    curs.executemany("INSERT INTO food2 VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", data)

    # Commit the inserted rows.
    conn.commit()

    return conn

def db_to_memory():

    # Now fetch back the inserted data and write it to JSON.
    curs.execute("SELECT * FROM food2 order by 'Livsmedelsnummer' ")
    recs = curs.fetchall()

    print "DB data as a list with a dict per DB record:"
    rows = [dict(rec) for rec in recs]
    print rows

    result=[]
    print 'Här blir det en tuple:'
    for row in curs.execute('select * from food2'):
        print row
        result+=row


    print 'result'
    print tuple(result)

    print 'slut på det'

    # We can also close the connection if we are done with it.
    conn.close()

    return 'Good-bye World'


#@app.route('/fields')
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

#@app.route('/import')
def prepare_import():

    with open('LivsmedelsDB_201611160847_01.csv') as csvfile:
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

#@app.route('/unicode')
def unicodeimport ():

    print (u'Här börjar det')

    def unicode_csv_reader(utf8_data, dialect=csv.excel, **kwargs):
        csv_reader = csv.reader(utf8_data, dialect=dialect, **kwargs)
        for row in csv_reader:
            yield [unicode(cell, 'utf-8') for cell in row]
    data = []
    filename = 'LivsmedelsDB_201611160847_01.csv'
    reader = unicode_csv_reader(open(filename))
    for field1 in reader:
        data.append(tuple(field1))

    reader.close()

    print (data)

    return (u'Hej då')