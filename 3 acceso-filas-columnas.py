import pandas as pd
import numpy as np
datos=pd.read_csv("ATP.csv")
print(datos.info())
print(datos.head())#mostrar primeros 5 renglones
print('\n')
print(datos.iloc[0:5])
print('\n')
print(datos.iloc[[0,3,6,24],])#accediendo a los renglones 0.3.6.24
#columnas
print(datos.iloc[:,0:2])#todas las filas, solo 2 columnas
print(datos.iloc[[0,3,6,24],0:4])
#rangos de regiones y renglones
print(datos.iloc[0:5,5:8])