import pyodbc
import pandas as pd
from sqlalchemy import create_engine

server = 'JERAL_BENITES'
database = 'picks'
username = 'sa'
password = 'zaperoko1'


connection_string = f'mssql+pyodbc://{username}:{password}@{server}/{database}?driver=ODBC+Driver+17+for+SQL+Server'
engine = create_engine(connection_string)

# Define una consulta SQL
sql_query = "select * FROM [dbo].[match_bet] AS matchb "
# Reemplaza 'tu_tabla' por el nombre de la tabla que desees analizar.

# Ejecuta la consulta y carga los datos en un DataFrame de Pandas
data = pd.read_sql(sql_query, engine)

# Realiza análisis de datos con Pandas
# Por ejemplo, puedes calcular estadísticas descriptivas:
summary_stats = data.head()
print("Estadísticas descriptivas:")
print(summary_stats)

# Puedes realizar otras operaciones de análisis de datos aquí.
#%%
