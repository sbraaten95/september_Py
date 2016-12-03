from flask import Flask, render_template, request, redirect, jsonify

from mysqlconnection import MySQLConnector

app = Flask(__name__)

mysql = MySQLConnector(app, 'Notes')

@app.route('/notes')
def index():
    return render_template('index.html', notes=mysql.query_db("SELECT * FROM notes"))

@app.route('/notes/index_json')
def index_json():
    return jsonify(mysql.query_db("SELECT * FROM notes"))

@app.route('/notes/create', methods=['POST'])
def create():
	mysql.query_db('INSERT INTO notes(title, description) VALUES("{}", "{}")'.format(request.form['title'], request.form['description']))
	return jsonify(mysql.query_db("SELECT * FROM notes"))

@app.route('/notes/edit', methods=['POST'])
def edit():
	mysql.query_db("UPDATE notes SET description = :description WHERE id = :id", { 'description': request.form['description'], 'id': request.form['userId'] })
	return jsonify(mysql.query_db("SELECT * FROM notes"))

@app.route('/notes/delete', methods=['POST'])
def delete():
	mysql.query_db("DELETE FROM notes WHERE id = :id", {'id': request.form['userId']})
	return jsonify(mysql.query_db("SELECT * FROM notes"))

app.run(debug=True)