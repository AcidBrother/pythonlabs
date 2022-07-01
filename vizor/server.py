from __future__ import print_function
from pprint import pprint
from flask import Flask
from flask import render_template
from flask import jsonify
from flask import request
from flask_cors import CORS
import json

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

def db_user_select():
    print("user selection")

def db_user_create():
    s = '''CREATE TABLE IF NOT EXISTS user (name TEXT NOT NULL, login text NOT NULL)'''
    slog = "created user table"
    db_call(s, slog)

def db_user_add(user_name, user_login, user_device):
    s = '''INSERT OR IGNORE INTO user (name, login) VALUES ("'''  + user_name +'''","''' + user_login + '''",''' + user_device + ''')'''
    slog = "Added " + user_name + " " + user_login + " " + user_device +"to user"
    db_call(s, slog)

def db_user_update(user_id, user_name, user_login, user_device):
    s = '''UPDATE user SET user_name= "'''+user_name+'''" , user_login= "'''+user_login+'''" , user_device='''+ user_device + ''' WHERE user_id= '''+user_id
    print('===================================')
    print(s)
    print('===================================')
    slog = "Updated "+ user_id + " " + user_name + " " + user_login + " " + user_device + "to user"
    db_call(s, slog)

def db_user_select_by_id(user_id):
    s = '''SELECT * FROM user WHERE ROWID =''' +  user_id
    slog = "Selected " + user_id + " user"
    return db_call_select(s,slog)

def db_user_select_all():
    s = '''SELECT * FROM user '''
    slog = "Selected all " + " user"
    return db_call_select(s,slog)

def db_helper_create():
    s = '''CREATE TABLE IF NOT EXISTS helper (name TEXT NOT NULL, login TEXT NOT NULL, user_id INTEGER NOT NULL)'''
    slog = "created helper table"
    db_call_select(s, slog)

def db_helper_add(helper_name, helper_login, user_id, helper_device):
    s = '''INSERT OR IGNORE INTO helper (helper_name, helper_login, user_id, helper_device) VALUES ("'''  + helper_name +'''","''' + helper_login + '''",''' + user_id + ''','''+helper_device+''')'''
    print('===================================')
    print(s)
    print('===================================')
    slog = "Added " + helper_name + " " + helper_login + " " + user_id + " " + helper_device + "to helper"
    db_call(s, slog)

def db_helper_select_by_id(rowid):
    s = '''SELECT * FROM helper WHERE ROWID =''' +  rowid
    slog = "Selected " + rowid + " helper"
    return db_call_select(s,slog)

def db_helper_select_by_user_id(user_id):
    s = '''SELECT * FROM helper WHERE user_id =''' +  user_id
    slog = "Selected by" + user_id + " helper"
    return db_call_select(s,slog)

def db_helper_select_all():
    s = '''SELECT * FROM helper '''
    slog = "Selected all " + " helper"
    return db_call_select(s,slog)

def db_helper_delete_by_id(helper_id):
    s = '''DELETE FROM helper WHERE helper_id =''' +  helper_id
    slog = "Deleted by" + helper_id + " helper"
    return db_call(s,slog)

def db_helper_update(helper_id, helper_name, helper_login, user_id, helper_device):
    s = '''UPDATE helper SET helper_name= "'''+helper_name+'''" , helper_login= "'''+helper_login+'''" , user_id= '''+user_id+ ''', helper_device='''+ helper_device + ''' WHERE helper_id= '''+helper_id
    print('===================================')
    print(s)
    print('===================================')
    slog = "Updated "+ helper_id + " " + helper_name + " " + helper_login + " " + user_id + " " + helper_device + "to helper"
    db_call(s, slog)


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
    print('===================================')
    print(s)
    print('===================================')
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

@app.route('/db/user/create')
def hanlder_db_user_create():
    db_user_create()
    return "<p>Created user table</p>"


@app.route('/db/user/insert', methods = ['POST'])
def hanlder_db_user_insert():
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        json = request.json
        req_is_ok = False
        arg_user_name  = json[('user_name')]
        arg_user_login = json[('user_login')]
        arg_user_device = str(json[('user_device')])
        if not((arg_user_name is None) or (arg_user_login is None) or (arg_user_device is None)):
            req_is_ok = True
        if req_is_ok:
            db_user_add(arg_user_name, arg_user_login, arg_user_device)
            resp = jsonify(success=True)
            return resp
    else:
        return 'Content-Type not supported!', 400


