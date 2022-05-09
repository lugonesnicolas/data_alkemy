CREATE TABLE data_norm
AS SELECT cod_localidad,id_provincia,id_departamento,categoria,provincia,localidad,nombre,domicilio FROM bibliotecas;
INSERT INTO data_norm (cod_localidad,id_provincia,id_departamento,categoria,provincia,localidad,nombre,domicilio) 
SELECT cod_localidad,id_provincia,id_departamento,categoria,provincia,localidad,nombre,domicilio FROM cines;
INSERT INTO data_norm (cod_localidad,id_provincia,id_departamento,categoria,provincia,localidad,nombre,domicilio) 
SELECT cod_localidad,id_provincia,id_departamento,categoria,provincia,localidad,nombre,domicilio FROM museos;


CREATE TABLE registros_count
AS SELECT categoria,COUNT (*) FROM data_norm GROUP BY categoria;


CREATE TABLE registros_fuente_bibliotecas
AS SELECT "Fuente" AS fuente,COUNT(*) FROM bibliotecas GROUP BY fuente;

CREATE TABLE registros_fuente_cines(fuente,"count")
AS SELECT "Fuente" AS fuente,COUNT(*) FROM cines GROUP BY fuente ;

CREATE TABLE registros_fuente_museos
AS SELECT fuente,COUNT(*) FROM museos GROUP BY fuente;

CREATE TABLE registros_fuente
AS SELECT fuente,"count" FROM registros_fuente_bibliotecas;
INSERT INTO registros_fuente(fuente,"count")
SELECT fuente,"count" FROM registros_fuente_cines;
INSERT INTO registros_fuente(fuente,"count")
SELECT fuente,"count" FROM registros_fuente_museos;


CREATE TABLE registros_provincia_categoria
AS SELECT DISTINCT provincia,categoria,COUNT (*) FROM data_norm GROUP BY provincia,categoria;


CREATE TABLE cines_count
AS SELECT DISTINCT provincia,"Pantallas" AS pantallas,"Butacas","espacio_INCAA" FROM cines GROUP BY provincia,pantallas,"Butacas","espacio_INCAA";


DROP TABLE registros_fuente_bibliotecas;
DROP TABLE registros_fuente_cines;
DROP TABLE registros_fuente_museos;

