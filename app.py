from flask import Flask, render_template, request, redirect
from flask_mysqldb import MySQL

app = Flask(_name_)

#Crear la conexion a la BD
mysql = MySQL()
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'proyectowebflask'
app.config['MYSQL_PORT'] = 3306

mysql.init_app(app)

@app.route('/')
def index():
    sql= "SELECT * FROM equipos"
    conexion = mysql.connection
    cursor=conexion.cursor()
    cursor.execute(sql)
    equipos=cursor.fetchall
    conexion.commit()
    return render_template('sitio/index.html', equipos=equipos)

if _name_ == '_main_':
    app.run(debug=True)