from flask import Flask, jsonify
app = Flask(__name__)

import mysql.connector

conexion = mysql.connector.connect(
    user="adrian",
    password="12345",
    database="oferta_academica"
)

cursor = conexion.cursor()
print("bien")
@app.route("/api/v1/oferta/")
def hello():
    query = "SELECT instancia_materia.id, nrc, cupos, disponibles, seccion, "\
            "carrera.nombre, materia.nombre, clave, creditos, " \
            "profesor.nombre, profesor.ses, fecha_inicio, fecha_fin "\
            "FROM instancia_materia LEFT JOIN materia ON id_materia=materia.id " \
            "LEFT JOIN profesor ON id_profesor=profesor.id "\
            "LEFT JOIN periodo ON id_periodo=periodo.id " \
            "LEFT JOIN carrera ON id_carrera=carrera.id"

    query_horario = "SELECT hora, dias, aula, edificio " \
        "FROM horario " \
        "WHERE id_instancia_materia=%s"

    cursor.execute(query)
    ofertas = cursor.fetchall()
    print(len(ofertas))
    lista_ofertas = []
    for oferta in ofertas:
        cursor.execute(query_horario, (oferta[0], ))
        horarios = cursor.fetchall()
        o = {
            "id": oferta[0],
            "nrc": oferta[1],
            "cupos": oferta[2],
            "disponibles": oferta[3],
            "seccion": oferta[4],
            "carrera": oferta[5],
            "materia": oferta[6],
            "clave_materia": oferta[7],
            "creditos": oferta[8],
            "profesor": oferta[9],
            "ses_profesor": oferta[10],
            "periodo": str(oferta[11]) + " - " + str(oferta[12]),
            "horarios": horarios
        }

        lista_ofertas.append(o)
    return jsonify(lista_ofertas)



app.run()


#@app.route("/")
#def prueba():
    #return "Hello world2"



"""
SELECT instancia_materia.id, nrc, cupos, disponibles, seccion, carrera,
materia.nombre, clave, creditos, profesor.nombre, 
profesor.ses, fecha_inicio, fecha_fin
FROM instancia_materia LEFT JOIN materia ON id_materia=materia.id 
LEFT JOIN profesor ON id_profesor=profesor.id
LEFT JOIN periodo ON id_periodo=periodo.id;




SELECT hora, ses, dias, aula, edificio
FROM horario WHERE id_instancia_materia=1;
"""

