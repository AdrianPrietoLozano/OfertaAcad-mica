import glob
import json
import mysql.connector

files = glob.glob("*.json") # regresa una lista

conexion = mysql.connector.connect(
    user='adrian',
    password='12345',
    database='oferta_academica')
cursor = conexion.cursor()

id_periodo = 1

dic_materias = {"IGFO": 1, "INBI": 2, "INCE": 3, "INCO": 4, 
	"INNI": 5, "INRO": 6, }

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


def insertar_instancia_materia(oferta_materia, id_materia, id_profesor, id_periodo):
    insert = "INSERT INTO instancia_materia(nrc, cupos, disponibles, seccion, " \
			"id_carrera, id_materia, id_profesor, id_periodo) "\
			"VALUES(%s, %s, %s, %s, %s, %s, %s, %s)"
    cursor.execute(insert, (oferta_materia["nrc"],
							oferta_materia["cupos"],
							oferta_materia["disponibles"],
							oferta_materia["seccion"],
							dic_materias[oferta_materia["carrera"]],
							id_materia,
							id_profesor,
							id_periodo))
    conexion.commit()
    return cursor.lastrowid


for file in files:
    with open(file) as f:
        ofertas = json.load(f)
        for oferta in ofertas:
            # MATERIA
            id_materia = get_id_materia(oferta["clave"])
            if id_materia == -1: # no existe la materia
                id_materia = insertar_materia(oferta)

            # PROFESOR
            id_profesor = get_id_profesor(oferta["profesor"])
            if id_profesor == -1: # no existe el profesor
                id_profesor = insertar_profesor(oferta)

            # INSTANCIA_MATERIA
            id_instancia_materia = insertar_instancia_materia(oferta,
                        									id_materia,
                        									id_profesor,
                        									id_periodo)

            for horario in oferta["horario"]:
                insert = "INSERT INTO horario(hora, ses, dias, aula, edificio, "\
                		"id_instancia_materia) VALUES (%s, %s, %s, %s, %s, %s)"
                cursor.execute(insert, (horario["hora"],
                						horario["ses_horario"],
                						horario["dias"],
                						horario["aula"],
                						horario["edificio"],
                						id_instancia_materia))
                conexion.commit()
        print("Listo", f.name)


conexion.close()




            