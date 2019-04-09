import requests
import re
from bs4 import BeautifulSoup


url = "http://consulta.siiau.udg.mx/wco/sspseca.consulta_oferta?ciclop=201910&cup=D&majrp=INCO&crsep=&materiap=&horaip=&horafp=&edifp=&aulap=&ordenp=0&mostrarp=1000"

r = requests.get(url)
r.encoding = "ISO-8859-1"

soup = BeautifulSoup(r.text, "html.parser")

tabla = soup.find("table")
filas = tabla.find_all("tr", {"style": re.compile("background-color:")})

for fila in filas:
	datos_columna = fila.find_all("td", {"class": "tddatos"})

	diccionario = {
		"nrc" : datos_columna[0].text,
		"clave" : datos_columna[1].text,
		"materia" : datos_columna[2].text,
		"seccion" : datos_columna[3].text,
		"creditos" : datos_columna[4].text,
		"cupos" : datos_columna[5].text,
		"disponibles" : datos_columna[6].text
	}

	datos_profesor = fila.find_all("td", {"class": "tdprofesor"})

	if len(datos_profesor) > 0:
		num_profesor = datos_profesor[0].text
		profesor = datos_profesor[1].text
	else:
		num_profesor = -1
		profesor = "N/A"

	datos_horario = fila.find_all("td", {"width": re.compile("")})

	if len(datos_horario) > 0:
		diccionario["ses"] = datos_horario[0].text
		diccionario["hora"] = datos_horario[1].text
		diccionario["dias"] = datos_horario[2].text
		diccionario["edificio"] = datos_horario[3].text
		diccionario["aula"] = datos_horario[4].text
		diccionario["periodo"] = datos_horario[5].text
	else:
		diccionario["ses"] = diccionario["hora"] = diccionario["dias"] = \
		diccionario["edificio"] = diccionario["aula"] = diccionario["periodo"] = "N/A"
	

	"""
	print(datos_horario[0].text, datos_horario[1].text, datos_horario[2].text, \
		datos_horario[3].text,\
		datos_horario[4].text,\
		datos_horario[5].text\
		)
	"""

	#print(diccionario)

	#print(datos_profesor)

	#print(nrc, clave, materia, seccion, creditos, cupos, disponibles, num_profesor, profesor, \
		#ses, hora, dias, edificio, aula, periodo)


print(len(filas))
