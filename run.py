from cgitb import html
from flask import Flask, render_template, url_for, request, flash, session, redirect, jsonify, json
from numpy import array
import psycopg2, os, random, time
from json import *
from datetime import datetime
from dotenv import load_dotenv, find_dotenv
import requests
from app.loginSc import main2
from app.register import registerFunc
from datetime import datetime

from app.dbQuery import databaseQuery

todaysDate = datetime.today().strftime('%Y-%m-%d')

load_dotenv(find_dotenv())
test5 = ''
KEY = os.environ.get("KEY")
date = datetime.today().strftime('%Y-%m-%d')
host = 'localhost'
app = Flask(__name__)
app.secret_key = KEY

@app.route('/', methods =["GET", "POST"])
def main():
    main2()
    if (main2.renderer != 1):
        return main2.renderer
    return render_template("index.html")
            
@app.route('/login', methods =["GET", "POST"])
def login():
    if ("user" in session):   
        products = databaseQuery('SELECT * FROM product;')
       
        
        return render_template("login.html", items=products)
       
    else: 
        return redirect(url_for("main" ))



@app.route('/register', methods =["GET", "POST"])
def register22():
    if request.method == "POST":
        registerFunc()
    
    return render_template('register.html')



@app.route('/postmethod', methods = ['GET', 'POST'])
def getPost():
    
    getPost.jsdata = request.get_json('javascriptData') 
    print(databaseQuery(f"select exists(SELECT * FROM cart WHERE id = {main2.fetching[0]} AND item = '{getPost.jsdata[0]}');"))
    print(f"INSERT INTO cart VALUES ({main2.fetching[0]}, '{getPost.jsdata[0]}', '{getPost.jsdata[1]}', 1);")

    
    if databaseQuery(f"SELECT * FROM cart WHERE id = {main2.fetching[0]} AND item = '{getPost.jsdata[0]}';") == []:
        databaseQuery(f"INSERT INTO cart VALUES ({main2.fetching[0]}, '{getPost.jsdata[0]}', '{getPost.jsdata[1]}', 1);")
        return jsonify(getPost.jsdata)
    else:
        databaseQuery(f"UPDATE cart SET qnt = qnt+1 WHERE id = '{main2.fetching[0]}' AND item = '{getPost.jsdata[0]}';")
        return jsonify(getPost.jsdata)
        
@app.route('/purchase', methods =["GET", "POST"])
def purchase():
    if ("user" in session): 
        
        a = databaseQuery(f"SELECT * FROM cart WHERE id = {main2.fetching[0]};")
       
        totalSum = 0
        for x in range(len(a)):
            totalSum = totalSum+a[x][2]*a[x][3]
       
        invoiceNr = 'Invoice'+str(random.randrange(1, 454330))
        if request.method == "POST":
             if  (request.form['Purchasebtn'] == 'Purchase'):
                 # loop through cart
                 for w in range(len(a)):
                    databaseQuery(f"UPDATE product SET stock = stock-{a[w][3]} WHERE item = '{a[w][1]}';") 
                    
                    
                    
                 databaseQuery(f"INSERT INTO history (id, invoice, price, date) VALUES ({main2.fetching[0]},  '{invoiceNr}', '{totalSum}', '{todaysDate}');")
                 databaseQuery(f"DELETE FROM cart WHERE id={main2.fetching[0]};")
                 return render_template("login.html")
            
                 
        else:
            return render_template("purchase.html", cart=a)

@app.route('/purchaseHis', methods =["GET", "POST"])
def history():
    if ("user" in session): 
        hist = databaseQuery(f"SELECT * FROM history WHERE id = {main2.fetching[0]};")
        return render_template("history.html", hist=hist)
                 
    else:
        return render_template("history.html") 

@app.route('/clearcart', methods =["GET", "POST"])
def clear():
    clearBtn = "False"
    clearBtn = request.get_json('javascriptData') 
    print(clearBtn)
    if clearBtn == "True":
        databaseQuery(f"DELETE FROM cart WHERE id={main2.fetching[0]};")



    

@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("main"))

if __name__ == '__main__':
    app.run( debug = True)






