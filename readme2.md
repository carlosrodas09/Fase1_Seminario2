PROYECTO LABORATORIO FASE 1 SEMINARIO DE SISTEMAS 2

# Índice
* [Objetivos](#objetivos)
* [Descripcion](#descripcion)
  * [Fase 1](#fase01)
    * [Fuentes](#fuente)
    * [Limpieza](#limpieza)
  * [Fase 2](#fase02)
    * [EDA MONOVARIABLE](#eda_Mono_Variable)
      * [Datos_Mono Cuantitativos](#datos_Monovariables_Cuantitativvos)
      * [Datos_Mono Cuanlitativos](#datos_Monovariables_Cualitativvos)
    * [EDA MULTIVARIABLE](#eda_Multi_Variable)
      * [Datos_Multi Cuantitativos](#datos_Multivariables_Cuantitativvos)
      * [Datos_Multi Cuanlitativos](#datos_Multivariables_Cualitativvos)
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

## - Fuente
Para este proyecto se tienen 2 archivos fuente.

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

# Fase02
Como analista de datos, usted debe ser capaz de obtener los datos que sus
colegas han procesado a través de un proceso ETL. Actualmente, estos se
encuentran en una base de datos SQL, por lo tanto, usted tiene que obtener estos
datos por medio de pandas. 


# Eda_Mono_Variable
# Datos_Monovariables_Cuantitativvos

Debe realizar un análisis mono variable de la cantidad de nuevas muertes,
cantidad de muertes acumuladas y población de los municipios. Para el análisis se
deben mostrar los estadísticos de conteo, valores únicos, promedio, desviación
estándar, mínimo, máximo y cuartiles.
Además, se debe realizar un histograma y un diagrama de caja con cada una de
las variables mencionadas anteriormente. 

```python
df.shape  # Despliega el numero de variables y numero de observaciones

df.dtypes  #Instruccion Despliega el tipo de dato de cada una de las variables

df.count()  #Cuenta los datos no nulos en cada columna del Dataset

df.isna().sum().sum() #Determinacion de valores nulos en todo el dataset

df.isna().sum() #Determinacion de valores nulos por columna

df.describe()


df.describe(include='all')

df.info()  #Muestra toda la info del DataSet

df.duplicated()   #Manejo o busqueda de valores duplicados

#Calculo de percentiles
p0=df.New_deaths.min()
p100=df.New_deaths.max()
q1=df.New_deaths.quantile(0.25)
q2=df.New_deaths.quantile(0.5)
q3=df.New_deaths.quantile(0.75)
iqr=q3-q1
#Calculo lc y uc
lc= q1-1.5*iqr
uc=q3 +1.5*iqr
print( "p0 = " , p0 ,", p100 = " , p100 ,", q1 = " , q1,", q2 = " , q2,", q3 = " , q3 ,", iqr = " , iqr ,", lc = " , lc ,", uc = " , uc)

df.New_deaths.clip(upper=uc,inplace=True)   # Funcion para normalizar Outliers.
df.New_deaths.plot(kind='box') #Outlier Nuevas muertes

df.New_deaths.plot(kind='hist',grid=True)
plt.title("CANTIDAD DE NUEVAS MUERTES")
plt.show()
```



# Datos_Monovariables_Cualitativvos
Debe realizar un análisis mono variable de los municipios y departamentos. En
este únicamente se deben realizar diagramas de barras para el conteo de
registros. 


```python
sns.set(style="darkgrid")
ax = sns.countplot(x="departamento", data=df, palette="Set2")

import plotly.graph_objects as go
top=pd.value_counts(df['departamento'])
fig = go.Figure([go.Bar(x=top.index, y=top.values , text=top.values,marker_color='indianred')])
fig.update_traces(texttemplate='%{text:.2s}', textposition='outside')
fig.show()


fr=df[df['Country']=='Guatemala']
nannef=fr.dropna()
import plotly.express as px
fig = px.treemap(nannef, path=['Country','departamento'],
                  color='departamento', hover_data=['departamento'],color_continuous_scale='Purples')
fig.show()
```


TRANSFORMACIONES

Si se llega a encontrar un sesgo o se encuentra que los datos no cuentan con la
escala correcta, se deben realizar las transformaciones necesarias para poder
continuar con el EDA multivariable.

```python
departments1={}
df['departamento']=df['departamento'].fillna('Unknown')
cou1=list(df['departamento'])
for i in cou1:
    #print(i)
    i=list(i.split(','))
    if len(i)==1:
        if i in list(departments1.keys()):
            departments1[i]+=1
        else:
            departments1[i[0]]=1
    else:
        for j in i:
            if j in list(departments1.keys()):
                departments1[j]+=1
            else:
                departments1[j]=1

departments_fin1={}
for country,no in departments1.items():
    country=country.replace(' ','')
    if country in list(departments_fin1.keys()):
        departments_fin1[country]+=no
    else:
        departments_fin1[country]=no
        
countries_fin1={k: v for k, v in sorted(departments_fin1.items(), key=lambda item: item[1], reverse= True)}

# Set the width and height of the figure
plt.figure(figsize=(15,15))

# Add title
plt.title("MAPA DE DATOS DE DEPARTAMENTOS")

# Bar chart showing average arrival delay for Spirit Airlines flights by month
sns.barplot(y=list(departments_fin1.keys()), x=list(departments_fin1.values()))

# Add label for vertical axis
plt.ylabel("Arrival delay (in minutes)")
```



# Eda_Multi_Variable
# Datos_Multivariables_Cuantitativvos
Para los datos cuantitativos se debe realizar gráficas de dispersión entre las
variables cantidad de nuevas muertes, cantidad de muertes acumuladas y
población de los municipios.

```python
df.plot(x='departamento', y='New_deaths',kind='scatter')
plt.show()

df.plot(x='municipio', y='New_deaths',kind='scatter')
plt.show()

sns.set(style="darkgrid")
sns.kdeplot(data=df['New_deaths'], shade=True)
```



# Datos_Multivariables_Cualitativvos
Para los datos cualitativos se deben realizar gráficas de barras, mapas de calor y
cualquier otra gráfica que el estudiante crea conveniente para comparar las
variables municipios y departamentos con las variables cuantitativas. Es decir:
• Municipios vs cantidad de nuevas muertes
• Departamentos vs cantidad de nuevas muertes
• Municipios vs población
• Departamentos vs población
• Municipios vs cantidad de muertes acumuladas
• Departamentos vs cantidad de muertes acumuladas

```python
df['New_deaths'] = pd.to_numeric(df['New_deaths'])
correlation_matrix = df.corr().abs()

plt.figure(figsize=(10, 8))
sns.set(style="white")

sns.heatmap(correlation_matrix, annot=True, fmt=".2f", cmap='coolwarm', square=True, linewidths=.5)

plt.title('Mapa de Calor de Correlación')
plt.show()




fr=df[df['departamento']=='QUETZALTENANGO']
nannef=fr.dropna()
import plotly.express as px
fig = px.treemap(nannef, path=['departamento','municipio','New_deaths'],
                  color='New_deaths', hover_data=['New_deaths','municipio'],color_continuous_scale='Purples')
fig.show()




df.plot(x='municipio', y='New_deaths',kind='scatter')
plt.show()
```




CONCLUSIONES

1. LOS DEPARTAMENTOS DONDE EXISTE UNA MAYOR CANTIDAD DE MUERTES NUEVAS SON: HUEHUETENANGO, SAN MARCOS, QUETZALTENANGO, QUICHE Y SUCHITEPEQUEZ, ESTO VA EN FUNCION DE LA CANTIDAD DE POBLACION Y EL NUMERO DE CASOS REGISTRADOS EXITOSAMENTE.  POR LO QUE SE ACONSEJA TOMAR MEJORES MEDIDAS DE SEGURIDAD SOCIAL PARA EVITAR QUE ESTE NUMERO CREZCA



2. LOS DEPARTAMENTOS DONDE HAY UNA MENOR CANTIDAD DE MUERTES ACUMULADAS SON: IZABAL, JALAPA, EL PROGRESO, BAJA VERAPAZ Y RETALHULEU, ESTO VA EN FUNCION DE LA CANTIDAD DE POBLACION Y EL NUMERO DE CASOS REGISTRADOS EXITOSAMENTE. LAS MEDIDAS DE SEGURIDAD DEBEN SEGUIR SIN DESCARTAR UN ESTUDIO DE CAMPO MAS PRECISO PARA COMPROBAR LA EFICIENCIA DE LOS METODOS PARA MANTENER LA SALUD DE LA POBLACION DE ESOS DEPARTAMENTOS.



3. LOS DEPARTAMENTOS DONDE HAY UNA CANTIDAD PROMEDIO DE MUERTES ACUMULADAS SON: ALTA VERAPAZ, GUATEMALA, JUTIAPA, SOLOLA, CHIMALTENANGO Y SACATEPEQUEZ, ESTO VA EN FUNCION DE LA CANTIDAD DE POBLACION Y EL NUMERO DE CASOS REGISTRADOS EXITOSAMENTE. LAS MEDIDAS DE SEGURIDAD DEBEN SEGUIR SIN DESCARTAR UN ESTUDIO DE CAMPO.





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
8. GOOGLE COLAB

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