@app.route('/db/user/<user_id>', methods = ['PUT'])
def hanlder_db_user_put(user_id):
    content_type = request.headers.get('Content-Type')

    if (content_type == 'application/json'):
        json = request.json
        req_is_ok = False
        arg_user_name  = json[('user_name')]
        arg_user_login = json[('user_login')]
        arg_user_device = str(json[('user_device')])
        if not((arg_user_name is None) or (arg_user_login is None) or (arg_user_device is None)):
            req_is_ok = True
        if req_is_ok:
            db_user_update(arg_user_name, arg_user_login, arg_user_device)
            resp = jsonify(success=True)
            return resp
    else:
        return 'Content-Type not supported!', 400



@app.route('/db/user/<user_id>', methods = ['GET'])
def hanlder_db_user_get_by_id(user_id):
    res = db_user_select_by_id(user_id)
    print(res)
    return jsonify(res)


@app.route('/db/user/getall', methods = ['GET'])
def hanlder_db_user_get_all():
    res = db_user_select_all()
    print(res)
    return jsonify(res)

@app.route('/db/helper/create')
def hanlder_db_helper_create():
    db_helper_create()
    return "<p>Created helper table</p>", 200


@app.route('/db/helper/insert', methods = ['POST'])
def hanlder_db_helper_insert():
    content_type = request.headers.get('Content-Type')

    if (content_type == 'application/json'):
        json = request.json
        req_is_ok = False
        arg_helper_name  = json[('helper_name')]
        arg_helper_login = json[('helper_login')]
        arg_user_id = str(json[('user_id')])
        arg_helper_device = str(json[('helper_device')])
        if not((arg_helper_name is None) or (arg_helper_login is None) or (arg_user_id is None) or (arg_helper_device is None)):
            req_is_ok = True
        if req_is_ok:
            db_helper_add(arg_helper_name, arg_helper_login, arg_user_id, arg_helper_device)
            resp = jsonify(success=True)
            return resp
    else:
        return 'Content-Type not supported!', 400

@app.route('/db/helper/get', methods = ['GET'])
def hanlder_db_helper_get_by_id():
    res = db_helper_select_by_id(arg_id)
    print(res)
    return jsonify(res)

@app.route('/db/helper/getbyuser', methods = ['GET'])
def hanlder_db_helper_get_by_user_id():
    res = db_helper_select_by_user_id(user_id)
    print(res)
    return jsonify(res)

@app.route('/db/helper/getall', methods = ['GET'])
def hanlder_db_helper_get_all():
    res = db_helper_select_all()
    print(res)
    return jsonify(res)

@app.route('/db/helper/<helper_id>', methods = ['DELETE'])
def hanlder_db_helper_delete_by_id(helper_id):
    res = db_helper_delete_by_id(helper_id)
    print(res)
    return jsonify(res)



@app.route('/db/helper/<helper_id>', methods = ['PUT'])
def hanlder_db_helper_put(helper_id):
    content_type = request.headers.get('Content-Type')

    if (content_type == 'application/json'):
        json = request.json
        req_is_ok = False
        arg_helper_name  = json[('helper_name')]
        arg_helper_login = json[('helper_login')]
        arg_user_id = str(json[('user_id')])
        arg_helper_device = str(json[('helper_device')])
        if not((arg_helper_name is None) or (arg_helper_login is None) or (arg_user_id is None) or (arg_helper_device is None)):
            req_is_ok = True
        if req_is_ok:
            db_helper_update(helper_id, arg_helper_name, arg_helper_login, arg_user_id, arg_helper_device)
            resp = jsonify(success=True)
            return resp
    else:
        return 'Content-Type not supported!', 400



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
    content_type = request.headers.get('Content-Type')

    if (content_type == 'application/json'):
        json = request.json
        req_is_ok = False
        arg_device_name  = json['device_name']
        arg_os_version = json['os_version']
        arg_app_version = str(json['app_version'])
        if not((arg_device_name is None) or (arg_os_version is None) or (arg_app_version is None)):
            req_is_ok = True
        if req_is_ok:
            db_device_update(device_id, arg_device_name, arg_os_version, arg_app_version)
            resp = jsonify(success=True)
            return resp
    else:
        return 'Content-Type not supported!', 400



@app.route('/db/devices', methods = ['GET'])
def hanlder_db_device_get_all():
    res = db_device_select_all()
    print(res)
    return jsonify(res)


@app.route('/db/device', methods = ['POST'])
def hanlder_db_device_post():
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        json = request.json
        req_is_ok = False
        arg_device_name  = json['device_name']
        arg_os_version = json['os_version']
        arg_app_version = str(json['app_version'])
        if not((arg_device_name is None) or (arg_os_version is None) or (arg_app_version is None)):
            req_is_ok = True
        if req_is_ok:
            db_device_add(arg_device_name, arg_os_version, arg_app_version)
            resp = jsonify(success=True)
            return resp
    else:
        return 'Content-Type not supported!', 400
