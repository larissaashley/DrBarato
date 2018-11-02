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

@app.route('/medicos', methods=['POST'])
def medicos():
	jss = request.get_json()
	# data = json.loads(jss)
	return getMedicos(jss["city"],jss["speciality"],jss["state"])

def getMedicos(cidade,especialidade,estado):
	cur = mysql.connect().cursor()
	cur.execute("select * from drbarato.medico")
	r = [dict((cur.description[i][0], value)
			  for i, value in enumerate(row)) for row in cur.fetchall()]
	return jsonify({'medicos' : r})

if __name__ == '__main__':
	app.run()
