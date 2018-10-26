from flask import Flask, jsonify, request
import DAOdrBarato
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

#______________________________________Classes para o BD _________________________

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tipo_id = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    senha = db.Column(db.String(20), nullable=False, default='default.jpg')
    nascimento = db.Column(db.Date, nullable=False)
    especialidades = db.relationship('Especialidade', secondary=especialidade_medico, backref=db.backref('espec_med', lazy='dynamic'))# Essa linha representa um relacionamento e não uma coluna explicação em https://www.youtube.com/watch?v=OvhoYbjtiKc
    lugares = db.relationship('Lugar', backref=db.backref('lugs')


class Especialidade(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    especialidade = db.Column(db.String(50), nullable=False)
    medicos = db.relationship('Usuario', secondary=especialidade_medico, backref=db.backref('medicos_spec', lazy='dynamic'))


class especialidade_medico(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_especialidade = db.Column(db.Interger, db.ForeignKey('especialidade.id') )
    id_medico = db.Column(db.Integer, db.ForeignKey('usuario.id'))

    
class Medico(db.Model):
    id = db.Column(db.Integer,db.ForeignKey('usuario.id'), primary_key=True)
    formacao = db.Column(db.String(50), unique=True, nullable=False)
    anos_exp = db.Column(db.String(120), unique=True, nullable=False)
    bio = db.Column(db.String(20), nullable=False, default='default.jpg')
    

class Documento(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    documento = db.Column(db.String(50), nullable = False)
    tipo_doc = db.Column(db.String(20), nullable = False)
    id_usario = db.Column(db.Integer, db.ForeignKey('usuario.id'))



class Lugar(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_usuario = db.Column(db.Interger, db.ForeignKey('usuario.id'))
    estado = db.Column(db.String(2), nullable=False)
    cidade = db.Column(db.String(100), nullable=False)
    logradouro = db.Column(db.String(250))
    bairro = db.Column(db.String(250))
    complemento = db.Column(db.String(250))
    CEP = db.Column(db.String(250))	

#_____________daqui para baixo tem que para cada tabela colocar o nome certo das colunas




class Agendamento(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_medico = 

    



#__________________________________Rotas_________________________



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

@app.route("/rest/doutores", methods=['POST'])
def getDoctos():
    jss = request.get_json()
    


if __name__ == '__main__':
    app.run(debug=True)
