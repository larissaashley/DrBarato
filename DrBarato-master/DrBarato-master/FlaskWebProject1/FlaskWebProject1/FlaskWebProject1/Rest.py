from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import datetime

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydb.db'
db = SQLAlchemy(app)
ma = Marshmallow(app)

#______________________________________Classes para o BD _________________________


espec_med =  db.Table('espec_med',
    db.Column('id_espec_med',db.Integer, primary_key=True),
    db.Column('id_especialidade',db.Integer, db.ForeignKey('especialidade.id_especialidade')),
    db.Column('id_usuario',db.Integer, db.ForeignKey('usuario.id_usuario'))
	)	

class Usuario(db.Model):
    id_usuario = db.Column(db.Integer, primary_key=True)
    tipo_id = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    senha = db.Column(db.String(20), nullable=False, default='default.jpg')
    nascimento = db.Column(db.Date, nullable=False)
    especialidades = db.relationship('Especialidade', secondary=espec_med, backref=db.backref('especs', lazy='dynamic'))# Essa linha representa um relacionamento e não uma coluna explicação em https://www.youtube.com/watch?v=OvhoYbjtiKc
    lugares = db.relationship('Lugar', backref = db.backref('lugs', lazy = 'dynamic'))
    documentos = db.relationship('Documento', backref = db.backref('docs', lazy = 'dynamic'))



class Especialidade(db.Model):
    id_especialidade = db.Column(db.Integer, primary_key=True)
    especialidade = db.Column(db.String(50), nullable=False)
    medicos = db.relationship('Usuario', secondary=espec_med, backref=db.backref('medicos_spec', lazy='dynamic'))

 
class Medico(db.Model):
    id_medico= db.Column(db.Integer,db.ForeignKey('usuario.id_usuario'), primary_key=True)
    formacao = db.Column(db.String(50), unique=True, nullable=False)
    anos_exp = db.Column(db.String(120), unique=True, nullable=False)
    bio = db.Column(db.String(20), nullable=False, default='default.jpg')
    

class Documento(db.Model):
    id_documento = db.Column(db.Integer, primary_key=True)
    documento = db.Column(db.String(50), nullable = False)
    tipo_doc = db.Column(db.String(20), nullable = False)
    id_usario = db.Column(db.Integer, db.ForeignKey('usuario.id_usuario'))



class Lugar(db.Model):
    id_lugar = db.Column(db.Integer, primary_key=True)
    id_usuario = db.Column(db.Integer, db.ForeignKey('usuario.id_usuario'))
    estado = db.Column(db.String(2), nullable=False)
    cidade = db.Column(db.String(100), nullable=False)
    logradouro = db.Column(db.String(250))
    bairro = db.Column(db.String(250))
    complemento = db.Column(db.String(250))
    CEP = db.Column(db.String(250))	



class Agendamento(db.Model):
    id_agendamento = db.Column(db.Integer, primary_key=True)
    id_medico = db.Column(db.Integer,db.ForeignKey('usuario.id_usuario'), nullable=False)
    id_paciente = db.Column(db.Integer,db.ForeignKey('usuario.id_usuario'), nullable=False)
    cadastro = db.Column(db.Integer, nullable=False)
    inicio = db.Column(db.DateTime, nullable=False)
    fim = db.Column(db.DateTime, nullable=False)
    in_status = db.Column(db.Integer, nullable=False)
    valor = db.Column(db.Float)

    #________________Configuração de schemas para o Marshmallow____

class Usuario_Schema(ma.ModelSchema):
    class Meta:
        model = Usuario

class Especialidade_Schema(ma.ModelSchema):
    class Meta:
        model = Especialidade

class Medico_Schema(ma.ModelSchema):
    class Meta:
        model = Medico

class Documento_Schema(ma.ModelSchema):
    class Meta:
        mode1 = Documento

class Lugar_Schema(ma.ModelSchema):
    class Meta:
        mode1 = Lugar

class Agendamento_Schema(ma.ModelSchema):
    class Meta:
        mode1 = Agendamento

#__________________________________Rotas_________________________


@app.route("/rest/doutor", methods=['POST'])
def getDoctos():
    jss = request.get_json()
    obj = json.loads(jss)
    
    #https://www.pythoncentral.io/sqlalchemy-orm-examples/
    query = db.session.query(Usuario).join(Lugar.id_usuario).filter(Lugar.estado == obj['state'], Lugar.cidade == obj['city'],Usuario.especialidades.any(especialidade.id_especialidade == obj['id']))
    user_schema = Usuario_Schema(many=True) #many= True para quando vai tazer varios dados quando for um só não precisa
    output = user_schema.dump(query).data #https://www.youtube.com/watch?v=kRNXKzfYrPU usar esse para passar do query pro JSON

    return jsonify(json.dump(output)) #json.dump() passa um objeto para string JSON

if __name__ == '__main__':
    app.run(debug=True)

	
@app.route("/rest/agendamento/<int:dr_id>", methods=['GET', 'POST'])
def agendamento(dr_id):
    if(request.method == 'POST'):
        jss = request.get_json()
        data = json.loads(jss)
        return jsonify(postHorario(jss, dr_id))
    else: 
        usr = Usuario.query.get(dr_id)
        user_schema = Usuario_Schema()
        output = user_schema.dump(query).data
        return jsonify(json.dump(output))
