import mysql.connector
from Classes import *
import json


db = mysql.connector.connect( 
host="127.0.0.1:8080",
user="root",
passwd="Dasfgh"
)

cursor = db.cursor()

def atualizaDoutor(dr_id,nome):
	try:
		cmd = "UPDATE MEDICO SET nome = '"+nome+"' WHERE ID_medico = "+dr_id+"
		cursor.execute(cmd)
		return "Inserido com sucesso"
	except (MySQLdb.Error, MySQLdb.Warning) as e:
        return e
		

def getDoutor(dr_id): 
    try:
        cmd = "SELECT * FROM MEDICO WHERE ID_medico = "+dr_id
		cursor.execute(cmd)
		result = cursor.fetchone()
		med = medico(result["id_usario"],result["formacao"],result["anos_experincia"],result["bio"])
        return json.loads(med) #BD>Python Object>JSON
    except (MySQLdb.Error, MySQLdb.Warning) as e:
        return e

def postDoutor(jss):
    return "null"


def postHorario(jss, dr_id):
    return "null"

def  getHorario(jss, dr_id):
    return "null"
