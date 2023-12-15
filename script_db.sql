
CREATE DATABASE seminario2;
use seminario2;


CREATE TABLE report_country (
    id INT NOT NULL AUTO_INCREMENT,
    fecha DATE,
    codigo VARCHAR(25),
    nuevos INT,
    casos_acum INT,
    nuevas INT,
    muertes_acum INT,
    PRIMARY KEY (id)
);

CREATE TABLE departament (
    codigo INT PRIMARY KEY,
    nombre VARCHAR(50)
);

CREATE TABLE municipality (
    codigo INT PRIMARY KEY,
    nombre VARCHAR(50),
    departamento INT,
    poblacion INT,
    FOREIGN KEY (departamento) REFERENCES departament(codigo)
);

CREATE TABLE report_municipality (
    fecha DATE,
    codigo INT,
    numero_casos INT,
    PRIMARY KEY (fecha, codigo),
    FOREIGN KEY (codigo) REFERENCES municipality(codigo)
);
