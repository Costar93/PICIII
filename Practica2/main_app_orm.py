from __future__ import print_function
import sys
import sqlite3
from flask import render_template
from flask import Flask, redirect, url_for, request
from datetime import datetime, date
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy_declarative import User, Base

app = Flask(__name__)

#Functions

def db_session():
    '''Generate a database session used to do queries on the db'''
    # Create engine and bind base to it
    path_to_db = "mydatabase.db"
    engine = create_engine('sqlite:///' + path_to_db)
    Base.metadata.bind = engine
    # Make a new session and return it
    DBSession = sessionmaker(bind = engine)
    session = DBSession()
    return session

def user_exists(username):
    #load session
    session = db_session()
    #Checking if user exists
    session.query(User).all()
    try:
        user = session.query(User).filter_by(username=username).one()
        return True
    except:
        return False

def save_data(username,fullname,email,password):
    #Check if user_exists() for register
    if user_exists(username):
        return False
    else:
    #Adding user
        try:
            #load session
            session = db_session()
            #saving user
            new_user = User(username=username, fullname=fullname, email=email, password=password)
            session.add(new_user)
            session.commit()
            return True
        except:
            return False

def user_data(username,password):
    #load session
    session = db_session()
    #Checking login data
    session.query(User).all()
    try:
        user = session.query(User).filter_by(username=username).all()
        pass1 = []
        for row in user:
            pass1.append(row.password)
        if password == pass1[0]:
            return True
    except:
        return False

def get_data():
    #load session
    session = db_session()
    #searching users
    session.query(User).all()
    user = session.query(User).all()
    list_of_lists=[]
    for row in user:
        list_of_lists.append((row.username,row.fullname,row.email))
    return list_of_lists

#Routes

@app.route('/')
def hello():
    #main page
    return render_template('landing_page.html')

@app.route('/show_users', methods=['GET', 'POST'])
def hist_data():
    #Show all data from database
    historical_data = get_data()
    return render_template('show_users_table.html',historical_data=historical_data)

@app.route('/insert_user', methods=['GET', 'POST'])
def user_register():
    #register webpage
    if request.method == 'GET':
        return render_template('insert_user.html')
    elif request.method == 'POST':
        username = request.form.get('username')
        fullname = request.form.get('fullname')
        email = request.form.get('email')
        password = request.form.get('password')
        if username != "" and fullname != "" and email != "" and password != "":
            if save_data(username,fullname,email,password):
                return render_template('register_succesfully.html',username=username,fullname=fullname)
            else:
                return render_template('register_error.html')
        else:
            return render_template('register_error.html')

@app.route('/login', methods=['GET', 'POST'])
def user_login():
    #login webpage
    if request.method == 'GET':
            return render_template('login_user.html')
    elif request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if user_data(username,password):
            return render_template('login_succesfully.html',username=username)
        else:
            return render_template('login_error.html')

if __name__ == '__main__':
    app.debug = True
    app.run("0.0.0.0")
