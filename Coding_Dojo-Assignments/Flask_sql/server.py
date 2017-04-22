from flask import Flask
from mysqlconnection import MySQLConnector

print MySQLConnector
app = Flask(__name__)
mysql = MySQLConnector(app,"cities_and_states")

print mysql.query_db("SELECT * FROM cities")

app.run(debug=True, port=8000)
