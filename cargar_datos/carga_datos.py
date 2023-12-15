import pandas as pd

import tratamiento_datos.tratamiento
from tratamiento_datos import tratamiento as t
import main
import queries




def obtener_dataframe():
    return t.unir_dataframe(t.tratar_datos_municipio(),t.tratar_datos_pais())


def insert_report_country(dataframe):
    dataframe.to_csv('new_data.csv', index=False)
    #print(new_dataframe['Date_reported'])
    rows = len(dataframe)
 #   new_dataframe.to_csv("todo.csv",index=False)
#    new_dataframe['Date_reported'] = pd.to_datetime(new_dataframe['Date_reported']).dt.strftime('%d/%mm/%YYYY')
    #new_dataframe['Date_reported'].dt.strftime('%Y-%m-%d')

    for inicio in range(0, rows, main.batch):
        fin = inicio + main.batch
        lote_df = dataframe.iloc[inicio:fin]
        lst_report_country = []
        for x, fila in lote_df.iterrows():
            date_reported = fila['Date_reported']
            date_reported = date_reported.strftime('%Y-%m-%d')
            country_code = fila['Country_code']
            new_cases = fila['New_cases']
            cumulative_cases = fila['Cumulative_cases']
            new_deaths = fila['New_deaths']
            cumulative_deaths = fila['Cumulative_deaths']

            lst_report_country.append(queries.report_country(
                fecha=date_reported,
                codigo=country_code,
                nuevos=new_cases,
                casos_acum=cumulative_cases,
                nuevas=new_deaths,
                muertes_acum=cumulative_deaths
            ))
        queries.report_country_insert(lst_report_country)
def insert_municipals( df_municipios):
    num_filas = len(df_municipios)
    df_municipios_temp = df_municipios.drop_duplicates("codigo_municipio")
    for inicio in range(0, num_filas, main.batch):
        fin = inicio + main.batch
        lote_df = df_municipios_temp.iloc[inicio:fin]
        lst_municipios = []
        for x, fila in lote_df.iterrows():
            codigo_municipio = fila['codigo_municipio']
            nombre_municipio = fila['municipio']
            codigo_departamento = fila['codigo_departamento']
            poblacion = fila['poblacion']
            lst_municipios.append(queries.municipality(
                codigo=codigo_municipio,
                nombre=nombre_municipio,
                departamento=codigo_departamento,
                poblacion=poblacion
            ))
        queries.insert_municipio(lst_municipios)

def insert_departament(dataframe):
    num_filas = len(dataframe)
    df_municipios_temp = dataframe.drop_duplicates("codigo_departamento")

    for inicio in range(0, num_filas, main.batch):
        fin = inicio + main.batch
        lote_df = df_municipios_temp.iloc[inicio:fin]
        lst_departament = []
        for x, fila in lote_df.iterrows():
            code_departament = fila['codigo_departamento']
            name_departament = fila['departamento']
            lst_departament.append(queries.departament(codigo=code_departament,
                                                nombre=name_departament))

        queries.insert_departamento(lst_departament)



def insert_report_municipals(df_report_municipals):
    df_limpio = df_report_municipals.drop_duplicates(subset=['fecha', 'codigo_municipio'])
    num_filas = len(df_limpio)

    for inicio in range(0, num_filas, main.batch):
        fin = inicio + main.batch
        lote_df = df_limpio.iloc[inicio:fin]
        lst_report = []
        for x,fila in lote_df.iterrows():
            fecha = fila['fecha']
            code_municipals = fila['codigo_municipio']
            number_cases = fila['numero_casos']
            lst_report.append(queries.report_municipality(
                fecha=fecha,
                codigo=code_municipals,
                numero_casos=number_cases
            ))
        queries.insert_reporte_municipio(lst_report)


def insert_data():
    all_data = obtener_dataframe()

    insert_report_country(all_data)
    insert_departament(all_data)
    insert_municipals(all_data)
    insert_report_municipals(all_data)

insert_data()
print(f"Batch exitosos {main.success}")
print(f"Batch con error {main.error}")









