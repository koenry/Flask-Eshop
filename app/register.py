from app.dbQuery import databaseQuery
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

host = 'localhost'
date = datetime.today().strftime('%Y-%m-%d')
def registerFunc():
    if (request.form['registerBtn'] == 'Register'):
        registerFunc.regusername = request.form.get("regusername")
        regpassword = request.form.get("regpassword") 
        regpassword2 = request.form.get("regpassword2") 
    
        fetching = databaseQuery(f"PREPARE test5 (text) AS SELECT id FROM users WHERE username = $1; EXECUTE test5('{registerFunc.regusername}');")
        
        print(fetching)
        print('ok')
        if (fetching is not None or registerFunc.regusername == "" or len(registerFunc.regusername) < 4 or registerFunc.regusername.isalnum() == False):
            
                flash('Username is taken or contains special characters!')
        else:
            
            if (regpassword == "" or len(regpassword) < 5): 
                flash('Password cannot be empty or less than 5 characters!')
            
            elif (regpassword == regpassword2):
                databaseQuery(f"INSERT INTO users(username, pwd) VALUES('{registerFunc.regusername}', crypt('{regpassword}', gen_salt('bf')) )")            
                flash('Account created!')
                
        
                
                
                return render_template("index.html")
            else:
                flash('Passwords do not match!')
