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

#EM CONSTRUÇÃO: Possíveis erros de datetime
@app.route('/schedule', methods=['POST','GET'])
def agendamento():
	if (request.method == 'POST'): 										
		jss = request.get_json()
		return DAO.createAgendamento(jss["id_medico"],jss["inicio"],jss["fim"])
	else:
		return DAO.getAgendamento(jss["id_agendamento"])

if __name__ == '__main__':
	app.run()

