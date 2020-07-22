import pandas as pd 
import matplotlib.pyplot as plt
# datos = pd.read_csv('ArtJan2018resumido.csv')
# df=pd.DataFrame(datos)
# df['fecha']=datos['pubDate'].str.extract('(../../..)',expand=True) #se extrae la parte de la fecha
# print(df['fecha'])

datos=pd.read_csv('Ejemplo.csv')
df=pd.DataFrame(datos)
df['hora']=df['fecha'].str.extract('(..:..:..)',expand=True)
print(df['hora'])
df['hora']=pd.to_datetime(df['hora'])
df['hora 1']=pd.to_datetime(df['hora 1'])
df['diferencia']=df['hora']-df['hora 1']
print(df['diferencia'])

plt.plot(df['hora'],df['valor 2'],'-')
_=plt.xticks(rotation=45)
plt.show()#forma de mostar el grafico