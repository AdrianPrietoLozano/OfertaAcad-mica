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

CREATE TABLE perido(
	id INT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
	fecha_inicio DATE NOT NULL,
	fecha_fin DATE NOT NULL
);