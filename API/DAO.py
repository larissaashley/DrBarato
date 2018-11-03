from flask import Flask, jsonify, request, json
from flaskext.mysql import MySQL

app = Flask(__name__)

mysql = MySQL()

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'drbarato'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'

mysql.init_app(app)

def getMedicos(cidade,especialidade,estado):
	cur = mysql.connect().cursor()
	cur.execute('SELECT * FROM MEDICO LEFT JOIN LUGAR ON MEDICO.ID_USUARIO = LUGAR.ID_USUARIO WHERE LUGAR.CIDADE = "'+cidade+'" AND LUGAR.ESTADO = "'+estado+'"')
	r = [dict((cur.description[i][0], value)
			  for i, value in enumerate(row)) for row in cur.fetchall()]
	return jsonify({'medicos' : r})

def getMedico(idMedico):
	cur = mysql.connect().cursor()
	cur.execute('SELECT * FROM MEDICO WHERE ID_USUARIO = "'+idMedico+'"')
	r = [dict((cur.description[i][0], value)
			  for i, value in enumerate(row)) for row in cur.fetchall()]
	return jsonify({'medicos' : r})	