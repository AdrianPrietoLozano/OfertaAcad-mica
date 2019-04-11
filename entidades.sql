DROP DATABASE oferta_academica;
CREATE DATABASE oferta_academica;
USE oferta_academica;

CREATE TABLE materia(
	id INT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
	nombre VARCHAR(100) NOT NULL,
	clave VARCHAR(10) NOT NULL,
	creditos SMALLINT NOT NULL
);


CREATE TABLE profesor(
	id INT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
	nombre VARCHAR(100) NOT NULL,
	ses TINYINT UNSIGNED NOT NULL
);


CREATE TABLE periodo(
	id INT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
	fecha_inicio DATE NOT NULL,
	fecha_fin DATE NOT NULL
);


CREATE TABLE instancia_materia(
	id INT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
	nrc VARCHAR(20),
	cupos SMALLINT,
	disponibles SMALLINT,
	seccion VARCHAR(10),
	carrera CHAR(10),
	id_materia INT UNSIGNED NOT NULL,
	id_profesor INT UNSIGNED NOT NULL,
	id_periodo INT UNSIGNED NOT NULL,
	FOREIGN KEY(id_materia) REFERENCES materia(id),
	FOREIGN KEY(id_profesor) REFERENCES profesor(id),
	FOREIGN KEY(id_periodo) REFERENCES periodo(id)
);


CREATE TABLE horario(
	id INT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
	hora VARCHAR(20) NOT NULL,
	ses TINYINT UNSIGNED NOT NULL,
	dias VARCHAR(10) NOT NULL,
	aula VARCHAR(10) NOT NULL,
	edificio VARCHAR(10) NOT NULL,
	id_instancia_materia INT UNSIGNED NOT NULL,
	FOREIGN KEY(id_instancia_materia) REFERENCES instancia_materia(id)
);


INSERT INTO periodo(fecha_inicio, fecha_fin)
	VALUES(STR_TO_DATE('16/01/19','%d/%m/%Y'),
			STR_TO_DATE('31/05/19','%d/%m/%Y'));


GRANT ALL PRIVILEGES ON oferta_academica . * TO 'adrian'@'localhost';