from app import app
from flaskext.mysql import MySQL

mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'root'
# ali taba pass: 2350343aA@
# ali vaziri pass: password
app.config['MYSQL_DATABASE_PASSWORD'] = 'password'
# ali taba DB: final_project
# ali vaziri DB: game_store
app.config['MYSQL_DATABASE_DB'] = 'game_store'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)
