from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from sqlalchemy.ext.automap import automap_base
import main

conection = f'mysql+mysqlconnector://{main.user}:{main.passw}@{main.host}/{main.db}'
engine = create_engine(conection)

Base = automap_base()
Base.prepare(engine, reflect=True)

report_country = Base.classes.report_country
departament = Base.classes.departament
municipality = Base.classes.municipality
report_municipality = Base.classes.report_municipality

session = Session(engine)

def report_country_insert(lst_report_country):
    try:
        session.add_all(lst_report_country)
        session.commit()
        main.success += 1
    except Exception as e:
        session.rollback()
        print(e)
        main.error += 1
def insert_departamento( lst_departamento):
    try:
        session.add_all(lst_departamento)
        session.commit()
        main.success += 1
    except Exception:
        session.rollback()
        main.error += 1

def insert_municipio( lst_municipio):
    try:
        session.add_all(lst_municipio)
        session.commit()
        main.success += 1
    except Exception:
        session.rollback()
        main.error += 1

def insert_reporte_municipio( lst_report_municipals):
    try:
        session.add_all(lst_report_municipals)
        session.commit()
        main.success += 1
    except Exception as e:
        session.rollback()
        main.error += 1
