# foodcluster
Taking data from Swedish Livsmedlesverket, clustring and visualizing using Plotly. Python using Flask.

Setting up the environment (some of this will be moved to requirements.txt)

* Detta är guiden jag använde för att komma igång: http://docs.python-guide.org/en/latest/dev/virtualenvs/ (eller var det denna? https://www.dabapps.com/blog/introduction-to-pip-and-virtualenv-python/). Installera virtualenv och starta det:
--> pip install virtualenv
* I terminalen, gå till local directory
--> kolla så att du är på rätt plats och kolla vart din python 2.7 ligger, se nästa rad för var min ligger
--> virtualenv -p /usr/local/Cellar/python/2.7.12_2/bin/python2.7 venv (eller vad nu din path är)
(Min blev 2.7.13 Alltså: virtualenv -p /usr/local/Cellar/python/2.7.13/bin/python2.7 venv )
--> source venv/bin/activate
(du bör nu se att det står (venv) på din kommandorad)
Dependencies:
--> pip install flask
--> pip install plotly
...
* Berätta för flask hur den startas (detta kan hoppas över men blir smidigare, du behöver bara köra det en gång):
--> export FLASK_APP=cluster-test.py
--> flask run

Current result of pip freeze:```
aniso8601==1.2.0
appdirs==1.4.3
click==6.7
decorator==4.0.11
enum34==1.1.6
Flask==0.12
Flask-RESTful==0.3.5
functools32==3.2.3.post2
ipython-genutils==0.1.0
itsdangerous==0.24
Jinja2==2.9.5
jsonschema==2.6.0
jupyter-core==4.3.0
MarkupSafe==0.23
nbformat==4.3.0
numpy==1.12.0
packaging==16.8
plotly==2.0.2
pyparsing==2.2.0
python-dateutil==2.6.0
pytz==2016.10
requests==2.13.0
scikit-learn==0.18.1
scipy==0.18.1
simplejson==3.10.0
six==1.10.0
SQLAlchemy==1.1.6
traitlets==4.3.2
Werkzeug==0.11.15

cd ~/Development/kodamat
virtualenv -p /usr/local/Cellar/python/2.7.13/bin/python2.7 venv
[Se upp för permission denied -> sudo]
pip install flask
pip install --upgrade pip
pip install plotly

export FLASK_APP=cluster-test.py
flask run

Om nu inte alla dependencies är ok i cluster-test.py så får man följande felaktiga felmeddelande...

Error: The file/path provided (cluster-test) does not appear to exist.  Please verify the path is correct.  If app is not on PYTHONPATH, ensure the extension is .py

Går igenom dependencies för att se vilken som hindrar appen från att alls köras...

pip install json får man inte göra. Samma med sqlite3
(installerar sudo pip install simplejson)
(sudo) pip install sklearn OK
numpy, scipy, requests ska inte installeras
pip install csv ska man tydligen inte göra
pip install lookup gav följande fel:
Could not find function xmlCheckVersion in library libxml2. Is libxml2 installed?
    Perhaps try: xcode-select --install
Och när jag gjorde xcode-select skickade den mig att installera vissa xcode-verktyg (som jag trodde fanns på maskinen...)

Funkade inte iaf. Funkade med sudo: sudo pip install lookup
Efter det gör den en setup.py install for lxml som jag inte vet vad det är





