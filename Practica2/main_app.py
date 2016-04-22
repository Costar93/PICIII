from __future__ import print_function
import sys
import sqlite3
from flask import render_template
from flask import Flask, redirect, url_for, request
from datetime import datetime, date

app = Flask(__name__)

#Functions

def user_exists(username):
    conn = sqlite3.connect('users.db')
    cursor = conn.execute("SELECT username from users where username=:Id",
    {"Id": username})
    data = [row for row in cursor]
    for user in data:
        if user[0] == username:
            print ("1111111111")
            conn.close()
            return True

def save_data(username,fullname,email,password):
    #Check if user_exists()
    if user_exists(username):
        print ("2222222222")
        return False

    else:
    #Adding user
        print ("3333333333")
        try:
            conn = sqlite3.connect('users.db')
            conn.execute("insert into users (username,fullname,email,password) values (?, ?, ?, ?)",
                     (username,
                      fullname,
                      email,
                      password))
            conn.commit()
            conn.close()
            return True
        except:
            conn.close()
            return False

def user_data(username,password):
    #change the conn line to open it in the all devices
    #conn = sqlite3.connect('/home/pi/Desktop/db/users.db')
    conn = sqlite3.connect('users.db')
    cursor = conn.execute("SELECT username, password from users where username=:Id",
    {"Id": username})
    data = [row for row in cursor]
    for user in data:
        if user[1] == password:
            conn.close()
            return True
    else:
        conn.close()
        return False

def get_data():
    #change the conn line to open it in the all devices
    #conn = sqlite3.connect('/home/pi/Desktop/db/users.db')
    conn = sqlite3.connect('users.db')
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
        print(username=="", fullname=="", email=="", password=="")
        if username != "" and fullname != "" and email != "" and password != "":
            if save_data(username,fullname,email,password):
                return render_template('register_succesfully.html',username=username,fullname=fullname)
            else:
                return render_template('register_error.html')
        else:
            return render_template('register_error.html')

@app.route('/login', methods=['GET', 'POST'])
def user_login():
    if request.method == 'GET':
            return render_template('login_user.html')
    elif request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if user_data(username,password):
            return render_template('login_succesfully.html',username=username)
        else:
            return "Error Login"

if __name__ == '__main__':
    app.debug = True
    app.run("0.0.0.0")
