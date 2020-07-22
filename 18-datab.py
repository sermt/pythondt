import pandas as pd 
import matplotlib.pyplot as plt 
import numpy as np 
datos=pd.read_csv("data.csv")
"""
print(datos.info())
print(datos.dtypes)
print(datos.describe())
print(datos.head(5))
"""
"""df1=datos.loc[datos['school']=='GP']
print(df1.info())

df2=datos.loc[datos['school']=='MS']
print(df2.info())

print("¿Cuántos estudiantes viajan mas de una hora?")

print(df1.where(df1.traveltime==4).traveltime.count())
print(df1['traveltime'].describe())

plt.figure
df1['traveltime'].hist()
plt.show()"""

print("¿Cuántos estudiantes tienen problemas?")
df1=pd.DataFrame(datos)
df1=datos.loc[datos['school']=='GP']
print(df1.where(df1.famrel==1).internet.count())
plt.figure
df1['famrel'].hist()
#plt.show()


print("Tabla pivote usuario \n")
agrupar=input("Cómo quieres agrupar los datos? ")
datos=input("Cual dato quieres analizar? ")
tabla=pd.pivot_table(df1,index=[agrupar],values=datos,aggfunc=[np.mean,min,max])
print(tabla)

if df1.where(df1.famrel<=2).famrel.count()>0:
	print("Se requiere una atención personalizada")
	tutores=df1.where(df1.famrel<=2).famrel.count()/2
	print("Se necesitan ", int(round(tutores)), " tutores")