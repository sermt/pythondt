import pandas as pd 
import numpy as np
datos= { "nombres": ["juan","mario","maria","ana","andrea"], "calificaciones": [9,6,4,8,10], "materia": ["matematicas","matematicas","matematicas","matematicas","matematicas"]}

df=pd.DataFrame(datos)
print(df)
print('\n'*2)

#datos no validos
datos= { "nombres": ["juan","mario","maria","ana","andrea"], "calificaciones": [np.nan,6,4,8,10], "materia": ["N/A","matematicas","matematicas","matematicas","matematicas"]}

df2=pd.DataFrame(datos)
print(df2)
print('\n')
df2nonan=pd.DataFrame(df2)
df2nonan=df2nonan.replace(np.nan,"0")#elimina los nan y los cambia por 0 / df2nonan.dropna(how="any",inplace=True) desaparece toda la linea del nan
print(df2nonan)
print('\n'*2)
#eliminar registro buscando por columna
columna= df2[df2["materia"]!= "N/A"]
print(columna)
print('\n'*2)
#llenar con 0 cualquier valor
df3=pd.DataFrame(df2)
df3.fillna(0,inplace=True)
print(df3)
print(df3.describe())
df2["calificaciones"]=df2.calificaciones.astype(int)
print(df2.describe())
print('\n'*2)

#EStadisticas individuales
print("promedio", df2["calificaciones"].mean())
