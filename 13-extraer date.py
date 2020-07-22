import pandas as pd 
import datetime 
datos = pd.read_csv('datosnum.csv')
df=pd.DataFrame(datos)

hora=df['A'].str.extract('((?:[01]\d|2[0-3]):[0-5]\d:[0-5]\d)')
hora2=df['C'].str.extract('((?:[01]\d|2[0-3]):[0-5]\d:[0-5]\d)')
hora3=df['F'].str.extract('(\d+(?:\.\d+)?)')
print(hora)

df2=pd.DataFrame()
df2=df2.fillna(0)

df2['A']=hora[0].tolist()
df2['C']=hora2[0].tolist() #Lo hice de esta forma porque la que ellos tienen no me funcionaba.. espero alguien lo resuelva
df2['F']=hora3[0].tolist()
print(df2)
#agrupacion por minutos
#

df2['A']=pd.DatetimeIndex(df2['A'])
#print("Antes del index: ",df2)
df2.set_index(keys='A',inplace=True)
print(df2)
inicio=datetime.time(11,18,0)
fin=datetime.time(11,19,0)
print(df2[['F']].between_time(inicio,fin))