import pandas as pd 
datos=pd.read_csv("movies2.csv")
df=pd.DataFrame(datos)
maxi=df["Runtime (Minutes)"].max()#maximo valor -duracion de una pelicula
print("La maxima duracion en horas es de: ",maxi/60, '\n')
indice=	df["Runtime (Minutes)"].idxmax()
print(indice)
print(df._get_value(df["Runtime (Minutes)"].idxmax(), "Title")) #obtenemos el valor con base en el idmxa
print(df._get_value(828,'Title')) #forma optima conociendo la posicion
#agrupaciones
df1=df.groupby(['Genre'])[["Votes"]].sum()
print("El genero mas gustado es: ")
likes=df.groupby(['Genre'])[["Votes"]].sum()

print(likes['Votes'].idxmax(),end="")
print(" con: ",likes['Votes'].max(), "likes")
print("\n"*5)
#promedio de presupuesto por director
df2=df.groupby(["Director"])[["Rating"]].sum() #obtenemos los rating de cada director
df2=df.groupby(["Director"])[["Rating"]].mean() #obtenemos el promedio de rating
print(df2)
print("Ordenados por rating promedio: \n",df2.sort_values(by='Rating', ascending=False))
