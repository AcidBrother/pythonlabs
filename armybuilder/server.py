from __future__ import print_function
from pprint import pprint
from flask import Flask
from flask import render_template
from project import *
import json
import sqlite3
#export FLASK_APP=server

app = Flask(__name__)

print("")
print("⣿⣿⣿⣿⣿⣿⠏⠌⣾⣿⣿")
print("⣿⣿⣿⣿⣿⠀⠀⠸⠿⣿⣿⣿")
print("⣿⣿⣿⣿⠃⠀⣠⣾⣿⣿⣿")
print("⣿⣿⡿⠃⠀⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿")
print("⣿⣿⠃⠀⠀⣾⣿⣿⣿⣿⣿⣦⠀⠈⠻⣿⣿⣿")
print("⣿⣿⠀⠀⠀⣿⣿⣿⠟⠉⠉⠉⢃⣤⠀⠈⢿⣿⣿⣿")
print("⣿⣿⠀⠀⠀⢸⣿⡟⠀⠀⠀⠀⢹⣿⣧⠀⠀⠙⣿⣿")
print("⣿⣿⡆⠀⠀⠈⠻⡅⠀⠀⠀⠀⣸⣿⠿⠇⠀⠀⢸⣿")
print("⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠔⠛⠁⠀⠀⠀⣠⣿⣿")
print("⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⣿")
print("⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⣿")
print("⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⣠⣿")
print("⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⢰⣿")
print("⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿")
print("⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿")
print("⣿⣿⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿")
print("⣿⣿⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿")
print("⣿⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿")
print("")

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)


@app.route('/unit/')
@app.route('/unit/<name>')
def unit(name=None):
    if (name=="necw"):
        return render_template('unit.html',n=n1)
    if (name=="cads"):
        return render_template('unit.html',n=n2)
