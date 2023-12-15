from gesta_archivos import leer_csv
import pandas as pd
import main
import os

def tratar_datos_pais():
    paises = leer_csv.obtener_dataframe(main.url_paises)

    #Eliminar duplicados
    paises.drop_duplicates(inplace=True)

    #Filtrar paises
    paises = paises[paises['Country'] == "Guatemala"]

    #TRATAR DATOS NULOS
    for columna in paises.columns:
        if paises[columna].dtype == 'int64':
            paises[columna].fillna(paises[columna].mean(), inplace=True)

    # Filtrar por fecha
    paises["Date_reported"] = pd.to_datetime(paises['Date_reported'] , format='%m/%d/%Y')
    #paises['Date_reported'].dt.strftime('%Y-%m-%d')
    #print(paises["Date_reported"].dtype)
    # if isinstance(paises['Date_reported'], pd.Timestamp):
    #     paises['Date_reported'] = paises['Date_reported'].date()
    paises = paises[(paises['Date_reported'] >= main.fecha_inicial) & (paises['Date_reported'] <= main.fecha_final)]

    # Archivo prueba
    paises.to_csv('datos.csv', index=False)

    return paises
    #################################
    #################################
    #################################
def tratar_datos_municipio():
    departamento = leer_csv.obtener_dataframe(main.url_municipios)

    # Eliminar duplicados
    departamento.drop_duplicates(inplace=True)


    # TRATAR DATOS NULOS
    for columna in departamento.columns:
        if departamento[columna].dtype == 'int64':
            departamento[columna].fillna(departamento[columna].mean(), inplace=True)

    #convertir encabezados de fecha  en columnas y agregarle nombre a la nueva columna
    departamento_convertido = departamento.melt(
        id_vars=['departamento', 'codigo_departamento', 'municipio', 'codigo_municipio', 'poblacion'],
        var_name='fecha',
        value_name='numero_casos')

    departamento_convertido['fecha'] = pd.to_datetime(departamento_convertido['fecha'], format='%m/%d/%Y')

    #Filtrar por fecha
    departamento_convertido["fecha"] = pd.to_datetime(departamento_convertido['fecha'])
    departamento_convertido = departamento_convertido[
        (departamento_convertido['fecha'] >= main.fecha_inicial) & (departamento_convertido['fecha'] <= main.fecha_final)]

    #elimina duplicados en base a la fecha y codigo de municipio
    departamento_convertido = departamento_convertido.drop_duplicates(subset=['fecha', 'codigo_municipio'])

    # Archivo prueba
    departamento_convertido.to_csv('datos2.csv', index=False)
    return departamento_convertido

def unir_dataframe(departamentos, paises):
#    pd.merge(departamentos, paises, left_on='fecha', right_on='Date_reported', how='left').to_csv("all.csv")
    return pd.merge(departamentos, paises, left_on='fecha', right_on='Date_reported', how='left')























