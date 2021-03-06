import requests
import re
import json
from bs4 import BeautifulSoup



class OfertaAcademica:
	def __init__(self):
		self.diccionario_urls = { \
			"inco": "http://consulta.siiau.udg.mx/wco/sspseca.consulta_oferta?ciclop=201910&cup=D&majrp=INCO&crsep=&materiap=&horaip=&horafp=&edifp=&aulap=&ordenp=0&mostrarp=1000",
			"inni": "http://consulta.siiau.udg.mx/wco/sspseca.consulta_oferta?ciclop=201910&cup=D&majrp=INNI&crsep=&materiap=&horaip=&horafp=&edifp=&aulap=&ordenp=0&mostrarp=1000",
			"inro": "http://consulta.siiau.udg.mx/wco/sspseca.consulta_oferta?ciclop=201910&cup=D&majrp=INRO&crsep=&materiap=&horaip=&horafp=&edifp=&aulap=&ordenp=0&mostrarp=1000",
			"ince": "http://consulta.siiau.udg.mx/wco/sspseca.consulta_oferta?ciclop=201910&cup=D&majrp=INCE&crsep=&materiap=&horaip=&horafp=&edifp=&aulap=&ordenp=0&mostrarp=1000",
			"inbi": "http://consulta.siiau.udg.mx/wco/sspseca.consulta_oferta?ciclop=201910&cup=D&majrp=INBI&crsep=&materiap=&horaip=&horafp=&edifp=&aulap=&ordenp=0&mostrarp=1000",
			"igfo": "http://consulta.siiau.udg.mx/wco/sspseca.consulta_oferta?ciclop=201910&cup=D&majrp=IGFO&crsep=&materiap=&horaip=&horafp=&edifp=&aulap=&ordenp=0&mostrarp=1000"
		}

	def get_filas(self, url):
		r = requests.get(url)
		r.encoding = "ISO-8859-1"

		soup = BeautifulSoup(r.text, "html.parser")
		tabla = soup.find("table")
		filas = tabla.find_all("tr", {"style": re.compile("background-color:")})

		return filas

	def separar_datos_columna(self, datos_columna):
		diccionario = {
				"nrc" : datos_columna[0].text,
				"clave" : datos_columna[1].text,
				"materia" : datos_columna[2].text,
				"seccion" : datos_columna[3].text,
				"creditos" : datos_columna[4].text,
				"cupos" : datos_columna[5].text,
				"disponibles" : datos_columna[6].text
			}

		return diccionario
		
	def separar_datos_profesor(self, datos_profesor):
		diccionario = {}
		if len(datos_profesor) > 0:
				diccionario["ses_profesor"] = datos_profesor[0].text
				diccionario["profesor"] = datos_profesor[1].text
		else:
			diccionario["ses_profesor"] = 0
			diccionario["profesor"] = "N/A"

		return diccionario

	def separar_datos_horario(self, datos_horario):
		
		lista_horarios = []
		tablas = datos_horario.find_all("tr")

		for tabla in tablas:
			diccionario = {}
			datos = tabla.find_all("td")

			if len(datos) > 0:
				diccionario["ses_horario"] = datos[0].text
				diccionario["hora"] = datos[1].text
				diccionario["dias"] = datos[2].text
				diccionario["edificio"] = datos[3].text
				diccionario["aula"] = datos[4].text
				diccionario["periodo"] = datos[5].text
				#fecha_inicio, fecha_fin = separar_fechas(datos[5].text)
				#diccionario["fecha_inicio"] = fecha_inicio
				#diccionario["fecha_fin"] = fecha_inicio

				lista_horarios.append(diccionario)

		return lista_horarios

	def to_json(self, lista, nombre_archivo):
		with open(nombre_archivo, "w") as archivo:
			json.dump(lista, archivo, sort_keys=False, indent=4)

	def scraping(self):
		for carrera, url in self.diccionario_urls.items():
			filas = self.get_filas(url)

			lista = []
			for fila in filas:
				datos_columna = fila.find_all("td", {"class": "tddatos"})
				diccionario = self.separar_datos_columna(datos_columna)

				datos_profesor = fila.find_all("td", {"class": "tdprofesor"})
				diccionario.update(self.separar_datos_profesor(datos_profesor))

				diccionario["carrera"] = carrera.upper()

				datos_horario = fila.find("table", {"class": "td1"})
				diccionario["horario"] = self.separar_datos_horario(datos_horario)

				lista.append(diccionario)

			print(carrera, "=", len(lista))
			self.to_json(lista, carrera + ".json")


oferta_academica = OfertaAcademica()
oferta_academica.scraping()