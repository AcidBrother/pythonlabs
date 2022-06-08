from __future__ import print_function
from pprint import pprint
from flask import Flask
from flask import render_template
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
    con = sqlite3.connect('test.db')
    cur = con.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS users (name text, login text)''')
    con.commit()
    con.close()
    print("created users table")

#def db_users_refill()

def db_helpers_create():
    s = '''CREATE TABLE IF NOT EXISTS helpers (name text, login text)'''
    slog = "created helpers table"
    db_call(s, slog)

def db_call(s,slog):
    con = sqlite3.connect('test.db')
    cur = con.cursor()
    cur.execute(s)
    con.commit()
    con.close()
    print(slog)


con = sqlite3.connect('test.db')
cursor = con.cursor()
print("База данных создана и успешно подключена к SQLite")
sqlite_select_query = "select sqlite_version();"
cursor.execute(sqlite_select_query)
record = cursor.fetchall()
print("Версия базы данных SQLite: ", record)
cursor.close()


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

@app.route('/db/users')
def db_users():
    db_users_create()
    db_helpers_create()
    return "<p>It's db/users/</p>"

