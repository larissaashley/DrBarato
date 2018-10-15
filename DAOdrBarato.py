import mysql.connector


db = mysql.connector.connect( 
host="127.0.0.1:8080",
user="root",
passwd="Dasfgh"
)

cursor = db.cursor()

def atualizaDoutor(jss,dr_id):
    return "null"

def getDoutor(dr_id):
    return "null"

def postDoutor(jss):
    return "null"


def postHorario(jss, dr_id):
    return "null"

def  getHorario(jss, dr_id):
    return "null"
