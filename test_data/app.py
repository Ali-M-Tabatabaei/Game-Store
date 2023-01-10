from flask import Flask
from flaskext.mysql import MySQL
import pymysql
from flask import jsonify
from faker import Faker

app = Flask(__name__)
mysql = MySQL(app)

app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = '2350343aA@'
app.config['MYSQL_DATABASE_DB'] = 'Game_store'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'

connection = mysql.connect()
cursor = connection.cursor(pymysql.cursors.DictCursor)

fake = Faker()
Faker.seed(1)
