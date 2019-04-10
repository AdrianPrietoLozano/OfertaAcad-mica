import glob
import json
import mysql.connector

files = glob.glob("*.json") # regresa una lista

conexion = mysql.connector.connect(
    user='adrian',
    password='12345',
    database='oferta_academica')
cursor = conexion.cursor()


def insertar_materia(oferta_materia):
    insert = "INSERT INTO materia(nombre, clave, creditos) "\
            "VALUES(%s, %s, %s)"
    cursor.execute(insert, (oferta_materia["materia"],
                            oferta_materia["clave"],
                            oferta_materia["creditos"]))
    conexion.commit()
    return cursor.lastrowid

def get_id_materia(clave):
    select = "SELECT id FROM materia WHERE clave=%s"
    cursor.execute(select, (clave, ))
    rows = cursor.fetchall()
    
    if len(rows) > 0:
        return rows[0][0]
    return -1

def get_id_profesor(nombre):
    select = "SELECT id FROM profesor WHERE nombre=%s"
    cursor.execute(select, (nombre, ))
    rows = cursor.fetchall()

    if len(rows) > 0:
        return rows[0][0]
    return -1


def insertar_profesor(oferta_materia):
    insert = "INSERT INTO profesor(nombre, ses) "\
            "VALUES(%s, %s)"
    cursor.execute(insert, (oferta_materia["profesor"],
                            oferta_materia["ses_profesor"]))
    conexion.commit()
    return cursor.lastrowid

for file in files:
    with open(file) as f:
        print(f.name)
        ofertas = json.load(f)
        for oferta in ofertas:
            # MATERIA
            id_materia = get_id_materia(oferta["clave"])
            if id_materia == -1: # no existe la materia
                id_materia = insertar_materia(oferta)

            # PROFESOR
            id_profesor = get_id_profesor(oferta["profesor"])
            if id_profesor == -1: # no existe el profesor
                id_materia = insertar_profesor(oferta)
            


conexion.close()

            