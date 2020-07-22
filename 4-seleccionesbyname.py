import pandas as pd 
import numpy as np 

datos=pd.read_csv("ATP.csv")

print(datos.head())
print(datos.set_index("Location", inplace=True))#fijamos el indice como location
print(datos.loc["Adelaide"])
print("atlanta y superficie")
print(datos.loc["Atlanta", "Surface"])
print("seleccion amplia")
print(datos.loc[["Atlanta", "Melbourne"],["Court","Tournament","Round"]])
print("seleccion amplia con rango")
print(datos.loc[["Atlanta", "Melbourne"],"Series":"Round"])
print("Seleccion solo con Grand Slam")
print(datos.loc[datos["Series"].str.endswith("Slam")])