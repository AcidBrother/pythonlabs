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

def db_users_select_by_id(rowid):
    s = '''SELECT * FROM users WHERE ROWID =''' +  rowid
    slog = "Selected " + rowid + " user"
    return db_call_select(s,slog)

def db_users_select_all():
    s = '''SELECT * FROM users '''
    slog = "Selected all " + " user"
    return db_call_select(s,slog)

def db_helpers_create():
    s = '''CREATE TABLE IF NOT EXISTS helpers (name TEXT NOT NULL, login TEXT NOT NULL, user_id INTEGER NOT NULL)'''
    slog = "created helpers table"
    db_call_select(s, slog)

def db_helpers_add(name, login, user_id):
    s = '''INSERT OR IGNORE INTO helpers (name, login, user_id) VALUES ("'''  + name +'''","''' + login + '''",''' + user_id + ''')'''
    slog = "Added " + name + " " + login + " " + user_id + "to helpers"
    db_call(s, slog)

def db_helpers_select_by_id(rowid):
    s = '''SELECT * FROM helpers WHERE ROWID =''' +  rowid
    slog = "Selected " + rowid + " helper"
    return db_call_select(s,slog)

def db_helpers_select_by_user_id(user_id):
    s = '''SELECT * FROM helpers WHERE user_id =''' +  user_id
    slog = "Selected by" + user_id + " helper"
    return db_call_select(s,slog)

def db_helpers_select_all():
    s = '''SELECT * FROM helpers '''
    slog = "Selected all " + " helper"
    return db_call_select(s,slog)

def db_call(s,slog):
    con = sqlite3.connect('test.db')
    cur = con.cursor()
    cur.execute(s)
    con.commit()
    con.close()
    print(slog)

def db_call_select(s,slog):
    con = sqlite3.connect('test.db')
    cur = con.cursor()
    cur.execute(s)
    rows = cur.fetchall()
    con.close()
    print(slog)
    return rows


#=========================================================
#=========================================================


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

@app.route('/db/users/insert', methods = ['GET','POST'])
def hanlder_db_users_insert():
    req_is_ok = False
    if (request.method == 'POST'):
        arg_name  = request.args.get('name')
        arg_login = request.args.get('login')
        if not((arg_name is None) or (arg_login is None)):
            req_is_ok = True
    if req_is_ok:
        db_users_add(arg_name, arg_login)
        resp = jsonify(success=True)
        return resp
    else:
        return "Incorrect request", 400

@app.route('/db/users/get', methods = ['GET','POST'])
def hanlder_db_users_get_by_id():
    req_is_ok = False
    if (request.method == 'GET'):
        arg_id  = request.args.get('id')
        if not(arg_id is None):
            req_is_ok = True
        if req_is_ok:
            res = db_users_select_by_id(arg_id)
            print(res)
            return jsonify(res)
        else:
            return "Incorrect request", 400

@app.route('/db/users/getall', methods = ['GET','POST'])
def hanlder_db_users_get_all():
    req_is_ok = False
    if (request.method == 'GET'):
        req_is_ok = True
    if req_is_ok:
        res = db_users_select_all()
        print(res)
        return jsonify(res)
    else:
        return "Incorrect request", 400

@app.route('/db/helpers/create')
def hanlder_db_helpers_create():
    db_helpers_create()
    return "<p>Created helpers table</p>", 200

@app.route('/db/helpers/insert', methods = ['GET','POST'])
def hanlder_db_helpers_insert():
    req_is_ok = False
    if (request.method == 'POST'):
        arg_name  = request.args.get('name')
        arg_login = request.args.get('login')
        arg_user_id = request.args.get('user_id')
        if not((arg_name is None) or (arg_login is None) or (arg_user_id is None)):
            req_is_ok = True
    if req_is_ok:
        db_helpers_add(arg_name, arg_login, arg_user_id)
        resp = jsonify(success=True)
        return resp
    else:
        return "Incorrect request", 400


@app.route('/db/helpers/get', methods = ['GET','POST'])
def hanlder_db_helpers_get_by_id():
    req_is_ok = False
    if (request.method == 'GET'):
        arg_id  = request.args.get('id')
        if not(arg_id is None):
            req_is_ok = True
        if req_is_ok:
            res = db_helpers_select_by_id(arg_id)
            print(res)
            return jsonify(res)
        else:
            return "Incorrect request", 400

@app.route('/db/helpers/getbyuser', methods = ['GET','POST'])
def hanlder_db_helpers_get_by_user_id():
    req_is_ok = False
    if (request.method == 'GET'):
        arg_user_id  = request.args.get('user_id')
        if not(arg_user_id is None):
            req_is_ok = True
        if req_is_ok:
            res = db_helpers_select_by_user_id(arg_user_id)
            print(res)
            return jsonify(res)
        else:
            return "Incorrect request", 400

@app.route('/db/helpers/getall', methods = ['GET','POST'])
def hanlder_db_helpers_get_all():
    req_is_ok = False
    if (request.method == 'GET'):
        req_is_ok = True
    if req_is_ok:
        res = db_helpers_select_all()
        print(res)
        return jsonify(res)
    else:
        return "Incorrect request", 400
