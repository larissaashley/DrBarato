from flask import Flask, jsonify, request
from DAOdrBarato import atualizaDoutor, getDoutor, postDoutor, postHorario, getHorario


app = Flask(__name__)

@app.route("/rest/user/<int:dr_id>", methods=['GET', 'POST'])		 	#define rota e quais são os métodos disponiveis GET e/ou POST
def dr(dr_id):
    if (request.method == 'POST'): 										#POST atualiza dados do DR
        jss = request.get_json() 
		data = json.loads(jss) 											#transferencia do JSON para objeto python
        return jsonify(atualizaDoutor(data["nome"],data["ID_medico"])) 	#passa valores para metodo DAO que conectara com banco de dados. Resposta convertera para JSON e retornara
    else:
        return jsonify(getDoutor(dr_id))

@app.route("/rest/user", methods=['POST'])
def newUser():
    jss = request.get_json()
	data = json.loads(jss)
    return jsonify(postDoutor(data["ID_usuario"], data["nome"], 		#tem que retornar o ID do user criado
								data["dt_nascimento"], data["telefone"], 
								data["ID_documento"],data["documento"],
								data["tipo_doc"]))

	
@app.route("/rest/agendamento/<int:dr_id>", methods=['GET', 'POST'])
def agendamento(dr_id):
    if(request.method == 'POST'):
		jss = request.get_json()
		data = json.loads(jss)
		return jsonify(postHorario(jss, dr_id))
    else: 
        return jsonify(getHorario(jss, dr_id))
        
if __name__ == '__main__':
    app.run(debug=True)
