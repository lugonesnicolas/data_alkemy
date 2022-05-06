CREATE TABLE IF NOT EXISTS data_norm (
    cod_localidad INTEGER,
    id_provincia INTEGER,
    id_departamento INTEGER,
    categoria VARCHAR(250),
    provincia VARCHAR(250),
    localidad VARCHAR(250),
    nombre VARCHAR(250),
    domicilio VARCHAR(250),
    codigo_postal VARCHAR(250),
    numero_de_telefono VARCHAR(250),
    mail VARCHAR(250),
    web VARCHAR(250)
);
CREATE TABLE IF NOT EXISTS cines_count (
    provincia VARCHAR(250),
    Pantallas INTEGER,
    Butacas INTEGER,
    espacio_INCAA INTEGER
);

COPY "data_norm" FROM 'C:\Users\lugon\OneDrive\Escritorio\data_alchemy\datos_norm\data_norm.csv' DELIMITER ',' CSV HEADER;
COPY "cines_count" FROM 'C:\Users\lugon\OneDrive\Escritorio\data_alchemy\datos_norm\cines_count.csv' DELIMITER ',' CSV HEADER;
