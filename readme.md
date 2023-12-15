PROYECTO LABORATORIO FASE 1 SEMINARIO DE SISTEMAS 2

# Índice
* [Objetivos](#objetivos)
* [Descripcion](#descripcion)
  * [Fase 1](#fase01)
    * [Fuentes](#fuente)
    * [Limpieza](#limpieza)
  * [Inicio](#inicio)
    * [Estructura](#estructura)
    * [Prerrequisitos](#prerrequisitos)
    * [Utilizacion](#utilizacion)
      * [Base de datos](#db)
      * [Dependencias](#dependencias)
---

# Objetivos
• Comprender el proceso de extracción, transformación y carga de los datos.
• Utilizar diferentes fuentes de datos para que los estudiantes se familiaricen
con los formatos en los que se pueden obtener.
• Que los alumnos se familiaricen y apliquen lo aprendido del lenguaje de
programación Python y la librería Pandas para realizar el procesamiento de
los datos.
• Que los alumnos apliquen lo aprendido de la ciencia de datos y de los
procesos de ETL en un proyecto práctico. 


# Descripcion
Se le ha contratado como un consultor externo para realizar un estudio de los
datos recopilados por el Ministerio de Salud durante la pandemia del Covid-19
Estos datos fueron obtenidos por medio de tabulación de estos durante todos los
días del año 2020.

Como científico de datos, su primera tarea asignada es realizar la recolección y
limpieza de los datos, para posteriormente guardarlos en una base de datos. Por
medio de la recolección se busca que usted obtenga todos los datos de 2 fuentes
principales. 

# Fase01
La fase 1 se centra en el proceso de ETL, se debe poner en practica los procesos de extraccion, 
transformacion y carga de los datos. 

# Fuente
Para este proyecto se tienen 2 archivos fuente
    - CSV (Remoto)
    - CSV (Local)
    
# Limpieza
- Identificacion de datos
  - Tratamiento de datos faltantes: se coloco el promedio de los datos
    - Eliminacion de duplicados
        ```python
                def tratar_datos_pais():
                paises = leer_csv.obtener_dataframe(main.url_paises)
            
                #Eliminar duplicados
                paises.drop_duplicates(inplace=True)
        ```
      
    - Filtrar por pais
        ```python
                #Filtrar paises
                paises = paises[paises['Country'] == "Guatemala"]
        ```
      
      - Tratar datos nulos
          ```python
                # TRATAR DATOS NULOS
                for columna in departamento.columns:
                    if departamento[columna].dtype == 'int64':
                        departamento[columna].fillna(departamento[columna].mean(), inplace=True)
          ```

    - Filtrar por fecha
        ```python
                paises["Date_reported"] = pd.to_datetime(paises['Date_reported'])
                print(paises["Date_reported"].dtype)
                # if isinstance(paises['Date_reported'], pd.Timestamp):
                #     paises['Date_reported'] = paises['Date_reported'].date()
                paises = paises[(paises['Date_reported'] >= main.fecha_inicial) & (paises['Date_reported'] <= main.fecha_final)]
            
                # Archivo prueba
                paises.to_csv('datos.csv', index=False)
            
                return paises
        ```

      - Unir dataframes
          ```python
                  def unir_dataframe(departamentos, paises):
                    pd.merge(departamentos, paises, left_on='fecha', right_on='Date_reported', how='left').to_csv("all.csv")
                    paises.to_csv('paises.csv', index=False)
                    return pd.merge(departamentos, paises, left_on='fecha', right_on='Date_reported', how='left')
          ```

# Inicio
Se describira la estructura del proyecto como los requisitos previos para el desarrollo del
proyecto y demas recursos que utilizara.

# Estructura
El proyecto se divide en 3 carpetas generales con sus respectivos archivos los cuales son:
  1-gesta_archivos
    - _init_.py
    -leer_csv.py
  2-tratamiento_datos
    - _init_.py
    -tratamiento.py
  3-cargar_datos
    - _init_.py
    -carga_datos.py
    -queries.py
  -script_db.sql
  - requirements.txt
  -Readme.md


# Prerrequisitos
  1-Python3.10
  2-Mysql 8.0
  3-pandas 
  4-numpy
  5-SQLAlchemy
  6-Automap
  7-mysql-connector-python

# Utilizacion
Al comienzo de la ejecucion se debe montar el "SCHEMA" de la base de datos y crearla, para la demostracion
la BD se llamará "seminario2" y seguidamente se podrá ejecutar el proyecto realizado en python utilizando
Pandas.

# DB
-ImagenER


# Dependencias
```Console
pip install -r requirements.txt
```

Para la version en consola al terminar la ejecucion mostrara un mensaje
de los batch procesados correctamente

