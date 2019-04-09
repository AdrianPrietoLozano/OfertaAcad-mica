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

	nrc = datos_columna[0].text
	clave =datos_columna[1].text
	materia = datos_columna[2].text
	seccion = datos_columna[3].text
	creditos = datos_columna[4].text
	cupos = datos_columna[5].text
	disponibles = datos_columna[6].text

	datos_profesor = fila.find_all("td", {"class": "tdprofesor"})

	if len(datos_profesor) > 0:
		num_profesor = datos_profesor[0].text
		profesor = datos_profesor[1].text
	else:
		num_profesor = -1
		profesor = "N/A"


	#print(datos_profesor)

	print(nrc, clave, materia, seccion, creditos, cupos, disponibles, num_profesor, profesor)


print(len(filas))
