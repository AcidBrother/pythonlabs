from __future__ import print_function
from pprint import pprint
from flask import Flask
from flask import render_template
from flask import jsonify
from flask import request

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

print("=======================================")
print("Server started")
print("=======================================")

def db_users_select():
    print("users selection")

def db_users_create():
    s = '''CREATE TABLE IF NOT EXISTS users (name TEXT NOT NULL, login text NOT NULL)'''
    slog = "created users table"
    db_call(s, slog)

def db_users_add(name, login):
    s = '''INSERT OR IGNORE INTO users (name, login) VALUES ("'''  + name +'''","''' + login + '''")'''
    slog = "Added " + name + " " + login + "to users"
    db_call(s, slog)

def db_helpers_create():
    s = '''CREATE TABLE IF NOT EXISTS helpers (name TEXT NOT NULL, login TEXT NOT NULL, user_id INTEGER NOT NULL)'''
    slog = "created helpers table"
    db_call(s, slog)

def db_helpers_add(name, login, user_id):
    s = '''INSERT OR IGNORE INTO helpers (name, login, user_id) VALUES ("'''  + name +'''","''' + login + '''",''' + user_id + ''')'''
    slog = "Added " + name + " " + login + " " + user_id + "to helpers"
    db_call(s, slog)


def db_call(s,slog):
    con = sqlite3.connect('test.db')
    cur = con.cursor()
    cur.execute(s)
    con.commit()
    con.close()
    print(slog)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

@app.route('/db/users/create')
def hanlder_db_users_create():
    db_users_create()
    return "<p>Created users table</p>"

@app.route('/db/users/insert', methods = ['GET'])
def hanlder_db_users_insert():
    req_is_ok = False
    if request.method == 'GET':
        arg_name  = request.args.get('name')
        arg_login = request.args.get('login')
        if not((arg_name is None) or (arg_login is None)):
            req_is_ok = True
    if req_is_ok:
        db_users_add(arg_name, arg_login)
        resp = jsonify(success=True)
        return "<p>Added new user</p>"
    else:
        return "<p>Error, not enough args</p>"

@app.route('/db/helpers/create')
def hanlder_db_helpers_create():
    db_heplers_create()
    return "<p>Created helpers table</p>"
