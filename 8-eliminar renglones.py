import pandas as pd 
datos=pd.read_csv("canciones.csv")
print(datos.info())
print(datos)
print("\n"*3)
filas=len(datos.index) #obtener la cantidad de filas
#print(filas)
datos.drop(31, inplace=True) #elimina una fila en especifico de "datos"
datos.drop(datos.index[0:5],inplace=True) #eliminamos filas en un rango determinado
print(datos)