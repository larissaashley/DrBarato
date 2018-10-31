#Cada classe representa um tabela do BD
#criar classes facilita na crição do JSON
#BD>Python Object>JSON

class usuario(object):
    id_usuario = 0
    tipo_ID = 0
    senha = ""
    nome = ""
    dt_nascimento = ""
    telefone = 0

    def __init__(self, id_usuario, tipo_ID, senha, nome, dt_nascimento, telefone ):
        self.id_usuario = id_usuario
        self.tipo_ID = tipo_ID
        self.senha = senha
        self.nome = nome
        self.dt_nascimento = dt_nascimento
        self.telefone = telefone

class medico(object):
        id_usuario = 0
        formacao = ""
        anos_experiencia = 0
        bio = ""

        def __init__(self, id_usario, formacao, anos_experiencia, bio ):
            self.id_usuario = id_usario
            self.formacao = formacao
            self.anos_experiencia = anos_experiencia
            self.bio = bio

            

#Fazer

