from flask import Flask, render_template, json, request, redirect, url_for, flash, session
from flask_mysqldb import MySQL
from waitress import serve
import MySQLdb.cursors
import re
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

# Session
app.secret_key = 'mysecretkey'

@app.route('/home')
def home():
    return render_template('mainprofile.html')

@app.route('/home2')
def home2():
    return render_template('mainprofile2.html')

@app.route('/home3')
def home3():
    return render_template('mainprofile3.html')


if __name__ == '__main__':
    app.run(debug=True)
