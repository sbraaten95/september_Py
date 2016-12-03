from flask import Flask, render_template, request, redirect, flash, session
import re
from connection import MySQLConnector
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
app.secret_key = "nope"
mysql = MySQLConnector(app, 'email_validation')
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/check', methods=['POST'])
def check():
    flagged = True
    if len(request.form['email']) == 0:
        flash("ENTER AN EMAIL")
        flagged = False
        return render_template('index.html')
    if not EMAIL_REGEX.match(request.form['email']):
        flash("INVALID EMAIL")
        flagged = False
        return render_template('index.html')
    if flagged:
        flash("VALID EMAIL")
        email = request.form['email']
        query = "INSERT INTO emails (email, created_at, updated_at) VALUES (:email, NOW(), NOW())"
        data = {"email" : email}
        session['email'] = email
        if mysql.query_db(query, data):
            print "Successfully saved to database"
        return redirect('/success')
        
@app.route('/success')
def success():
    query = "SELECT * FROM emails"
    emails = mysql.query_db(query)
    return render_template('success.html', emails = emails)

app.run(debug=True)