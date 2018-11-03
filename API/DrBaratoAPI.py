from flask import Flask, jsonify, request, json
from flaskext.mysql import MySQL
import DAO

app = Flask(__name__)

@app.route('/doctors', methods=['POST','GET'])
def medicos():
	jss = request.get_json()
	return DAO.getMedicos(jss["city"],jss["speciality"],jss["state"])

@app.route('/doctor', methods=['POST','GET'])
def medico():
	jss = request.get_json()
	return DAO.getMedico(jss["id_usuario"])

if __name__ == '__main__':
	app.run()

