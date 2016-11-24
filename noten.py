import json
import os, sys
import markdown
from flask import Flask, render_template
from flask_flatpages import FlatPages
import urllib
from flask_frozen import Freezer

DEBUG = True
FLATPAGES_AUTO_RELOAD = DEBUG
FLATPAGES_EXTENSION = '.md'

app = Flask(__name__)
app.config.from_object(__name__)
pages = FlatPages(app)
freezer = Freezer(app)

def readJSON(file):
    data=[]
    print(file)
    with open("data/"+file+".json", encoding='utf-8') as data_file:
        data+=json.loads(data_file.read())
    return data

@freezer.register_generator
def noten():
    vert = ["et_gs","et_it","et_gmm","et_amr","et_eet","et_mel","ist_gs","psy_ba","bio_ba"]
    for ver in vert:
        yield {"name": ver}

@app.route('/<name>/')
def noten(name):
    data=readJSON(name)
    return render_template('noten.html',CONST=CONST ,facher=facher, data=data)

@app.route('/')
def home():
    return render_template('home.html',CONST=CONST ,facher=facher)

CONST={
    "url":"http://www.p4w5.eu/noten/"
}
facher=readJSON("index")
if __name__ == '__main__':
    freezer.freeze()
    app.run(port=5000)
