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
