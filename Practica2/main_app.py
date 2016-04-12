from __future__ import print_function
import sys
import sqlite3
from flask import render_template
from flask import Flask, redirect, url_for, request
from datetime import datetime, date

app = Flask(__name__)

#Functions

def save_data(username,fullname,email,password):
    conn = sqlite3.connect('/home/pi/Desktop/db/users.db')
    try:
        conn.execute("insert into users (username,fullname,email,password) values (?, ?, ?, ?)",
                 (username,
                  fullname,
                  email,
                  password))
        conn.commit()
        conn.close()
        return True
    except:
        return False

def user_data(username,password):
    conn = sqlite3.connect('/home/pi/Desktop/db/users.db')
    cursor = conn.execute("SELECT username from users")
    data = [row for row in cursor]
    i = 0
    for user in data:
        if user[0] == username:
            i = 1
    print(1, file=sys.stderr)
    if i == 1:
        if password_data(username,password):
            return True
        else:
            return False
    else:
        return False

def password_data(username2,password2):
    conn = sqlite3.connect('/home/pi/Desktop/db/users.db')
    print(username2, file=sys.stderr)
    cursor = conn.execute("SELECT password FROM users WHERE username='str(username2)'")
    #No reconeix username2 com la paraula que conte, per tant no guarda contrasenya
    data = [row for row in cursor]
    print(data, file=sys.stderr)
    i = 0
    for password in data:
        print(password[0], file=sys.stderr)
        if password[0] == password2:
            i = 1
    if i == 1:
        return True
    else:
        return False

def get_data():
    conn = sqlite3.connect('/home/pi/Desktop/db/users.db')
    cursor = conn.execute("SELECT username,fullname,email from users")
    data = [row for row in cursor]
    conn.close()
    return data

#Routes

@app.route('/')
def hello():
    return render_template('landing_page.html')

@app.route('/show_users', methods=['GET', 'POST'])
def hist_data():
    historical_data = get_data()
    return render_template('show_users_table.html',historical_data=historical_data)

@app.route('/insert_user', methods=['GET', 'POST'])
def user_register():
    if request.method == 'GET':
            return render_template('insert_user.html')
    elif request.method == 'POST':
        username = request.form.get('username')
        fullname = request.form.get('fullname')
        email = request.form.get('email')
        password = request.form.get('password')
        if save_data(username,fullname,email,password):
            return redirect(url_for('hello'))
        else:
            return "Register Error"

@app.route('/login', methods=['GET', 'POST'])
def user_login():
    if request.method == 'GET':
            return render_template('login_user.html')
    elif request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if user_data(username,password):
            return redirect(url_for('hello'))
        else:
            return "Error Login"

if __name__ == '__main__':
    app.debug = True
    app.run("0.0.0.0")
