from cgitb import html
from flask import Flask, render_template, url_for, request, flash, session, redirect, jsonify, json
from numpy import array
import psycopg2, os, random, time
from json import *
from werkzeug.utils import secure_filename
from datetime import datetime
from dotenv import load_dotenv, find_dotenv
import requests
from app.dbQuery import databaseQuery

load_dotenv(find_dotenv())
test5 = ''
KEY = os.environ.get("KEY")
date = datetime.today().strftime('%Y-%m-%d')

app = Flask(__name__)
app.secret_key = KEY

def main2():
    main2.renderer = 1;
    authenticate = 0 # authentication control? still WIP
    if  request.method == "POST":
        if  (request.form['loginBtn'] == 'Login'):
            main2.username = request.form.get("fname")
            session["user"] = main2.username
            password = request.form.get("lname") 
        
            superduperQuery = f"PREPARE test5 (text, text) AS SELECT id FROM users WHERE username = $1 AND pwd = crypt($2, pwd); EXECUTE test5('{main2.username}', '{password}'); "
            main2.fetching = databaseQuery(superduperQuery)
            print(main2.fetching[0])
            if (main2.fetching is not None):
                products = databaseQuery('SELECT * FROM product;')
                main2.renderer = render_template("login.html", items=products)      

            else:
                print('kk')
                time.sleep(2)
                flash('Wrong Username or Password!')      
        else:
            time.sleep(2)
            flash('Wrong Username or Password!')    
    return render_template("index.html")