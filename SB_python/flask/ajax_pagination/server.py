from flask import Flask, render_template, request, redirect, jsonify

from mysqlconnection import MySQLConnector

app = Flask(__name__)

mysql = MySQLConnector(app, 'lead_gen_business')

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/getfirst')
def getleads():
	return jsonify(mysql.query_db("SELECT * FROM leads LIMIT 0, 5"))

@app.route('/getall')
def getall():
	return jsonify(mysql.query_db("SELECT * FROM leads"))

@app.route('/filterleads', methods=['POST'])
def filterleads():
	name = "%" + request.form['name']
	return jsonify(mysql.query_db("SELECT * FROM leads WHERE first_name LIKE :name OR last_name LIKE :name AND  "))

app.run(debug=True)