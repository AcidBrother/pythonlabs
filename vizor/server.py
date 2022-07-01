from __future__ import print_function
from pprint import pprint
from flask import Flask
from flask import render_template
from flask import jsonify
from flask import request
from flask_cors import CORS

import sqlite3

#export FLASK_APP=server

app = Flask(__name__)
CORS(app)

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
    s = '''INSERT OR IGNORE INTO helper (name, login, user_id) VALUES ("'''  + name +'''","''' + login + '''",''' + user_id + ''')'''
    slog = "Added " + name + " " + login + " " + user_id + "to helper"
    db_call(s, slog)

def db_helper_select_by_id(helper_id):
    s = '''SELECT * FROM helper WHERE ROWID =''' +  helper_id
    slog = "Selected " + helper_id + " helper"
    return db_call_select(s,slog)

def db_helpers_select_by_user_id(user_id):
    s = '''SELECT * FROM helper WHERE user_id =''' +  user_id
    slog = "Selected by" + user_id + " helper"
    return db_call_select(s,slog)

def db_helpers_select_all():
    s = '''SELECT * FROM helper '''
    slog = "Selected all " + " helper"
    return db_call_select(s,slog)



def db_device_select_by_id(device_id):
    s = '''SELECT * FROM device WHERE device_id =''' +  device_id
    slog = "Selected by" + device_id + " device"
    return db_call_select(s,slog)

def db_device_delete_by_id(device_id):
    s = '''DELETE FROM device WHERE device_id =''' +  device_id
    slog = "Deleted by" + device_id + " device"
    return db_call(s,slog)

def db_device_select_all():
    s = '''SELECT * FROM device '''
    slog = "Selected all " + " device"
    return db_call_select(s,slog)

def db_device_add(device_name, os_version, app_version):
    s = '''INSERT OR IGNORE INTO device (device_name, os_version, app_version) VALUES ("'''  + device_name +'''","''' + os_version + '''",''' + app_version + ''')'''
    slog = "Added " + device_name + " " + os_version + " " + app_version + "to device"
    db_call(s, slog)

def db_device_update(device_id, device_name, os_version, app_version):
    s = '''UPDATE device SET device_name= "'''+device_name+'''" , os_version= "'''+os_version+'''" , app_version= '''+app_version+ ''' WHERE device_id= '''+device_id
    slog = "Updated "+ device_id + " " + device_name + " " + os_version + " " + app_version + "to device"
    db_call(s, slog)

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


@app.route('/db/helper/<helper_id>', methods = ['GET'])
def hanlder_db_helper_get_by_id(helper_id):
    reslist = db_helper_select_by_id(helper_id)
    res = reslist[0]
    print(res)
    return jsonify(helper_id = res[0],helper_name = res[1],helper_login = res[2],user_id = res[3],device_id = res[4])

@app.route('/db/helpers/getbyuser', methods = ['GET'])
def hanlder_db_helpers_get_by_user_id():
    res = db_helpers_select_by_user_id(arg_user_id)
    print(res)
    return jsonify(res)

@app.route('/db/helpers/getall', methods = ['GET'])
def hanlder_db_helpers_get_all():
    res = db_helpers_select_all()
    print(res)
    return jsonify(res)


#Почистить. Всё по CRUD




@app.route('/db/device/<device_id>', methods = ['GET'])
def hanlder_db_device_get(device_id):
    reslist = db_device_select_by_id(device_id)
    res = reslist[0]
    print(res)
    return jsonify(device_id = res[0],device_name = res[1],os_version = res[2],app_version = res[3])

@app.route('/db/device/<device_id>', methods = ['DELETE'])
def hanlder_db_device_delete_by_id(device_id):
    res = db_device_delete_by_id(device_id)
    print(res)
    return jsonify(res)

@app.route('/db/device/<device_id>', methods = ['PUT'])
def hanlder_db_device_put(device_id):
    req_is_ok = False
    arg_device_name  = request.args.get('device_name')
    arg_os_version = request.args.get('os_version')
    arg_app_version = request.args.get('app_version')
    if not((arg_device_name is None) or (arg_os_version is None) or (arg_app_version is None)):
        req_is_ok = True
    if req_is_ok:
        db_device_update(device_id, arg_device_name, arg_os_version, arg_app_version)
        resp = jsonify(success=True)
        return resp
    else:
        return "Incorrect request", 400

@app.route('/db/devices', methods = ['GET'])
def hanlder_db_device_get_all():
    res = db_device_select_all()
    print(res)
    return jsonify(device_id = res[0],device_name = res[1],os_version = res[2],app_version = res[3])


@app.route('/db/device', methods = ['POST'])
def hanlder_db_device_post():
    req_is_ok = False
    arg_device_name  = request.args.get('device_name')
    arg_os_version = request.args.get('os_version')
    arg_app_version = request.args.get('app_version')
    if not((arg_device_name is None) or (arg_os_version is None) or (arg_app_version is None)):
        req_is_ok = True
    if req_is_ok:
        db_device_add(arg_device_name, arg_os_version, arg_app_version)
        resp = jsonify(success=True)
        return resp
    else:
        return "Incorrect request", 400
