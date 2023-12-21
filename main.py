import os



fecha_inicial='2021-01-01'
fecha_final='2021-01-15'
url_paises='C:\\Users\\Charly\\Documents\\U 2023_12\\Seminario de Sistemas 2\\Laboratorio\\ProyectoFase1\\global.csv'
url_municipios='C:\\Users\\Charly\\Documents\\U 2023_12\\Seminario de Sistemas 2\\Laboratorio\\ProyectoFase1\\municipio.csv'

#url_paises='https://seminario2.blob.core.windows.net/fase1/global_calificacion.csv?sp=r&st=2023-12-14T23:42:34Z&se=2023-12-15T07:42:34Z&sv=2022-11-02&sr=b&sig=m9dGWwEwEoQfmb7NRg2UMLm1cVKx2gTETFJVxv9WUZ4%3D'
#url_municipios='C:\\Users\\Charly\\Documents\\U 2023_12\\Seminario de Sistemas 2\\Laboratorio\\ProyectoFase1\\ArchivosCalificacion\\municipio.csv'
#\\

host = os.environ.get('host')
user = os.environ.get('user')
passw = os.environ.get('pass')
db = os.environ.get('database')

batch = 500
success = 0
error = 0
retry = 3



print(f"Batch exitosos {success}")
print(f"Batch con error {error}")









