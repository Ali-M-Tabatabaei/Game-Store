from app import app
from flaskext.mysql import MySQL

mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = '2350343aA@'
app.config['MYSQL_DATABASE_DB'] = 'final_project'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)
