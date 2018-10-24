from flask import Flask, jsonify, request
from DAOdrBarato import atualizaDoutor, getDoutor, postDoutor, postHorario, getHorario
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
    especialidades = db.relationship('Usuarios', secondary=especialidade_medico, backref=db.backref('medicos')# Essa linha representa um relacionamento e não uma coluna explicação em https://www.youtube.com/watch?v=OvhoYbjtiKc
    #ainda imcompleto

    def __repr__(self): # oq vai imprimir quando chamar a classe
        return f"Usuario('{self.tipo_id}', '{self.email}', '{self.senha}','{self.nascimento}')"


class Medico(db.Model):
    id = db.Column(db.Integer,db.ForeignKey('usuario.id'), primary_key=True)
    formacao = db.Column(db.String(50), unique=True, nullable=False)
    anos_exp = db.Column(db.String(120), unique=True, nullable=False)
    bio = db.Column(db.String(20), nullable=False, default='default.jpg')
    

    def __repr__(self):
        return f"Usuario('{self.tipo_id}', '{self.formacao}', '{self.anos_exp}','{self.bio}')"

class Especialidade(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    especialidade = db.Column(db.String(50, nullable=False)
    
    def __repr__(self):
        return f"Usuario('{self.especialidade}')"

class especialidade_medico(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_espec = 

    def __repr__(self):
        return f"Usuario('{self.tipo_id}', '{self.email}', '{self.senha}','{self.nascimento}')"

#_____________daqui para baixo tem que para cada tabela colocar o nome certo das colunas

class documento(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tipo_id = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    senha = db.Column(db.String(20), nullable=False, default='default.jpg')
    nascimento = db.Column(db.Date, nullable=False)
    #posts = db.relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        return f"Usuario('{self.tipo_id}', '{self.email}', '{self.senha}','{self.nascimento}')"


class lugar(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tipo_id = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    senha = db.Column(db.String(20), nullable=False, default='default.jpg')
    nascimento = db.Column(db.Date, nullable=False)
    #posts = db.relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        return f"Usuario('{self.tipo_id}', '{self.email}', '{self.senha}','{self.nascimento}')"


class Agendamento(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tipo_id = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    senha = db.Column(db.String(20), nullable=False, default='default.jpg')
    nascimento = db.Column(db.Date, nullable=False)
    #posts = db.relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        return f"Usuario('{self.tipo_id}', '{self.email}', '{self.senha}','{self.nascimento}')"



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
